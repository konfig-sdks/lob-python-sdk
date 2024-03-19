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


class LobConfidenceScore(BaseModel):
    # A numerical score between 0 and 100 that represents the percentage of mailpieces Lob has sent to this addresses that have been delivered successfully over the past 2 years. Will be `null` if no tracking data exists for this address. 
    score: typing.Optional[typing.Union[int, float]] = Field(alias='score')

    # Indicates the likelihood that the address is a valid, mail-receiving address. Possible values are:   - `high` — Over 70% of mailpieces Lob has sent to this address were delivered successfully and recent mailings were also successful.   - `medium` — Between 40% and 70% of mailpieces Lob has sent to this address were delivered successfully.   - `low` — Less than 40% of mailpieces Lob has sent to this address were delivered successfully and recent mailings weren't successful.   - `\"\"` — No tracking data exists for this address or lob deliverability was unable to find a corresponding level of mail success. 
    level: Literal["high", "medium", "low", ""] = Field(alias='level')
    class Config:
        arbitrary_types_allowed = True
