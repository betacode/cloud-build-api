# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found at https://build.cloud.unity3d.com/login/me  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ``` 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrgsorgidprojectsprojectidbuildtargetsFailureDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'label': 'str',
        'resolution_hint': 'str',
        'stages': 'list[ERRORUNKNOWN]',
        'failure_type': 'str',
        'count': 'float'
    }

    attribute_map = {
        'label': 'label',
        'resolution_hint': 'resolutionHint',
        'stages': 'stages',
        'failure_type': 'failureType',
        'count': 'count'
    }

    def __init__(self, label=None, resolution_hint=None, stages=None, failure_type=None, count=None):
        """
        OrgsorgidprojectsprojectidbuildtargetsFailureDetails - a model defined in Swagger
        """

        self._label = None
        self._resolution_hint = None
        self._stages = None
        self._failure_type = None
        self._count = None

        if label is not None:
          self.label = label
        if resolution_hint is not None:
          self.resolution_hint = resolution_hint
        if stages is not None:
          self.stages = stages
        if failure_type is not None:
          self.failure_type = failure_type
        if count is not None:
          self.count = count

    @property
    def label(self):
        """
        Gets the label of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :return: The label of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :param label: The label of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :type: str
        """

        self._label = label

    @property
    def resolution_hint(self):
        """
        Gets the resolution_hint of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :return: The resolution_hint of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :rtype: str
        """
        return self._resolution_hint

    @resolution_hint.setter
    def resolution_hint(self, resolution_hint):
        """
        Sets the resolution_hint of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :param resolution_hint: The resolution_hint of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :type: str
        """

        self._resolution_hint = resolution_hint

    @property
    def stages(self):
        """
        Gets the stages of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :return: The stages of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """
        Sets the stages of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :param stages: The stages of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :type: list[ERRORUNKNOWN]
        """

        self._stages = stages

    @property
    def failure_type(self):
        """
        Gets the failure_type of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :return: The failure_type of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :rtype: str
        """
        return self._failure_type

    @failure_type.setter
    def failure_type(self, failure_type):
        """
        Sets the failure_type of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :param failure_type: The failure_type of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :type: str
        """

        self._failure_type = failure_type

    @property
    def count(self):
        """
        Gets the count of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :return: The count of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.

        :param count: The count of this OrgsorgidprojectsprojectidbuildtargetsFailureDetails.
        :type: float
        """

        self._count = count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsFailureDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
