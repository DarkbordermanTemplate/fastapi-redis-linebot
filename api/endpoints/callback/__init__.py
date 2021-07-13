from endpoints.classes import Resource

from .post import DOC as post_doc
from .post import post

CALLBACK = [
    Resource(
        "POST", "/callback", post, "Line callback webhook", "Callback webhook", post_doc
    )
]
