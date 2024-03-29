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


class LetterDetailsReturned(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Properties that the letters in your Creative should have. Check within in order to add a QR code to your creative.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def address_placement() -> typing.Type['AddressPlacement']:
                return AddressPlacement
            
            
            class buckslips(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BuckslipId']:
                        return BuckslipId
                    max_items = 1
                    min_items = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'buckslips':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cards(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CardId']:
                        return CardId
                    max_items = 1
                    min_items = 0
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cards':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def custom_envelope() -> typing.Type['CustomEnvelopeReturned']:
                return CustomEnvelopeReturned
            color = schemas.BoolSchema
            double_sided = schemas.BoolSchema
        
            @staticmethod
            def extra_service() -> typing.Type['ExtraService']:
                return ExtraService
            file_original_url = schemas.StrSchema
        
            @staticmethod
            def mail_type() -> typing.Type['MailType']:
                return MailType
            __annotations__ = {
                "address_placement": address_placement,
                "buckslips": buckslips,
                "cards": cards,
                "custom_envelope": custom_envelope,
                "color": color,
                "double_sided": double_sided,
                "extra_service": extra_service,
                "file_original_url": file_original_url,
                "mail_type": mail_type,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_placement"]) -> 'AddressPlacement': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buckslips"]) -> MetaOapg.properties.buckslips: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cards"]) -> MetaOapg.properties.cards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_envelope"]) -> 'CustomEnvelopeReturned': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["double_sided"]) -> MetaOapg.properties.double_sided: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra_service"]) -> 'ExtraService': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_original_url"]) -> MetaOapg.properties.file_original_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mail_type"]) -> 'MailType': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address_placement", "buckslips", "cards", "custom_envelope", "color", "double_sided", "extra_service", "file_original_url", "mail_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_placement"]) -> typing.Union['AddressPlacement', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buckslips"]) -> typing.Union[MetaOapg.properties.buckslips, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cards"]) -> typing.Union[MetaOapg.properties.cards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_envelope"]) -> typing.Union['CustomEnvelopeReturned', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["double_sided"]) -> typing.Union[MetaOapg.properties.double_sided, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra_service"]) -> typing.Union['ExtraService', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_original_url"]) -> typing.Union[MetaOapg.properties.file_original_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mail_type"]) -> typing.Union['MailType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address_placement", "buckslips", "cards", "custom_envelope", "color", "double_sided", "extra_service", "file_original_url", "mail_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        address_placement: typing.Union['AddressPlacement', schemas.Unset] = schemas.unset,
        buckslips: typing.Union[MetaOapg.properties.buckslips, list, tuple, None, schemas.Unset] = schemas.unset,
        cards: typing.Union[MetaOapg.properties.cards, list, tuple, None, schemas.Unset] = schemas.unset,
        custom_envelope: typing.Union['CustomEnvelopeReturned', schemas.Unset] = schemas.unset,
        color: typing.Union[MetaOapg.properties.color, bool, schemas.Unset] = schemas.unset,
        double_sided: typing.Union[MetaOapg.properties.double_sided, bool, schemas.Unset] = schemas.unset,
        extra_service: typing.Union['ExtraService', schemas.Unset] = schemas.unset,
        file_original_url: typing.Union[MetaOapg.properties.file_original_url, str, schemas.Unset] = schemas.unset,
        mail_type: typing.Union['MailType', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LetterDetailsReturned':
        return super().__new__(
            cls,
            *args,
            address_placement=address_placement,
            buckslips=buckslips,
            cards=cards,
            custom_envelope=custom_envelope,
            color=color,
            double_sided=double_sided,
            extra_service=extra_service,
            file_original_url=file_original_url,
            mail_type=mail_type,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.address_placement import AddressPlacement
from lob_python_sdk.model.buckslip_id import BuckslipId
from lob_python_sdk.model.card_id import CardId
from lob_python_sdk.model.custom_envelope_returned import CustomEnvelopeReturned
from lob_python_sdk.model.extra_service import ExtraService
from lob_python_sdk.model.mail_type import MailType
