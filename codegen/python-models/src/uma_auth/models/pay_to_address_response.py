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




from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uma_auth.models.quote import Quote
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PayToAddressResponse(BaseModel):
    """
    PayToAddressResponse
    """ # noqa: E501
    preimage: StrictStr = Field(description="The preimage of the payment.")
    quote: Quote
    total_budget_currency_amount: Optional[Annotated[int, Field(strict=True, gt=0)]] = Field(default=None, description="The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null. ")
    __properties: ClassVar[List[str]] = ["preimage", "quote", "total_budget_currency_amount"]

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
        """Create an instance of PayToAddressResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of quote
        if self.quote:
            _dict['quote'] = self.quote.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PayToAddressResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "preimage": obj.get("preimage"),
            "quote": Quote.from_dict(obj.get("quote")) if obj.get("quote") is not None else None,
            "total_budget_currency_amount": obj.get("total_budget_currency_amount")
        })
        return _obj


