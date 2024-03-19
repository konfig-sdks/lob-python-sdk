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


class FailureStatusCode(
    schemas.EnumBase,
    schemas.IntSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A conventional HTTP status code:
  * `401` - Authorization error with your API key or account
  * `403` - Forbidden error with your API key or account
  * `404` - The requested item does not exist
  * `413` - Payload too large
  * `422` - The query or body parameters did not pass validation
  * `429` - Too many requests have been sent with an API key in a given amount of time
  * `500` - An internal server error occurred, please contact support@lob.com

    """


    class MetaOapg:
        enum_value_to_name = {
            401: "POSITIVE_401",
            403: "POSITIVE_403",
            404: "POSITIVE_404",
            413: "POSITIVE_413",
            422: "POSITIVE_422",
            429: "POSITIVE_429",
            500: "POSITIVE_500",
        }
    
    @schemas.classproperty
    def POSITIVE_401(cls):
        return cls(401)
    
    @schemas.classproperty
    def POSITIVE_403(cls):
        return cls(403)
    
    @schemas.classproperty
    def POSITIVE_404(cls):
        return cls(404)
    
    @schemas.classproperty
    def POSITIVE_413(cls):
        return cls(413)
    
    @schemas.classproperty
    def POSITIVE_422(cls):
        return cls(422)
    
    @schemas.classproperty
    def POSITIVE_429(cls):
        return cls(429)
    
    @schemas.classproperty
    def POSITIVE_500(cls):
        return cls(500)
