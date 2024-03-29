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


class Zip(
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
                    "cities",
                    "id",
                    "zip_code_type",
                    "object",
                }
                
                class properties:
                
                    @staticmethod
                    def id() -> typing.Type['ZipId']:
                        return ZipId
                    
                    
                    class cities(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ZipLookupCity']:
                                return ZipLookupCity
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ZipLookupCity'], typing.List['ZipLookupCity']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'cities':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ZipLookupCity':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def zip_code_type() -> typing.Type['ZipCodeType']:
                        return ZipCodeType
                    
                    
                    class object(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "us_zip_lookup": "US_ZIP_LOOKUP",
                            }
                        
                        @schemas.classproperty
                        def US_ZIP_LOOKUP(cls):
                            return cls("us_zip_lookup")
                    __annotations__ = {
                        "id": id,
                        "cities": cities,
                        "zip_code_type": zip_code_type,
                        "object": object,
                    }
            
            cities: MetaOapg.properties.cities
            id: 'ZipId'
            zip_code_type: 'ZipCodeType'
            object: MetaOapg.properties.object
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'ZipId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["cities"]) -> MetaOapg.properties.cities: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["zip_code_type"]) -> 'ZipCodeType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "cities", "zip_code_type", "object", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'ZipId': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["cities"]) -> MetaOapg.properties.cities: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["zip_code_type"]) -> 'ZipCodeType': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "cities", "zip_code_type", "object", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                cities: typing.Union[MetaOapg.properties.cities, list, tuple, ],
                id: 'ZipId',
                zip_code_type: 'ZipCodeType',
                object: typing.Union[MetaOapg.properties.object, str, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    cities=cities,
                    id=id,
                    zip_code_type=zip_code_type,
                    object=object,
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
                Zip5,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Zip':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.zip5 import Zip5
from lob_python_sdk.model.zip_code_type import ZipCodeType
from lob_python_sdk.model.zip_id import ZipId
from lob_python_sdk.model.zip_lookup_city import ZipLookupCity
