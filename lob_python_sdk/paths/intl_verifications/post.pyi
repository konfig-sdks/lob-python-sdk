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

from lob_python_sdk.model.secondary_line import SecondaryLine as SecondaryLineSchema
from lob_python_sdk.model.postal_code import PostalCode as PostalCodeSchema
from lob_python_sdk.model.intl_verification_writable import IntlVerificationWritable as IntlVerificationWritableSchema
from lob_python_sdk.model.primary_line import PrimaryLine as PrimaryLineSchema
from lob_python_sdk.model.recipient import Recipient as RecipientSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.city import City as CitySchema
from lob_python_sdk.model.intl_verification import IntlVerification as IntlVerificationSchema
from lob_python_sdk.model.country_extended import CountryExtended as CountryExtendedSchema

from lob_python_sdk.type.country_extended import CountryExtended
from lob_python_sdk.type.city import City
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.intl_verification import IntlVerification
from lob_python_sdk.type.intl_verification_writable import IntlVerificationWritable
from lob_python_sdk.type.primary_line import PrimaryLine
from lob_python_sdk.type.postal_code import PostalCode
from lob_python_sdk.type.secondary_line import SecondaryLine
from lob_python_sdk.type.recipient import Recipient

from ...api_client import Dictionary
from lob_python_sdk.pydantic.country_extended import CountryExtended as CountryExtendedPydantic
from lob_python_sdk.pydantic.postal_code import PostalCode as PostalCodePydantic
from lob_python_sdk.pydantic.secondary_line import SecondaryLine as SecondaryLinePydantic
from lob_python_sdk.pydantic.recipient import Recipient as RecipientPydantic
from lob_python_sdk.pydantic.city import City as CityPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.intl_verification import IntlVerification as IntlVerificationPydantic
from lob_python_sdk.pydantic.primary_line import PrimaryLine as PrimaryLinePydantic
from lob_python_sdk.pydantic.intl_verification_writable import IntlVerificationWritable as IntlVerificationWritablePydantic

# Header params


class XLangOutputSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def NATIVE(cls):
        return cls("native")
    
    @schemas.classproperty
    def MATCH(cls):
        return cls("match")
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-lang-output': typing.Union[XLangOutputSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_lang_output = api_client.HeaderParameter(
    name="x-lang-output",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XLangOutputSchema,
)
# body param
SchemaForRequestBodyApplicationJson = IntlVerificationWritableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = IntlVerificationWritableSchema
SchemaForRequestBodyMultipartFormData = IntlVerificationWritableSchema


request_body_intl_verification_writable = api_client.RequestBody(
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
RatelimitLimitSchema = schemas.IntSchema
RatelimitRemainingSchema = schemas.IntSchema
RatelimitResetSchema = schemas.IntSchema
SchemaFor200ResponseBodyApplicationJson = IntlVerificationSchema
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
    body: IntlVerification


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: IntlVerification


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _verification_mapped_args(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if recipient is not None:
            _body["recipient"] = recipient
        if primary_line is not None:
            _body["primary_line"] = primary_line
        if secondary_line is not None:
            _body["secondary_line"] = secondary_line
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if postal_code is not None:
            _body["postal_code"] = postal_code
        if country is not None:
            _body["country"] = country
        if address is not None:
            _body["address"] = address
        args.body = body if body is not None else _body
        if x_lang_output is not None:
            _header_params["x-lang-output"] = x_lang_output
        args.header = _header_params
        return args

    async def _averification_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Single Verify
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_lang_output,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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
            path_template='/intl_verifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_intl_verification_writable.serialize(body, content_type)
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


    def _verification_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
        Single Verify
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_lang_output,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
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
            path_template='/intl_verifications',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_intl_verification_writable.serialize(body, content_type)
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


class VerificationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def averification(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verification_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
        )
        return await self._averification_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def verification(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verification_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
        )
        return self._verification_oapg(
            body=args.body,
            header_params=args.header,
        )

class Verification(BaseApi):

    async def averification(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> IntlVerificationPydantic:
        raw_response = await self.raw.averification(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
            **kwargs,
        )
        if validate:
            return RootModel[IntlVerificationPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntlVerificationPydantic, raw_response.body)
    
    
    def verification(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
        validate: bool = False,
    ) -> IntlVerificationPydantic:
        raw_response = self.raw.verification(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
        )
        if validate:
            return RootModel[IntlVerificationPydantic](raw_response.body).root
        return api_client.construct_model_instance(IntlVerificationPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._verification_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
        )
        return await self._averification_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        body: typing.Optional[IntlVerificationWritable] = None,
        recipient: typing.Optional[Recipient] = None,
        primary_line: typing.Optional[PrimaryLine] = None,
        secondary_line: typing.Optional[SecondaryLine] = None,
        city: typing.Optional[City] = None,
        state: typing.Optional[str] = None,
        postal_code: typing.Optional[PostalCode] = None,
        country: typing.Optional[CountryExtended] = None,
        address: typing.Optional[str] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._verification_mapped_args(
            body=body,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            address=address,
            x_lang_output=x_lang_output,
        )
        return self._verification_oapg(
            body=args.body,
            header_params=args.header,
        )

