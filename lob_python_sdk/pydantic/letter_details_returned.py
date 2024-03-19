# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from lob_python_sdk.pydantic.address_placement import AddressPlacement
from lob_python_sdk.pydantic.buckslip_id import BuckslipId
from lob_python_sdk.pydantic.card_id import CardId
from lob_python_sdk.pydantic.custom_envelope_returned import CustomEnvelopeReturned
from lob_python_sdk.pydantic.extra_service import ExtraService
from lob_python_sdk.pydantic.mail_type import MailType

class LetterDetailsReturned(BaseModel):
    address_placement: typing.Optional[AddressPlacement] = Field(None, alias='address_placement')

    # A single-element array containing an existing buckslip id in a string format. See [buckslips](#tag/Buckslips) for more information.
    buckslips: typing.Optional[typing.Optional[typing.List[BuckslipId]]] = Field(None, alias='buckslips')

    # A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information.
    cards: typing.Optional[typing.Optional[typing.List[CardId]]] = Field(None, alias='cards')

    custom_envelope: typing.Optional[CustomEnvelopeReturned] = Field(None, alias='custom_envelope')

    # Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white.
    color: typing.Optional[bool] = Field(None, alias='color')

    # Set this attribute to `true` for double sided printing, or `false` for for single sided printing. Defaults to `true`.
    double_sided: typing.Optional[bool] = Field(None, alias='double_sided')

    extra_service: typing.Optional[ExtraService] = Field(None, alias='extra_service')

    # The original URL of the `file` template.
    file_original_url: typing.Optional[str] = Field(None, alias='file_original_url')

    mail_type: typing.Optional[MailType] = Field(None, alias='mail_type')
    class Config:
        arbitrary_types_allowed = True
