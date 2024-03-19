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


SelfMailerTypes = Literal["self_mailer.created", "self_mailer.rendered_pdf", "self_mailer.rendered_thumbnails", "self_mailer.deleted", "self_mailer.delivered", "self_mailer.failed", "self_mailer.mailed", "self_mailer.in_transit", "self_mailer.in_local_area", "self_mailer.international_exit", "self_mailer.processed_for_delivery", "self_mailer.re-routed", "self_mailer.returned_to_sender", "self_mailer.viewed"]
