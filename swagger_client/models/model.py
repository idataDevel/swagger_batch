# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.dataset import Dataset  # noqa: F401,E501
#from swagger_client.models.model import Model  # noqa: F401,E501


class Model(object):
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
        'id': 'str',
        'base_model': 'Model',
        'datasets': 'list[Dataset]',
        'model_kind': 'str',
        'name': 'str',
        'description': 'str',
        'properties': 'dict(str, str)',
        'locale': 'str',
        'created_date_time': 'datetime',
        'last_action_date_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'base_model': 'baseModel',
        'datasets': 'datasets',
        'model_kind': 'modelKind',
        'name': 'name',
        'description': 'description',
        'properties': 'properties',
        'locale': 'locale',
        'created_date_time': 'createdDateTime',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status'
    }

    def __init__(self, id=None, base_model=None, datasets=None, model_kind=None, name=None, description=None, properties=None, locale=None, created_date_time=None, last_action_date_time=None, status=None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._base_model = None
        self._datasets = None
        self._model_kind = None
        self._name = None
        self._description = None
        self._properties = None
        self._locale = None
        self._created_date_time = None
        self._last_action_date_time = None
        self._status = None
        self.discriminator = None

        self.id = id
        if base_model is not None:
            self.base_model = base_model
        if datasets is not None:
            self.datasets = datasets
        self.model_kind = model_kind
        self.name = name
        if description is not None:
            self.description = description
        if properties is not None:
            self.properties = properties
        if locale is not None:
            self.locale = locale
        self.created_date_time = created_date_time
        self.last_action_date_time = last_action_date_time
        self.status = status

    @property
    def id(self):
        """Gets the id of this Model.  # noqa: E501

        The identifier of this entity  # noqa: E501

        :return: The id of this Model.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.

        The identifier of this entity  # noqa: E501

        :param id: The id of this Model.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def base_model(self):
        """Gets the base_model of this Model.  # noqa: E501

        The base model used for adaptation  # noqa: E501

        :return: The base_model of this Model.  # noqa: E501
        :rtype: Model
        """
        return self._base_model

    @base_model.setter
    def base_model(self, base_model):
        """Sets the base_model of this Model.

        The base model used for adaptation  # noqa: E501

        :param base_model: The base_model of this Model.  # noqa: E501
        :type: Model
        """

        self._base_model = base_model

    @property
    def datasets(self):
        """Gets the datasets of this Model.  # noqa: E501

        Datasets used for adaptation  # noqa: E501

        :return: The datasets of this Model.  # noqa: E501
        :rtype: list[Dataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this Model.

        Datasets used for adaptation  # noqa: E501

        :param datasets: The datasets of this Model.  # noqa: E501
        :type: list[Dataset]
        """

        self._datasets = datasets

    @property
    def model_kind(self):
        """Gets the model_kind of this Model.  # noqa: E501

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :return: The model_kind of this Model.  # noqa: E501
        :rtype: str
        """
        return self._model_kind

    @model_kind.setter
    def model_kind(self, model_kind):
        """Sets the model_kind of this Model.

        The kind of this model (e.g. acoustic, language ...)  # noqa: E501

        :param model_kind: The model_kind of this Model.  # noqa: E501
        :type: str
        """
        if model_kind is None:
            raise ValueError("Invalid value for `model_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Acoustic", "Language", "AcousticAndLanguage", "CustomVoice", "LanguageGeneration", "Sentiment", "LanguageIdentification", "Diarization"]  # noqa: E501
        if model_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `model_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(model_kind, allowed_values)
            )

        self._model_kind = model_kind

    @property
    def name(self):
        """Gets the name of this Model.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.

        The name of the object  # noqa: E501

        :param name: The name of this Model.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Model.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.

        The description of the object  # noqa: E501

        :param description: The description of this Model.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this Model.  # noqa: E501

        The custom properties of this entity  # noqa: E501

        :return: The properties of this Model.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Model.

        The custom properties of this entity  # noqa: E501

        :param properties: The properties of this Model.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def locale(self):
        """Gets the locale of this Model.  # noqa: E501

        The locale of the contained data  # noqa: E501

        :return: The locale of this Model.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Model.

        The locale of the contained data  # noqa: E501

        :param locale: The locale of this Model.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Model.  # noqa: E501

        The time-stamp when the object was created  # noqa: E501

        :return: The created_date_time of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Model.

        The time-stamp when the object was created  # noqa: E501

        :param created_date_time: The created_date_time of this Model.  # noqa: E501
        :type: datetime
        """
        if created_date_time is None:
            raise ValueError("Invalid value for `created_date_time`, must not be `None`")  # noqa: E501

        self._created_date_time = created_date_time

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Model.  # noqa: E501

        The time-stamp when the current status was entered  # noqa: E501

        :return: The last_action_date_time of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Model.

        The time-stamp when the current status was entered  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Model.  # noqa: E501
        :type: datetime
        """
        if last_action_date_time is None:
            raise ValueError("Invalid value for `last_action_date_time`, must not be `None`")  # noqa: E501

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Model.  # noqa: E501

        The status of the object  # noqa: E501

        :return: The status of this Model.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Model.

        The status of the object  # noqa: E501

        :param status: The status of this Model.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Succeeded", "Failed", "NotStarted", "Running"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(Model, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
