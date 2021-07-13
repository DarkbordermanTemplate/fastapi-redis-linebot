from cache import CacheUser
from common.line.classes import Event, QuickReplyMessage, TextMessage
from common.line.utilities import reply_message

from ..classes import State


class Question(State):
    name = "question"

    def execute(self, user_id="", payload: Event = None, **kwargs):
        user = CacheUser.get(user_id)
        # Check the user is in stage or not
        if user and user["state"] == self.name and user["machine"] == self.machine.name:
            try:
                answer = int(payload.message["text"])
                if answer == 2:
                    reply_message(payload.replyToken, TextMessage("Correct answer"))
                    return "Correct answer"
                reply_message(payload.replyToken, TextMessage("Incorrect answer"))
                return "Incorrect answer"
            except ValueError:
                reply_message(payload.replyToken, TextMessage("Invalid option"))
                return "Invalid option"
        # First time enter, the user will now keep in this stage until further reply
        # Setup the session
        CacheUser.set(user_id, {"machine": self.machine.name, "stage": self.name})
        reply_message(
            payload.replyToken,
            QuickReplyMessage("What is the result of 1+1 ?", [("2", "2"), ("1", "1")]),
        )
        return "OK"
