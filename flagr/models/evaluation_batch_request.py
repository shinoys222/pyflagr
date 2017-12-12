# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flagr.models.evaluation_entity import EvaluationEntity  # noqa: F401,E501


class EvaluationBatchRequest(object):
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
        'entities': 'list[EvaluationEntity]',
        'enable_debug': 'bool',
        'flag_i_ds': 'list[int]'
    }

    attribute_map = {
        'entities': 'entities',
        'enable_debug': 'enableDebug',
        'flag_i_ds': 'flagIDs'
    }

    def __init__(self, entities=None, enable_debug=None, flag_i_ds=None):  # noqa: E501
        """EvaluationBatchRequest - a model defined in Swagger"""  # noqa: E501

        self._entities = None
        self._enable_debug = None
        self._flag_i_ds = None
        self.discriminator = None

        self.entities = entities
        if enable_debug is not None:
            self.enable_debug = enable_debug
        self.flag_i_ds = flag_i_ds

    @property
    def entities(self):
        """Gets the entities of this EvaluationBatchRequest.  # noqa: E501


        :return: The entities of this EvaluationBatchRequest.  # noqa: E501
        :rtype: list[EvaluationEntity]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this EvaluationBatchRequest.


        :param entities: The entities of this EvaluationBatchRequest.  # noqa: E501
        :type: list[EvaluationEntity]
        """
        if entities is None:
            raise ValueError("Invalid value for `entities`, must not be `None`")  # noqa: E501

        self._entities = entities

    @property
    def enable_debug(self):
        """Gets the enable_debug of this EvaluationBatchRequest.  # noqa: E501


        :return: The enable_debug of this EvaluationBatchRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_debug

    @enable_debug.setter
    def enable_debug(self, enable_debug):
        """Sets the enable_debug of this EvaluationBatchRequest.


        :param enable_debug: The enable_debug of this EvaluationBatchRequest.  # noqa: E501
        :type: bool
        """

        self._enable_debug = enable_debug

    @property
    def flag_i_ds(self):
        """Gets the flag_i_ds of this EvaluationBatchRequest.  # noqa: E501


        :return: The flag_i_ds of this EvaluationBatchRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._flag_i_ds

    @flag_i_ds.setter
    def flag_i_ds(self, flag_i_ds):
        """Sets the flag_i_ds of this EvaluationBatchRequest.


        :param flag_i_ds: The flag_i_ds of this EvaluationBatchRequest.  # noqa: E501
        :type: list[int]
        """
        if flag_i_ds is None:
            raise ValueError("Invalid value for `flag_i_ds`, must not be `None`")  # noqa: E501

        self._flag_i_ds = flag_i_ds

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
        if not isinstance(other, EvaluationBatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
