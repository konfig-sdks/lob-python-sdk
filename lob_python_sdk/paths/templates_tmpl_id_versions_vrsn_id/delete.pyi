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

from lob_python_sdk.model.template_version_deletion import TemplateVersionDeletion as TemplateVersionDeletionSchema
from lob_python_sdk.model.tmpl_id import TmplId as TmplIdSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.vrsn_id import VrsnId as VrsnIdSchema

from lob_python_sdk.type.template_version_deletion import TemplateVersionDeletion
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.tmpl_id import TmplId
from lob_python_sdk.type.vrsn_id import VrsnId

from ...api_client import Dictionary
from lob_python_sdk.pydantic.vrsn_id import VrsnId as VrsnIdPydantic
from lob_python_sdk.pydantic.template_version_deletion import TemplateVersionDeletion as TemplateVersionDeletionPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.tmpl_id import TmplId as TmplIdPydantic

# Path params
TmplIdSchema = schemas.Schema
VrsnIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'tmpl_id': typing.Union[TmplIdSchema, ],
        'vrsn_id': typing.Union[VrsnIdSchema, ],
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
request_path_vrsn_id = api_client.PathParameter(
    name="vrsn_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VrsnIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = TemplateVersionDeletionSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TemplateVersionDeletion


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TemplateVersionDeletion


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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

    def _delete_version_mapped_args(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if tmpl_id is not None:
            _path_params["tmpl_id"] = tmpl_id
        if vrsn_id is not None:
            _path_params["vrsn_id"] = vrsn_id
        args.path = _path_params
        return args

    async def _adelete_version_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Delete
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tmpl_id,
            request_path_vrsn_id,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates/{tmpl_id}/versions/{vrsn_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _delete_version_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Delete
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_tmpl_id,
            request_path_vrsn_id,
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
        method = 'delete'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/templates/{tmpl_id}/versions/{vrsn_id}',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class DeleteVersionRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adelete_version(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_version_mapped_args(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
        )
        return await self._adelete_version_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete_version(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_version_mapped_args(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
        )
        return self._delete_version_oapg(
            path_params=args.path,
        )

class DeleteVersion(BaseApi):

    async def adelete_version(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
        validate: bool = False,
        **kwargs,
    ) -> TemplateVersionDeletionPydantic:
        raw_response = await self.raw.adelete_version(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
            **kwargs,
        )
        if validate:
            return TemplateVersionDeletionPydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateVersionDeletionPydantic, raw_response.body)
    
    
    def delete_version(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
        validate: bool = False,
    ) -> TemplateVersionDeletionPydantic:
        raw_response = self.raw.delete_version(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
        )
        if validate:
            return TemplateVersionDeletionPydantic(**raw_response.body)
        return api_client.construct_model_instance(TemplateVersionDeletionPydantic, raw_response.body)


class ApiFordelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def adelete(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._delete_version_mapped_args(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
        )
        return await self._adelete_version_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def delete(
        self,
        tmpl_id: TmplId,
        vrsn_id: VrsnId,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._delete_version_mapped_args(
            tmpl_id=tmpl_id,
            vrsn_id=vrsn_id,
        )
        return self._delete_version_oapg(
            path_params=args.path,
        )

