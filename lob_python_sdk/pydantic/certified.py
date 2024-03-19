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
from lob_python_sdk.pydantic.custom_envelope_returned import CustomEnvelopeReturned
from lob_python_sdk.pydantic.letter_generated_base import LetterGeneratedBase
from lob_python_sdk.pydantic.mail_type import MailType
from lob_python_sdk.pydantic.merge_variables import MergeVariables
from lob_python_sdk.pydantic.metadata import Metadata
from lob_python_sdk.pydantic.resource_description import ResourceDescription
from lob_python_sdk.pydantic.return_address import ReturnAddress
from lob_python_sdk.pydantic.return_envelope_returned import ReturnEnvelopeReturned
from lob_python_sdk.pydantic.send_date import SendDate
from lob_python_sdk.pydantic.tracking_event_certified import TrackingEventCertified

Certified = typing.Union[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]],LetterGeneratedBase]
