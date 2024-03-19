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


class CompanyInput(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class any_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "city",
                            "state",
                        }
                
                    
                    city: schemas.AnyTypeSchema
                    state: schemas.AnyTypeSchema
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                
                class any_of_1(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "zip_code",
                        }
                
                    
                    zip_code: schemas.AnyTypeSchema
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'any_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            _configuration=_configuration,
                            **kwargs,
                        )
                
                @classmethod
                @functools.lru_cache()
                def any_of(cls):
                    # we need this here to make our import statements work
                    # we must store _composed_schemas in here so the code is only run
                    # when we invoke this method. If we kept this at the class
                    # level we would get an error because the class level
                    # code would be run when this module is imported, and these composed
                    # classes don't exist yet because their module has not finished
                    # loading
                    return [
                        cls.any_of_0,
                        cls.any_of_1,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "primary_line",
                    "company",
                }
                
                class properties:
                
                    @staticmethod
                    def company() -> typing.Type['IdentityValidationCompany']:
                        return IdentityValidationCompany
                
                    @staticmethod
                    def primary_line() -> typing.Type['PrimaryLineUs']:
                        return PrimaryLineUs
                
                    @staticmethod
                    def secondary_line() -> typing.Type['SecondaryLine']:
                        return SecondaryLine
                
                    @staticmethod
                    def urbanization() -> typing.Type['Urbanization']:
                        return Urbanization
                    
                    
                    class city(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.StrSchema
                            
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
                                    CityNoDescription,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'city':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class state(
                        schemas.StrSchema
                    ):
                        pass
                    
                    
                    class zip_code(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_0 = schemas.StrSchema
                            
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
                                    ZipCode,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'zip_code':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "company": company,
                        "primary_line": primary_line,
                        "secondary_line": secondary_line,
                        "urbanization": urbanization,
                        "city": city,
                        "state": state,
                        "zip_code": zip_code,
                    }
            
            primary_line: 'PrimaryLineUs'
            company: 'IdentityValidationCompany'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'IdentityValidationCompany': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["primary_line"]) -> 'PrimaryLineUs': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["secondary_line"]) -> 'SecondaryLine': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["urbanization"]) -> 'Urbanization': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["zip_code"]) -> MetaOapg.properties.zip_code: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["company", "primary_line", "secondary_line", "urbanization", "city", "state", "zip_code", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> 'IdentityValidationCompany': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["primary_line"]) -> 'PrimaryLineUs': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["secondary_line"]) -> typing.Union['SecondaryLine', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["urbanization"]) -> typing.Union['Urbanization', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["zip_code"]) -> typing.Union[MetaOapg.properties.zip_code, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company", "primary_line", "secondary_line", "urbanization", "city", "state", "zip_code", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                primary_line: 'PrimaryLineUs',
                company: 'IdentityValidationCompany',
                secondary_line: typing.Union['SecondaryLine', schemas.Unset] = schemas.unset,
                urbanization: typing.Union['Urbanization', schemas.Unset] = schemas.unset,
                city: typing.Union[MetaOapg.properties.city, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
                zip_code: typing.Union[MetaOapg.properties.zip_code, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    primary_line=primary_line,
                    company=company,
                    secondary_line=secondary_line,
                    urbanization=urbanization,
                    city=city,
                    state=state,
                    zip_code=zip_code,
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
    ) -> 'CompanyInput':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.city_no_description import CityNoDescription
from lob_python_sdk.model.identity_validation_company import IdentityValidationCompany
from lob_python_sdk.model.primary_line_us import PrimaryLineUs
from lob_python_sdk.model.secondary_line import SecondaryLine
from lob_python_sdk.model.urbanization import Urbanization
from lob_python_sdk.model.zip_code import ZipCode
