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

from lob_python_sdk.model.template_version_writable import TemplateVersionWritable as TemplateVersionWritableSchema
from lob_python_sdk.model.tmpl_id import TmplId as TmplIdSchema
from lob_python_sdk.model.template_version import TemplateVersion as TemplateVersionSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.resource_description import ResourceDescription as ResourceDescriptionSchema
from lob_python_sdk.model.template_html import TemplateHtml as TemplateHtmlSchema
from lob_python_sdk.model.engine import Engine as EngineSchema
from lob_python_sdk.model.template_required_vars import TemplateRequiredVars as TemplateRequiredVarsSchema

from lob_python_sdk.type.template_version import TemplateVersion
from lob_python_sdk.type.template_html import TemplateHtml
from lob_python_sdk.type.template_required_vars import TemplateRequiredVars
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.engine import Engine
from lob_python_sdk.type.tmpl_id import TmplId
from lob_python_sdk.type.template_version_writable import TemplateVersionWritable

from ...api_client import Dictionary
from lob_python_sdk.pydantic.resource_description import ResourceDescription as ResourceDescriptionPydantic
from lob_python_sdk.pydantic.template_html import TemplateHtml as TemplateHtmlPydantic
from lob_python_sdk.pydantic.engine import Engine as EnginePydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.template_required_vars import TemplateRequiredVars as TemplateRequiredVarsPydantic
from lob_python_sdk.pydantic.template_version import TemplateVersion as TemplateVersionPydantic
from lob_python_sdk.pydantic.template_version_writable import TemplateVersionWritable as TemplateVersionWritablePydantic
from lob_python_sdk.pydantic.tmpl_id import TmplId as TmplIdPydantic

# Path params
TmplIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'tmpl_id': typing.Union[TmplIdSchema, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_tmpl_id = api_client.PathParameter(
    name="tmpl_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=TmplIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TemplateVersionWritableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = TemplateVersionWritableSchema
SchemaForRequestBodyMultipartFormData = TemplateVersionWritableSchema


request_body_template_version_writable = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = TemplateVersionSchema
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
    body: TemplateVersion


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TemplateVersion


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

    def _create_new_version_mapped_args(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if html is not None:
            _body["html"] = html
        if engine is not None:
            _body["engine"] = engine
        if required_vars is not None:
            _body["required_vars"] = required_vars
        args.body = _body
        if tmpl_id is not None:
            _path_params["tmpl_id"] = tmpl_id
        args.path = _path_params
        return args

    async def _acreate_new_version_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Create
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tmpl_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/templates/{tmpl_id}/versions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_template_version_writable.serialize(body, content_type)
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


    def _create_new_version_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Create
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tmpl_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
            path_template='/templates/{tmpl_id}/versions',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_template_version_writable.serialize(body, content_type)
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


class CreateNewVersionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_version(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_version_mapped_args(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
        )
        return await self._acreate_new_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_version(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_version_mapped_args(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
        )
        return self._create_new_version_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewVersion(BaseApi):

    async def acreate_new_version(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
        validate: bool = False,
        **kwargs,
    ) -> TemplateVersionPydantic:
        raw_response = await self.raw.acreate_new_version(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
            **kwargs,
        )
        if validate:
            return RootModel[TemplateVersionPydantic](raw_response.body).root
        return api_client.construct_model_instance(TemplateVersionPydantic, raw_response.body)
    
    
    def create_new_version(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
        validate: bool = False,
    ) -> TemplateVersionPydantic:
        raw_response = self.raw.create_new_version(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
        )
        if validate:
            return RootModel[TemplateVersionPydantic](raw_response.body).root
        return api_client.construct_model_instance(TemplateVersionPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_version_mapped_args(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
        )
        return await self._acreate_new_version_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        html: TemplateHtml,
        tmpl_id: TmplId,
        description: typing.Optional[ResourceDescription] = None,
        engine: typing.Optional[Engine] = None,
        required_vars: typing.Optional[TemplateRequiredVars] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_version_mapped_args(
            html=html,
            tmpl_id=tmpl_id,
            description=description,
            engine=engine,
            required_vars=required_vars,
        )
        return self._create_new_version_oapg(
            body=args.body,
            path_params=args.path,
        )

