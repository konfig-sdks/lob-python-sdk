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


class LetterTypes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Unique identifier referring to status of letter
    """
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("letter.created")
    
    @schemas.classproperty
    def RENDERED_PDF(cls):
        return cls("letter.rendered_pdf")
    
    @schemas.classproperty
    def RENDERED_THUMBNAILS(cls):
        return cls("letter.rendered_thumbnails")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("letter.deleted")
    
    @schemas.classproperty
    def DELIVERED(cls):
        return cls("letter.delivered")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("letter.failed")
    
    @schemas.classproperty
    def MAILED(cls):
        return cls("letter.mailed")
    
    @schemas.classproperty
    def IN_TRANSIT(cls):
        return cls("letter.in_transit")
    
    @schemas.classproperty
    def IN_LOCAL_AREA(cls):
        return cls("letter.in_local_area")
    
    @schemas.classproperty
    def INTERNATIONAL_EXIT(cls):
        return cls("letter.international_exit")
    
    @schemas.classproperty
    def PROCESSED_FOR_DELIVERY(cls):
        return cls("letter.processed_for_delivery")
    
    @schemas.classproperty
    def REROUTED(cls):
        return cls("letter.re-routed")
    
    @schemas.classproperty
    def RETURNED_TO_SENDER(cls):
        return cls("letter.returned_to_sender")
    
    @schemas.classproperty
    def CERTIFIED_MAILED(cls):
        return cls("letter.certified.mailed")
    
    @schemas.classproperty
    def CERTIFIED_IN_TRANSIT(cls):
        return cls("letter.certified.in_transit")
    
    @schemas.classproperty
    def CERTIFIED_IN_LOCAL_AREA(cls):
        return cls("letter.certified.in_local_area")
    
    @schemas.classproperty
    def CERTIFIED_PROCESSED_FOR_DELIVERY(cls):
        return cls("letter.certified.processed_for_delivery")
    
    @schemas.classproperty
    def CERTIFIED_REROUTED(cls):
        return cls("letter.certified.re-routed")
    
    @schemas.classproperty
    def CERTIFIED_RETURNED_TO_SENDER(cls):
        return cls("letter.certified.returned_to_sender")
    
    @schemas.classproperty
    def CERTIFIED_DELIVERED(cls):
        return cls("letter.certified.delivered")
    
    @schemas.classproperty
    def CERTIFIED_PICKUP_AVAILABLE(cls):
        return cls("letter.certified.pickup_available")
    
    @schemas.classproperty
    def CERTIFIED_ISSUE(cls):
        return cls("letter.certified.issue")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_CREATED(cls):
        return cls("letter.return_envelope.created")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_DELIVERED(cls):
        return cls("letter.return_envelope.delivered")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_IN_TRANSIT(cls):
        return cls("letter.return_envelope.in_transit")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_IN_LOCAL_AREA(cls):
        return cls("letter.return_envelope.in_local_area")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_INTERNATIONAL_EXIT(cls):
        return cls("letter.return_envelope.international_exit")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_PROCESSED_FOR_DELIVERY(cls):
        return cls("letter.return_envelope.processed_for_delivery")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_RE_ROUTED(cls):
        return cls("letter.return_envelope.re_routed")
    
    @schemas.classproperty
    def RETURN_ENVELOPE_RETURNED_TO_SENDER(cls):
        return cls("letter.return_envelope.returned_to_sender")
    
    @schemas.classproperty
    def VIEWED(cls):
        return cls("letter.viewed")
