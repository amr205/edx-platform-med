"""
MFE Context API Serializers
"""

from rest_framework import serializers


class ProvidersSerializer(serializers.Serializer):
    """
    Providers Serializers
    """

    id = serializers.CharField(allow_null=True)
    name = serializers.CharField(allow_null=True)
    iconClass = serializers.CharField(source='icon_class', allow_null=True)
    iconImage = serializers.CharField(source='icon_image', allow_null=True)
    skipHintedLogin = serializers.BooleanField(source='skip_hinted_login', default=False)
    loginUrl = serializers.CharField(source='login_url', allow_null=True)
    registerUrl = serializers.CharField(source='register_url', allow_null=True)


class PipelineUserDetailsSerializer(serializers.Serializer):
    """
    Pipeline User Details Serializers
    """

    username = serializers.CharField(allow_null=True)
    email = serializers.CharField(allow_null=True)
    name = serializers.CharField(source='fullname', allow_null=True)
    firstName = serializers.CharField(source='first_name', allow_null=True)
    lastName = serializers.CharField(source='last_name', allow_null=True)


class ContextDataSerializer(serializers.Serializer):
    """
    Context Data Serializers
    """

    currentProvider = serializers.CharField(source='current_provider', allow_null=True)
    platformName = serializers.CharField(source='platform_name', allow_null=True)
    providers = serializers.ListField(
        child=ProvidersSerializer(),
        allow_null=True
    )
    secondaryProviders = serializers.ListField(
        child=ProvidersSerializer(),
        source='secondary_providers',
        allow_null=True
    )
    finishAuthUrl = serializers.CharField(source='finish_auth_url', allow_null=True)
    errorMessage = serializers.CharField(source='error_message', allow_null=True)
    registerFormSubmitButtonText = serializers.CharField(source='register_form_submit_button_text', allow_null=True)
    syncLearnerProfileData = serializers.BooleanField(source='sync_learner_profile_data', allow_null=True)
    countryCode = serializers.CharField(source='country_code', allow_null=True)
    pipelineUserDetails = PipelineUserDetailsSerializer(source='pipeline_user_details', allow_null=True)


class MFEContextSerializer(serializers.Serializer):
    """
    Serializer class to convert the keys of MFE Context Response dict object to camelCase format.
    """

    contextData = ContextDataSerializer(
        source='context_data',
        default={}
    )
    registrationFields = serializers.DictField(
        source='registration_fields',
        default={}
    )
    optionalFields = serializers.DictField(
        source='optional_fields',
        default={
            'extended_profile': []
        }
    )
