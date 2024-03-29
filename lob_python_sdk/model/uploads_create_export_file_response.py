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


class UploadsCreateExportFileResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
            "message",
            "errors",
        }
        
        class properties:
            
            
            class code(
                schemas.EnumBase,
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        400: "POSITIVE_400",
                        404: "POSITIVE_404",
                    }
                
                @schemas.classproperty
                def POSITIVE_400(cls):
                    return cls(400)
                
                @schemas.classproperty
                def POSITIVE_404(cls):
                    return cls(404)
            message = schemas.StrSchema
        
            @staticmethod
            def errors() -> typing.Type['UploadsCreateExportFileResponseErrors']:
                return UploadsCreateExportFileResponseErrors
            __annotations__ = {
                "code": code,
                "message": message,
                "errors": errors,
            }
    
    code: MetaOapg.properties.code
    message: MetaOapg.properties.message
    errors: 'UploadsCreateExportFileResponseErrors'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errors"]) -> 'UploadsCreateExportFileResponseErrors': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "message", "errors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errors"]) -> 'UploadsCreateExportFileResponseErrors': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "message", "errors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, decimal.Decimal, int, float, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        errors: 'UploadsCreateExportFileResponseErrors',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UploadsCreateExportFileResponse':
        return super().__new__(
            cls,
            *args,
            code=code,
            message=message,
            errors=errors,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.uploads_create_export_file_response_errors import UploadsCreateExportFileResponseErrors
