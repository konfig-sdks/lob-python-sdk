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

from lob_python_sdk.type.campaign_id import CampaignId
from lob_python_sdk.type.failure_reason import FailureReason
from lob_python_sdk.type.from_us import FromUs
from lob_python_sdk.type.generated import Generated
from lob_python_sdk.type.postcard_base import PostcardBase
from lob_python_sdk.type.psc_id import PscId
from lob_python_sdk.type.psc_use_type import PscUseType
from lob_python_sdk.type.signed_link import SignedLink
from lob_python_sdk.type.status import Status
from lob_python_sdk.type.tracking_event_normal import TrackingEventNormal

Postcard = typing.Union[PostcardBase,Generated,FromUs,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
