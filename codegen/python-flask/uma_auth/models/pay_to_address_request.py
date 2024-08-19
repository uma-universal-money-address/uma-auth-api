from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth import util


class PayToAddressRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, receiver_address=None, sending_currency_code=None, sending_currency_amount=None, receiving_currency_code=None):  # noqa: E501
        """PayToAddressRequest - a model defined in OpenAPI

        :param receiver_address: The receiver_address of this PayToAddressRequest.  # noqa: E501
        :type receiver_address: str
        :param sending_currency_code: The sending_currency_code of this PayToAddressRequest.  # noqa: E501
        :type sending_currency_code: str
        :param sending_currency_amount: The sending_currency_amount of this PayToAddressRequest.  # noqa: E501
        :type sending_currency_amount: int
        :param receiving_currency_code: The receiving_currency_code of this PayToAddressRequest.  # noqa: E501
        :type receiving_currency_code: str
        """
        self.openapi_types = {
            'receiver_address': str,
            'sending_currency_code': str,
            'sending_currency_amount': int,
            'receiving_currency_code': str
        }

        self.attribute_map = {
            'receiver_address': 'receiver_address',
            'sending_currency_code': 'sending_currency_code',
            'sending_currency_amount': 'sending_currency_amount',
            'receiving_currency_code': 'receiving_currency_code'
        }

        self._receiver_address = receiver_address
        self._sending_currency_code = sending_currency_code
        self._sending_currency_amount = sending_currency_amount
        self._receiving_currency_code = receiving_currency_code

    @classmethod
    def from_dict(cls, dikt) -> 'PayToAddressRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PayToAddressRequest of this PayToAddressRequest.  # noqa: E501
        :rtype: PayToAddressRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def receiver_address(self) -> str:
        """Gets the receiver_address of this PayToAddressRequest.

        The LUD16 address to pay.  # noqa: E501

        :return: The receiver_address of this PayToAddressRequest.
        :rtype: str
        """
        return self._receiver_address

    @receiver_address.setter
    def receiver_address(self, receiver_address: str):
        """Sets the receiver_address of this PayToAddressRequest.

        The LUD16 address to pay.  # noqa: E501

        :param receiver_address: The receiver_address of this PayToAddressRequest.
        :type receiver_address: str
        """
        if receiver_address is None:
            raise ValueError("Invalid value for `receiver_address`, must not be `None`")  # noqa: E501

        self._receiver_address = receiver_address

    @property
    def sending_currency_code(self) -> str:
        """Gets the sending_currency_code of this PayToAddressRequest.

        The code of the currency being sent from the sender's wallet.  # noqa: E501

        :return: The sending_currency_code of this PayToAddressRequest.
        :rtype: str
        """
        return self._sending_currency_code

    @sending_currency_code.setter
    def sending_currency_code(self, sending_currency_code: str):
        """Sets the sending_currency_code of this PayToAddressRequest.

        The code of the currency being sent from the sender's wallet.  # noqa: E501

        :param sending_currency_code: The sending_currency_code of this PayToAddressRequest.
        :type sending_currency_code: str
        """
        if sending_currency_code is None:
            raise ValueError("Invalid value for `sending_currency_code`, must not be `None`")  # noqa: E501

        self._sending_currency_code = sending_currency_code

    @property
    def sending_currency_amount(self) -> int:
        """Gets the sending_currency_amount of this PayToAddressRequest.

        The amount to send in the smallest unit of the sending currency (eg. cents).  # noqa: E501

        :return: The sending_currency_amount of this PayToAddressRequest.
        :rtype: int
        """
        return self._sending_currency_amount

    @sending_currency_amount.setter
    def sending_currency_amount(self, sending_currency_amount: int):
        """Sets the sending_currency_amount of this PayToAddressRequest.

        The amount to send in the smallest unit of the sending currency (eg. cents).  # noqa: E501

        :param sending_currency_amount: The sending_currency_amount of this PayToAddressRequest.
        :type sending_currency_amount: int
        """
        if sending_currency_amount is None:
            raise ValueError("Invalid value for `sending_currency_amount`, must not be `None`")  # noqa: E501
        if sending_currency_amount is not None and sending_currency_amount <= 0:  # noqa: E501
            raise ValueError("Invalid value for `sending_currency_amount`, must be a value greater than `0`")  # noqa: E501

        self._sending_currency_amount = sending_currency_amount

    @property
    def receiving_currency_code(self) -> str:
        """Gets the receiving_currency_code of this PayToAddressRequest.

        The code of the currency being received by the receiver. If not provided, the receiver's default currency will be used.  # noqa: E501

        :return: The receiving_currency_code of this PayToAddressRequest.
        :rtype: str
        """
        return self._receiving_currency_code

    @receiving_currency_code.setter
    def receiving_currency_code(self, receiving_currency_code: str):
        """Sets the receiving_currency_code of this PayToAddressRequest.

        The code of the currency being received by the receiver. If not provided, the receiver's default currency will be used.  # noqa: E501

        :param receiving_currency_code: The receiving_currency_code of this PayToAddressRequest.
        :type receiving_currency_code: str
        """

        self._receiving_currency_code = receiving_currency_code
