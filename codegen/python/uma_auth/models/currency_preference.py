from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth import util


class CurrencyPreference(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, symbol=None, name=None, multiplier=None, decimals=None, min=None, max=None):  # noqa: E501
        """CurrencyPreference - a model defined in OpenAPI

        :param code: The code of this CurrencyPreference.  # noqa: E501
        :type code: str
        :param symbol: The symbol of this CurrencyPreference.  # noqa: E501
        :type symbol: str
        :param name: The name of this CurrencyPreference.  # noqa: E501
        :type name: str
        :param multiplier: The multiplier of this CurrencyPreference.  # noqa: E501
        :type multiplier: float
        :param decimals: The decimals of this CurrencyPreference.  # noqa: E501
        :type decimals: float
        :param min: The min of this CurrencyPreference.  # noqa: E501
        :type min: float
        :param max: The max of this CurrencyPreference.  # noqa: E501
        :type max: float
        """
        self.openapi_types = {
            'code': str,
            'symbol': str,
            'name': str,
            'multiplier': float,
            'decimals': float,
            'min': float,
            'max': float
        }

        self.attribute_map = {
            'code': 'code',
            'symbol': 'symbol',
            'name': 'name',
            'multiplier': 'multiplier',
            'decimals': 'decimals',
            'min': 'min',
            'max': 'max'
        }

        self._code = code
        self._symbol = symbol
        self._name = name
        self._multiplier = multiplier
        self._decimals = decimals
        self._min = min
        self._max = max

    @classmethod
    def from_dict(cls, dikt) -> 'CurrencyPreference':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CurrencyPreference of this CurrencyPreference.  # noqa: E501
        :rtype: CurrencyPreference
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this CurrencyPreference.

        The ISO-4217 currency code.  # noqa: E501

        :return: The code of this CurrencyPreference.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this CurrencyPreference.

        The ISO-4217 currency code.  # noqa: E501

        :param code: The code of this CurrencyPreference.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def symbol(self) -> str:
        """Gets the symbol of this CurrencyPreference.

        The currency symbol.  # noqa: E501

        :return: The symbol of this CurrencyPreference.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this CurrencyPreference.

        The currency symbol.  # noqa: E501

        :param symbol: The symbol of this CurrencyPreference.
        :type symbol: str
        """
        if symbol is None:
            raise ValueError("Invalid value for `symbol`, must not be `None`")  # noqa: E501

        self._symbol = symbol

    @property
    def name(self) -> str:
        """Gets the name of this CurrencyPreference.

        The currency name.  # noqa: E501

        :return: The name of this CurrencyPreference.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this CurrencyPreference.

        The currency name.  # noqa: E501

        :param name: The name of this CurrencyPreference.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def multiplier(self) -> float:
        """Gets the multiplier of this CurrencyPreference.

        Estimated number of milli-sats per smallest unit of this currency (eg. cents) If base_sending_currency_code was specified, this is the rate relative to that currency instead of milli-sats.  # noqa: E501

        :return: The multiplier of this CurrencyPreference.
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier: float):
        """Sets the multiplier of this CurrencyPreference.

        Estimated number of milli-sats per smallest unit of this currency (eg. cents) If base_sending_currency_code was specified, this is the rate relative to that currency instead of milli-sats.  # noqa: E501

        :param multiplier: The multiplier of this CurrencyPreference.
        :type multiplier: float
        """
        if multiplier is None:
            raise ValueError("Invalid value for `multiplier`, must not be `None`")  # noqa: E501

        self._multiplier = multiplier

    @property
    def decimals(self) -> float:
        """Gets the decimals of this CurrencyPreference.

        Number of digits after the decimal point for display on the sender side, and to add clarity around what the \"smallest unit\" of the currency is. For example, in USD, by convention, there are 2 digits for cents - $5.95. In this case, `decimals` would be 2. Note that the multiplier is still always in the smallest unit (cents). In addition to display purposes, this field can be used to resolve ambiguity in what the multiplier means. For example, if the currency is \"BTC\" and the multiplier is 1000, really we're exchanging in SATs, so `decimals` would be 8.  # noqa: E501

        :return: The decimals of this CurrencyPreference.
        :rtype: float
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals: float):
        """Sets the decimals of this CurrencyPreference.

        Number of digits after the decimal point for display on the sender side, and to add clarity around what the \"smallest unit\" of the currency is. For example, in USD, by convention, there are 2 digits for cents - $5.95. In this case, `decimals` would be 2. Note that the multiplier is still always in the smallest unit (cents). In addition to display purposes, this field can be used to resolve ambiguity in what the multiplier means. For example, if the currency is \"BTC\" and the multiplier is 1000, really we're exchanging in SATs, so `decimals` would be 8.  # noqa: E501

        :param decimals: The decimals of this CurrencyPreference.
        :type decimals: float
        """
        if decimals is None:
            raise ValueError("Invalid value for `decimals`, must not be `None`")  # noqa: E501

        self._decimals = decimals

    @property
    def min(self) -> float:
        """Gets the min of this CurrencyPreference.

        The minimum amount that can be received in this currency.  # noqa: E501

        :return: The min of this CurrencyPreference.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min: float):
        """Sets the min of this CurrencyPreference.

        The minimum amount that can be received in this currency.  # noqa: E501

        :param min: The min of this CurrencyPreference.
        :type min: float
        """
        if min is None:
            raise ValueError("Invalid value for `min`, must not be `None`")  # noqa: E501

        self._min = min

    @property
    def max(self) -> float:
        """Gets the max of this CurrencyPreference.

        The maximum amount that can be received in this currency.  # noqa: E501

        :return: The max of this CurrencyPreference.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max: float):
        """Sets the max of this CurrencyPreference.

        The maximum amount that can be received in this currency.  # noqa: E501

        :param max: The max of this CurrencyPreference.
        :type max: float
        """
        if max is None:
            raise ValueError("Invalid value for `max`, must not be `None`")  # noqa: E501

        self._max = max