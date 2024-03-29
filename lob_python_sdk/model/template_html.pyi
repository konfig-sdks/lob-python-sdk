# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from lob_python_sdk import schemas  # noqa: F401


class TemplateHtml(
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An HTML string of less than 100,000 characters to be used as the `published_version` of this template. See [here](#section/HTML-Examples) for guidance on designing HTML templates. Please see endpoint specific documentation for any other product-specific HTML details:
- [Postcards](#operation/postcard_create) - `front` and `back`
- [Self Mailers](#operation/self_mailer_create) - `inside` and `outside`
- [Letters](#operation/letter_create) - `file`
- [Checks](#operation/check_create) - `check_bottom` and `attachment`
- [Cards](#operation/card_create) - `front` and `back`

If there is a syntax error with your variable names within your HTML, then an error will be thrown, e.g. using a `{{#users}}` opening tag without the corresponding closing tag `{{/users}}`.

    """
    pass
