from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth.models.quote import Quote
from uma_auth import util

from uma_auth.models.quote import Quote  # noqa: E501

class PayToAddressResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, preimage=None, quote=None, total_budget_currency_amount=None):  # noqa: E501
        """PayToAddressResponse - a model defined in OpenAPI

        :param preimage: The preimage of this PayToAddressResponse.  # noqa: E501
        :type preimage: str
        :param quote: The quote of this PayToAddressResponse.  # noqa: E501
        :type quote: Quote
        :param total_budget_currency_amount: The total_budget_currency_amount of this PayToAddressResponse.  # noqa: E501
        :type total_budget_currency_amount: int
        """
        self.openapi_types = {
            'preimage': str,
            'quote': Quote,
            'total_budget_currency_amount': int
        }

        self.attribute_map = {
            'preimage': 'preimage',
            'quote': 'quote',
            'total_budget_currency_amount': 'total_budget_currency_amount'
        }

        self._preimage = preimage
        self._quote = quote
        self._total_budget_currency_amount = total_budget_currency_amount

    @classmethod
    def from_dict(cls, dikt) -> 'PayToAddressResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PayToAddressResponse of this PayToAddressResponse.  # noqa: E501
        :rtype: PayToAddressResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def preimage(self) -> str:
        """Gets the preimage of this PayToAddressResponse.

        The preimage of the payment.  # noqa: E501

        :return: The preimage of this PayToAddressResponse.
        :rtype: str
        """
        return self._preimage

    @preimage.setter
    def preimage(self, preimage: str):
        """Sets the preimage of this PayToAddressResponse.

        The preimage of the payment.  # noqa: E501

        :param preimage: The preimage of this PayToAddressResponse.
        :type preimage: str
        """
        if preimage is None:
            raise ValueError("Invalid value for `preimage`, must not be `None`")  # noqa: E501

        self._preimage = preimage

    @property
    def quote(self) -> Quote:
        """Gets the quote of this PayToAddressResponse.


        :return: The quote of this PayToAddressResponse.
        :rtype: Quote
        """
        return self._quote

    @quote.setter
    def quote(self, quote: Quote):
        """Sets the quote of this PayToAddressResponse.


        :param quote: The quote of this PayToAddressResponse.
        :type quote: Quote
        """
        if quote is None:
            raise ValueError("Invalid value for `quote`, must not be `None`")  # noqa: E501

        self._quote = quote

    @property
    def total_budget_currency_amount(self) -> int:
        """Gets the total_budget_currency_amount of this PayToAddressResponse.

        The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null.   # noqa: E501

        :return: The total_budget_currency_amount of this PayToAddressResponse.
        :rtype: int
        """
        return self._total_budget_currency_amount

    @total_budget_currency_amount.setter
    def total_budget_currency_amount(self, total_budget_currency_amount: int):
        """Sets the total_budget_currency_amount of this PayToAddressResponse.

        The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null.   # noqa: E501

        :param total_budget_currency_amount: The total_budget_currency_amount of this PayToAddressResponse.
        :type total_budget_currency_amount: int
        """
        if total_budget_currency_amount is not None and total_budget_currency_amount <= 0:  # noqa: E501
            raise ValueError("Invalid value for `total_budget_currency_amount`, must be a value greater than `0`")  # noqa: E501

        self._total_budget_currency_amount = total_budget_currency_amount
