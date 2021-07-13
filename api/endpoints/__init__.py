"""Routing table, gather route to main router for API"""
from typing import List

from endpoints.classes import Resource

from .callback import CALLBACK
from .health import HEALTH

RESOURCES: List[Resource] = HEALTH + CALLBACK
