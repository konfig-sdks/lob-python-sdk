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


class Campaign(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_2(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "use_type",
                    "schedule_type",
                    "date_modified",
                    "date_created",
                    "is_draft",
                    "auto_cancel_if_ncoa",
                    "creatives",
                    "name",
                    "description",
                    "id",
                    "object",
                    "uploads",
                }
                
                class properties:
                
                    @staticmethod
                    def id() -> typing.Type['CmpId']:
                        return CmpId
                    is_draft = schemas.BoolSchema
                    
                    
                    class creatives(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Creative']:
                                return Creative
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Creative'], typing.List['Creative']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'creatives':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Creative':
                            return super().__getitem__(i)
                    
                    
                    class uploads(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Upload']:
                                return Upload
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Upload'], typing.List['Upload']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'uploads':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Upload':
                            return super().__getitem__(i)
                    
                    
                    class object(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def CAMPAIGN(cls):
                            return cls("campaign")
                
                    @staticmethod
                    def use_type() -> typing.Type['CmpUseType']:
                        return CmpUseType
                    __annotations__ = {
                        "id": id,
                        "is_draft": is_draft,
                        "creatives": creatives,
                        "uploads": uploads,
                        "object": object,
                        "use_type": use_type,
                    }
            
            use_type: 'CmpUseType'
            schedule_type: schemas.AnyTypeSchema
            date_modified: schemas.AnyTypeSchema
            date_created: schemas.AnyTypeSchema
            is_draft: MetaOapg.properties.is_draft
            auto_cancel_if_ncoa: schemas.AnyTypeSchema
            creatives: MetaOapg.properties.creatives
            name: schemas.AnyTypeSchema
            description: schemas.AnyTypeSchema
            id: 'CmpId'
            object: MetaOapg.properties.object
            uploads: MetaOapg.properties.uploads
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'CmpId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["is_draft"]) -> MetaOapg.properties.is_draft: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["creatives"]) -> MetaOapg.properties.creatives: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["uploads"]) -> MetaOapg.properties.uploads: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["use_type"]) -> 'CmpUseType': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "is_draft", "creatives", "uploads", "object", "use_type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'CmpId': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["is_draft"]) -> MetaOapg.properties.is_draft: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["creatives"]) -> MetaOapg.properties.creatives: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["uploads"]) -> MetaOapg.properties.uploads: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["use_type"]) -> 'CmpUseType': ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "is_draft", "creatives", "uploads", "object", "use_type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                use_type: 'CmpUseType',
                schedule_type: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                date_modified: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                date_created: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                is_draft: typing.Union[MetaOapg.properties.is_draft, bool, ],
                auto_cancel_if_ncoa: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                creatives: typing.Union[MetaOapg.properties.creatives, list, tuple, ],
                name: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                description: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                id: 'CmpId',
                object: typing.Union[MetaOapg.properties.object, str, ],
                uploads: typing.Union[MetaOapg.properties.uploads, list, tuple, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_2':
                return super().__new__(
                    cls,
                    *args,
                    use_type=use_type,
                    schedule_type=schedule_type,
                    date_modified=date_modified,
                    date_created=date_created,
                    is_draft=is_draft,
                    auto_cancel_if_ncoa=auto_cancel_if_ncoa,
                    creatives=creatives,
                    name=name,
                    description=description,
                    id=id,
                    object=object,
                    uploads=uploads,
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
                CampaignWritable,
                cls.all_of_2,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Campaign':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.campaign_writable import CampaignWritable
from lob_python_sdk.model.cmp_id import CmpId
from lob_python_sdk.model.cmp_use_type import CmpUseType
from lob_python_sdk.model.creative import Creative
from lob_python_sdk.model.lob_base import LobBase
from lob_python_sdk.model.upload import Upload
