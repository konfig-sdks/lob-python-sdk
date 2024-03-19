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


class RecipientValidation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['IdentityValidationId']:
                return IdentityValidationId
        
            @staticmethod
            def recipient() -> typing.Type['IdentityValidationRecipient']:
                return IdentityValidationRecipient
        
            @staticmethod
            def primary_line() -> typing.Type['PrimaryLineUs']:
                return PrimaryLineUs
        
            @staticmethod
            def secondary_line() -> typing.Type['SecondaryLine']:
                return SecondaryLine
        
            @staticmethod
            def urbanization() -> typing.Type['Urbanization']:
                return Urbanization
            last_line = schemas.StrSchema
            
            
            class score(
                schemas.Float32Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'float'
                    inclusive_maximum = 100
                    inclusive_minimum = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'score':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class confidence(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "high": "HIGH",
                        "medium": "MEDIUM",
                        "low": "LOW",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def HIGH(cls):
                    return cls("high")
                
                @schemas.classproperty
                def MEDIUM(cls):
                    return cls("medium")
                
                @schemas.classproperty
                def LOW(cls):
                    return cls("low")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class object(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "id_validation": "ID_VALIDATION",
                    }
                
                @schemas.classproperty
                def ID_VALIDATION(cls):
                    return cls("id_validation")
            __annotations__ = {
                "id": id,
                "recipient": recipient,
                "primary_line": primary_line,
                "secondary_line": secondary_line,
                "urbanization": urbanization,
                "last_line": last_line,
                "score": score,
                "confidence": confidence,
                "object": object,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'IdentityValidationId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient"]) -> 'IdentityValidationRecipient': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_line"]) -> 'PrimaryLineUs': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondary_line"]) -> 'SecondaryLine': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urbanization"]) -> 'Urbanization': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_line"]) -> MetaOapg.properties.last_line: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["score"]) -> MetaOapg.properties.score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["confidence"]) -> MetaOapg.properties.confidence: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "recipient", "primary_line", "secondary_line", "urbanization", "last_line", "score", "confidence", "object", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['IdentityValidationId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient"]) -> typing.Union['IdentityValidationRecipient', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_line"]) -> typing.Union['PrimaryLineUs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondary_line"]) -> typing.Union['SecondaryLine', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urbanization"]) -> typing.Union['Urbanization', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_line"]) -> typing.Union[MetaOapg.properties.last_line, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["score"]) -> typing.Union[MetaOapg.properties.score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["confidence"]) -> typing.Union[MetaOapg.properties.confidence, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "recipient", "primary_line", "secondary_line", "urbanization", "last_line", "score", "confidence", "object", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union['IdentityValidationId', schemas.Unset] = schemas.unset,
        recipient: typing.Union['IdentityValidationRecipient', schemas.Unset] = schemas.unset,
        primary_line: typing.Union['PrimaryLineUs', schemas.Unset] = schemas.unset,
        secondary_line: typing.Union['SecondaryLine', schemas.Unset] = schemas.unset,
        urbanization: typing.Union['Urbanization', schemas.Unset] = schemas.unset,
        last_line: typing.Union[MetaOapg.properties.last_line, str, schemas.Unset] = schemas.unset,
        score: typing.Union[MetaOapg.properties.score, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        confidence: typing.Union[MetaOapg.properties.confidence, str, schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecipientValidation':
        return super().__new__(
            cls,
            *args,
            id=id,
            recipient=recipient,
            primary_line=primary_line,
            secondary_line=secondary_line,
            urbanization=urbanization,
            last_line=last_line,
            score=score,
            confidence=confidence,
            object=object,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.identity_validation_id import IdentityValidationId
from lob_python_sdk.model.identity_validation_recipient import IdentityValidationRecipient
from lob_python_sdk.model.primary_line_us import PrimaryLineUs
from lob_python_sdk.model.secondary_line import SecondaryLine
from lob_python_sdk.model.urbanization import Urbanization
