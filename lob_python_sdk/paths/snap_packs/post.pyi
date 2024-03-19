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

from lob_python_sdk.model.snap_pack import SnapPack as SnapPackSchema
from lob_python_sdk.model.snap_pack_size import SnapPackSize as SnapPackSizeSchema
from lob_python_sdk.model.mail_type import MailType as MailTypeSchema
from lob_python_sdk.model.snap_pack_use_type import SnapPackUseType as SnapPackUseTypeSchema
from lob_python_sdk.model.snap_pack_editable import SnapPackEditable as SnapPackEditableSchema
from lob_python_sdk.model.inline_address import InlineAddress as InlineAddressSchema
from lob_python_sdk.model.error import Error as ErrorSchema
from lob_python_sdk.model.metadata import Metadata as MetadataSchema
from lob_python_sdk.model.resource_description import ResourceDescription as ResourceDescriptionSchema
from lob_python_sdk.model.inline_address_us import InlineAddressUs as InlineAddressUsSchema
from lob_python_sdk.model.send_date import SendDate as SendDateSchema
from lob_python_sdk.model.merge_variables import MergeVariables as MergeVariablesSchema

from lob_python_sdk.type.mail_type import MailType
from lob_python_sdk.type.merge_variables import MergeVariables
from lob_python_sdk.type.inline_address_us import InlineAddressUs
from lob_python_sdk.type.snap_pack_use_type import SnapPackUseType
from lob_python_sdk.type.snap_pack_size import SnapPackSize
from lob_python_sdk.type.error import Error
from lob_python_sdk.type.inline_address import InlineAddress
from lob_python_sdk.type.snap_pack_editable import SnapPackEditable
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.snap_pack import SnapPack
from lob_python_sdk.type.send_date import SendDate

from ...api_client import Dictionary
from lob_python_sdk.pydantic.metadata import Metadata as MetadataPydantic
from lob_python_sdk.pydantic.resource_description import ResourceDescription as ResourceDescriptionPydantic
from lob_python_sdk.pydantic.snap_pack_editable import SnapPackEditable as SnapPackEditablePydantic
from lob_python_sdk.pydantic.send_date import SendDate as SendDatePydantic
from lob_python_sdk.pydantic.inline_address import InlineAddress as InlineAddressPydantic
from lob_python_sdk.pydantic.snap_pack_size import SnapPackSize as SnapPackSizePydantic
from lob_python_sdk.pydantic.snap_pack_use_type import SnapPackUseType as SnapPackUseTypePydantic
from lob_python_sdk.pydantic.mail_type import MailType as MailTypePydantic
from lob_python_sdk.pydantic.error import Error as ErrorPydantic
from lob_python_sdk.pydantic.inline_address_us import InlineAddressUs as InlineAddressUsPydantic
from lob_python_sdk.pydantic.snap_pack import SnapPack as SnapPackPydantic
from lob_python_sdk.pydantic.merge_variables import MergeVariables as MergeVariablesPydantic

# Query params


class IdempotencyKeySchema(
    schemas.StrSchema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'idempotency_key': typing.Union[IdempotencyKeySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_idempotency_key2 = api_client.QueryParameter(
    name="idempotency_key",
    style=api_client.ParameterStyle.FORM,
    schema=IdempotencyKeySchema,
    explode=True,
)
# Header params


class IdempotencyKeySchema(
    schemas.StrSchema
):
    pass
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'Idempotency-Key': typing.Union[IdempotencyKeySchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_idempotency_key = api_client.HeaderParameter(
    name="Idempotency-Key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdempotencyKeySchema,
)
# body param
SchemaForRequestBodyApplicationJson = SnapPackEditableSchema
SchemaForRequestBodyMultipartFormData = SnapPackEditableSchema


request_body_snap_pack_editable = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
RatelimitLimitSchema = schemas.IntSchema
RatelimitRemainingSchema = schemas.IntSchema
RatelimitResetSchema = schemas.IntSchema
SchemaFor200ResponseBodyApplicationJson = SnapPackSchema
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
    body: SnapPack


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SnapPack


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

    def _create_new_snap_pack_mapped_args(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if metadata is not None:
            _body["metadata"] = metadata
        if mail_type is not None:
            _body["mail_type"] = mail_type
        if merge_variables is not None:
            _body["merge_variables"] = merge_variables
        if send_date is not None:
            _body["send_date"] = send_date
        if size is not None:
            _body["size"] = size
        if to is not None:
            _body["to"] = to
        if _from is not None:
            _body["from"] = _from
        if inside is not None:
            _body["inside"] = inside
        if outside is not None:
            _body["outside"] = outside
        if billing_group_id is not None:
            _body["billing_group_id"] = billing_group_id
        if use_type is not None:
            _body["use_type"] = use_type
        if color is not None:
            _body["color"] = color
        args.body = body if body is not None else _body
        if idempotency_key2 is not None:
            _query_params["idempotency_key"] = idempotency_key2
        if idempotency_key is not None:
            _header_params["Idempotency-Key"] = idempotency_key
        args.query = _query_params
        args.header = _header_params
        return args

    async def _acreate_new_snap_pack_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_idempotency_key2,
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
        for parameter in (
            request_header_idempotency_key,
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
            path_template='/snap_packs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_snap_pack_editable.serialize(body, content_type)
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


    def _create_new_snap_pack_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_idempotency_key2,
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
        for parameter in (
            request_header_idempotency_key,
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
            path_template='/snap_packs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_snap_pack_editable.serialize(body, content_type)
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


class CreateNewSnapPackRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_snap_pack(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_snap_pack_mapped_args(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
        )
        return await self._acreate_new_snap_pack_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def create_new_snap_pack(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_snap_pack_mapped_args(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
        )
        return self._create_new_snap_pack_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

class CreateNewSnapPack(BaseApi):

    async def acreate_new_snap_pack(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SnapPackPydantic:
        raw_response = await self.raw.acreate_new_snap_pack(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
            **kwargs,
        )
        if validate:
            return RootModel[SnapPackPydantic](raw_response.body).root
        return api_client.construct_model_instance(SnapPackPydantic, raw_response.body)
    
    
    def create_new_snap_pack(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SnapPackPydantic:
        raw_response = self.raw.create_new_snap_pack(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
        )
        if validate:
            return RootModel[SnapPackPydantic](raw_response.body).root
        return api_client.construct_model_instance(SnapPackPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_snap_pack_mapped_args(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
        )
        return await self._acreate_new_snap_pack_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        body: SnapPackEditable,
        description: typing.Optional[ResourceDescription] = None,
        metadata: typing.Optional[Metadata] = None,
        mail_type: typing.Optional[MailType] = None,
        merge_variables: typing.Optional[MergeVariables] = None,
        send_date: typing.Optional[SendDate] = None,
        size: typing.Optional[SnapPackSize] = None,
        to: typing.Optional[typing.Union[AdrId, InlineAddress]] = None,
        _from: typing.Optional[typing.Union[AdrId, InlineAddressUs]] = None,
        inside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        outside: typing.Optional[typing.Union[HtmlString, TmplId, RemoteFileUrl, LocalFilePath]] = None,
        billing_group_id: typing.Optional[str] = None,
        use_type: typing.Optional[SnapPackUseType] = None,
        color: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        idempotency_key: typing.Optional[str] = None,
        idempotency_key2: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_snap_pack_mapped_args(
            body=body,
            description=description,
            metadata=metadata,
            mail_type=mail_type,
            merge_variables=merge_variables,
            send_date=send_date,
            size=size,
            to=to,
            _from=_from,
            inside=inside,
            outside=outside,
            billing_group_id=billing_group_id,
            use_type=use_type,
            color=color,
            idempotency_key=idempotency_key,
            idempotency_key2=idempotency_key2,
        )
        return self._create_new_snap_pack_oapg(
            body=args.body,
            query_params=args.query,
            header_params=args.header,
        )

