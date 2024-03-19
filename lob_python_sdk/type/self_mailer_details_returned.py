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

from lob_python_sdk.type.mail_type import MailType
from lob_python_sdk.type.self_mailer_size import SelfMailerSize

class RequiredSelfMailerDetailsReturned(TypedDict):
    pass

class OptionalSelfMailerDetailsReturned(TypedDict, total=False):
    mail_type: MailType

    size: SelfMailerSize

    # The original URL of the `inside` template.
    inside_original_url: str

    # The original URL of the `outside` template.
    outside_original_url: str

class SelfMailerDetailsReturned(RequiredSelfMailerDetailsReturned, OptionalSelfMailerDetailsReturned):
    pass
