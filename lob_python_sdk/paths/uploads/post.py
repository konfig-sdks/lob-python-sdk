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

from lob_python_sdk.model.required_address_column_mapping import RequiredAddressColumnMapping as RequiredAddressColumnMappingSchema
from lob_python_sdk.model.upload import Upload as UploadSchema
from lob_python_sdk.model.uploads_metadata import UploadsMetadata as UploadsMetadataSchema
from lob_python_sdk.model.upload_create_response import UploadCreateResponse as UploadCreateResponseSchema
from lob_python_sdk.model.optional_address_column_mapping import OptionalAddressColumnMapping as OptionalAddressColumnMappingSchema
from lob_python_sdk.model.upload_writable import UploadWritable as UploadWritableSchema

from lob_python_sdk.type.upload_create_response import UploadCreateResponse
from lob_python_sdk.type.upload_writable import UploadWritable
from lob_python_sdk.type.uploads_metadata import UploadsMetadata
from lob_python_sdk.type.required_address_column_mapping import RequiredAddressColumnMapping
from lob_python_sdk.type.upload import Upload
from lob_python_sdk.type.optional_address_column_mapping import OptionalAddressColumnMapping

from ...api_client import Dictionary
from lob_python_sdk.pydantic.upload_writable import UploadWritable as UploadWritablePydantic
from lob_python_sdk.pydantic.optional_address_column_mapping import OptionalAddressColumnMapping as OptionalAddressColumnMappingPydantic
from lob_python_sdk.pydantic.upload import Upload as UploadPydantic
from lob_python_sdk.pydantic.uploads_metadata import UploadsMetadata as UploadsMetadataPydantic
from lob_python_sdk.pydantic.upload_create_response import UploadCreateResponse as UploadCreateResponsePydantic
from lob_python_sdk.pydantic.required_address_column_mapping import RequiredAddressColumnMapping as RequiredAddressColumnMappingPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = UploadWritableSchema


request_body_upload_writable = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'basicAuth',
]
SchemaFor201ResponseBodyApplicationJson = UploadSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Upload


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Upload


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = UploadCreateResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: UploadCreateResponse


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: UploadCreateResponse


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '201': _response_for_201,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_mapped_args(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if campaign_id is not None:
            _body["campaignId"] = campaign_id
        if required_address_column_mapping is not None:
            _body["requiredAddressColumnMapping"] = required_address_column_mapping
        if optional_address_column_mapping is not None:
            _body["optionalAddressColumnMapping"] = optional_address_column_mapping
        if metadata is not None:
            _body["metadata"] = metadata
        if merge_variable_column_mapping is not None:
            _body["mergeVariableColumnMapping"] = merge_variable_column_mapping
        args.body = _body
        return args

    async def _acreate_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create
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
            path_template='/uploads',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_upload_writable.serialize(body, content_type)
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
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


    def _create_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create
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
            path_template='/uploads',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_upload_writable.serialize(body, content_type)
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
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
        )
        return await self._acreate_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
        )
        return self._create_oapg(
            body=args.body,
        )

class Create(BaseApi):

    async def acreate(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> UploadPydantic:
        raw_response = await self.raw.acreate(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
            **kwargs,
        )
        if validate:
            return RootModel[UploadPydantic](raw_response.body).root
        return api_client.construct_model_instance(UploadPydantic, raw_response.body)
    
    
    def create(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        validate: bool = False,
    ) -> UploadPydantic:
        raw_response = self.raw.create(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
        )
        if validate:
            return RootModel[UploadPydantic](raw_response.body).root
        return api_client.construct_model_instance(UploadPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
        )
        return await self._acreate_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None],
        required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = None,
        optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = None,
        metadata: typing.Optional[UploadsMetadata] = None,
        merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            campaign_id=campaign_id,
            required_address_column_mapping=required_address_column_mapping,
            optional_address_column_mapping=optional_address_column_mapping,
            metadata=metadata,
            merge_variable_column_mapping=merge_variable_column_mapping,
        )
        return self._create_oapg(
            body=args.body,
        )

