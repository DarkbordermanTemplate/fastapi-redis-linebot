from typing import List, Optional, Tuple

# pylint: disable=E0611
from pydantic import BaseModel

# pylint: enable=E0611


class Event(BaseModel):
    replyToken: Optional[str]
    type: str
    mode: str
    timestamp: int
    source: dict
    message: Optional[dict]


class TextMessage:
    """Line text message class"""

    text = ""

    def __init__(self, text: str):
        self.text = text

    def format(self) -> dict:
        """Return format for messaging API"""
        return {"type": "text", "text": self.text}


class QuickReplyMessage(TextMessage):
    """
    A QuickReply message
    Combination of TextMessage and reply options
    """

    quick_replies = []

    def __init__(self, text: str, quick_replies: List[Tuple[str, str]]):
        super().__init__(text)
        self.quick_replies = quick_replies

    def format(self):
        """Return format for messaging API"""
        payload = super().format()
        payload["quickReply"] = {"items": []}
        for item in self.quick_replies:
            payload["quickReply"]["items"].append(
                {
                    "type": "action",
                    "action": {"type": "message", "label": item[0], "text": item[1]},
                }
            )
        return payload
