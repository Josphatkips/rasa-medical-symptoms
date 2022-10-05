# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionSymptoms(Action):

    def name(self) -> Text:
        return "action_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print('action_symptoms')
        return []
class ActionDiagnosis(Action):

    def name(self) -> Text:
        return "action_diagnosis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        myelements=[]
        payload = "/symptoms_intent{\"symptoms\":\"" + str('Cough') + "\"}"

        newobj={
                "title": "Cough",
                "subtitle": "Cough",
                # "image_url": content['thumbnail'],
                "buttons": [ 
                    
                    {
                    "title": "Cough",
                    # "url": row['listing_url'],
                    # "type": "web_url"
                    "type": "postback",
                    "payload":payload
                    },
                    
                ]
            }
        myelements.append(newobj)
        payload = "/symptoms_intent{\"symptoms\":\"" + str('Chest pain') + "\"}"

        newobj={
                "title": "Chest pain",
                "subtitle": "Chest pain",
                # "image_url": content['thumbnail'],
                "buttons": [ 
                    
                    {
                    "title": "Chest pain",
                    # "url": row['listing_url'],
                    # "type": "web_url"
                    "type": "postback",
                    "payload":payload
                    },
                    
                ]
            }
        myelements.append(newobj)
        message = {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": myelements
                        
                        }
                    }

            
        dispatcher.utter_message(attachment=message)

        dispatcher.utter_message(text="Hello World!")

        return []
