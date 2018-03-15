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


class OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles(object):
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
        'build_bundles': 'bool',
        'base_path': 'str',
        'build_asset_bundle_options': 'str',
        'copy_to_streaming_assets': 'bool',
        'copy_bundle_patterns': 'list[str]'
    }

    attribute_map = {
        'build_bundles': 'buildBundles',
        'base_path': 'basePath',
        'build_asset_bundle_options': 'buildAssetBundleOptions',
        'copy_to_streaming_assets': 'copyToStreamingAssets',
        'copy_bundle_patterns': 'copyBundlePatterns'
    }

    def __init__(self, build_bundles=None, base_path=None, build_asset_bundle_options=None, copy_to_streaming_assets=None, copy_bundle_patterns=None):
        """
        OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles - a model defined in Swagger
        """

        self._build_bundles = None
        self._base_path = None
        self._build_asset_bundle_options = None
        self._copy_to_streaming_assets = None
        self._copy_bundle_patterns = None

        if build_bundles is not None:
          self.build_bundles = build_bundles
        if base_path is not None:
          self.base_path = base_path
        if build_asset_bundle_options is not None:
          self.build_asset_bundle_options = build_asset_bundle_options
        if copy_to_streaming_assets is not None:
          self.copy_to_streaming_assets = copy_to_streaming_assets
        if copy_bundle_patterns is not None:
          self.copy_bundle_patterns = copy_bundle_patterns

    @property
    def build_bundles(self):
        """
        Gets the build_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        enable asset bundle builds for this target

        :return: The build_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :rtype: bool
        """
        return self._build_bundles

    @build_bundles.setter
    def build_bundles(self, build_bundles):
        """
        Sets the build_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        enable asset bundle builds for this target

        :param build_bundles: The build_bundles of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :type: bool
        """

        self._build_bundles = build_bundles

    @property
    def base_path(self):
        """
        Gets the base_path of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        base path relative to Assets folder where asset bundles are output. Default is 'AssetBundles'

        :return: The base_path of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """
        Sets the base_path of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        base path relative to Assets folder where asset bundles are output. Default is 'AssetBundles'

        :param base_path: The base_path of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :type: str
        """

        self._base_path = base_path

    @property
    def build_asset_bundle_options(self):
        """
        Gets the build_asset_bundle_options of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        comma separated list of flags from BuildAssetBundleOptions. see https://docs.unity3d.com/ScriptReference/BuildAssetBundleOptions.html

        :return: The build_asset_bundle_options of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :rtype: str
        """
        return self._build_asset_bundle_options

    @build_asset_bundle_options.setter
    def build_asset_bundle_options(self, build_asset_bundle_options):
        """
        Sets the build_asset_bundle_options of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        comma separated list of flags from BuildAssetBundleOptions. see https://docs.unity3d.com/ScriptReference/BuildAssetBundleOptions.html

        :param build_asset_bundle_options: The build_asset_bundle_options of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :type: str
        """

        self._build_asset_bundle_options = build_asset_bundle_options

    @property
    def copy_to_streaming_assets(self):
        """
        Gets the copy_to_streaming_assets of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        copy bundles to streaming assets folder, which will be packaged into the exported player.

        :return: The copy_to_streaming_assets of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :rtype: bool
        """
        return self._copy_to_streaming_assets

    @copy_to_streaming_assets.setter
    def copy_to_streaming_assets(self, copy_to_streaming_assets):
        """
        Sets the copy_to_streaming_assets of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        copy bundles to streaming assets folder, which will be packaged into the exported player.

        :param copy_to_streaming_assets: The copy_to_streaming_assets of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :type: bool
        """

        self._copy_to_streaming_assets = copy_to_streaming_assets

    @property
    def copy_bundle_patterns(self):
        """
        Gets the copy_bundle_patterns of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        array of patterns to match (C# Regular Expressions) when copying asset bundle files. By default, all bundles will be copied.

        :return: The copy_bundle_patterns of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :rtype: list[str]
        """
        return self._copy_bundle_patterns

    @copy_bundle_patterns.setter
    def copy_bundle_patterns(self, copy_bundle_patterns):
        """
        Sets the copy_bundle_patterns of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        array of patterns to match (C# Regular Expressions) when copying asset bundle files. By default, all bundles will be copied.

        :param copy_bundle_patterns: The copy_bundle_patterns of this OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles.
        :type: list[str]
        """

        self._copy_bundle_patterns = copy_bundle_patterns

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
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsSettingsAdvancedUnityAssetBundles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
