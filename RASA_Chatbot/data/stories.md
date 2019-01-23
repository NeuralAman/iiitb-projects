## Generated Story 737645275462998541
* greet
    - utter_greet
* inform{"cuisine": "mexican", "location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "coimbatore"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform
    - utter_price_not_in_range
* inform{"price": "300 - 700"}
    - slot{"price": "300 - 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -235690178848547834
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "test@test.com"}
    - slot{"email": "test@test.com"}
    - check_email_id
    - slot{"email": "test@test.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -8743941007632466346
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
* deny
    - utter_goodbye
    - resetbot

## Generated Story 5817224822406962727
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* affirm
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 4053170002342279161
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -7386108988992284170
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 4061208525057911897
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "ooty"}
    - slot{"location": "ooty"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "ooty"}
    - slot{"location": "ooty"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* deny
    - utter_goodbye
    - resetbot

## Generated Story -8029597467764774085
* greet
    - utter_greet
* restaurant_search{"cuisine": "swedish", "location": "bangalore"}
    - slot{"cuisine": "swedish"}
    - slot{"location": "bangalore"}
    - check_location_cuisine
    - slot{"location": "bangalore"}
    - slot{"cuisine": null}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -8189403749050019021
* greet
    - utter_greet
* restaurant_search{"cuisine": "danish", "location": "whitefield"}
    - slot{"cuisine": "danish"}
    - slot{"location": "whitefield"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": null}
    - utter_location_double_check
* inform{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -4478909241232582189
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "ooty"}
    - slot{"cuisine": "american"}
    - slot{"location": "ooty"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "american"}
    - utter_location_double_check
* inform{"location": "ooty"}
    - slot{"location": "ooty"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 5522646671522438996
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - check_location
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -2754296850313171627
* restaurant_search{"cuisine": "chinese", "location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - check_location_cuisine
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "ttkk@yyy.in"}
    - slot{"email": "ttkk@yyy.in"}
    - check_email_id
    - slot{"email": "ttkk@yyy.in"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -1546414155324033052
* restaurant_search{"cuisine": "danish", "location": "delhi"}
    - slot{"cuisine": "danish"}
    - slot{"location": "delhi"}
    - check_location_cuisine
    - slot{"location": "delhi"}
    - slot{"cuisine": null}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300-700"}
    - slot{"price": "300-700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform
    - utter_bonappetitnomail
    - resetbot

## Generated Story 2908385417665430996
* restaurant_search{"cuisine": "spanish", "location": "whitefields"}
    - slot{"cuisine": "spanish"}
    - slot{"location": "whitefields"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": null}
    - utter_ask_location
* inform{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300 - 700"}
    - slot{"price": "300 - 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -7293598047994889937
* restaurant_search{"cuisine": "chinese", "location": "me"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "me"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "chinese"}
    - utter_location_double_check
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -8511074515550527667
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location_cuisine
    - slot{"location": "chennai"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story 8914858741259653226
* restaurant_search{"cuisine": "mexican", "location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "coimbatore"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* affirm
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -7301434528605314256
* inform{"cuisine": "south indian", "location": "coimbatore"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "coimbatore"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "timkoumar@gmail.com"}
    - slot{"email": "timkoumar@gmail.com"}
    - check_email_id
    - slot{"email": "timkoumar@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -5100572875561823552
* greet
    - utter_greet
* chitchat
    - utter_chitchat
* chitchat
    - utter_chitchat
* chitchat
    - utter_ask_continue
* affirm
    - utter_ask_service
* chitchat
    - utter_chitchat
    - utter_goodbye
    - resetbot

## Generated Story 1822454785388990290
* chitchat
    - utter_greet
* chitchat
    - utter_ask_service
* chitchat
    - utter_chitchat
    - utter_ask_continue
* affirm
    - utter_ask_service
* stop
    - utter_chitchat
    - utter_goodbye
    - resetbot

## Generated Story 6491299898846731299
* chitchat
    - utter_greet
* chitchat
    - utter_ask_service
* stop
    - utter_goodbye
    - resetbot

## Generated Story 4736847563664662383
* chitchat
    - utter_greet
* chitchat
    - utter_ask_service
* affirm
    - utter_ask_location
* inform
    - utter_location_double_check
    - utter_location_double_check
* inform{"location": "pune"}
    - slot{"location": "pune"}
    - check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "ert@hg.hg.uk"}
    - slot{"email": "ert@hg.hg.uk"}
    - check_email_id
    - slot{"email": "ert@hg.hg.uk"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 8771533529429686358
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "pune"}
    - slot{"location": "pune"}
    - check_location
    - slot{"location": "pune"}
    - utter_ask_cuisine
* option
    - utter_usetext
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* option
    - utter_usetext
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -4749913850340941463
* greet
    - utter_greet
* inform{"cuisine": "mexican", "location": "surat"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "surat"}
    - check_location_cuisine
    - slot{"location": "surat"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* option
    - utter_usetext
    - utter_ask_price
* inform{"price": "800"}
    - slot{"price": "800"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 1081098089406454173
* greet
    - utter_greet
* chitchat
    - utter_ask_service
* chitchat
    - utter_ask_location
* inform{"location": "ooty"}
    - slot{"location": "ooty"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "ooty"}
    - slot{"location": "ooty"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* option
    - utter_usetext
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* option
    - utter_usetext
    - utter_ask_price
* inform{"price": "800"}
    - slot{"price": "800"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* chitchat
    - utter_bonappetitnomail
    - resetbot

## Generated Story 9104991339316195363
* greet
    - utter_greet
* chitchat
    - utter_ask_service
* chitchat
    - utter_chitchat
* chitchat
    - utter_ask_continue
* affirm
    - utter_ask_service
* chitchat
    - utter_chitchat
    - utter_goodbye
    - resetbot

## Generated Story 3149647724973666002
* greet
    - utter_greet
* stop
    - utter_ask_service
* affirm
    - utter_ask_location
* inform{"location": "newyork"}
    - slot{"location": "newyork"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "whitefields"}
    - slot{"location": "whitefields"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "nanded"}
    - slot{"location": "nanded"}
    - check_location
    - slot{"location": "nanded"}
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
    - utter_ask_cuisine
* option
    - utter_usetext
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 1310612905043908871
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "cmbatore"}
    - slot{"location": "cmbatore"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "djk@idsnl.com"}
    - slot{"email": "djk@idsnl.com"}
    - check_email_id
    - slot{"email": "djk@idsnl.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 7586163473785792895
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "cmbatore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "cmbatore"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "mexican"}
    - utter_location_double_check
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* affirm
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "dsgj@hfuk.hu.cn"}
    - slot{"email": "dsgj@hfuk.hu.cn"}
    - check_email_id
    - slot{"email": "dsgj@hfuk.hu.cn"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -5487856129425169171
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - check_location_cuisine
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -1341902538486874529
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "coimbatore"}
    - slot{"cuisine": "american"}
    - slot{"location": "coimbatore"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "dasu@nd.com"}
    - slot{"email": "dasu@nd.com"}
    - check_email_id
    - slot{"email": "dasu@nd.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -3029224077081749377
* greet
    - utter_greet
* restaurant_search{"location": "salem"}
    - slot{"location": "salem"}
    - check_location
    - slot{"location": "salem"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - check_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "jkhd@yuhj.hj.nh"}
    - slot{"email": "jkhd@yuhj.hj.nh"}
    - check_email_id
    - slot{"email": "jkhd@yuhj.hj.nh"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -3029224077181749377
* greet
    - utter_greet
* restaurant_search{"location": "trichy"}
    - slot{"location": "trichy"}
    - check_location
    - slot{"location": "trichy"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "jkhd@yuhj.com"}
    - slot{"email": "jkhd@yuhj.com"}
    - check_email_id
    - slot{"email": "jkhd@yuhj.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -3029124077181749377
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - check_location
    - slot{"location": "patna"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "fk1@yuhj.com"}
    - slot{"email": "fk1@yuhj.com"}
    - check_email_id
    - slot{"email": "fk1@yuhj.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -435121170374808259
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - check_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "sgyj@ycsf.com"}
    - slot{"email": "sgyj@ycsf.com"}
    - check_email_id
    - slot{"email": "sgyj@ycsf.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -435121170304808259
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - check_location
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "gjynh@ycsf.com"}
    - slot{"email": "gjynh@ycsf.com"}
    - check_email_id
    - slot{"email": "gjynh@ycsf.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -435121170304800259
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "erode"}
    - slot{"location": "erode"}
    - check_location
    - slot{"location": "erode"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "ljfs@bc.com"}
    - slot{"email": "ljfs@bc.com"}
    - check_email_id
    - slot{"email": "ljfs@bc.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -1624307192706848893
* greet
    - utter_greet
* restaurant_search{"location": "chnnai"}
    - slot{"location": "chnnai"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"location": "chennai"}
    - utter_ask_cuisine
* inform{"cuisine": "iatlian"}
    - slot{"cuisine": "iatlian"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -1624307198706848893
* greet
    - utter_greet
* restaurant_search{"location": "nasik"}
    - slot{"location": "nasik"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "nashik"}
    - slot{"location": "nashik"}
    - check_location
    - slot{"location": "nashik"}
    - utter_ask_cuisine
* inform{"cuisine": "mexi"}
    - slot{"cuisine": "mexi"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -1614307198706848893
* greet
    - utter_greet
* restaurant_search{"location": "thrisur"}
    - slot{"location": "thrisur"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "thrissur"}
    - slot{"location": "thrissur"}
    - check_location
    - slot{"location": "thrissur"}
    - utter_ask_cuisine
* inform{"cuisine": "amrican"}
    - slot{"cuisine": "amrican"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 8970427742983330932
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "surat"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "surat"}
    - check_location_cuisine
    - slot{"location": "surat"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 8970427742983330932
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "nellore"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "nellore"}
    - check_location_cuisine
    - slot{"location": "nellore"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -8114065574788632927
* greet
    - utter_greet
* restaurant_search{"location": "palani"}
    - slot{"location": "palani"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "palani"}
    - slot{"location": "palani"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "pollachi"}
    - slot{"location": "pollachi"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "pollachi"}
    - slot{"location": "pollachi"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "kodaikanal"}
    - slot{"location": "kodaikanal"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kodaikanal"}
    - slot{"location": "kodaikanal"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "maduari"}
    - slot{"location": "maduari"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "madurai"}
    - slot{"location": "madurai"}
    - check_location
    - slot{"location": "madurai"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "hddb@ufnju.com"}
    - slot{"email": "hddb@ufnju.com"}
    - check_email_id
    - slot{"email": "hddb@ufnju.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -8154075574788632927
* greet
    - utter_greet
* restaurant_search{"location": "theni"}
    - slot{"location": "theni"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "theni"}
    - slot{"location": "theni"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "kumily"}
    - slot{"location": "kumily"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kumily"}
    - slot{"location": "kumily"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "kotagiri"}
    - slot{"location": "kotagiri"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kotagiri"}
    - slot{"location": "kotagiri"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "chavara"}
    - slot{"location": "chavara"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "madurai"}
    - slot{"location": "madurai"}
    - check_location
    - slot{"location": "madurai"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "hddb@ufnju.com"}
    - slot{"email": "hddb@ufnju.com"}
    - check_email_id
    - slot{"email": "hddb@ufnju.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -8214075574788632927
* greet
    - utter_greet
* restaurant_search{"location": "pala"}
    - slot{"location": "pala"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "pala"}
    - slot{"location": "pala"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "vypin"}
    - slot{"location": "vypin"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "vypin"}
    - slot{"location": "vypin"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "aluva"}
    - slot{"location": "aluva"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "aluva"}
    - slot{"location": "aluva"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* affirm
    - utter_ask_location
* inform{"location": "ranni"}
    - slot{"location": "ranni"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kollam"}
    - slot{"location": "kollam"}
    - check_location
    - slot{"location": "kollam"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "hddb@ufnju.com"}
    - slot{"email": "hddb@ufnju.com"}
    - check_email_id
    - slot{"email": "hddb@ufnju.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 9136640067584310607
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "kolam"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolam"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "chinese"}
    - utter_location_double_check
* inform{"location": "kolam"}
    - slot{"location": "kolam"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "kollam"}
    - slot{"location": "kollam"}
    - check_location
    - slot{"location": "kollam"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 9137649067584310607
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "hosur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hosur"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "mexican"}
    - utter_location_double_check
* inform{"location": "hosur"}
    - slot{"location": "hosur"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - check_location
    - slot{"location": "Bangalore"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 9137649067584310617
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "sira"}
    - slot{"cuisine": "italian"}
    - slot{"location": "sira"}
    - check_location_cuisine
    - slot{"location": null}
    - slot{"cuisine": "italian"}
    - utter_location_double_check
* inform{"location": "sira"}
    - slot{"location": "sira"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - check_location
    - slot{"location": "Mysore"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 3861834501880448470
* greet
    - utter_greet
* inform{"cuisine": "south indian", "location": "coimbatore", "price": "300"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "coimbatore"}
    - slot{"price": "300"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "south indian"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 3861834501880449470
* greet
    - utter_greet
* inform{"cuisine": "north indian", "location": "coimbatore", "price": "300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "coimbatore"}
    - slot{"price": "300"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "north indian"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 3861834501881449470
* greet
    - utter_greet
* inform{"cuisine": "north indian", "location": "salem", "price": "300"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "salem"}
    - slot{"price": "300"}
    - check_location_cuisine
    - slot{"location": "salem"}
    - slot{"cuisine": "north indian"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -2860248525296041096
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "bangalore", "price": "500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bangalore"}
    - slot{"price": "500"}
    - check_location_cuisine
    - slot{"location": "bangalore"}
    - slot{"cuisine": "chinese"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -2860248524296041096
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "bangalore", "price": "400"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": "400"}
    - check_location_cuisine
    - slot{"location": "bangalore"}
    - slot{"cuisine": "italian"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story -2860248524196041096
* greet
    - utter_greet
* inform{"cuisine": "mexican", "location": "mysore", "price": "600"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mysore"}
    - slot{"price": "600"}
    - check_location_cuisine
    - slot{"location": "mysore"}
    - slot{"cuisine": "mexican"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* deny
    - utter_goodbye
    - resetbot

## Generated Story 7561743720005979194
* greet
    - utter_greet
* inform{"cuisine": "mexican", "location": "coimbatore", "price": "500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "coimbatore"}
    - slot{"price": "500"}
    - check_location_cuisine
    - slot{"location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - check_price
    - slot{"price": null}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* affirm
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* option
    - utter_bonappetitnomail
    - resetbot

## Generated Story 5197546353686726968
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - check_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 6469791942071157616
* greet
    - utter_greet
* restaurant_search{"location": "ramnagar"}
    - slot{"location": "ramnagar"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - check_location
    - slot{"location": "kochi"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform
    - utter_bonappetitnomail
    - resetbot

## Generated Story 430177284235838979
* greet
    - utter_greet
* restaurant_search{"location": "saibabacolony"}
    - slot{"location": "saibabacolony"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "saibabacolony"}
    - slot{"location": "saibabacolony"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - check_location
    - slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot


## Generated Story 1822368715040285349
* greet
    - utter_greet
* restaurant_search{"location": "sripuram"}
    - slot{"location": "sripuram"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "sripuram"}
    - slot{"location": "sripuram"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - check_location
    - slot{"location": "jaipur"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 1822368715040281349
* greet
    - utter_greet
* restaurant_search{"location": "gandhipuram"}
    - slot{"location": "gandhipuram"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "gandhipuram"}
    - slot{"location": "gandhipuram"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "nellore"}
    - slot{"location": "nellore"}
    - check_location
    - slot{"location": "nellore"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 1822368715040281349
* greet
    - utter_greet
* restaurant_search{"location": "shantinagar"}
    - slot{"location": "shantinagar"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "shantinagar"}
    - slot{"location": "shantinagar"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "varanasi"}
    - slot{"location": "varanasi"}
    - check_location
    - slot{"location": "varanasi"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 5395614098693134793
* greet
    - utter_greet
* restaurant_search{"location": "koramangala"}
    - slot{"location": "koramangala"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "koramangala"}
    - slot{"location": "koramangala"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "nagpur"}
    - slot{"location": "nagpur"}
    - check_location
    - slot{"location": "nagpur"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "300"}
    - slot{"price": "300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "bdhs@dk.com"}
    - slot{"email": "bdhs@dk.com"}
    - check_email_id
    - slot{"email": "bdhs@dk.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -294688543478130212
* greet
    - utter_greet
* restaurant_search{"location": "ankali"}
    - slot{"location": "ankali"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "ankali"}
    - slot{"location": "ankali"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "sangli"}
    - slot{"location": "sangli"}
    - check_location
    - slot{"location": "sangli"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -4662966102728082173
* greet
    - utter_greet
* restaurant_search{"location": "daari"}
    - slot{"location": "daari"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "daari"}
    - slot{"location": "daari"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "jhansi"}
    - slot{"location": "jhansi"}
    - check_location
    - slot{"location": "jhansi"}
    - utter_ask_cuisine
* inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 4703533832846554857
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "inodre"}
    - slot{"location": "inodre"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "indore"}
    - slot{"location": "indore"}
    - check_location
    - slot{"location": "indore"}
    - utter_ask_cuisine
* inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "300-700"}
    - slot{"price": "300-700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "dhh@yh.com"}
    - slot{"email": "dhh@yh.com"}
    - check_email_id
    - slot{"email": "dhh@yh.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -6525384940825651933
* greet
    - utter_greet
* inform{"cuisine": "american", "location": "moradabad"}
    - slot{"cuisine": "american"}
    - slot{"location": "moradabad"}
    - check_location_cuisine
    - slot{"location": "moradabad"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "700"}
    - slot{"price": "700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 890616792180061203
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "bikaner"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bikaner"}
    - check_location_cuisine
    - slot{"location": "bikaner"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "<200"}
    - slot{"price": "<200"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">500"}
    - slot{"price": ">500"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 890616892180061203
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "solapur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "solapur"}
    - check_location_cuisine
    - slot{"location": "solapur"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<400"}
    - slot{"price": "<400"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">600"}
    - slot{"price": ">600"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -3816750027003218374
* greet
    - utter_greet
* restaurant_search{"location": "ranchi"}
    - slot{"location": "ranchi"}
    - check_location
    - slot{"location": "ranchi"}
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -3816750027003118374
* greet
    - utter_greet
* restaurant_search{"location": "ludhiana"}
    - slot{"location": "ludhiana"}
    - check_location
    - slot{"location": "ludhiana"}
    - utter_ask_cuisine
* inform{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "<300"}
    - slot{"price": "<300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -3816750027003218374
* greet
    - utter_greet
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - check_location
    - slot{"location": "patna"}
    - utter_ask_cuisine
* inform{"cuisine": "danish"}
    - slot{"cuisine": "danish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "<300"}
    - slot{"price": "<300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 4047370910718905482
* greet
    - utter_greet
* restaurant_search{"location": "indore"}
    - slot{"location": "indore"}
    - check_location
    - slot{"location": "indore"}
    - utter_ask_cuisine
* inform{"cuisine": "danish"}
    - slot{"cuisine": "danish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - check_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* inform{"price": "<500"}
    - slot{"price": "<500"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "timkoumar@gmail.com"}
    - slot{"email": "timkoumar@gmail.com"}
    - check_email_id
    - slot{"email": "timkoumar@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 4047270910718905482
* greet
    - utter_greet
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - check_location
    - slot{"location": "goa"}
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - check_cuisine
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* inform{"price": "<900"}
    - slot{"price": "<900"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* affirm
    - utter_ask_email
* inform{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - check_email_id
    - slot{"email": "test@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -524701826807488834
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "cuttak"}
    - slot{"location": "cuttak"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "cuttack"}
    - slot{"location": "cuttack"}
    - check_location
    - slot{"location": "cuttack"}
    - utter_ask_cuisine
* inform{"cuisine": "danish"}
    - slot{"cuisine": "danish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<500"}
    - slot{"price": "<500"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": null}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -524702826807488834
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "cbe"}
    - slot{"location": "cbe"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* inform{"cuisine": "danish"}
    - slot{"cuisine": "danish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<300"}
    - slot{"price": "<300"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": null}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story 2933006331160015641
* greet
    - utter_greet
* restaurant_search{"location": "conoor"}
    - slot{"location": "conoor"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "connoor"}
    - slot{"location": "connoor"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "durgapur"}
    - slot{"location": "durgapur"}
    - check_location
    - slot{"location": "durgapur"}
    - utter_ask_cuisine
* inform{"cuisine": "danish"}
    - slot{"cuisine": "danish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "<900"}
    - slot{"price": "<900"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "timkoumar@gmail.com"}
    - slot{"email": "timkoumar@gmail.com"}
    - check_email_id
    - slot{"email": "timkoumar@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 2933006339160015641
* greet
    - utter_greet
* restaurant_search{"location": "kotagiri"}
    - slot{"location": "kotagiri"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kotagiri"}
    - slot{"location": "kotagiri"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "raipur"}
    - slot{"location": "raipur"}
    - check_location
    - slot{"location": "raipur"}
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - check_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* inform{"price": "<900"}
    - slot{"price": "<900"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "test@gmail.com"}
    - slot{"email": "test@gmail.com"}
    - check_email_id
    - slot{"email": "test@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story 2933006339160015641
* greet
    - utter_greet
* restaurant_search{"location": "racecourse"}
    - slot{"location": "racecourse"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "racecourse"}
    - slot{"location": "racecourse"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<900"}
    - slot{"price": "<900"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "tgvh@gmail.com"}
    - slot{"email": "tgvh@gmail.com"}
    - check_email_id
    - slot{"email": "tgvh@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot

## Generated Story -3208130880009090652
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "hopecollege"}
    - slot{"location": "hopecollege"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "hopecollege"}
    - slot{"location": "hopecollege"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* option
    - utter_usetext
    - utter_ask_cuisine
* inform{"cuisine": "japanese"}
    - slot{"cuisine": "japanese"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* option
    - utter_usetext
    - utter_ask_price
* inform{"price": "<200"}
    - slot{"price": "<200"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -3208130980009090652
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "pellamedu"}
    - slot{"location": "pellamedu"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "pellamedu"}
    - slot{"location": "pellamedu"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* option
    - utter_usetext
    - utter_ask_cuisine
* inform{"cuisine": "swedish"}
    - slot{"cuisine": "swedish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* option
    - utter_usetext
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
    - check_price
    - slot{"price": "300_700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -8069402575189470336
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* inform{"location": "nelampur"}
    - slot{"location": "nelampur"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "nelampur"}
    - slot{"location": "nelampur"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "surat"}
    - slot{"location": "surat"}
    - check_location
    - slot{"location": "surat"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<300"}
    - slot{"price": "<300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* deny
    - utter_bonappetitnomail
    - resetbot

## Generated Story -6987570422906046575
* greet
    - utter_greet
* restaurant_search{"location": "kolam"}
    - slot{"location": "kolam"}
    - check_location
    - slot{"location": null}
    - utter_location_double_check
* inform{"location": "kolam"}
    - slot{"location": "kolam"}
    - check_location
    - slot{"location": null}
    - utter_location_not_served
* inform{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - check_location
    - slot{"location": "coimbatore"}
    - utter_ask_cuisine
* inform{"cuisine": "irish"}
    - slot{"cuisine": "irish"}
    - check_cuisine
    - slot{"cuisine": null}
    - utter_cuisine_not_avilable
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": "<200"}
    - slot{"price": "<200"}
    - check_price
    - slot{"price": null}
    - utter_price_not_in_range
    - utter_ask_price
* inform{"price": "<300"}
    - slot{"price": "<300"}
    - check_price
    - slot{"price": "<300"}
    - action_restaurant
    - slot{"results": null}
    - utter_noresults
    - utter_ask_continue
* affirm
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - check_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* inform{"price": ">700"}
    - slot{"price": ">700"}
    - check_price
    - slot{"price": ">700"}
    - action_restaurant
    - slot{"results": "Available"}
    - utter_require_email
* inform{"email": "timkoumar@gmail.com"}
    - slot{"email": "timkoumar@gmail.com"}
    - check_email_id
    - slot{"email": "timkoumar@gmail.com"}
    - send_email
    - utter_bonappetitmail
    - resetbot