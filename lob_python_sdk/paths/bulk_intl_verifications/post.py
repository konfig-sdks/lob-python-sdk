# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from lob_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from lob_python_sdk.api_response import AsyncGeneratorResponse
from lob_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lob_python_sdk import schemas  # noqa: F401

from lob_python_sdk.model.intl_verifications import IntlVerifications as IntlVerificationsSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.multiple_components_intl import MultipleComponentsIntl as MultipleComponentsIntlSchema
from lob_python_sdk.model.intl_verifications_payload import IntlVerificationsPayload as IntlVerificationsPayloadSchema

from lob_python_sdk.type.intl_verifications import IntlVerifications
from lob_python_sdk.type.multiple_components_intl import MultipleComponentsIntl
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.intl_verifications_payload import IntlVerificationsPayload

from ...api_client import Dictionary
from lob_python_sdk.pydantic.intl_verifications_payload import IntlVerificationsPayload as IntlVerificationsPayloadPydantic
from lob_python_sdk.pydantic.multiple_components_intl import MultipleComponentsIntl as MultipleComponentsIntlPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.intl_verifications import IntlVerifications as IntlVerificationsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = IntlVerificationsPayloadSchema
SchemaForRequestBodyMultipartFormData = IntlVerificationsPayloadSchema


request_body_intl_verifications_payload = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
_auth = [
    'basicAuth',
]
RatelimitLimitSchema = schemas.IntSchema
ratelimit_limit_parameter = api_client.HeaderParameter(
    name="ratelimit-limit",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RatelimitLimitSchema,
)
RatelimitRemainingSchema = schemas.IntSchema
ratelimit_remaining_parameter = api_client.HeaderParameter(
    name="ratelimit-remaining",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RatelimitRemainingSchema,
)
RatelimitResetSchema = schemas.IntSchema
ratelimit_reset_parameter = api_client.HeaderParameter(
    name="ratelimit-reset",
    style=api_client.ParameterStyle.SIMPLE,
    schema=RatelimitResetSchema,
)
SchemaFor200ResponseBodyApplicationJson = IntlVerificationsSchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'ratelimit-limit': RatelimitLimitSchema,
        'ratelimit-remaining': RatelimitRemainingSchema,
        'ratelimit-reset': RatelimitResetSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: IntlVerifications


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IntlVerifications


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        ratelimit_limit_parameter,
        ratelimit_remaining_parameter,
        ratelimit_reset_parameter,
    ]
)
SchemaFor0ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Error


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _verify_bulk_addresses_mapped_args(
        self,
        addresses: typing.List[MultipleComponentsIntl],
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if addresses is not None:
            _body["addresses"] = addresses
        args.body = _body
        return args

    async def _averify_bulk_addresses_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Bulk Verify
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bulk/intl_verifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_intl_verifications_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _verify_bulk_addresses_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Bulk Verify
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/bulk/intl_verifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_intl_verifications_payload.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class VerifyBulkAddressesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def averify_bulk_addresses(
        self,
        addresses: typing.List[MultipleComponentsIntl],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_bulk_addresses_mapped_args(
            addresses=addresses,
        )
        return await self._averify_bulk_addresses_oapg(
            body=args.body,
            **kwargs,
        )
    
    def verify_bulk_addresses(
        self,
        addresses: typing.List[MultipleComponentsIntl],
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_bulk_addresses_mapped_args(
            addresses=addresses,
        )
        return self._verify_bulk_addresses_oapg(
            body=args.body,
        )

class VerifyBulkAddresses(BaseApi):

    async def averify_bulk_addresses(
        self,
        addresses: typing.List[MultipleComponentsIntl],
        validate: bool = False,
        **kwargs,
    ) -> IntlVerificationsPydantic:
        raw_response = await self.raw.averify_bulk_addresses(
            addresses=addresses,
            **kwargs,
        )
        if validate:
            return IntlVerificationsPydantic(**raw_response.body)
        return api_client.construct_model_instance(IntlVerificationsPydantic, raw_response.body)
    
    
    def verify_bulk_addresses(
        self,
        addresses: typing.List[MultipleComponentsIntl],
        validate: bool = False,
    ) -> IntlVerificationsPydantic:
        raw_response = self.raw.verify_bulk_addresses(
            addresses=addresses,
        )
        if validate:
            return IntlVerificationsPydantic(**raw_response.body)
        return api_client.construct_model_instance(IntlVerificationsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        addresses: typing.List[MultipleComponentsIntl],
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verify_bulk_addresses_mapped_args(
            addresses=addresses,
        )
        return await self._averify_bulk_addresses_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        addresses: typing.List[MultipleComponentsIntl],
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verify_bulk_addresses_mapped_args(
            addresses=addresses,
        )
        return self._verify_bulk_addresses_oapg(
            body=args.body,
        )

