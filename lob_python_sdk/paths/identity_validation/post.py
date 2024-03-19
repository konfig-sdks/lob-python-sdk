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

from lob_python_sdk.model.urbanization import Urbanization as UrbanizationSchema
from lob_python_sdk.model.secondary_line import SecondaryLine as SecondaryLineSchema
from lob_python_sdk.model.recipient import Recipient as RecipientSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.primary_line_us import PrimaryLineUs as PrimaryLineUsSchema
from lob_python_sdk.model.identity_validation_writable import IdentityValidationWritable as IdentityValidationWritableSchema
from lob_python_sdk.model.identity_validation_company import IdentityValidationCompany as IdentityValidationCompanySchema
from lob_python_sdk.model.identity_validation import IdentityValidation as IdentityValidationSchema

from lob_python_sdk.type.identity_validation import IdentityValidation
from lob_python_sdk.type.identity_validation_company import IdentityValidationCompany
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.primary_line_us import PrimaryLineUs
from lob_python_sdk.type.urbanization import Urbanization
from lob_python_sdk.type.identity_validation_writable import IdentityValidationWritable
from lob_python_sdk.type.secondary_line import SecondaryLine
from lob_python_sdk.type.recipient import Recipient

from ...api_client import Dictionary
from lob_python_sdk.pydantic.identity_validation import IdentityValidation as IdentityValidationPydantic
from lob_python_sdk.pydantic.urbanization import Urbanization as UrbanizationPydantic
from lob_python_sdk.pydantic.identity_validation_company import IdentityValidationCompany as IdentityValidationCompanyPydantic
from lob_python_sdk.pydantic.secondary_line import SecondaryLine as SecondaryLinePydantic
from lob_python_sdk.pydantic.recipient import Recipient as RecipientPydantic
from lob_python_sdk.pydantic.primary_line_us import PrimaryLineUs as PrimaryLineUsPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.identity_validation_writable import IdentityValidationWritable as IdentityValidationWritablePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = IdentityValidationWritableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = IdentityValidationWritableSchema
SchemaForRequestBodyMultipartFormData = IdentityValidationWritableSchema


request_body_identity_validation_writable = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
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
SchemaFor200ResponseBodyApplicationJson = IdentityValidationSchema
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
    body: IdentityValidation


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IdentityValidation


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

    def _validation_mapped_args(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if recipient is not None:
            _body["recipient"] = recipient
        if primary_line is not None:
            _body["primary_line"] = primary_line
        if secondary_line is not None:
            _body["secondary_line"] = secondary_line
        if urbanization is not None:
            _body["urbanization"] = urbanization
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if zip_code is not None:
            _body["zip_code"] = zip_code
        if company is not None:
            _body["company"] = company
        args.body = body if body is not None else _body
        return args

    async def _avalidation_oapg(
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
        Identity Validation
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
            path_template='/identity_validation',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_identity_validation_writable.serialize(body, content_type)
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


    def _validation_oapg(
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
        Identity Validation
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
            path_template='/identity_validation',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_identity_validation_writable.serialize(body, content_type)
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


class ValidationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def avalidation(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validation_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
        )
        return await self._avalidation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def validation(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validation_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
        )
        return self._validation_oapg(
            body=args.body,
        )

class Validation(BaseApi):

    async def avalidation(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
        validate: bool = False,
        **kwargs,
    ) -> IdentityValidationPydantic:
        raw_response = await self.raw.avalidation(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
            **kwargs,
        )
        if validate:
            return RootModel[IdentityValidationPydantic](raw_response.body).root
        return api_client.construct_model_instance(IdentityValidationPydantic, raw_response.body)
    
    
    def validation(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
        validate: bool = False,
    ) -> IdentityValidationPydantic:
        raw_response = self.raw.validation(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
        )
        if validate:
            return RootModel[IdentityValidationPydantic](raw_response.body).root
        return api_client.construct_model_instance(IdentityValidationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._validation_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
        )
        return await self._avalidation_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        body: IdentityValidationWritable,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLineUs] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        urbanization: typing.Optional[Urbanization] = None,
        city: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        company: typing.Optional[IdentityValidationCompany] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._validation_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            city=city,
            state=state,
            zip_code=zip_code,
            company=company,
        )
        return self._validation_oapg(
            body=args.body,
        )

