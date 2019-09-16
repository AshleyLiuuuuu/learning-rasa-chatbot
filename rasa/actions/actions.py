from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json

def Post_http(temp):
    post_url = "http://dora-query-engine.leandata.top/query"
    headers = {'content-type':'application/json'}
    body = {'q':temp,'modelName':'dm_articles'}
    _response = requests.post(post_url,data = json.dumps(body),headers = headers)
    return _response.json()
class ActionAnalyseMonthly(Action):
   def name(self):
      return "action_month"
   def run(self,
           dispatcher,
           tracker,
           domain):
        print(tracker)
        msg = tracker.latest_message['text']
        temp = ""
        name = tracker.latest_message['intent'].get("name")
        if(name is None):
             temp = msg
        else:
            value = tracker.get_slot('keywords')
            if(value):
                 temp = "{} sort:term:asc group by publish_time monthly".format(value)
            else:
                temp = msg
        return_slots = []
        print(temp)
        rsp = Post_http(temp)
        dispatcher.utter_message("{}".format(rsp))
        for slot in tracker.slots:
                return_slots.append(SlotSet(slot, None))
        return return_slots

class ActionAnalyseYearly(Action):
   def name(self):
      return "action_year"
   def run(self,
           dispatcher,
           tracker,
           domain):
        value = tracker.get_slot('keywords')
        temp = ""
        msg = tracker.latest_message['text']
        name = tracker.latest_message['intent'].get("name")
        if(name is None):
            temp = msg
        else:
            if (value):
                temp = "{} sort:term:asc group by publish_time yearly".format(value)
            else:
                temp = msg
        print(temp)
        rsp = Post_http(temp)
        dispatcher.utter_message("{}".format(rsp))
        return_slots = []
        print(rsp)
        for slot in tracker.slots:
            return_slots.append(SlotSet(slot, None))
        return return_slots
