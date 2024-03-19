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


class ZipCodeType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A description of the ZIP code type. For more detailed information about
each ZIP code type, see [US Verification Details](#tag/US-Verification-Types).

    """


    class MetaOapg:
        enum_value_to_name = {
            "standard": "STANDARD",
            "po_box": "PO_BOX",
            "unique": "UNIQUE",
            "military": "MILITARY",
            "": "EMPTY",
        }
    
    @schemas.classproperty
    def STANDARD(cls):
        return cls("standard")
    
    @schemas.classproperty
    def PO_BOX(cls):
        return cls("po_box")
    
    @schemas.classproperty
    def UNIQUE(cls):
        return cls("unique")
    
    @schemas.classproperty
    def MILITARY(cls):
        return cls("military")
    
    @schemas.classproperty
    def EMPTY(cls):
        return cls("")
