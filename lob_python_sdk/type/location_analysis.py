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


class RequiredLocationAnalysis(TypedDict):
    # A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be used with `longitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). 
    latitude: typing.Optional[typing.Union[int, float]]

    # A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be used with `latitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). 
    longitude: typing.Optional[typing.Union[int, float]]

    # The distance from the input location to this exact zip code in miles. 
    distance: typing.Union[int, float]

class OptionalLocationAnalysis(TypedDict, total=False):
    pass

class LocationAnalysis(RequiredLocationAnalysis, OptionalLocationAnalysis):
    pass
