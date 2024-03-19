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

class RequiredCampaignWritable(TypedDict):
    # Name of the campaign.
    name: str

    schedule_type: CmpScheduleType

    use_type: CmpUseType

class OptionalCampaignWritable(TypedDict, total=False):
    description: ResourceDescription

    # Unique identifier prefixed with `bg_`.
    billing_group_id: typing.Optional[str]

    # If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign.
    target_delivery_date: typing.Optional[datetime]

    # If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign.
    send_date: typing.Optional[datetime]

    # A window, in minutes, within which the campaign can be canceled.
    cancel_window_campaign_minutes: typing.Optional[int]

    metadata: Metadata

    # Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA.
    auto_cancel_if_ncoa: bool

class CampaignWritable(RequiredCampaignWritable, OptionalCampaignWritable):
    pass
