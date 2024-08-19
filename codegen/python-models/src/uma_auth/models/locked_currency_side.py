# coding: utf-8

"""
    UMA Auth API

    This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.

    The version of the OpenAPI document: 0.1
    Contact: info@lightspark.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class LockedCurrencySide(str, Enum):
    """
    The side of the quote which should be locked and specified in the `locked_currency_amount`. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \"sending\", and the `locked_currency_amount` to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \"receiving\" and the `locked_currency_amount` to 10000 (in cents).
    """

    """
    allowed enum values
    """
    SENDING = 'sending'
    RECEIVING = 'receiving'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LockedCurrencySide from a JSON string"""
        return cls(json.loads(json_str))

