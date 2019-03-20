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


class Constraint(object):
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
        'id': 'int',
        '_property': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_property': 'property',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, id=None, _property=None, operator=None, value=None):  # noqa: E501
        """Constraint - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self.__property = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self._property = _property
        self.operator = operator
        self.value = value

    @property
    def id(self):
        """Gets the id of this Constraint.  # noqa: E501


        :return: The id of this Constraint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Constraint.


        :param id: The id of this Constraint.  # noqa: E501
        :type: int
        """
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def _property(self):
        """Gets the _property of this Constraint.  # noqa: E501


        :return: The _property of this Constraint.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this Constraint.


        :param _property: The _property of this Constraint.  # noqa: E501
        :type: str
        """
        if _property is None:
            raise ValueError("Invalid value for `_property`, must not be `None`")  # noqa: E501
        if _property is not None and len(_property) < 1:
            raise ValueError("Invalid value for `_property`, length must be greater than or equal to `1`")  # noqa: E501

        self.__property = _property

    @property
    def operator(self):
        """Gets the operator of this Constraint.  # noqa: E501


        :return: The operator of this Constraint.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Constraint.


        :param operator: The operator of this Constraint.  # noqa: E501
        :type: str
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501
        allowed_values = ["EQ", "NEQ", "LT", "LTE", "GT", "GTE", "EREG", "NEREG", "IN", "NOTIN", "CONTAINS", "NOTCONTAINS"]  # noqa: E501
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator` ({0}), must be one of {1}"  # noqa: E501
                .format(operator, allowed_values)
            )

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this Constraint.  # noqa: E501


        :return: The value of this Constraint.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Constraint.


        :param value: The value of this Constraint.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, Constraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
