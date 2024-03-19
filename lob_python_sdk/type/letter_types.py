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


LetterTypes = Literal["letter.created", "letter.rendered_pdf", "letter.rendered_thumbnails", "letter.deleted", "letter.delivered", "letter.failed", "letter.mailed", "letter.in_transit", "letter.in_local_area", "letter.international_exit", "letter.processed_for_delivery", "letter.re-routed", "letter.returned_to_sender", "letter.certified.mailed", "letter.certified.in_transit", "letter.certified.in_local_area", "letter.certified.processed_for_delivery", "letter.certified.re-routed", "letter.certified.returned_to_sender", "letter.certified.delivered", "letter.certified.pickup_available", "letter.certified.issue", "letter.return_envelope.created", "letter.return_envelope.delivered", "letter.return_envelope.in_transit", "letter.return_envelope.in_local_area", "letter.return_envelope.international_exit", "letter.return_envelope.processed_for_delivery", "letter.return_envelope.re_routed", "letter.return_envelope.returned_to_sender", "letter.viewed"]
