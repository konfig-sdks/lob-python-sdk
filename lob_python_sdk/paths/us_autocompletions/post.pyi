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

from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.us_autocompletions import UsAutocompletions as UsAutocompletionsSchema
from lob_python_sdk.model.us_autocompletions_writable import UsAutocompletionsWritable as UsAutocompletionsWritableSchema

from lob_python_sdk.type.us_autocompletions_writable import UsAutocompletionsWritable
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.us_autocompletions import UsAutocompletions

from ...api_client import Dictionary
from lob_python_sdk.pydantic.us_autocompletions import UsAutocompletions as UsAutocompletionsPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.us_autocompletions_writable import UsAutocompletionsWritable as UsAutocompletionsWritablePydantic

# Query params


class CaseSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def UPPER(cls):
        return cls("upper")
    
    @schemas.classproperty
    def PROPER(cls):
        return cls("proper")


class ValidAddressesSchema(
    schemas.EnumBase,
    schemas.BoolSchema
):
    
    @schemas.classproperty
    def TRUE(cls):
        return cls(True)
    
    @schemas.classproperty
    def FALSE(cls):
        return cls(False)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'case': typing.Union[CaseSchema, str, ],
        'valid_addresses': typing.Union[ValidAddressesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_case = api_client.QueryParameter(
    name="case",
    style=api_client.ParameterStyle.FORM,
    schema=CaseSchema,
    explode=True,
)
request_query_valid_addresses = api_client.QueryParameter(
    name="valid_addresses",
    style=api_client.ParameterStyle.FORM,
    schema=ValidAddressesSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = UsAutocompletionsWritableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = UsAutocompletionsWritableSchema
SchemaForRequestBodyMultipartFormData = UsAutocompletionsWritableSchema


request_body_us_autocompletions_writable = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = UsAutocompletionsSchema
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
    body: UsAutocompletions


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: UsAutocompletions


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

    def _get_suggestions_mapped_args(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if address_prefix is not None:
            _body["address_prefix"] = address_prefix
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if zip_code is not None:
            _body["zip_code"] = zip_code
        if geo_ip_sort is not None:
            _body["geo_ip_sort"] = geo_ip_sort
        args.body = _body
        if case is not None:
            _query_params["case"] = case
        if valid_addresses is not None:
            _query_params["valid_addresses"] = valid_addresses
        args.query = _query_params
        return args

    async def _aget_suggestions_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Autocomplete
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_case,
            request_query_valid_addresses,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/us_autocompletions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_us_autocompletions_writable.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_suggestions_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Autocomplete
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_case,
            request_query_valid_addresses,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
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
            path_template='/us_autocompletions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_us_autocompletions_writable.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetSuggestionsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_suggestions(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_suggestions_mapped_args(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
        )
        return await self._aget_suggestions_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def get_suggestions(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_suggestions_mapped_args(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
        )
        return self._get_suggestions_oapg(
            body=args.body,
            query_params=args.query,
        )

class GetSuggestions(BaseApi):

    async def aget_suggestions(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> UsAutocompletionsPydantic:
        raw_response = await self.raw.aget_suggestions(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
            **kwargs,
        )
        if validate:
            return UsAutocompletionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(UsAutocompletionsPydantic, raw_response.body)
    
    
    def get_suggestions(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> UsAutocompletionsPydantic:
        raw_response = self.raw.get_suggestions(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
        )
        if validate:
            return UsAutocompletionsPydantic(**raw_response.body)
        return api_client.construct_model_instance(UsAutocompletionsPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_suggestions_mapped_args(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
        )
        return await self._aget_suggestions_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        address_prefix: str,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip_code: typing.Optional[str] = None,
        geo_ip_sort: typing.Optional[bool] = None,
        case: typing.Optional[str] = None,
        valid_addresses: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_suggestions_mapped_args(
            address_prefix=address_prefix,
            city=city,
            state=state,
            zip_code=zip_code,
            geo_ip_sort=geo_ip_sort,
            case=case,
            valid_addresses=valid_addresses,
        )
        return self._get_suggestions_oapg(
            body=args.body,
            query_params=args.query,
        )

