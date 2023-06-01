# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.configuration import Server
from whatsappcloudapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from whatsappcloudapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from whatsappcloudapi.models.get_business_profile_id_response import GetBusinessProfileIDResponse
from whatsappcloudapi.models.success_response import SuccessResponse


class BusinessProfilesController(BaseController):

    """A Controller to access Endpoints in the whatsappcloudapi API."""
    def __init__(self, config):
        super(BusinessProfilesController, self).__init__(config)

    def get_business_profile_id(self,
                                phone_number_id,
                                fields=None):
        """Does a GET request to /{Phone-Number-ID}/whatsapp_business_profile.

        Use this endpoint to retrieve your business’ profile. This business
        profile is visible to consumers in the chat thread next to the profile
        photo. The profile information will contain a business profile ID
        which you can use to make API calls.

        Args:
            phone_number_id (string): TODO: type description here.
            fields (string, optional): Here you can specify what you want to
                know from your business as a comma separated list of fields.
                Available fields include: id, about, messaging_product,
                address, description, vertical, email, websites,
                profile_picture_url

        Returns:
            GetBusinessProfileIDResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{Phone-Number-ID}/whatsapp_business_profile')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('Phone-Number-ID')
                            .value(phone_number_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('fields')
                         .value(fields))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetBusinessProfileIDResponse.from_dictionary)
        ).execute()

    def update_business_profile(self,
                                phone_number_id,
                                body):
        """Does a POST request to /{Phone-Number-ID}/whatsapp_business_profile.

        Use this endpoint to update your business’ profile information such as
        the business description, email or address.

        Args:
            phone_number_id (string): TODO: type description here.
            body (UpdateBusinessProfileRequest): TODO: type description here.

        Returns:
            SuccessResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{Phone-Number-ID}/whatsapp_business_profile')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('Phone-Number-ID')
                            .value(phone_number_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SuccessResponse.from_dictionary)
        ).execute()