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


class UploadState(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The `state` property on the `upload` object. As the file is processed, the `state` will change from `Ready for Validation` to `Validating` and then will be either `Scheduled` (successfully processed) or `Errored` (Unsuccessfully processed).
    """


    class MetaOapg:
        enum_value_to_name = {
            "Preprocessing": "PREPROCESSING",
            "Draft": "DRAFT",
            "Ready for Validation": "READY_FOR_VALIDATION",
            "Validating": "VALIDATING",
            "Scheduled": "SCHEDULED",
            "Cancelled": "CANCELLED",
            "Errored": "ERRORED",
        }
    
    @schemas.classproperty
    def PREPROCESSING(cls):
        return cls("Preprocessing")
    
    @schemas.classproperty
    def DRAFT(cls):
        return cls("Draft")
    
    @schemas.classproperty
    def READY_FOR_VALIDATION(cls):
        return cls("Ready for Validation")
    
    @schemas.classproperty
    def VALIDATING(cls):
        return cls("Validating")
    
    @schemas.classproperty
    def SCHEDULED(cls):
        return cls("Scheduled")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("Cancelled")
    
    @schemas.classproperty
    def ERRORED(cls):
        return cls("Errored")