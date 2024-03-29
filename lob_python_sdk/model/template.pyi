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


class Template(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "versions",
            "id",
            "published_version",
        }
        
        class properties:
        
            @staticmethod
            def id() -> typing.Type['TmplId']:
                return TmplId
            
            
            class versions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TemplateVersion']:
                        return TemplateVersion
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TemplateVersion'], typing.List['TemplateVersion']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'versions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TemplateVersion':
                    return super().__getitem__(i)
            
            
            class published_version(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.AnyTypeSchema
                    
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
                            TemplateVersion,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'published_version':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def description() -> typing.Type['ResourceDescription']:
                return ResourceDescription
            
            
            class object(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TEMPLATE(cls):
                    return cls("template")
        
            @staticmethod
            def metadata() -> typing.Type['Metadata']:
                return Metadata
            date_created = schemas.DateTimeSchema
            date_modified = schemas.DateTimeSchema
            deleted = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "versions": versions,
                "published_version": published_version,
                "description": description,
                "object": object,
                "metadata": metadata,
                "date_created": date_created,
                "date_modified": date_modified,
                "deleted": deleted,
            }
    
    versions: MetaOapg.properties.versions
    id: 'TmplId'
    published_version: MetaOapg.properties.published_version
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'TmplId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_version"]) -> MetaOapg.properties.published_version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_created"]) -> MetaOapg.properties.date_created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_modified"]) -> MetaOapg.properties.date_modified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "versions", "published_version", "description", "object", "metadata", "date_created", "date_modified", "deleted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'TmplId': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_version"]) -> MetaOapg.properties.published_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_created"]) -> typing.Union[MetaOapg.properties.date_created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_modified"]) -> typing.Union[MetaOapg.properties.date_modified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> typing.Union[MetaOapg.properties.deleted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "versions", "published_version", "description", "object", "metadata", "date_created", "date_modified", "deleted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        versions: typing.Union[MetaOapg.properties.versions, list, tuple, ],
        id: 'TmplId',
        published_version: typing.Union[MetaOapg.properties.published_version, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
        object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
        date_created: typing.Union[MetaOapg.properties.date_created, str, datetime, schemas.Unset] = schemas.unset,
        date_modified: typing.Union[MetaOapg.properties.date_modified, str, datetime, schemas.Unset] = schemas.unset,
        deleted: typing.Union[MetaOapg.properties.deleted, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Template':
        return super().__new__(
            cls,
            *args,
            versions=versions,
            id=id,
            published_version=published_version,
            description=description,
            object=object,
            metadata=metadata,
            date_created=date_created,
            date_modified=date_modified,
            deleted=deleted,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription
from lob_python_sdk.model.template_version import TemplateVersion
from lob_python_sdk.model.tmpl_id import TmplId
