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


class Dataset(object):
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
        'data_import_kind': 'str',
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
        'data_import_kind': 'dataImportKind',
        'name': 'name',
        'description': 'description',
        'properties': 'properties',
        'locale': 'locale',
        'created_date_time': 'createdDateTime',
        'last_action_date_time': 'lastActionDateTime',
        'status': 'status'
    }

    def __init__(self, id=None, data_import_kind=None, name=None, description=None, properties=None, locale=None, created_date_time=None, last_action_date_time=None, status=None):  # noqa: E501
        """Dataset - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._data_import_kind = None
        self._name = None
        self._description = None
        self._properties = None
        self._locale = None
        self._created_date_time = None
        self._last_action_date_time = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.data_import_kind = data_import_kind
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
        """Gets the id of this Dataset.  # noqa: E501

        The identifier of this entity  # noqa: E501

        :return: The id of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Dataset.

        The identifier of this entity  # noqa: E501

        :param id: The id of this Dataset.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def data_import_kind(self):
        """Gets the data_import_kind of this Dataset.  # noqa: E501

        The kind of the dataset (e.g. acoustic data, language data ...)  # noqa: E501

        :return: The data_import_kind of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._data_import_kind

    @data_import_kind.setter
    def data_import_kind(self, data_import_kind):
        """Sets the data_import_kind of this Dataset.

        The kind of the dataset (e.g. acoustic data, language data ...)  # noqa: E501

        :param data_import_kind: The data_import_kind of this Dataset.  # noqa: E501
        :type: str
        """
        if data_import_kind is None:
            raise ValueError("Invalid value for `data_import_kind`, must not be `None`")  # noqa: E501
        allowed_values = ["None", "Language", "Acoustic", "Pronunciation", "CustomVoice", "LanguageGeneration", "AudioFiles"]  # noqa: E501
        if data_import_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `data_import_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(data_import_kind, allowed_values)
            )

        self._data_import_kind = data_import_kind

    @property
    def name(self):
        """Gets the name of this Dataset.  # noqa: E501

        The name of the object  # noqa: E501

        :return: The name of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Dataset.

        The name of the object  # noqa: E501

        :param name: The name of this Dataset.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Dataset.  # noqa: E501

        The description of the object  # noqa: E501

        :return: The description of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Dataset.

        The description of the object  # noqa: E501

        :param description: The description of this Dataset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def properties(self):
        """Gets the properties of this Dataset.  # noqa: E501

        The custom properties of this entity  # noqa: E501

        :return: The properties of this Dataset.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Dataset.

        The custom properties of this entity  # noqa: E501

        :param properties: The properties of this Dataset.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def locale(self):
        """Gets the locale of this Dataset.  # noqa: E501

        The locale of the contained data  # noqa: E501

        :return: The locale of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Dataset.

        The locale of the contained data  # noqa: E501

        :param locale: The locale of this Dataset.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def created_date_time(self):
        """Gets the created_date_time of this Dataset.  # noqa: E501

        The time-stamp when the object was created  # noqa: E501

        :return: The created_date_time of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this Dataset.

        The time-stamp when the object was created  # noqa: E501

        :param created_date_time: The created_date_time of this Dataset.  # noqa: E501
        :type: datetime
        """
        if created_date_time is None:
            raise ValueError("Invalid value for `created_date_time`, must not be `None`")  # noqa: E501

        self._created_date_time = created_date_time

    @property
    def last_action_date_time(self):
        """Gets the last_action_date_time of this Dataset.  # noqa: E501

        The time-stamp when the current status was entered  # noqa: E501

        :return: The last_action_date_time of this Dataset.  # noqa: E501
        :rtype: datetime
        """
        return self._last_action_date_time

    @last_action_date_time.setter
    def last_action_date_time(self, last_action_date_time):
        """Sets the last_action_date_time of this Dataset.

        The time-stamp when the current status was entered  # noqa: E501

        :param last_action_date_time: The last_action_date_time of this Dataset.  # noqa: E501
        :type: datetime
        """
        if last_action_date_time is None:
            raise ValueError("Invalid value for `last_action_date_time`, must not be `None`")  # noqa: E501

        self._last_action_date_time = last_action_date_time

    @property
    def status(self):
        """Gets the status of this Dataset.  # noqa: E501

        The status of the object  # noqa: E501

        :return: The status of this Dataset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Dataset.

        The status of the object  # noqa: E501

        :param status: The status of this Dataset.  # noqa: E501
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
        if issubclass(Dataset, dict):
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
        if not isinstance(other, Dataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
