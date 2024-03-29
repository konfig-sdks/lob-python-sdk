# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

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


class Events(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "event_type",
            "reference_id",
            "date_created",
            "id",
            "body",
            "object",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            body = schemas.DictSchema
            reference_id = schemas.StrSchema
        
            @staticmethod
            def event_type() -> typing.Type['EventType']:
                return EventType
            date_created = schemas.DateTimeSchema
            
            
            class object(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EVENT(cls):
                    return cls("event")
            __annotations__ = {
                "id": id,
                "body": body,
                "reference_id": reference_id,
                "event_type": event_type,
                "date_created": date_created,
                "object": object,
            }
    
    event_type: 'EventType'
    reference_id: MetaOapg.properties.reference_id
    date_created: MetaOapg.properties.date_created
    id: MetaOapg.properties.id
    body: MetaOapg.properties.body
    object: MetaOapg.properties.object
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference_id"]) -> MetaOapg.properties.reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_type"]) -> 'EventType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "body", "reference_id", "event_type", "date_created", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body"]) -> MetaOapg.properties.body: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference_id"]) -> MetaOapg.properties.reference_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_type"]) -> 'EventType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "body", "reference_id", "event_type", "date_created", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        event_type: 'EventType',
        reference_id: typing.Union[MetaOapg.properties.reference_id, str, ],
        date_created: typing.Union[MetaOapg.properties.date_created, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        body: typing.Union[MetaOapg.properties.body, dict, frozendict.frozendict, ],
        object: typing.Union[MetaOapg.properties.object, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Events':
        return super().__new__(
            cls,
            *args,
            event_type=event_type,
            reference_id=reference_id,
            date_created=date_created,
            id=id,
            body=body,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.event_type import EventType
