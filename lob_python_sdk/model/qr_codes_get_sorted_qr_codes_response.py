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


class QrCodesGetSortedQrCodesResponse(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    object = schemas.StrSchema
                    count = schemas.IntSchema
                    total_count = schemas.IntSchema
                    scanned_count = schemas.IntSchema
                    
                    
                    class data(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['QrCodeScans']:
                                return QrCodeScans
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['QrCodeScans'], typing.List['QrCodeScans']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'data':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'QrCodeScans':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "object": object,
                        "count": count,
                        "total_count": total_count,
                        "scanned_count": scanned_count,
                        "data": data,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["total_count"]) -> MetaOapg.properties.total_count: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["scanned_count"]) -> MetaOapg.properties.scanned_count: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["object", "count", "total_count", "scanned_count", "data", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["total_count"]) -> typing.Union[MetaOapg.properties.total_count, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["scanned_count"]) -> typing.Union[MetaOapg.properties.scanned_count, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["object", "count", "total_count", "scanned_count", "data", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
                count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                total_count: typing.Union[MetaOapg.properties.total_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                scanned_count: typing.Union[MetaOapg.properties.scanned_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    object=object,
                    count=count,
                    total_count=total_count,
                    scanned_count=scanned_count,
                    data=data,
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
    ) -> 'QrCodesGetSortedQrCodesResponse':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.qr_code_scans import QrCodeScans
