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


class QrCode(BaseModel):
    # Sets how a QR code is being positioned in the document. Together with this, you should provide one of 'top' or 'bottom', and one of 'left' or 'right'.
    position: Literal["relative"] = Field(alias='position')

    # The url to redirect the user when a QR code is scanned. The url must start with `https://`
    redirect_url: str = Field(alias='redirect_url')

    # The size (in inches) of the QR code with a minimum of 1 inch. All QR codes are generated as a square.
    width: str = Field(alias='width')

    # Vertical distance (in inches) to place QR code from the top. Only allowed if \"bottom\" isn't provided.
    top: typing.Optional[str] = Field(None, alias='top')

    # Horizontal distance (in inches) to place QR code from the right. Only allowed if \"left\" isn't provided.
    right: typing.Optional[str] = Field(None, alias='right')

    # Horizontal distance (in inches) to place QR code from the left. Only allowed if \"right\" isn't provided.
    left: typing.Optional[str] = Field(None, alias='left')

    # Vertical distance (in inches) to place QR code from the bottom. Only allowed if \"top\" isn't provided.
    bottom: typing.Optional[str] = Field(None, alias='bottom')

    # Specify the pages where the QR code should be stamped in a comma separated format. Your QR code can be printed in the same position on multiple pages. For postcards, the values should either be \"front\", \"back\" (for either front or back) or \"front,back\" (for the QR code to be printed on both sides). For self-mailers, the values should either be \"inside\", \"outside\" (for either inside or outside) or \"inside,outside\" (for the QR code to be printed on both sides). For letters, the values can be specific page numbers (\"1\", \"3\"), page number ranges such as \"1-3\", or a comma separated combination of both (\"1,3,5-7\").
    pages: typing.Optional[str] = Field(None, alias='pages')
    class Config:
        arbitrary_types_allowed = True
