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


CheckTypes = Literal["check.created", "check.rendered_pdf", "check.rendered_thumbnails", "check.deleted", "check.delivered", "check.failed", "check.mailed", "check.in_transit", "check.in_local_area", "check.international_exit", "check.processed_for_delivery", "check.re-routed", "check.returned_to_sender"]
