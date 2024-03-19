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

from lob_python_sdk.pydantic.campaign_id import CampaignId
from lob_python_sdk.pydantic.failure_reason import FailureReason
from lob_python_sdk.pydantic.from_us import FromUs
from lob_python_sdk.pydantic.generated import Generated
from lob_python_sdk.pydantic.self_mailer_base import SelfMailerBase
from lob_python_sdk.pydantic.sfm_id import SfmId
from lob_python_sdk.pydantic.sfm_use_type import SfmUseType
from lob_python_sdk.pydantic.signed_link import SignedLink
from lob_python_sdk.pydantic.status import Status
from lob_python_sdk.pydantic.tmpl_id import TmplId
from lob_python_sdk.pydantic.tracking_event_certified import TrackingEventCertified
from lob_python_sdk.pydantic.vrsn_id import VrsnId

SelfMailer = typing.Union[SelfMailerBase,Generated,FromUs,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
