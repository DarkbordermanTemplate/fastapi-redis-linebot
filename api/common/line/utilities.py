from typing import List

import requests
from config import Config
from loguru import logger
from requests import Response

from .classes import TextMessage


def push_message(user_id: str, messages: List[TextMessage]) -> Response:
    """
    Send message to line chatbot using push method

    Arguments:
        user_id (str): User ID
        message (TextMessage): Text Message to be sent

    Raises:
        Exception: Raise exception when response is not OK

    Returns:
        None
    """
    logger.info(
        f"Push message, user: {user_id} message: {[message.format() for message in messages]}"
    )

    try:
        return requests.post(
            "https://api.line.me/v2/bot/message/push",
            headers={
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": "Bearer " + Config.LINE_TOKEN,
            },
            json={
                "to": user_id,
                "messages": [message.format() for message in messages],
            },
        )
    except Exception as error:
        raise error


def reply_message(token: str, messages: List[TextMessage]) -> Response:
    """
    Send message to line chatbot using push method

    Arguments:
        token (str): Reply token
        message (TextMessage): Text Message to be sent

    Raises:
        Exception: Raise exception when response is not OK

    Returns:
        None
    """
    logger.info(
        f"Push message, token: {token} message: {[message.format() for message in messages]}"
    )

    try:
        return requests.post(
            "https://api.line.me/v2/bot/message/reply",
            headers={
                "Content-Type": "application/json; charset=UTF-8",
                "Authorization": "Bearer " + Config.LINE_TOKEN,
            },
            json={
                "replyToken": token,
                "messages": [message.format() for message in messages],
            },
        )
    except Exception as error:
        raise error
