from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted
import zomatopy
import json
import re
import pandas as pd
import math
import config_params
import sys,os
import smtplib
import warnings
warnings.filterwarnings("ignore")



sys.path.append(os.getcwd())
import config_params

operating_cities=config_params.operating_cities
valid_cusines=config_params.valid_cusines
sorting_criteria={"<300":('cost','asc'),"300_700":('rating','desc'),">700":('cost','desc')}
cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
msg=""
email_template=config_params.email_template


def fetch_and_process_data(zomato,lat, lon, cusine, price):
	results=zomato.restaurant_search("", lat, lon,cusine)
	d = json.loads(results)
	name,addr,costfor2,rating,cuisines=[],[],[],[],[]
	start=0
	if d['results_found'] == 0:
		return None
	else:
		pages=math.ceil(d['results_found']/20)  ####only 20 results per request and max we can fetch only 100 restaurants as per api limit
		if pages>5: pages=5

		sort,order=sorting_criteria.get(price,('rating','desc'))

		for i in range(0,pages+1):
			results=zomato.restaurant_search("", lat,lon,cusine,start=start,sort=sort,order=order)
			d = json.loads(results)
			for restaurant in d['restaurants']:
				name.append(restaurant['restaurant']['name'])
				addr.append(restaurant['restaurant']['location']['address'])
				rating.append(restaurant['restaurant']['user_rating']['aggregate_rating'])
				costfor2.append(restaurant['restaurant']['average_cost_for_two'])
				cuisines.append(restaurant['restaurant']['cuisines'])
			start=start+20

		df=pd.DataFrame({'name':name,'addr':addr,'costfor2':costfor2,'rating':rating,'cuisine':cuisines})
		df['rating'] = df['rating'].apply(pd.to_numeric)

		if price == '<300': df_filtered=df[df['costfor2'] < 300]
		elif price == '300_700': df_filtered=df[(df['costfor2'] >= 300) & (df['costfor2'] <= 700)]
		elif price == '300_700': df_filtered=df[df['costfor2'] > 700]
		else: df_filtered=df	

		if len(df_filtered['name'])==0:
			return None

		df_sorted=df_filtered.sort_values("rating",ascending=False)

		return df_sorted



def isLocationAvailable(zomato,tracker):
	loc = tracker.get_slot('location')
	location_available,lat,lon=0,0,0
	location_detail=zomato.get_location(loc, 1)
	d1 = json.loads(location_detail)	

	if len(d1["location_suggestions"]) !=0:
		location_available=1
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		return (location_available,lat,lon)
	else:
		return (location_available,lat,lon)



class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'
		
	def run(self, dispatcher, tracker, domain):
		global msg
		msg=''

		try:
			config=config_params.user_key
			zomato = zomatopy.initialize_app(config)
			location_available,lat,lon=isLocationAvailable(zomato,tracker)
			cuisine=str(cuisines_dict.get(tracker.get_slot('cuisine')))
			price=tracker.get_slot('price')

			if location_available:
				
				df_sorted=fetch_and_process_data(zomato, lat, lon, cuisine, price)

				if df_sorted is None:
					response= "no results"
					return [SlotSet('results',None)]

				else:			
					df_sorted['info']="Restaurant "+ df_sorted['name']+ " in "+ df_sorted['addr'] +\
							   		  " has been rated " + df_sorted['rating'].astype(str)
					response='\n'.join(df_sorted['info'].head(5).tolist())
					top10='\n'.join(df_sorted['info'].head(10).tolist())
					msg=top10

			else:
				response= "no results"
				return [SlotSet('results',None)]
			
			dispatcher.utter_message("Showing you top rated restaurants:\n" + response)
			return [SlotSet('results',"Available")]
		
		except Exception as e:
			dispatcher.utter_message("Issue encountered in fetching restaurants.Might be a connection issue\n" + str(e))
			return [SlotSet('results',None)]




class CheckCity(Action):
	def name(self):
		return 'check_location'
		
	def run(self, dispatcher, tracker, domain):
		if (tracker.get_slot('location')):
			#dispatcher.utter_message(tracker.get_slot('location'))
			loc = tracker.get_slot('location')
			if (loc.lower() not in [l.lower() for l in operating_cities]):
				return [SlotSet("location", None)]

			return [SlotSet('location',loc)]



class CheckCusine(Action):
	def name(self):
		return 'check_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		if (tracker.get_slot('cuisine')):
			#dispatcher.utter_message(tracker.get_slot('cuisine'))
			cuisine = tracker.get_slot('cuisine')
			if (cuisine.lower() not in [l.lower() for l in valid_cusines]):
				return [SlotSet("cuisine", None)]

			return [SlotSet('cuisine',cuisine)]


class CheckLocationCusine(Action):
	def name(self):
		return 'check_location_cuisine'
		
	def run(self, dispatcher, tracker, domain):
		is_location,is_cuisine=1,1
		if tracker.get_slot('location'):
			#dispatcher.utter_message(tracker.get_slot('location'))
			loc = tracker.get_slot('location')
			if (loc.lower() not in [l.lower() for l in operating_cities]): is_location=0
		else:
			is_location=0

		if tracker.get_slot('cuisine'):
			#dispatcher.utter_message(tracker.get_slot('cuisine'))
			cuisine = tracker.get_slot('cuisine')
			if (cuisine.lower() not in [l.lower() for l in valid_cusines]): is_cuisine=0
		else:
			is_cuisine=0

		if is_location==0 and is_cuisine==0: return [SlotSet("location", None),SlotSet("cuisine", None)]
		elif is_location==0 and is_cuisine==1: return [SlotSet("location", None),SlotSet("cuisine", cuisine)]
		elif is_location==1 and is_cuisine==0: return [SlotSet("location", loc),SlotSet("cuisine", None)]
		else: return [SlotSet("location", loc),SlotSet("cuisine", cuisine)]



class CheckPrices(Action):
	def name(self):
		return 'check_price'
		
	def run(self, dispatcher, tracker, domain):
		if tracker.get_slot('price'):
			#dispatcher.utter_message(tracker.get_slot('price'))
			price = tracker.get_slot('price')

			is_300 = re.search('300',price)
			is_700 = re.search('700',price)

			if is_300 and is_700: return [SlotSet("price", '300_700')]
			elif is_300 : return [SlotSet("price", '<300')]
			elif is_700 : return [SlotSet("price", '>700')]
			else: return [SlotSet("price", None)]

		else:
			return [SlotSet("price", None)]



class CheckEmail(Action):
	def name(self):
		return 'check_email_id'
		
	def run(self, dispatcher, tracker, domain):
		if tracker.get_slot('email'):
			#dispatcher.utter_message(tracker.get_slot('email'))
			email = tracker.get_slot('email')
			if (re.search('[A-z0-9]+@[A-z0-9]+[.][A-z]+[.]?[A-z]*',email)):
				return [SlotSet("email", email)]
			else:
				return [SlotSet("email", None)]
		else:
			return [SlotSet("email", None)]




class SendEmail(Action):
	def name(self):
		return 'send_email'
		
	def run(self, dispatcher, tracker, domain):
		try:
			global msg
			msg= (email_template %msg) 
			subject='Top rated {} restuartants near you'.format(tracker.get_slot('cuisine'))
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			sender_email=config_params.email
			receiver_email=tracker.get_slot('email')
			server.login(config_params.email, config_params.password)
			message = 'Subject: {}\n\n{}'.format(subject, msg)
			server.sendmail(receiver_email,receiver_email, message)	
			#dispatcher.utter_message('Email sent')
		except Exception as e:
			dispatcher.utter_message('Issue in sending message \n' + str(e))

		#dispatcher.utter_message('Email sent')




class RestartAction(Action):
	def name(self):
		return 'resetbot'
		
	def run(self, dispatcher, tracker, domain):
		try:
			dispatcher.utter_message('Thank you and bye bye.')
		except Exception as e:
			dispatcher.utter_message('Issue in resetting \n' + str(e))
		finally:
			return [Restarted()]