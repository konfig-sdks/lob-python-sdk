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


class IntlSuggestions(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "primary_number_range",
            "country",
            "primary_line",
            "city",
            "state",
            "zip_code",
        }
        
        class properties:
            primary_number_range = schemas.StrSchema
            primary_line = schemas.StrSchema
        
            @staticmethod
            def city() -> typing.Type['City']:
                return City
        
            @staticmethod
            def country() -> typing.Type['CountryExtended']:
                return CountryExtended
        
            @staticmethod
            def state() -> typing.Type['State']:
                return State
        
            @staticmethod
            def zip_code() -> typing.Type['PostalCode']:
                return PostalCode
            __annotations__ = {
                "primary_number_range": primary_number_range,
                "primary_line": primary_line,
                "city": city,
                "country": country,
                "state": state,
                "zip_code": zip_code,
            }
    
    primary_number_range: MetaOapg.properties.primary_number_range
    country: 'CountryExtended'
    primary_line: MetaOapg.properties.primary_line
    city: 'City'
    state: 'State'
    zip_code: 'PostalCode'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_number_range"]) -> MetaOapg.properties.primary_number_range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_line"]) -> MetaOapg.properties.primary_line: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> 'City': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> 'CountryExtended': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'State': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["primary_number_range", "primary_line", "city", "country", "state", "zip_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_number_range"]) -> MetaOapg.properties.primary_number_range: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_line"]) -> MetaOapg.properties.primary_line: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> 'City': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> 'CountryExtended': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> 'State': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip_code"]) -> 'PostalCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primary_number_range", "primary_line", "city", "country", "state", "zip_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        primary_number_range: typing.Union[MetaOapg.properties.primary_number_range, str, ],
        country: 'CountryExtended',
        primary_line: typing.Union[MetaOapg.properties.primary_line, str, ],
        city: 'City',
        state: 'State',
        zip_code: 'PostalCode',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntlSuggestions':
        return super().__new__(
            cls,
            *args,
            primary_number_range=primary_number_range,
            country=country,
            primary_line=primary_line,
            city=city,
            state=state,
            zip_code=zip_code,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.city import City
from lob_python_sdk.model.country_extended import CountryExtended
from lob_python_sdk.model.postal_code import PostalCode
from lob_python_sdk.model.state import State