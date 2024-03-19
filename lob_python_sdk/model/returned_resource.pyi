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


class ReturnedResource(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class one_of_0(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class all_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "resource_type",
                            "details",
                        }
                        
                        class properties:
                            
                            
                            class resource_type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def POSTCARD(cls):
                                    return cls("postcard")
                        
                            @staticmethod
                            def details() -> typing.Type['Returned']:
                                return Returned
                            __annotations__ = {
                                "resource_type": resource_type,
                                "details": details,
                            }
                
                    
                    resource_type: MetaOapg.properties.resource_type
                    details: 'Returned'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'Returned': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'Returned': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        details: 'Returned',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            resource_type=resource_type,
                            details=details,
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
                        CreativeBase,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class all_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "resource_type",
                            "details",
                            "from",
                        }
                        
                        class properties:
                            
                            
                            class resource_type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def LETTER(cls):
                                    return cls("letter")
                        
                            @staticmethod
                            def details() -> typing.Type['LetterDetailsReturned']:
                                return LetterDetailsReturned
                            __annotations__ = {
                                "resource_type": resource_type,
                                "details": details,
                            }
                
                    
                    resource_type: MetaOapg.properties.resource_type
                    details: 'LetterDetailsReturned'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'LetterDetailsReturned': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'LetterDetailsReturned': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        details: 'LetterDetailsReturned',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            resource_type=resource_type,
                            details=details,
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
                        CreativeBase,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_2(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class all_of_0(
                    schemas.AnyTypeSchema,
                ):
                
                
                    class MetaOapg:
                        required = {
                            "resource_type",
                            "details",
                        }
                        
                        class properties:
                            
                            
                            class resource_type(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                                
                                @schemas.classproperty
                                def SELF_MAILER(cls):
                                    return cls("self_mailer")
                        
                            @staticmethod
                            def details() -> typing.Type['SelfMailerDetailsReturned']:
                                return SelfMailerDetailsReturned
                            __annotations__ = {
                                "resource_type": resource_type,
                                "details": details,
                            }
                
                    
                    resource_type: MetaOapg.properties.resource_type
                    details: 'SelfMailerDetailsReturned'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'SelfMailerDetailsReturned': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'SelfMailerDetailsReturned': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "details", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        details: 'SelfMailerDetailsReturned',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            resource_type=resource_type,
                            details=details,
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
                        CreativeBase,
                    ]
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_2':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
                cls.one_of_2,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ReturnedResource':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.creative_base import CreativeBase
from lob_python_sdk.model.letter_details_returned import LetterDetailsReturned
from lob_python_sdk.model.returned import Returned
from lob_python_sdk.model.self_mailer_details_returned import SelfMailerDetailsReturned
