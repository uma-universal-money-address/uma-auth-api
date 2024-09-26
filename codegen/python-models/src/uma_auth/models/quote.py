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
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from uma_auth.models.currency import Currency
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Quote(BaseModel):
    """
    Quote
    """ # noqa: E501
    sending_currency: Currency
    receiving_currency: Currency
    payment_hash: StrictStr = Field(description="The payment hash of the quote. Used as an identifier to execute the quote.")
    expires_at: StrictInt = Field(description="The time the quote expires in unix timestamp.")
    multiplier: Union[Annotated[float, Field(strict=True, gt=0)], Annotated[int, Field(strict=True, gt=0)]] = Field(description="Number of sending currency units per receiving currency unit.")
    fees: Annotated[int, Field(strict=True, ge=0)] = Field(description="The fees associated with the quote in the smallest unit of the sending currency (eg. cents).")
    total_sending_amount: Annotated[int, Field(strict=True, gt=0)] = Field(description="The total amount that will be sent in the smallest unit of the sending currency (eg. cents).")
    total_receiving_amount: Annotated[int, Field(strict=True, gt=0)] = Field(description="The total amount that will be received in the smallest unit of the receiving currency (eg. cents).")
    created_at: StrictInt = Field(description="The time the quote was created in unix timestamp.")
    __properties: ClassVar[List[str]] = ["sending_currency", "receiving_currency", "payment_hash", "expires_at", "multiplier", "fees", "total_sending_amount", "total_receiving_amount", "created_at"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return self.model_dump_json(by_alias=True, exclude_unset=True)

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Quote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            mode="json",
            by_alias=True,
            exclude={
            },
            exclude_none=True,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of sending_currency
        if self.sending_currency:
            _dict['sending_currency'] = self.sending_currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of receiving_currency
        if self.receiving_currency:
            _dict['receiving_currency'] = self.receiving_currency.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Quote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sending_currency": Currency.from_dict(obj.get("sending_currency")) if obj.get("sending_currency") is not None else None,
            "receiving_currency": Currency.from_dict(obj.get("receiving_currency")) if obj.get("receiving_currency") is not None else None,
            "payment_hash": obj.get("payment_hash"),
            "expires_at": obj.get("expires_at"),
            "multiplier": obj.get("multiplier"),
            "fees": obj.get("fees"),
            "total_sending_amount": obj.get("total_sending_amount"),
            "total_receiving_amount": obj.get("total_receiving_amount"),
            "created_at": obj.get("created_at")
        })
        return _obj


