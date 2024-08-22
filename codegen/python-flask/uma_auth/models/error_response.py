from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from uma_auth.models.base_model import Model
from uma_auth.models.error_code import ErrorCode
from uma_auth import util

from uma_auth.models.error_code import ErrorCode  # noqa: E501

class ErrorResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, message=None):  # noqa: E501
        """ErrorResponse - a model defined in OpenAPI

        :param code: The code of this ErrorResponse.  # noqa: E501
        :type code: ErrorCode
        :param message: The message of this ErrorResponse.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'code': ErrorCode,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ErrorResponse of this ErrorResponse.  # noqa: E501
        :rtype: ErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> ErrorCode:
        """Gets the code of this ErrorResponse.


        :return: The code of this ErrorResponse.
        :rtype: ErrorCode
        """
        return self._code

    @code.setter
    def code(self, code: ErrorCode):
        """Sets the code of this ErrorResponse.


        :param code: The code of this ErrorResponse.
        :type code: ErrorCode
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this ErrorResponse.

        The error message.  # noqa: E501

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this ErrorResponse.

        The error message.  # noqa: E501

        :param message: The message of this ErrorResponse.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
