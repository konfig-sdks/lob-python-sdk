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
from lob_python_sdk.model.campaign_writable import CampaignWritable as CampaignWritableSchema
from lob_python_sdk.model.cmp_use_type import CmpUseType as CmpUseTypeSchema
from lob_python_sdk.model.cmp_schedule_type import CmpScheduleType as CmpScheduleTypeSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.resource_description import ResourceDescription as ResourceDescriptionSchema
from lob_python_sdk.model.campaign import Campaign as CampaignSchema

from lob_python_sdk.type.campaign import Campaign
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.campaign_writable import CampaignWritable
from lob_python_sdk.type.cmp_use_type import CmpUseType
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.cmp_schedule_type import CmpScheduleType

from ...api_client import Dictionary
from lob_python_sdk.pydantic.cmp_schedule_type import CmpScheduleType as CmpScheduleTypePydantic
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.cmp_use_type import CmpUseType as CmpUseTypePydantic
from lob_python_sdk.pydantic.resource_description import ResourceDescription as ResourceDescriptionPydantic
from lob_python_sdk.pydantic.campaign import Campaign as CampaignPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.campaign_writable import CampaignWritable as CampaignWritablePydantic

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
SchemaForRequestBodyApplicationJson = CampaignWritableSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CampaignWritableSchema
SchemaForRequestBodyMultipartFormData = CampaignWritableSchema


request_body_campaign_writable = api_client.RequestBody(
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

    def _create_mapped_args(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if billing_group_id is not None:
            _body["billing_group_id"] = billing_group_id
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
        if use_type is not None:
            _body["use_type"] = use_type
        if auto_cancel_if_ncoa is not None:
            _body["auto_cancel_if_ncoa"] = auto_cancel_if_ncoa
        args.body = _body
        if x_lang_output is not None:
            _header_params["x-lang-output"] = x_lang_output
        args.header = _header_params
        return args

    async def _acreate_oapg(
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
        Create
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
            path_template='/campaigns',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_campaign_writable.serialize(body, content_type)
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


    def _create_oapg(
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
        Create
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
            path_template='/campaigns',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_campaign_writable.serialize(body, content_type)
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


class CreateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
        )
        return await self._acreate_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
        )
        return self._create_oapg(
            body=args.body,
            header_params=args.header,
        )

class Create(BaseApi):

    async def acreate(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CampaignPydantic:
        raw_response = await self.raw.acreate(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
            **kwargs,
        )
        if validate:
            return RootModel[CampaignPydantic](raw_response.body).root
        return api_client.construct_model_instance(CampaignPydantic, raw_response.body)
    
    
    def create(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CampaignPydantic:
        raw_response = self.raw.create(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
        )
        if validate:
            return RootModel[CampaignPydantic](raw_response.body).root
        return api_client.construct_model_instance(CampaignPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
        )
        return await self._acreate_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        name: str,
        schedule_type: CmpScheduleType,
        use_type: CmpUseType,
        description: typing.Optional[ResourceDescription] = None,
        billing_group_id: typing.Optional[typing.Optional[str]] = None,
        target_delivery_date: typing.Optional[typing.Optional[datetime]] = None,
        send_date: typing.Optional[typing.Optional[datetime]] = None,
        cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = None,
        metadata: typing.Optional[Metadata] = None,
        auto_cancel_if_ncoa: typing.Optional[bool] = None,
        x_lang_output: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            name=name,
            schedule_type=schedule_type,
            use_type=use_type,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            x_lang_output=x_lang_output,
        )
        return self._create_oapg(
            body=args.body,
            header_params=args.header,
        )

