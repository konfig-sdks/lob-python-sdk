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


class UserProvided(
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Accepts an envelope ID for any customized envelope with available inventory. If no inventory is available for the specified ID, the letter will not be sent, and an error will be returned. If the letter has more than 6 sheets, it will be sent in a blank flat envelope. Custom envelopes may be created and ordered from the dashboard. This feature is exclusive to certain customers. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.
    """


    class MetaOapg:
        regex=[{
            'pattern': r'^env_[a-zA-Z0-9]+$',
        }]


    def __new__(
        cls,
        *args: typing.Union[None, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserProvided':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
