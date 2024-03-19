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

from lob_python_sdk.type.cmp_schedule_type import CmpScheduleType
from lob_python_sdk.type.cmp_use_type import CmpUseType
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.resource_description import ResourceDescription

class RequiredCampaignUpdatable(TypedDict):
    pass

class OptionalCampaignUpdatable(TypedDict, total=False):
    description: ResourceDescription

    name: str

    schedule_type: CmpScheduleType

    # If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign.
    target_delivery_date: datetime

    # If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign.
    send_date: datetime

    # A window, in minutes, within which the campaign can be canceled.
    cancel_window_campaign_minutes: int

    metadata: Metadata

    # Whether or not the campaign is still a draft. Can either be excluded or `false`.
    is_draft: bool

    use_type: CmpUseType

    # Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA.
    auto_cancel_if_ncoa: bool

class CampaignUpdatable(RequiredCampaignUpdatable, OptionalCampaignUpdatable):
    pass
