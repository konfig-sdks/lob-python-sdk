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


class InlineAddressUsChk(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.ComposedBase,
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "address_line1",
                    "address_state",
                    "address_zip",
                    "address_city",
                }
                
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
                            max_length = 40
                    
                    
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
                    
                    
                    class address_line1(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 50
                    
                    
                    class address_line2(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 50
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'address_line2':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class address_city(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 200
                    
                    
                    class address_state(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'^[a-zA-Z]{2}$',
                            }]
                    
                    
                    class address_zip(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'^\d{5}(-\d{4})?$',
                            }]
                    
                    
                    class phone(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 40
                    
                    
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
                            max_length = 100
                    
                    
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
                    
                    
                    class address_country(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "US": "US",
                            }
                        
                        @schemas.classproperty
                        def US(cls):
                            return cls("US")
                
                    @staticmethod
                    def metadata() -> typing.Type['Metadata']:
                        return Metadata
                    __annotations__ = {
                        "description": description,
                        "name": name,
                        "company": company,
                        "address_line1": address_line1,
                        "address_line2": address_line2,
                        "address_city": address_city,
                        "address_state": address_state,
                        "address_zip": address_zip,
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
        
            
            address_line1: MetaOapg.properties.address_line1
            address_state: MetaOapg.properties.address_state
            address_zip: MetaOapg.properties.address_zip
            address_city: MetaOapg.properties.address_city
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'Company': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_line1"]) -> MetaOapg.properties.address_line1: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_line2"]) -> MetaOapg.properties.address_line2: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_city"]) -> MetaOapg.properties.address_city: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_state"]) -> MetaOapg.properties.address_state: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_zip"]) -> MetaOapg.properties.address_zip: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_country"]) -> MetaOapg.properties.address_country: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "name", "company", "address_line1", "address_line2", "address_city", "address_state", "address_zip", "phone", "email", "address_country", "metadata", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union['Company', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_line1"]) -> MetaOapg.properties.address_line1: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_line2"]) -> typing.Union[MetaOapg.properties.address_line2, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_city"]) -> MetaOapg.properties.address_city: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_state"]) -> MetaOapg.properties.address_state: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_zip"]) -> MetaOapg.properties.address_zip: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_country"]) -> typing.Union[MetaOapg.properties.address_country, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "name", "company", "address_line1", "address_line2", "address_city", "address_state", "address_zip", "phone", "email", "address_country", "metadata", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                address_line1: typing.Union[MetaOapg.properties.address_line1, str, ],
                address_state: typing.Union[MetaOapg.properties.address_state, str, ],
                address_zip: typing.Union[MetaOapg.properties.address_zip, str, ],
                address_city: typing.Union[MetaOapg.properties.address_city, str, ],
                description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
                company: typing.Union['Company', schemas.Unset] = schemas.unset,
                address_line2: typing.Union[MetaOapg.properties.address_line2, None, str, schemas.Unset] = schemas.unset,
                phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
                email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                address_country: typing.Union[MetaOapg.properties.address_country, str, schemas.Unset] = schemas.unset,
                metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    address_line1=address_line1,
                    address_state=address_state,
                    address_zip=address_zip,
                    address_city=address_city,
                    description=description,
                    name=name,
                    company=company,
                    address_line2=address_line2,
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
                cls.all_of_0,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InlineAddressUsChk':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.company import Company
from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription