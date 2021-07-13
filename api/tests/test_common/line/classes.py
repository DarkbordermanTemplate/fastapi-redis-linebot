from common.line.classes import QuickReplyMessage, TextMessage

assert TextMessage("text").format() == {"text": "text", "type": "text"}
assert QuickReplyMessage("text", [("option", "reply")]).format() == {
    "quickReply": {
        "items": [
            {
                "action": {"label": "option", "text": "reply", "type": "message"},
                "type": "action",
            }
        ]
    },
    "text": "text",
    "type": "text",
}
