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

from lob_python_sdk.model.link_response import LinkResponse as LinkResponseSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.link_single import LinkSingle as LinkSingleSchema

from lob_python_sdk.type.link_single import LinkSingle
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.link_response import LinkResponse

from ...api_client import Dictionary
from lob_python_sdk.pydantic.link_single import LinkSingle as LinkSinglePydantic
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.link_response import LinkResponse as LinkResponsePydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic

# Path params
LinkIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'link_id': typing.Union[LinkIdSchema, str, ],
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


request_path_link_id = api_client.PathParameter(
    name="link_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=LinkIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = LinkSingleSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = LinkSingleSchema
SchemaForRequestBodyMultipartFormData = LinkSingleSchema


request_body_link_single = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = LinkResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LinkResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LinkResponse


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

    def _update_mapped_args(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if redirect_link is not None:
            _body["redirect_link"] = redirect_link
        if domain is not None:
            _body["domain"] = domain
        if slug is not None:
            _body["slug"] = slug
        if metadata_tag is not None:
            _body["metadata_tag"] = metadata_tag
        if billing_group_id is not None:
            _body["billing_group_id"] = billing_group_id
        args.body = _body
        if link_id is not None:
            _path_params["link_id"] = link_id
        args.path = _path_params
        return args

    async def _aupdate_oapg(
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
        Update a Link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_link_id,
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
        method = 'patch'.upper()
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
            path_template='/links/{link_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_link_single.serialize(body, content_type)
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


    def _update_oapg(
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
        Update a Link
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_link_id,
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
        method = 'patch'.upper()
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
            path_template='/links/{link_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_link_single.serialize(body, content_type)
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


class UpdateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_mapped_args(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
        )
        return await self._aupdate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_mapped_args(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
        )
        return self._update_oapg(
            body=args.body,
            path_params=args.path,
        )

class Update(BaseApi):

    async def aupdate(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LinkResponsePydantic:
        raw_response = await self.raw.aupdate(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
            **kwargs,
        )
        if validate:
            return LinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinkResponsePydantic, raw_response.body)
    
    
    def update(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LinkResponsePydantic:
        raw_response = self.raw.update(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
        )
        if validate:
            return LinkResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinkResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_mapped_args(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
        )
        return await self._aupdate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        redirect_link: str,
        link_id: str,
        domain: typing.Optional[str] = None,
        slug: typing.Optional[str] = None,
        metadata_tag: typing.Optional[Metadata] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_mapped_args(
            redirect_link=redirect_link,
            link_id=link_id,
            domain=domain,
            slug=slug,
            metadata_tag=metadata_tag,
            billing_group_id=billing_group_id,
        )
        return self._update_oapg(
            body=args.body,
            path_params=args.path,
        )

