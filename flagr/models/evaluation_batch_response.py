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

from flagr.models.eval_result import EvalResult  # noqa: F401,E501


class EvaluationBatchResponse(object):
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
        'evaluation_results': 'list[EvalResult]'
    }

    attribute_map = {
        'evaluation_results': 'evaluationResults'
    }

    def __init__(self, evaluation_results=None):  # noqa: E501
        """EvaluationBatchResponse - a model defined in Swagger"""  # noqa: E501

        self._evaluation_results = None
        self.discriminator = None

        self.evaluation_results = evaluation_results

    @property
    def evaluation_results(self):
        """Gets the evaluation_results of this EvaluationBatchResponse.  # noqa: E501


        :return: The evaluation_results of this EvaluationBatchResponse.  # noqa: E501
        :rtype: list[EvalResult]
        """
        return self._evaluation_results

    @evaluation_results.setter
    def evaluation_results(self, evaluation_results):
        """Sets the evaluation_results of this EvaluationBatchResponse.


        :param evaluation_results: The evaluation_results of this EvaluationBatchResponse.  # noqa: E501
        :type: list[EvalResult]
        """
        if evaluation_results is None:
            raise ValueError("Invalid value for `evaluation_results`, must not be `None`")  # noqa: E501

        self._evaluation_results = evaluation_results

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
        if not isinstance(other, EvaluationBatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
