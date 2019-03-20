# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice. The base path for all the APIs is \"/api/v1\".   # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PutVariantRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'key': 'str',
        'attachment': 'object'
    }

    attribute_map = {
        'key': 'key',
        'attachment': 'attachment'
    }

    def __init__(self, key=None, attachment=None):  # noqa: E501
        """PutVariantRequest - a model defined in Swagger"""  # noqa: E501

        self._key = None
        self._attachment = None
        self.discriminator = None

        self.key = key
        if attachment is not None:
            self.attachment = attachment

    @property
    def key(self):
        """Gets the key of this PutVariantRequest.  # noqa: E501


        :return: The key of this PutVariantRequest.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PutVariantRequest.


        :param key: The key of this PutVariantRequest.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if key is not None and len(key) < 1:
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501

        self._key = key

    @property
    def attachment(self):
        """Gets the attachment of this PutVariantRequest.  # noqa: E501


        :return: The attachment of this PutVariantRequest.  # noqa: E501
        :rtype: object
        """
        return self._attachment

    @attachment.setter
    def attachment(self, attachment):
        """Sets the attachment of this PutVariantRequest.


        :param attachment: The attachment of this PutVariantRequest.  # noqa: E501
        :type: object
        """

        self._attachment = attachment

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PutVariantRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
