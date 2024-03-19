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
from lob_python_sdk.model.links_response import LinksResponse as LinksResponseSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.date_filter import DateFilter as DateFilterSchema

from lob_python_sdk.type.links_response import LinksResponse
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.date_filter import DateFilter
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.cmp_id import CmpId

from ...api_client import Dictionary
from lob_python_sdk.pydantic.links_response import LinksResponse as LinksResponsePydantic
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.cmp_id import CmpId as CmpIdPydantic
from lob_python_sdk.pydantic.date_filter import DateFilter as DateFilterPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# Query params


class LimitSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 100
        inclusive_minimum = 1
OffsetSchema = schemas.IntSchema


class IncludeSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'IncludeSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
DateCreatedSchema = DateFilterSchema
MetadataSchema = MetadataSchema
CampaignIdSchema = schemas.Schema
ClickedSchema = schemas.BoolSchema
BillingGroupIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'offset': typing.Union[OffsetSchema, decimal.Decimal, int, ],
        'include': typing.Union[IncludeSchema, list, tuple, ],
        'date_created': typing.Union[DateCreatedSchema, ],
        'metadata': typing.Union[MetadataSchema, ],
        'campaign_id': typing.Union[CampaignIdSchema, ],
        'clicked': typing.Union[ClickedSchema, bool, ],
        'billing_group_id': typing.Union[BillingGroupIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_offset = api_client.QueryParameter(
    name="offset",
    style=api_client.ParameterStyle.FORM,
    schema=OffsetSchema,
    explode=True,
)
request_query_include = api_client.QueryParameter(
    name="include",
    style=api_client.ParameterStyle.FORM,
    schema=IncludeSchema,
    explode=True,
)
request_query_date_created = api_client.QueryParameter(
    name="date_created",
    style=api_client.ParameterStyle.DEEP_OBJECT,
    schema=DateFilterSchema,
    explode=True,
)
request_query_metadata = api_client.QueryParameter(
    name="metadata",
    style=api_client.ParameterStyle.DEEP_OBJECT,
    schema=MetadataSchema,
    explode=True,
)
request_query_campaign_id = api_client.QueryParameter(
    name="campaign_id",
    style=api_client.ParameterStyle.FORM,
    schema=CmpIdSchema,
    explode=True,
)
request_query_clicked = api_client.QueryParameter(
    name="clicked",
    style=api_client.ParameterStyle.FORM,
    schema=ClickedSchema,
    explode=True,
)
request_query_billing_group_id = api_client.QueryParameter(
    name="billing_group_id",
    style=api_client.ParameterStyle.FORM,
    schema=BillingGroupIdSchema,
    explode=True,
)
_auth = [
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = LinksResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LinksResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LinksResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_0_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if offset is not None:
            _query_params["offset"] = offset
        if include is not None:
            _query_params["include"] = include
        if date_created is not None:
            _query_params["date_created"] = date_created
        if metadata is not None:
            _query_params["metadata"] = metadata
        if campaign_id is not None:
            _query_params["campaign_id"] = campaign_id
        if clicked is not None:
            _query_params["clicked"] = clicked
        if billing_group_id is not None:
            _query_params["billing_group_id"] = billing_group_id
        args.query = _query_params
        return args

    async def _alist_0_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Retrieve all shortened links
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_include,
            request_query_date_created,
            request_query_metadata,
            request_query_campaign_id,
            request_query_clicked,
            request_query_billing_group_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/links',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _list_0_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        Retrieve all shortened links
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_offset,
            request_query_include,
            request_query_date_created,
            request_query_metadata,
            request_query_campaign_id,
            request_query_clicked,
            request_query_billing_group_id,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/links',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class List0Raw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_0(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_0_mapped_args(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
        )
        return await self._alist_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_0(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_0_mapped_args(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
        )
        return self._list_0_oapg(
            query_params=args.query,
        )

class List0(BaseApi):

    async def alist_0(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> LinksResponsePydantic:
        raw_response = await self.raw.alist_0(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
            **kwargs,
        )
        if validate:
            return LinksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinksResponsePydantic, raw_response.body)
    
    
    def list_0(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> LinksResponsePydantic:
        raw_response = self.raw.list_0(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
        )
        if validate:
            return LinksResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(LinksResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_0_mapped_args(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
        )
        return await self._alist_0_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CmpId] = None,
        clicked: typing.Optional[bool] = None,
        billing_group_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_0_mapped_args(
            limit=limit,
            offset=offset,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            clicked=clicked,
            billing_group_id=billing_group_id,
        )
        return self._list_0_oapg(
            query_params=args.query,
        )

