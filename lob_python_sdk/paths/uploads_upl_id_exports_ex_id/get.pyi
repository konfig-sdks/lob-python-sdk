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

from lob_python_sdk.model.ex_id import ExId as ExIdSchema
from lob_python_sdk.model.export_retrieve_response import ExportRetrieveResponse as ExportRetrieveResponseSchema
from lob_python_sdk.model.upl_id import UplId as UplIdSchema

from lob_python_sdk.type.export_retrieve_response import ExportRetrieveResponse
from lob_python_sdk.type.upl_id import UplId
from lob_python_sdk.type.ex_id import ExId

from ...api_client import Dictionary
from lob_python_sdk.pydantic.export_retrieve_response import ExportRetrieveResponse as ExportRetrieveResponsePydantic
from lob_python_sdk.pydantic.upl_id import UplId as UplIdPydantic
from lob_python_sdk.pydantic.ex_id import ExId as ExIdPydantic

# Path params
UplIdSchema = schemas.Schema
ExIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'upl_id': typing.Union[UplIdSchema, ],
        'ex_id': typing.Union[ExIdSchema, ],
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


request_path_upl_id = api_client.PathParameter(
    name="upl_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UplIdSchema,
    required=True,
)
request_path_ex_id = api_client.PathParameter(
    name="ex_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ExIdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ExportRetrieveResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ExportRetrieveResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ExportRetrieveResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _retrieve_1_mapped_args(
        self,
        upl_id: UplId,
        ex_id: ExId,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if upl_id is not None:
            _path_params["upl_id"] = upl_id
        if ex_id is not None:
            _path_params["ex_id"] = ex_id
        args.path = _path_params
        return args

    async def _aretrieve_1_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve Export
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_upl_id,
            request_path_ex_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/uploads/{upl_id}/exports/{ex_id}',
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


    def _retrieve_1_oapg(
        self,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve Export
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_upl_id,
            request_path_ex_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/uploads/{upl_id}/exports/{ex_id}',
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


class Retrieve1Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aretrieve_1(
        self,
        upl_id: UplId,
        ex_id: ExId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._retrieve_1_mapped_args(
            upl_id=upl_id,
            ex_id=ex_id,
        )
        return await self._aretrieve_1_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def retrieve_1(
        self,
        upl_id: UplId,
        ex_id: ExId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._retrieve_1_mapped_args(
            upl_id=upl_id,
            ex_id=ex_id,
        )
        return self._retrieve_1_oapg(
            path_params=args.path,
        )

class Retrieve1(BaseApi):

    async def aretrieve_1(
        self,
        upl_id: UplId,
        ex_id: ExId,
        validate: bool = False,
        **kwargs,
    ) -> ExportRetrieveResponsePydantic:
        raw_response = await self.raw.aretrieve_1(
            upl_id=upl_id,
            ex_id=ex_id,
            **kwargs,
        )
        if validate:
            return ExportRetrieveResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExportRetrieveResponsePydantic, raw_response.body)
    
    
    def retrieve_1(
        self,
        upl_id: UplId,
        ex_id: ExId,
        validate: bool = False,
    ) -> ExportRetrieveResponsePydantic:
        raw_response = self.raw.retrieve_1(
            upl_id=upl_id,
            ex_id=ex_id,
        )
        if validate:
            return ExportRetrieveResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExportRetrieveResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        upl_id: UplId,
        ex_id: ExId,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._retrieve_1_mapped_args(
            upl_id=upl_id,
            ex_id=ex_id,
        )
        return await self._aretrieve_1_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        upl_id: UplId,
        ex_id: ExId,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._retrieve_1_mapped_args(
            upl_id=upl_id,
            ex_id=ex_id,
        )
        return self._retrieve_1_oapg(
            path_params=args.path,
        )
