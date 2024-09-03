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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uma_auth.models.transaction_type import TransactionType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Transaction(BaseModel):
    """
    Transaction
    """ # noqa: E501
    type: TransactionType
    invoice: Optional[StrictStr] = Field(default=None, description="The full, encoded invoice.")
    description: Optional[StrictStr] = Field(default=None, description="The invoice's description.")
    description_hash: Optional[StrictStr] = Field(default=None, description="The invoice's description hash.")
    preimage: Optional[StrictStr] = Field(default=None, description="The payment preimage, optional if unpaid.")
    payment_hash: StrictStr = Field(description="Payment hash for the payment")
    amount: Annotated[int, Field(strict=True, gt=0)] = Field(description="Value in msats.")
    fees_paid: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Value in msats.")
    created_at: StrictInt = Field(description="The time the payment/invoice was created.")
    expires_at: Optional[StrictInt] = Field(default=None, description="The time the invoice expires.")
    settled_at: Optional[StrictInt] = Field(default=None, description="The time at which the transaction was settled, if it was settled.")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata attached to the invoice.")
    __properties: ClassVar[List[str]] = ["type", "invoice", "description", "description_hash", "preimage", "payment_hash", "amount", "fees_paid", "created_at", "expires_at", "settled_at", "metadata"]

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
        """Create an instance of Transaction from a JSON string"""
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
        # set to None if invoice (nullable) is None
        # and model_fields_set contains the field
        if self.invoice is None and "invoice" in self.model_fields_set:
            _dict['invoice'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if description_hash (nullable) is None
        # and model_fields_set contains the field
        if self.description_hash is None and "description_hash" in self.model_fields_set:
            _dict['description_hash'] = None

        # set to None if preimage (nullable) is None
        # and model_fields_set contains the field
        if self.preimage is None and "preimage" in self.model_fields_set:
            _dict['preimage'] = None

        # set to None if fees_paid (nullable) is None
        # and model_fields_set contains the field
        if self.fees_paid is None and "fees_paid" in self.model_fields_set:
            _dict['fees_paid'] = None

        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expires_at'] = None

        # set to None if settled_at (nullable) is None
        # and model_fields_set contains the field
        if self.settled_at is None and "settled_at" in self.model_fields_set:
            _dict['settled_at'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "invoice": obj.get("invoice"),
            "description": obj.get("description"),
            "description_hash": obj.get("description_hash"),
            "preimage": obj.get("preimage"),
            "payment_hash": obj.get("payment_hash"),
            "amount": obj.get("amount"),
            "fees_paid": obj.get("fees_paid"),
            "created_at": obj.get("created_at"),
            "expires_at": obj.get("expires_at"),
            "settled_at": obj.get("settled_at"),
            "metadata": obj.get("metadata")
        })
        return _obj


