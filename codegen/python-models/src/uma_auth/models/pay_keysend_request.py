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
from uma_auth.models.pay_keysend_request_tlv_records_inner import PayKeysendRequestTlvRecordsInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class PayKeysendRequest(BaseModel):
    """
    PayKeysendRequest
    """ # noqa: E501
    amount: Annotated[int, Field(strict=True, gt=0)] = Field(description="The amount to pay in msats.")
    pubkey: StrictStr = Field(description="The public key of the receiver's node.")
    preimage: Optional[StrictStr] = Field(default=None, description="Preimage of the payment.")
    tlv_records: Optional[List[PayKeysendRequestTlvRecordsInner]] = Field(default=None, description="The tlv records.")
    budget_currency_code: Optional[StrictStr] = Field(default=None, description="The code of the currency the sender used to set budget.  Optional if the budget is set to SAT.")
    __properties: ClassVar[List[str]] = ["amount", "pubkey", "preimage", "tlv_records", "budget_currency_code"]

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
        """Create an instance of PayKeysendRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tlv_records (list)
        _items = []
        if self.tlv_records:
            for _item in self.tlv_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tlv_records'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PayKeysendRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "pubkey": obj.get("pubkey"),
            "preimage": obj.get("preimage"),
            "tlv_records": [PayKeysendRequestTlvRecordsInner.from_dict(_item) for _item in obj.get("tlv_records")] if obj.get("tlv_records") is not None else None,
            "budget_currency_code": obj.get("budget_currency_code")
        })
        return _obj


