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


class ToAddressUsChk(
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
                required = {
                    "address_line1",
                    "address_state",
                    "address_zip",
                    "id",
                    "address_city",
                }
                
                class properties:
                
                    @staticmethod
                    def description() -> typing.Type['ResourceDescription']:
                        return ResourceDescription
                
                    @staticmethod
                    def id() -> typing.Type['AdrId']:
                        return AdrId
                    
                    
                    class object(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "address": "ADDRESS",
                            }
                        
                        @schemas.classproperty
                        def ADDRESS(cls):
                            return cls("address")
                    
                    
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
                    
                    
                    class company(
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
                        ) -> 'company':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
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
                    
                    
                    class address_country(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 13
                            min_length = 13
                            enum_value_to_name = {
                                "UNITED STATES": "UNITED_STATES",
                            }
                        
                        @schemas.classproperty
                        def UNITED_STATES(cls):
                            return cls("UNITED STATES")
                
                    @staticmethod
                    def metadata() -> typing.Type['Metadata']:
                        return Metadata
                    
                    
                    class recipient_moved(
                        schemas.BoolBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneBoolMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, bool, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'recipient_moved':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    __annotations__ = {
                        "description": description,
                        "id": id,
                        "object": object,
                        "name": name,
                        "company": company,
                        "phone": phone,
                        "email": email,
                        "address_line1": address_line1,
                        "address_line2": address_line2,
                        "address_city": address_city,
                        "address_state": address_state,
                        "address_zip": address_zip,
                        "address_country": address_country,
                        "metadata": metadata,
                        "recipient_moved": recipient_moved,
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
            id: 'AdrId'
            address_city: MetaOapg.properties.address_city
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'AdrId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["company"]) -> MetaOapg.properties.company: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
            
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
            def __getitem__(self, name: typing_extensions.Literal["address_country"]) -> MetaOapg.properties.address_country: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["recipient_moved"]) -> MetaOapg.properties.recipient_moved: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "object", "name", "company", "phone", "email", "address_line1", "address_line2", "address_city", "address_state", "address_zip", "address_country", "metadata", "recipient_moved", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'AdrId': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> typing.Union[MetaOapg.properties.company, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
            
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
            def get_item_oapg(self, name: typing_extensions.Literal["address_country"]) -> typing.Union[MetaOapg.properties.address_country, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["recipient_moved"]) -> typing.Union[MetaOapg.properties.recipient_moved, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "object", "name", "company", "phone", "email", "address_line1", "address_line2", "address_city", "address_state", "address_zip", "address_country", "metadata", "recipient_moved", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                address_line1: typing.Union[MetaOapg.properties.address_line1, str, ],
                address_state: typing.Union[MetaOapg.properties.address_state, str, ],
                address_zip: typing.Union[MetaOapg.properties.address_zip, str, ],
                id: 'AdrId',
                address_city: typing.Union[MetaOapg.properties.address_city, str, ],
                description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
                object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
                name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
                company: typing.Union[MetaOapg.properties.company, None, str, schemas.Unset] = schemas.unset,
                phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
                email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
                address_line2: typing.Union[MetaOapg.properties.address_line2, None, str, schemas.Unset] = schemas.unset,
                address_country: typing.Union[MetaOapg.properties.address_country, str, schemas.Unset] = schemas.unset,
                metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
                recipient_moved: typing.Union[MetaOapg.properties.recipient_moved, None, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    address_line1=address_line1,
                    address_state=address_state,
                    address_zip=address_zip,
                    id=id,
                    address_city=address_city,
                    description=description,
                    object=object,
                    name=name,
                    company=company,
                    phone=phone,
                    email=email,
                    address_line2=address_line2,
                    address_country=address_country,
                    metadata=metadata,
                    recipient_moved=recipient_moved,
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
    ) -> 'ToAddressUsChk':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.adr_id import AdrId
from lob_python_sdk.model.lob_base import LobBase
from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription
