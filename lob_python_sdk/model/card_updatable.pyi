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


class CardUpdatable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def description() -> typing.Type['CardDescription']:
                return CardDescription
            auto_reorder = schemas.BoolSchema
            
            
            class reorder_quantity(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "description": description,
                "auto_reorder": auto_reorder,
                "reorder_quantity": reorder_quantity,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'CardDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_reorder"]) -> MetaOapg.properties.auto_reorder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reorder_quantity"]) -> MetaOapg.properties.reorder_quantity: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "auto_reorder", "reorder_quantity", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['CardDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_reorder"]) -> typing.Union[MetaOapg.properties.auto_reorder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reorder_quantity"]) -> typing.Union[MetaOapg.properties.reorder_quantity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "auto_reorder", "reorder_quantity", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union['CardDescription', schemas.Unset] = schemas.unset,
        auto_reorder: typing.Union[MetaOapg.properties.auto_reorder, bool, schemas.Unset] = schemas.unset,
        reorder_quantity: typing.Union[MetaOapg.properties.reorder_quantity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CardUpdatable':
        return super().__new__(
            cls,
            *args,
            description=description,
            auto_reorder=auto_reorder,
            reorder_quantity=reorder_quantity,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.card_description import CardDescription
