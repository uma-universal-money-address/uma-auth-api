from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth import util


class PayInvoiceResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, preimage=None, total_budget_currency_amount=None):  # noqa: E501
        """PayInvoiceResponse - a model defined in OpenAPI

        :param preimage: The preimage of this PayInvoiceResponse.  # noqa: E501
        :type preimage: str
        :param total_budget_currency_amount: The total_budget_currency_amount of this PayInvoiceResponse.  # noqa: E501
        :type total_budget_currency_amount: int
        """
        self.openapi_types = {
            'preimage': str,
            'total_budget_currency_amount': int
        }

        self.attribute_map = {
            'preimage': 'preimage',
            'total_budget_currency_amount': 'total_budget_currency_amount'
        }

        self._preimage = preimage
        self._total_budget_currency_amount = total_budget_currency_amount

    @classmethod
    def from_dict(cls, dikt) -> 'PayInvoiceResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PayInvoiceResponse of this PayInvoiceResponse.  # noqa: E501
        :rtype: PayInvoiceResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def preimage(self) -> str:
        """Gets the preimage of this PayInvoiceResponse.

        The preimage of the payment.  # noqa: E501

        :return: The preimage of this PayInvoiceResponse.
        :rtype: str
        """
        return self._preimage

    @preimage.setter
    def preimage(self, preimage: str):
        """Sets the preimage of this PayInvoiceResponse.

        The preimage of the payment.  # noqa: E501

        :param preimage: The preimage of this PayInvoiceResponse.
        :type preimage: str
        """
        if preimage is None:
            raise ValueError("Invalid value for `preimage`, must not be `None`")  # noqa: E501

        self._preimage = preimage

    @property
    def total_budget_currency_amount(self) -> int:
        """Gets the total_budget_currency_amount of this PayInvoiceResponse.

        The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null.   # noqa: E501

        :return: The total_budget_currency_amount of this PayInvoiceResponse.
        :rtype: int
        """
        return self._total_budget_currency_amount

    @total_budget_currency_amount.setter
    def total_budget_currency_amount(self, total_budget_currency_amount: int):
        """Sets the total_budget_currency_amount of this PayInvoiceResponse.

        The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null.   # noqa: E501

        :param total_budget_currency_amount: The total_budget_currency_amount of this PayInvoiceResponse.
        :type total_budget_currency_amount: int
        """
        if total_budget_currency_amount is not None and total_budget_currency_amount <= 0:  # noqa: E501
            raise ValueError("Invalid value for `total_budget_currency_amount`, must be a value greater than `0`")  # noqa: E501

        self._total_budget_currency_amount = total_budget_currency_amount
