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

from lob_python_sdk.pydantic.cmp_id import CmpId
from lob_python_sdk.pydantic.optional_address_column_mapping import OptionalAddressColumnMapping
from lob_python_sdk.pydantic.required_address_column_mapping import RequiredAddressColumnMapping
from lob_python_sdk.pydantic.uploads_metadata import UploadsMetadata

class UploadWritable(BaseModel):
    campaign_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='campaignId')

    required_address_column_mapping: typing.Optional[RequiredAddressColumnMapping] = Field(None, alias='requiredAddressColumnMapping')

    optional_address_column_mapping: typing.Optional[OptionalAddressColumnMapping] = Field(None, alias='optionalAddressColumnMapping')

    metadata: typing.Optional[UploadsMetadata] = Field(None, alias='metadata')

    # The mapping of column headers in your file to the merge variables present in your creative. See our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#step-3-map-merge-variable-data-if-applicable-7\" target=\"_blank\">Campaign Audience Guide</a> for additional details. <br />If a merge variable has the same \"name\" as a \"key\" in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects, then they **CANNOT** have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects. If using customized QR code redirect from the Audience file, then a `qr_code_redirect_url` must be mapped to the column header as used in the CSV.
    merge_variable_column_mapping: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='mergeVariableColumnMapping')
    class Config:
        arbitrary_types_allowed = True
