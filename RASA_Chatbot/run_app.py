from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-359418684578-360311923670-373479391381-faf4e29bddac4cd131221b8cf0ffa627', #app verification token
							'xoxb-359418684578-372796513233-gHxeV6CHQFl8MPkZVrPHBsnQ', # bot verification token
							'7uAoXNmNANaqCa9WpALV9EhR', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))