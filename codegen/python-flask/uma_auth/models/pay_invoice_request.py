from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth import util


class PayInvoiceRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, invoice=None, amount=None):  # noqa: E501
        """PayInvoiceRequest - a model defined in OpenAPI

        :param invoice: The invoice of this PayInvoiceRequest.  # noqa: E501
        :type invoice: str
        :param amount: The amount of this PayInvoiceRequest.  # noqa: E501
        :type amount: int
        """
        self.openapi_types = {
            'invoice': str,
            'amount': int
        }

        self.attribute_map = {
            'invoice': 'invoice',
            'amount': 'amount'
        }

        self._invoice = invoice
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'PayInvoiceRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PayInvoiceRequest of this PayInvoiceRequest.  # noqa: E501
        :rtype: PayInvoiceRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invoice(self) -> str:
        """Gets the invoice of this PayInvoiceRequest.

        The bolt11 invoice to pay.  # noqa: E501

        :return: The invoice of this PayInvoiceRequest.
        :rtype: str
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice: str):
        """Sets the invoice of this PayInvoiceRequest.

        The bolt11 invoice to pay.  # noqa: E501

        :param invoice: The invoice of this PayInvoiceRequest.
        :type invoice: str
        """
        if invoice is None:
            raise ValueError("Invalid value for `invoice`, must not be `None`")  # noqa: E501

        self._invoice = invoice

    @property
    def amount(self) -> int:
        """Gets the amount of this PayInvoiceRequest.

        The amount to pay for a 0-amount invoice.  # noqa: E501

        :return: The amount of this PayInvoiceRequest.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this PayInvoiceRequest.

        The amount to pay for a 0-amount invoice.  # noqa: E501

        :param amount: The amount of this PayInvoiceRequest.
        :type amount: int
        """
        if amount is not None and amount <= 0:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must be a value greater than `0`")  # noqa: E501

        self._amount = amount
