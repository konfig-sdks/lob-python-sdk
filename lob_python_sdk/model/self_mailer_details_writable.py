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


class SelfMailerDetailsWritable(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Properties that the self mailers in your Creative should have. Check within in order to add a QR code to your creative.
    """


    class MetaOapg:
        required = {
            "color",
        }
        
        class properties:
        
            @staticmethod
            def mail_type() -> typing.Type['MailType']:
                return MailType
        
            @staticmethod
            def size() -> typing.Type['SelfMailerSize']:
                return SelfMailerSize
        
            @staticmethod
            def qr_code() -> typing.Type['QrCodeCampaigns']:
                return QrCodeCampaigns
            __annotations__ = {
                "mail_type": mail_type,
                "size": size,
                "qr_code": qr_code,
            }

    
    color: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mail_type"]) -> 'MailType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["size"]) -> 'SelfMailerSize': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["qr_code"]) -> 'QrCodeCampaigns': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["mail_type", "size", "qr_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mail_type"]) -> typing.Union['MailType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["size"]) -> typing.Union['SelfMailerSize', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["qr_code"]) -> typing.Union['QrCodeCampaigns', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["mail_type", "size", "qr_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        mail_type: typing.Union['MailType', schemas.Unset] = schemas.unset,
        size: typing.Union['SelfMailerSize', schemas.Unset] = schemas.unset,
        qr_code: typing.Union['QrCodeCampaigns', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SelfMailerDetailsWritable':
        return super().__new__(
            cls,
            *args,
            mail_type=mail_type,
            size=size,
            qr_code=qr_code,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.mail_type import MailType
from lob_python_sdk.model.qr_code_campaigns import QrCodeCampaigns
from lob_python_sdk.model.self_mailer_size import SelfMailerSize
