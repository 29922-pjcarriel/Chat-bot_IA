# actions.py
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Muestra el mensaje de bienvenida automático
        dispatcher.utter_message(text="👋 ¡Hola! Soy tu asistente de comandos Linux. Puedo ayudarte a aprender los comandos más útiles del sistema. 😊")

        return []
