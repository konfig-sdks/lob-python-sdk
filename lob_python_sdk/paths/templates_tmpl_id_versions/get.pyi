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

from lob_python_sdk.model.tmpl_id import TmplId as TmplIdSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.date_filter import DateFilter as DateFilterSchema
from lob_python_sdk.model.template_versions_get_list_response import TemplateVersionsGetListResponse as TemplateVersionsGetListResponseSchema

from lob_python_sdk.type.template_versions_get_list_response import TemplateVersionsGetListResponse
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.date_filter import DateFilter
from lob_python_sdk.type.tmpl_id import TmplId

from ...api_client import Dictionary
from lob_python_sdk.pydantic.date_filter import DateFilter as DateFilterPydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.template_versions_get_list_response import TemplateVersionsGetListResponse as TemplateVersionsGetListResponsePydantic
from lob_python_sdk.pydantic.tmpl_id import TmplId as TmplIdPydantic

# Query params


class LimitSchema(
    schemas.IntSchema
):
    pass


class BeforeAfterSchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    before = schemas.StrSchema
                    after = schemas.StrSchema
                    __annotations__ = {
                        "before": before,
                        "after": after,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["before"]) -> MetaOapg.properties.before: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["after"]) -> MetaOapg.properties.after: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["before", "after", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["before"]) -> typing.Union[MetaOapg.properties.before, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["after"]) -> typing.Union[MetaOapg.properties.after, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["before", "after", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                before: typing.Union[MetaOapg.properties.before, str, schemas.Unset] = schemas.unset,
                after: typing.Union[MetaOapg.properties.after, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    before=before,
                    after=after,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class all_of_1(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class one_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "before",
                        }
                
                    
                    before: schemas.AnyTypeSchema
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class one_of_1(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "after",
                        }
                
                    
                    after: schemas.AnyTypeSchema
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                @classmethod
                @functools.lru_cache()
                def one_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.one_of_0,
                        cls.one_of_1,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.all_of_0,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BeforeAfterSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )


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
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'before/after': typing.Union[BeforeAfterSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        'include': typing.Union[IncludeSchema, list, tuple, ],
        'date_created': typing.Union[DateCreatedSchema, ],
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
request_query_before_after = api_client.QueryParameter(
    name="before/after",
    style=api_client.ParameterStyle.FORM,
    schema=BeforeAfterSchema,
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
SchemaFor200ResponseBodyApplicationJson = TemplateVersionsGetListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TemplateVersionsGetListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TemplateVersionsGetListResponse


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

    def _get_list_mapped_args(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if before_after is not None:
            _query_params["before/after"] = before_after
        if include is not None:
            _query_params["include"] = include
        if date_created is not None:
            _query_params["date_created"] = date_created
        if tmpl_id is not None:
            _path_params["tmpl_id"] = tmpl_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_before_after,
            request_query_include,
            request_query_date_created,
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
            path_template='/templates/{tmpl_id}/versions',
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


    def _get_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_before_after,
            request_query_include,
            request_query_date_created,
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
            path_template='/templates/{tmpl_id}/versions',
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


class GetListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_list(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_list(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
        )
        return self._get_list_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetList(BaseApi):

    async def aget_list(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        validate: bool = False,
        **kwargs,
    ) -> TemplateVersionsGetListResponsePydantic:
        raw_response = await self.raw.aget_list(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            **kwargs,
        )
        if validate:
            return RootModel[TemplateVersionsGetListResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(TemplateVersionsGetListResponsePydantic, raw_response.body)
    
    
    def get_list(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        validate: bool = False,
    ) -> TemplateVersionsGetListResponsePydantic:
        raw_response = self.raw.get_list(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
        )
        if validate:
            return RootModel[TemplateVersionsGetListResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(TemplateVersionsGetListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_list_mapped_args(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
        )
        return await self._aget_list_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        tmpl_id: TmplId,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_list_mapped_args(
            tmpl_id=tmpl_id,
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
        )
        return self._get_list_oapg(
            query_params=args.query,
            path_params=args.path,
        )

