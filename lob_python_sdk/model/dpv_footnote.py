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


class DpvFootnote(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "AA": "AA",
            "A1": "A1",
            "BB": "BB",
            "CC": "CC",
            "N1": "N1",
            "F1": "F1",
            "G1": "G1",
            "U1": "U1",
            "M1": "M1",
            "M3": "M3",
            "P1": "P1",
            "P3": "P3",
            "R1": "R1",
            "R7": "R7",
            "RR": "RR",
        }
    
    @schemas.classproperty
    def AA(cls):
        return cls("AA")
    
    @schemas.classproperty
    def A1(cls):
        return cls("A1")
    
    @schemas.classproperty
    def BB(cls):
        return cls("BB")
    
    @schemas.classproperty
    def CC(cls):
        return cls("CC")
    
    @schemas.classproperty
    def N1(cls):
        return cls("N1")
    
    @schemas.classproperty
    def F1(cls):
        return cls("F1")
    
    @schemas.classproperty
    def G1(cls):
        return cls("G1")
    
    @schemas.classproperty
    def U1(cls):
        return cls("U1")
    
    @schemas.classproperty
    def M1(cls):
        return cls("M1")
    
    @schemas.classproperty
    def M3(cls):
        return cls("M3")
    
    @schemas.classproperty
    def P1(cls):
        return cls("P1")
    
    @schemas.classproperty
    def P3(cls):
        return cls("P3")
    
    @schemas.classproperty
    def R1(cls):
        return cls("R1")
    
    @schemas.classproperty
    def R7(cls):
        return cls("R7")
    
    @schemas.classproperty
    def RR(cls):
        return cls("RR")
