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


class AddressEditableIntl(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.ComposedBase,
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                
                    @staticmethod
                    def description() -> typing.Type['ResourceDescription']:
                        return ResourceDescription
                    
                    
                    class name(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                    
                    
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
                
                    @staticmethod
                    def company() -> typing.Type['Company']:
                        return Company
                    
                    
                    class phone(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'phone':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class email(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'email':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                
                    @staticmethod
                    def address_country() -> typing.Type['CountryExtended']:
                        return CountryExtended
                
                    @staticmethod
                    def metadata() -> typing.Type['Metadata']:
                        return Metadata
                    __annotations__ = {
                        "description": description,
                        "name": name,
                        "company": company,
                        "phone": phone,
                        "email": email,
                        "address_country": address_country,
                        "metadata": metadata,
                    }
                
                
                class any_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "name",
                        }
                
                    
                    name: schemas.AnyTypeSchema
                
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
                            "company",
                        }
                
                    
                    company: schemas.AnyTypeSchema
                
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
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'Company': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_country"]) -> 'CountryExtended': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "company", "phone", "email", "address_country", "metadata", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['Company', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_country"]) -> typing.Union['CountryExtended', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "company", "phone", "email", "address_country", "metadata", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
                company: typing.Union['Company', schemas.Unset] = schemas.unset,
                phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
                email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                address_country: typing.Union['CountryExtended', schemas.Unset] = schemas.unset,
                metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    description=description,
                    name=name,
                    company=company,
                    phone=phone,
                    email=email,
                    address_country=address_country,
                    metadata=metadata,
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
                AddressFieldsIntl,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddressEditableIntl':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.address_fields_intl import AddressFieldsIntl
from lob_python_sdk.model.company import Company
from lob_python_sdk.model.country_extended import CountryExtended
from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription
