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


class TrackingEventNormal(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "name",
                    "type",
                }
                
                class properties:
                    
                    
                    class type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "normal": "NORMAL",
                            }
                        
                        @schemas.classproperty
                        def NORMAL(cls):
                            return cls("normal")
                    
                    
                    class name(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "Mailed": "MAILED",
                                "In Transit": "IN_TRANSIT",
                                "In Local Area": "IN_LOCAL_AREA",
                                "Processed for Delivery": "PROCESSED_FOR_DELIVERY",
                                "Delivered": "DELIVERED",
                                "Re-Routed": "REROUTED",
                                "Returned to Sender": "RETURNED_TO_SENDER",
                                "International Exit": "INTERNATIONAL_EXIT",
                            }
                        
                        @schemas.classproperty
                        def MAILED(cls):
                            return cls("Mailed")
                        
                        @schemas.classproperty
                        def IN_TRANSIT(cls):
                            return cls("In Transit")
                        
                        @schemas.classproperty
                        def IN_LOCAL_AREA(cls):
                            return cls("In Local Area")
                        
                        @schemas.classproperty
                        def PROCESSED_FOR_DELIVERY(cls):
                            return cls("Processed for Delivery")
                        
                        @schemas.classproperty
                        def DELIVERED(cls):
                            return cls("Delivered")
                        
                        @schemas.classproperty
                        def REROUTED(cls):
                            return cls("Re-Routed")
                        
                        @schemas.classproperty
                        def RETURNED_TO_SENDER(cls):
                            return cls("Returned to Sender")
                        
                        @schemas.classproperty
                        def INTERNATIONAL_EXIT(cls):
                            return cls("International Exit")
                    
                    
                    class details(
                        schemas.EnumBase,
                        schemas.DictBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneFrozenDictMixin
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                None: "NONE",
                            }
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls(None)
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, None, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'details':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class location(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'location':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    __annotations__ = {
                        "type": type,
                        "name": name,
                        "details": details,
                        "location": location,
                    }
            
            name: MetaOapg.properties.name
            type: MetaOapg.properties.type
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "name", "details", "location", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "name", "details", "location", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                name: typing.Union[MetaOapg.properties.name, str, ],
                type: typing.Union[MetaOapg.properties.type, str, ],
                details: typing.Union[MetaOapg.properties.details, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
                location: typing.Union[MetaOapg.properties.location, None, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    name=name,
                    type=type,
                    details=details,
                    location=location,
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
                TrackingEventBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TrackingEventNormal':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.tracking_event_base import TrackingEventBase
