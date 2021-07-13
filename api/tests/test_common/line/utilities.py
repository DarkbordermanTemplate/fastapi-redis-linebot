from common.line.classes import TextMessage
from common.line.utilities import push_message, reply_message


def test_push_message(mocker):
    mocker.patch("requests.post")
    push_message("user_id", [TextMessage("text")])


def test_reply_message(mocker):
    mocker.patch("requests.post")
    reply_message("token", [TextMessage("text")])
