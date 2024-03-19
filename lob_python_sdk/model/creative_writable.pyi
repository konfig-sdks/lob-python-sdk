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


class CreativeWritable(
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
                            "back",
                            "details",
                            "front",
                            "campaign_id",
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
                            def campaign_id() -> typing.Type['CmpId']:
                                return CmpId
                        
                            @staticmethod
                            def front() -> typing.Type['CrvFront']:
                                return CrvFront
                        
                            @staticmethod
                            def back() -> typing.Type['CrvBack']:
                                return CrvBack
                        
                            @staticmethod
                            def details() -> typing.Type['Writable']:
                                return Writable
                            __annotations__ = {
                                "resource_type": resource_type,
                                "campaign_id": campaign_id,
                                "front": front,
                                "back": back,
                                "details": details,
                            }
                
                    
                    resource_type: MetaOapg.properties.resource_type
                    back: 'CrvBack'
                    details: 'Writable'
                    front: 'CrvFront'
                    campaign_id: 'CmpId'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["front"]) -> 'CrvFront': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["back"]) -> 'CrvBack': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'Writable': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "front", "back", "details", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["front"]) -> 'CrvFront': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["back"]) -> 'CrvBack': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'Writable': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "front", "back", "details", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        back: 'CrvBack',
                        details: 'Writable',
                        front: 'CrvFront',
                        campaign_id: 'CmpId',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            resource_type=resource_type,
                            back=back,
                            details=details,
                            front=front,
                            campaign_id=campaign_id,
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
                            "file",
                            "resource_type",
                            "details",
                            "from",
                            "campaign_id",
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
                            def campaign_id() -> typing.Type['CmpId']:
                                return CmpId
                        
                            @staticmethod
                            def details() -> typing.Type['LetterDetailsWritable']:
                                return LetterDetailsWritable
                        
                            @staticmethod
                            def file() -> typing.Type['CrvFile']:
                                return CrvFile
                            __annotations__ = {
                                "resource_type": resource_type,
                                "campaign_id": campaign_id,
                                "details": details,
                                "file": file,
                            }
                
                    
                    file: 'CrvFile'
                    resource_type: MetaOapg.properties.resource_type
                    details: 'LetterDetailsWritable'
                    campaign_id: 'CmpId'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'LetterDetailsWritable': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'CrvFile': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "details", "file", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'LetterDetailsWritable': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> 'CrvFile': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "details", "file", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        file: 'CrvFile',
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        details: 'LetterDetailsWritable',
                        campaign_id: 'CmpId',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            file=file,
                            resource_type=resource_type,
                            details=details,
                            campaign_id=campaign_id,
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
                            "outside",
                            "resource_type",
                            "details",
                            "inside",
                            "campaign_id",
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
                            def campaign_id() -> typing.Type['CmpId']:
                                return CmpId
                        
                            @staticmethod
                            def inside() -> typing.Type['CrvInside']:
                                return CrvInside
                        
                            @staticmethod
                            def outside() -> typing.Type['CrvOutside']:
                                return CrvOutside
                        
                            @staticmethod
                            def details() -> typing.Type['SelfMailerDetailsWritable']:
                                return SelfMailerDetailsWritable
                            __annotations__ = {
                                "resource_type": resource_type,
                                "campaign_id": campaign_id,
                                "inside": inside,
                                "outside": outside,
                                "details": details,
                            }
                
                    
                    outside: 'CrvOutside'
                    resource_type: MetaOapg.properties.resource_type
                    details: 'SelfMailerDetailsWritable'
                    inside: 'CrvInside'
                    campaign_id: 'CmpId'
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["inside"]) -> 'CrvInside': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["outside"]) -> 'CrvOutside': ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["details"]) -> 'SelfMailerDetailsWritable': ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "inside", "outside", "details", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> 'CmpId': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["inside"]) -> 'CrvInside': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["outside"]) -> 'CrvOutside': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> 'SelfMailerDetailsWritable': ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["resource_type", "campaign_id", "inside", "outside", "details", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                        outside: 'CrvOutside',
                        resource_type: typing.Union[MetaOapg.properties.resource_type, str, ],
                        details: 'SelfMailerDetailsWritable',
                        inside: 'CrvInside',
                        campaign_id: 'CmpId',
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'all_of_0':
                        return super().__new__(
                            cls,
                            *args,
                            outside=outside,
                            resource_type=resource_type,
                            details=details,
                            inside=inside,
                            campaign_id=campaign_id,
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
    ) -> 'CreativeWritable':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.cmp_id import CmpId
from lob_python_sdk.model.creative_base import CreativeBase
from lob_python_sdk.model.crv_back import CrvBack
from lob_python_sdk.model.crv_file import CrvFile
from lob_python_sdk.model.crv_front import CrvFront
from lob_python_sdk.model.crv_inside import CrvInside
from lob_python_sdk.model.crv_outside import CrvOutside
from lob_python_sdk.model.letter_details_writable import LetterDetailsWritable
from lob_python_sdk.model.self_mailer_details_writable import SelfMailerDetailsWritable
from lob_python_sdk.model.writable import Writable
