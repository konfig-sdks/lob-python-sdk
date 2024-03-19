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


class RequiredAddressColumnMapping(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The mapping of column headers in your file to Lob-required fields for the resource created. See our <a href="https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#required-columns-2" target="_blank">Campaign Audience Guide</a> for additional details.
    """


    class MetaOapg:
        required = {
            "address_line1",
            "address_state",
            "name",
            "address_zip",
            "address_city",
        }
        
        class properties:
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address_line1(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address_line1':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address_city(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address_city':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address_state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address_state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address_zip(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address_zip':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "address_line1": address_line1,
                "address_city": address_city,
                "address_state": address_state,
                "address_zip": address_zip,
            }
    
    address_line1: MetaOapg.properties.address_line1
    address_state: MetaOapg.properties.address_state
    name: MetaOapg.properties.name
    address_zip: MetaOapg.properties.address_zip
    address_city: MetaOapg.properties.address_city
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_line1"]) -> MetaOapg.properties.address_line1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_city"]) -> MetaOapg.properties.address_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_state"]) -> MetaOapg.properties.address_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_zip"]) -> MetaOapg.properties.address_zip: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "address_line1", "address_city", "address_state", "address_zip", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_line1"]) -> MetaOapg.properties.address_line1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_city"]) -> MetaOapg.properties.address_city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_state"]) -> MetaOapg.properties.address_state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_zip"]) -> MetaOapg.properties.address_zip: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "address_line1", "address_city", "address_state", "address_zip", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address_line1: typing.Union[MetaOapg.properties.address_line1, None, str, ],
        address_state: typing.Union[MetaOapg.properties.address_state, None, str, ],
        name: typing.Union[MetaOapg.properties.name, None, str, ],
        address_zip: typing.Union[MetaOapg.properties.address_zip, None, str, ],
        address_city: typing.Union[MetaOapg.properties.address_city, None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequiredAddressColumnMapping':
        return super().__new__(
            cls,
            *args,
            address_line1=address_line1,
            address_state=address_state,
            name=name,
            address_zip=address_zip,
            address_city=address_city,
            _configuration=_configuration,
            **kwargs,
        )
