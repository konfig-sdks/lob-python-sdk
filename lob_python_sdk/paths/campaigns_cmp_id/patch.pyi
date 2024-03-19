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

from lob_python_sdk.model.cmp_id import CmpId as CmpIdSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.cmp_use_type import CmpUseType as CmpUseTypeSchema
from lob_python_sdk.model.cmp_schedule_type import CmpScheduleType as CmpScheduleTypeSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.resource_description import ResourceDescription as ResourceDescriptionSchema
from lob_python_sdk.model.campaign import Campaign as CampaignSchema
from lob_python_sdk.model.campaign_updatable import CampaignUpdatable as CampaignUpdatableSchema

from lob_python_sdk.type.campaign import Campaign
from lob_python_sdk.type.campaign_updatable import CampaignUpdatable
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.cmp_use_type import CmpUseType
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.cmp_schedule_type import CmpScheduleType
from lob_python_sdk.type.cmp_id import CmpId

from ...api_client import Dictionary
from lob_python_sdk.pydantic.cmp_schedule_type import CmpScheduleType as CmpScheduleTypePydantic
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.cmp_use_type import CmpUseType as CmpUseTypePydantic
from lob_python_sdk.pydantic.resource_description import ResourceDescription as ResourceDescriptionPydantic
from lob_python_sdk.pydantic.campaign import Campaign as CampaignPydantic
from lob_python_sdk.pydantic.campaign_updatable import CampaignUpdatable as CampaignUpdatablePydantic
from lob_python_sdk.pydantic.cmp_id import CmpId as CmpIdPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic

# Path params
CmpIdSchema = schemas.Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'cmp_id': typing.Union[CmpIdSchema, ],
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


request_path_cmp_id = api_client.PathParameter(
    name="cmp_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CmpIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = CampaignUpdatableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CampaignUpdatableSchema
SchemaForRequestBodyMultipartFormData = CampaignUpdatableSchema


request_body_campaign_updatable = api_client.RequestBody(
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
SchemaFor200ResponseBodyApplicationJson = CampaignSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Campaign


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Campaign


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
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if schedule_type is not None:
            _body["schedule_type"] = schedule_type
        if target_delivery_date is not None:
            _body["target_delivery_date"] = target_delivery_date
        if send_date is not None:
            _body["send_date"] = send_date
        if cancel_window_campaign_minutes is not None:
            _body["cancel_window_campaign_minutes"] = cancel_window_campaign_minutes
        if metadata is not None:
            _body["metadata"] = metadata
        if is_draft is not None:
            _body["is_draft"] = is_draft
        if use_type is not None:
            _body["use_type"] = use_type
        if auto_cancel_if_ncoa is not None:
            _body["auto_cancel_if_ncoa"] = auto_cancel_if_ncoa
        args.body = _body
        if cmp_id is not None:
            _path_params["cmp_id"] = cmp_id
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
        Update
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_cmp_id,
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
            path_template='/campaigns/{cmp_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_campaign_updatable.serialize(body, content_type)
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
        Update
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_cmp_id,
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
            path_template='/campaigns/{cmp_id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_campaign_updatable.serialize(body, content_type)
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
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_mapped_args(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
        )
        return await self._aupdate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update(
        self,
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_mapped_args(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
        )
        return self._update_oapg(
            body=args.body,
            path_params=args.path,
        )

class Update(BaseApi):

    async def aupdate(
        self,
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> CampaignPydantic:
        raw_response = await self.raw.aupdate(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            **kwargs,
        )
        if validate:
            return RootModel[CampaignPydantic](raw_response.body).root
        return api_client.construct_model_instance(CampaignPydantic, raw_response.body)
    
    
    def update(
        self,
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> CampaignPydantic:
        raw_response = self.raw.update(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
        )
        if validate:
            return RootModel[CampaignPydantic](raw_response.body).root
        return api_client.construct_model_instance(CampaignPydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_mapped_args(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
        )
        return await self._aupdate_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        cmp_id: CmpId,
        description: typing.Optional[ResourceDescription] = None,
        name: typing.Optional[str] = None,
        schedule_type: typing.Optional[CmpScheduleType] = None,
        target_delivery_date: typing.Optional[datetime] = None,
        send_date: typing.Optional[datetime] = None,
        cancel_window_campaign_minutes: typing.Optional[int] = None,
        metadata: typing.Optional[Metadata] = None,
        is_draft: typing.Optional[bool] = None,
        use_type: typing.Optional[CmpUseType] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_mapped_args(
            cmp_id=cmp_id,
            description=description,
            name=name,
            schedule_type=schedule_type,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            is_draft=is_draft,
            use_type=use_type,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
        )
        return self._update_oapg(
            body=args.body,
            path_params=args.path,
        )

