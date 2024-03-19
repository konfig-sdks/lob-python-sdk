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

from lob_python_sdk.model.campaign_id import CampaignId as CampaignIdSchema
from lob_python_sdk.model.mail_type import MailType as MailTypeSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.date_filter import DateFilter as DateFilterSchema
from lob_python_sdk.model.send_date import SendDate as SendDateSchema
from lob_python_sdk.model.letters_list_response import LettersListResponse as LettersListResponseSchema
from lob_python_sdk.model.status import Status as StatusSchema

from lob_python_sdk.type.mail_type import MailType
from lob_python_sdk.type.letters_list_response import LettersListResponse
from lob_python_sdk.type.status import Status
from lob_python_sdk.type.campaign_id import CampaignId
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.date_filter import DateFilter
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.send_date import SendDate

from ...api_client import Dictionary
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.letters_list_response import LettersListResponse as LettersListResponsePydantic
from lob_python_sdk.pydantic.send_date import SendDate as SendDatePydantic
from lob_python_sdk.pydantic.campaign_id import CampaignId as CampaignIdPydantic
from lob_python_sdk.pydantic.date_filter import DateFilter as DateFilterPydantic
from lob_python_sdk.pydantic.status import Status as StatusPydantic
from lob_python_sdk.pydantic.mail_type import MailType as MailTypePydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# Query params


class LimitSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 100
        inclusive_minimum = 1


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
MetadataSchema = MetadataSchema


class CampaignIdSchema(
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneMixin
):


    def __new__(
        cls,
        *args: typing.Union[None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CampaignIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
StatusSchema = StatusSchema
ColorSchema = schemas.BoolSchema
ScheduledSchema = schemas.BoolSchema
SendDateSchema = SendDateSchema
MailTypeSchema = MailTypeSchema


class SortBySchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class date_created(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "asc": "ASC",
                                "desc": "DESC",
                            }
                        
                        @schemas.classproperty
                        def ASC(cls):
                            return cls("asc")
                        
                        @schemas.classproperty
                        def DESC(cls):
                            return cls("desc")
                    
                    
                    class send_date(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "asc": "ASC",
                                "desc": "DESC",
                            }
                        
                        @schemas.classproperty
                        def ASC(cls):
                            return cls("asc")
                        
                        @schemas.classproperty
                        def DESC(cls):
                            return cls("desc")
                    __annotations__ = {
                        "date_created": date_created,
                        "send_date": send_date,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["send_date"]) -> MetaOapg.properties.send_date: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["date_created", "send_date", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> typing.Union[MetaOapg.properties.date_created, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["send_date"]) -> typing.Union[MetaOapg.properties.send_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date_created", "send_date", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                date_created: typing.Union[MetaOapg.properties.date_created, str, schemas.Unset] = schemas.unset,
                send_date: typing.Union[MetaOapg.properties.send_date, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    date_created=date_created,
                    send_date=send_date,
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
                            "date_created",
                        }
                
                    
                    date_created: schemas.AnyTypeSchema
                
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
                            "send_date",
                        }
                
                    
                    send_date: schemas.AnyTypeSchema
                
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
    ) -> 'SortBySchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
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
        'metadata': typing.Union[MetadataSchema, ],
        'campaign_id': typing.Union[CampaignIdSchema, None, ],
        'status': typing.Union[StatusSchema, ],
        'color': typing.Union[ColorSchema, bool, ],
        'scheduled': typing.Union[ScheduledSchema, bool, ],
        'send_date': typing.Union[SendDateSchema, ],
        'mail_type': typing.Union[MailTypeSchema, ],
        'sort_by': typing.Union[SortBySchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
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
request_query_metadata = api_client.QueryParameter(
    name="metadata",
    style=api_client.ParameterStyle.DEEP_OBJECT,
    schema=MetadataSchema,
    explode=True,
)
request_query_campaign_id = api_client.QueryParameter(
    name="campaign_id",
    style=api_client.ParameterStyle.FORM,
    schema=CampaignIdSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_color = api_client.QueryParameter(
    name="color",
    style=api_client.ParameterStyle.FORM,
    schema=ColorSchema,
    explode=True,
)
request_query_scheduled = api_client.QueryParameter(
    name="scheduled",
    style=api_client.ParameterStyle.FORM,
    schema=ScheduledSchema,
    explode=True,
)
request_query_send_date = api_client.QueryParameter(
    name="send_date",
    style=api_client.ParameterStyle.FORM,
    schema=SendDateSchema,
    explode=True,
)
request_query_mail_type = api_client.QueryParameter(
    name="mail_type",
    style=api_client.ParameterStyle.FORM,
    schema=MailTypeSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
_auth = [
    'basicAuth',
]
SchemaFor200ResponseBodyApplicationJson = LettersListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: LettersListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: LettersListResponse


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

    def _list_mapped_args(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if limit is not None:
            _query_params["limit"] = limit
        if before_after is not None:
            _query_params["before/after"] = before_after
        if include is not None:
            _query_params["include"] = include
        if date_created is not None:
            _query_params["date_created"] = date_created
        if metadata is not None:
            _query_params["metadata"] = metadata
        if campaign_id is not None:
            _query_params["campaign_id"] = campaign_id
        if status is not None:
            _query_params["status"] = status
        if color is not None:
            _query_params["color"] = color
        if scheduled is not None:
            _query_params["scheduled"] = scheduled
        if send_date is not None:
            _query_params["send_date"] = send_date
        if mail_type is not None:
            _query_params["mail_type"] = mail_type
        if sort_by is not None:
            _query_params["sort_by"] = sort_by
        args.query = _query_params
        return args

    async def _alist_oapg(
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
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_before_after,
            request_query_include,
            request_query_date_created,
            request_query_metadata,
            request_query_campaign_id,
            request_query_status,
            request_query_color,
            request_query_scheduled,
            request_query_send_date,
            request_query_mail_type,
            request_query_sort_by,
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
            path_template='/letters',
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


    def _list_oapg(
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
        List
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_limit,
            request_query_before_after,
            request_query_include,
            request_query_date_created,
            request_query_metadata,
            request_query_campaign_id,
            request_query_status,
            request_query_color,
            request_query_scheduled,
            request_query_send_date,
            request_query_mail_type,
            request_query_sort_by,
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
            path_template='/letters',
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
        **kwargs,
    ) -> LettersListResponsePydantic:
        raw_response = await self.raw.alist(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
            **kwargs,
        )
        if validate:
            return RootModel[LettersListResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LettersListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
    ) -> LettersListResponsePydantic:
        raw_response = self.raw.list(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
        )
        if validate:
            return RootModel[LettersListResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(LettersListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        limit: typing.Optional[int] = None,
        before_after: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        include: typing.Optional[typing.List[str]] = None,
        date_created: typing.Optional[DateFilter] = None,
        metadata: typing.Optional[Metadata] = None,
        campaign_id: typing.Optional[CampaignId] = None,
        status: typing.Optional[Status] = None,
        color: typing.Optional[bool] = None,
        scheduled: typing.Optional[bool] = None,
        send_date: typing.Optional[SendDate] = None,
        mail_type: typing.Optional[MailType] = None,
        sort_by: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            limit=limit,
            before_after=before_after,
            include=include,
            date_created=date_created,
            metadata=metadata,
            campaign_id=campaign_id,
            status=status,
            color=color,
            scheduled=scheduled,
            send_date=send_date,
            mail_type=mail_type,
            sort_by=sort_by,
        )
        return self._list_oapg(
            query_params=args.query,
        )

