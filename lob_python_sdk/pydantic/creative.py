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

from lob_python_sdk.pydantic.campaign_list import CampaignList
from lob_python_sdk.pydantic.crv_id import CrvId
from lob_python_sdk.pydantic.lob_base import LobBase
from lob_python_sdk.pydantic.returned_resource import ReturnedResource

Creative = typing.Union[LobBase,ReturnedResource,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
