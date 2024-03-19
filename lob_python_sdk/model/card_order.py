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


class CardOrder(
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
                
                class properties:
                
                    @staticmethod
                    def id() -> typing.Type['CoId']:
                        return CoId
                
                    @staticmethod
                    def card_id() -> typing.Type['CardId']:
                        return CardId
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "pending": "PENDING",
                                "printing": "PRINTING",
                                "available": "AVAILABLE",
                                "cancelled": "CANCELLED",
                                "depleted": "DEPLETED",
                            }
                        
                        @schemas.classproperty
                        def PENDING(cls):
                            return cls("pending")
                        
                        @schemas.classproperty
                        def PRINTING(cls):
                            return cls("printing")
                        
                        @schemas.classproperty
                        def AVAILABLE(cls):
                            return cls("available")
                        
                        @schemas.classproperty
                        def CANCELLED(cls):
                            return cls("cancelled")
                        
                        @schemas.classproperty
                        def DEPLETED(cls):
                            return cls("depleted")
                    inventory = schemas.NumberSchema
                    quantity_ordered = schemas.NumberSchema
                    unit_price = schemas.NumberSchema
                    cancelled_reason = schemas.StrSchema
                    availability_date = schemas.DateTimeSchema
                    expected_availability_date = schemas.DateTimeSchema
                    __annotations__ = {
                        "id": id,
                        "card_id": card_id,
                        "status": status,
                        "inventory": inventory,
                        "quantity_ordered": quantity_ordered,
                        "unit_price": unit_price,
                        "cancelled_reason": cancelled_reason,
                        "availability_date": availability_date,
                        "expected_availability_date": expected_availability_date,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'CoId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["card_id"]) -> 'CardId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inventory"]) -> MetaOapg.properties.inventory: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["quantity_ordered"]) -> MetaOapg.properties.quantity_ordered: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["unit_price"]) -> MetaOapg.properties.unit_price: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cancelled_reason"]) -> MetaOapg.properties.cancelled_reason: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["availability_date"]) -> MetaOapg.properties.availability_date: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["expected_availability_date"]) -> MetaOapg.properties.expected_availability_date: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "card_id", "status", "inventory", "quantity_ordered", "unit_price", "cancelled_reason", "availability_date", "expected_availability_date", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['CoId', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["card_id"]) -> typing.Union['CardId', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inventory"]) -> typing.Union[MetaOapg.properties.inventory, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["quantity_ordered"]) -> typing.Union[MetaOapg.properties.quantity_ordered, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["unit_price"]) -> typing.Union[MetaOapg.properties.unit_price, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cancelled_reason"]) -> typing.Union[MetaOapg.properties.cancelled_reason, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["availability_date"]) -> typing.Union[MetaOapg.properties.availability_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["expected_availability_date"]) -> typing.Union[MetaOapg.properties.expected_availability_date, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "card_id", "status", "inventory", "quantity_ordered", "unit_price", "cancelled_reason", "availability_date", "expected_availability_date", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                id: typing.Union['CoId', schemas.Unset] = schemas.unset,
                card_id: typing.Union['CardId', schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                inventory: typing.Union[MetaOapg.properties.inventory, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                quantity_ordered: typing.Union[MetaOapg.properties.quantity_ordered, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                unit_price: typing.Union[MetaOapg.properties.unit_price, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                cancelled_reason: typing.Union[MetaOapg.properties.cancelled_reason, str, schemas.Unset] = schemas.unset,
                availability_date: typing.Union[MetaOapg.properties.availability_date, str, datetime, schemas.Unset] = schemas.unset,
                expected_availability_date: typing.Union[MetaOapg.properties.expected_availability_date, str, datetime, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    id=id,
                    card_id=card_id,
                    status=status,
                    inventory=inventory,
                    quantity_ordered=quantity_ordered,
                    unit_price=unit_price,
                    cancelled_reason=cancelled_reason,
                    availability_date=availability_date,
                    expected_availability_date=expected_availability_date,
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
                LobBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardOrder':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.card_id import CardId
from lob_python_sdk.model.co_id import CoId
from lob_python_sdk.model.lob_base import LobBase
