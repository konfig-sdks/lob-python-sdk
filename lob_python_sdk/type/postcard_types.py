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


PostcardTypes = Literal["postcard.created", "postcard.rendered_pdf", "postcard.rendered_thumbnails", "postcard.deleted", "postcard.delivered", "postcard.failed", "postcard.mailed", "postcard.in_transit", "postcard.in_local_area", "postcard.international_exit", "postcard.processed_for_delivery", "postcard.re-routed", "postcard.returned_to_sender", "postcard.viewed"]
