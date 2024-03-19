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
from lob_python_sdk.pydantic.signed_link import SignedLink
from lob_python_sdk.pydantic.snap_pack_base import SnapPackBase
from lob_python_sdk.pydantic.snap_pack_id import SnapPackId
from lob_python_sdk.pydantic.snap_pack_use_type import SnapPackUseType
from lob_python_sdk.pydantic.status import Status
from lob_python_sdk.pydantic.tmpl_id import TmplId
from lob_python_sdk.pydantic.tracking_event_normal import TrackingEventNormal
from lob_python_sdk.pydantic.vrsn_id import VrsnId

SnapPack = typing.Union[SnapPackBase,Generated,FromUs,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
