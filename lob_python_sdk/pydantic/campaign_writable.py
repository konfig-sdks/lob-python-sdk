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

from lob_python_sdk.pydantic.cmp_schedule_type import CmpScheduleType
from lob_python_sdk.pydantic.cmp_use_type import CmpUseType
from lob_python_sdk.pydantic.metadata import Metadata
from lob_python_sdk.pydantic.resource_description import ResourceDescription

class CampaignWritable(BaseModel):
    # Name of the campaign.
    name: str = Field(alias='name')

    schedule_type: CmpScheduleType = Field(alias='schedule_type')

    use_type: CmpUseType = Field(alias='use_type')

    description: typing.Optional[ResourceDescription] = Field(None, alias='description')

    # Unique identifier prefixed with `bg_`.
    billing_group_id: typing.Optional[typing.Optional[str]] = Field(None, alias='billing_group_id')

    # If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign.
    target_delivery_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='target_delivery_date')

    # If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign.
    send_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='send_date')

    # A window, in minutes, within which the campaign can be canceled.
    cancel_window_campaign_minutes: typing.Optional[typing.Optional[int]] = Field(None, alias='cancel_window_campaign_minutes')

    metadata: typing.Optional[Metadata] = Field(None, alias='metadata')

    # Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA.
    auto_cancel_if_ncoa: typing.Optional[bool] = Field(None, alias='auto_cancel_if_ncoa')
    class Config:
        arbitrary_types_allowed = True
