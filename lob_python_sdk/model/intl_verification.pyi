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


class IntlVerification(
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
                
                class properties:
                
                    @staticmethod
                    def components() -> typing.Type['IntlComponents']:
                        return IntlComponents
                
                    @staticmethod
                    def id() -> typing.Type['IntlVerId']:
                        return IntlVerId
                    last_line = schemas.StrSchema
                    country = schemas.StrSchema
                    
                    
                    class coverage(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SUBBUILDING(cls):
                            return cls("SUBBUILDING")
                        
                        @schemas.classproperty
                        def HOUSENUMBER_BUILDING(cls):
                            return cls("HOUSENUMBER/BUILDING")
                        
                        @schemas.classproperty
                        def STREET(cls):
                            return cls("STREET")
                        
                        @schemas.classproperty
                        def LOCALITY(cls):
                            return cls("LOCALITY")
                        
                        @schemas.classproperty
                        def SPARSE(cls):
                            return cls("SPARSE")
                    
                    
                    class deliverability(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def DELIVERABLE(cls):
                            return cls("deliverable")
                        
                        @schemas.classproperty
                        def DELIVERABLE_MISSING_INFO(cls):
                            return cls("deliverable_missing_info")
                        
                        @schemas.classproperty
                        def UNDELIVERABLE(cls):
                            return cls("undeliverable")
                        
                        @schemas.classproperty
                        def NO_MATCH(cls):
                            return cls("no_match")
                    
                    
                    class status(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def LV4(cls):
                            return cls("LV4")
                        
                        @schemas.classproperty
                        def LV3(cls):
                            return cls("LV3")
                        
                        @schemas.classproperty
                        def LV2(cls):
                            return cls("LV2")
                        
                        @schemas.classproperty
                        def LV1(cls):
                            return cls("LV1")
                        
                        @schemas.classproperty
                        def LF4(cls):
                            return cls("LF4")
                        
                        @schemas.classproperty
                        def LF3(cls):
                            return cls("LF3")
                        
                        @schemas.classproperty
                        def LF2(cls):
                            return cls("LF2")
                        
                        @schemas.classproperty
                        def LF1(cls):
                            return cls("LF1")
                        
                        @schemas.classproperty
                        def LM4(cls):
                            return cls("LM4")
                        
                        @schemas.classproperty
                        def LM3(cls):
                            return cls("LM3")
                        
                        @schemas.classproperty
                        def LM2(cls):
                            return cls("LM2")
                        
                        @schemas.classproperty
                        def LU1(cls):
                            return cls("LU1")
                    
                    
                    class object(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def INTL_VERIFICATION(cls):
                            return cls("intl_verification")
                    __annotations__ = {
                        "components": components,
                        "id": id,
                        "last_line": last_line,
                        "country": country,
                        "coverage": coverage,
                        "deliverability": deliverability,
                        "status": status,
                        "object": object,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["components"]) -> 'IntlComponents': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'IntlVerId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["last_line"]) -> MetaOapg.properties.last_line: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["coverage"]) -> MetaOapg.properties.coverage: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["deliverability"]) -> MetaOapg.properties.deliverability: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["components", "id", "last_line", "country", "coverage", "deliverability", "status", "object", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["components"]) -> typing.Union['IntlComponents', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union['IntlVerId', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["last_line"]) -> typing.Union[MetaOapg.properties.last_line, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["coverage"]) -> typing.Union[MetaOapg.properties.coverage, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["deliverability"]) -> typing.Union[MetaOapg.properties.deliverability, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["components", "id", "last_line", "country", "coverage", "deliverability", "status", "object", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                components: typing.Union['IntlComponents', schemas.Unset] = schemas.unset,
                id: typing.Union['IntlVerId', schemas.Unset] = schemas.unset,
                last_line: typing.Union[MetaOapg.properties.last_line, str, schemas.Unset] = schemas.unset,
                country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
                coverage: typing.Union[MetaOapg.properties.coverage, str, schemas.Unset] = schemas.unset,
                deliverability: typing.Union[MetaOapg.properties.deliverability, str, schemas.Unset] = schemas.unset,
                status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
                object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    components=components,
                    id=id,
                    last_line=last_line,
                    country=country,
                    coverage=coverage,
                    deliverability=deliverability,
                    status=status,
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
                IntlVerificationBase,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntlVerification':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.intl_components import IntlComponents
from lob_python_sdk.model.intl_ver_id import IntlVerId
from lob_python_sdk.model.intl_verification_base import IntlVerificationBase