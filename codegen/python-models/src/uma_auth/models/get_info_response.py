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




from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from uma_auth.models.currency_preference import CurrencyPreference
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetInfoResponse(BaseModel):
    """
    GetInfoResponse
    """ # noqa: E501
    alias: Optional[StrictStr] = Field(default=None, description="The alias of the user's node.")
    color: Optional[StrictStr] = Field(default=None, description="The color of the user's node.")
    pubkey: StrictStr = Field(description="The pubkey of the user's node.")
    network: StrictStr = Field(description="The bitcoin network of the user's node.")
    block_height: Optional[StrictInt] = Field(default=None, description="The current block height of the user's node.")
    block_hash: Optional[StrictStr] = Field(default=None, description="The current block hash of the user's node.")
    methods: List[StrictStr] = Field(description="A list of supported methods for this connection.")
    lud16: Optional[StrictStr] = Field(default=None, description="The lightning or UMA address for the user.")
    currencies: Optional[List[CurrencyPreference]] = Field(default=None, description="The currencies the user's wallet supports. Ordered by preference. If not provided, assume this user only supports BTC.")
    __properties: ClassVar[List[str]] = ["alias", "color", "pubkey", "network", "block_height", "block_hash", "methods", "lud16", "currencies"]

    @field_validator('network')
    def network_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('regtest', 'signet', 'testnet', 'mainnet'):
            raise ValueError("must be one of enum values ('regtest', 'signet', 'testnet', 'mainnet')")
        return value

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
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GetInfoResponse from a JSON string"""
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
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in currencies (list)
        _items = []
        if self.currencies:
            for _item in self.currencies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['currencies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetInfoResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alias": obj.get("alias"),
            "color": obj.get("color"),
            "pubkey": obj.get("pubkey"),
            "network": obj.get("network"),
            "block_height": obj.get("block_height"),
            "block_hash": obj.get("block_hash"),
            "methods": obj.get("methods"),
            "lud16": obj.get("lud16"),
            "currencies": [CurrencyPreference.from_dict(_item) for _item in obj.get("currencies")] if obj.get("currencies") is not None else None
        })
        return _obj


