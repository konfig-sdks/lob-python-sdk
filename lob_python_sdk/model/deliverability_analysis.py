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


class DeliverabilityAnalysis(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A nested object containing a breakdown of the deliverability of an address.
    """


    class MetaOapg:
        required = {
            "dpv_throwback",
            "lacs_indicator",
            "suite_return_code",
            "dpv_door_not_accessible",
            "ews_match",
            "dpv_inactive_reason",
            "dpv_non_delivery_day_flag",
            "dpv_active",
            "dpv_non_delivery_day_values",
            "dpv_no_secure_location",
            "dpv_confirmation",
            "dpv_vacant",
            "dpv_cmra",
            "lacs_return_code",
            "dpv_footnotes",
        }
        
        class properties:
            
            
            class dpv_confirmation(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "S": "S",
                        "D": "D",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def S(cls):
                    return cls("S")
                
                @schemas.classproperty
                def D(cls):
                    return cls("D")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_cmra(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_vacant(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_active(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_inactive_reason(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "01": "POSITIVE_01",
                        "02": "POSITIVE_02",
                        "03": "POSITIVE_03",
                        "04": "POSITIVE_04",
                        "05": "POSITIVE_05",
                        "06": "POSITIVE_06",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def POSITIVE_01(cls):
                    return cls("01")
                
                @schemas.classproperty
                def POSITIVE_02(cls):
                    return cls("02")
                
                @schemas.classproperty
                def POSITIVE_03(cls):
                    return cls("03")
                
                @schemas.classproperty
                def POSITIVE_04(cls):
                    return cls("04")
                
                @schemas.classproperty
                def POSITIVE_05(cls):
                    return cls("05")
                
                @schemas.classproperty
                def POSITIVE_06(cls):
                    return cls("06")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_throwback(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_non_delivery_day_flag(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            dpv_non_delivery_day_values = schemas.StrSchema
            
            
            class dpv_no_secure_location(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_door_not_accessible(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class dpv_footnotes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DpvFootnote']:
                        return DpvFootnote
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DpvFootnote'], typing.List['DpvFootnote']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dpv_footnotes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DpvFootnote':
                    return super().__getitem__(i)
            ews_match = schemas.BoolSchema
            
            
            class lacs_indicator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Y": "Y",
                        "N": "N",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            lacs_return_code = schemas.StrSchema
            
            
            class suite_return_code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "A": "A",
                        "00": "POSITIVE_00",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def A(cls):
                    return cls("A")
                
                @schemas.classproperty
                def POSITIVE_00(cls):
                    return cls("00")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            __annotations__ = {
                "dpv_confirmation": dpv_confirmation,
                "dpv_cmra": dpv_cmra,
                "dpv_vacant": dpv_vacant,
                "dpv_active": dpv_active,
                "dpv_inactive_reason": dpv_inactive_reason,
                "dpv_throwback": dpv_throwback,
                "dpv_non_delivery_day_flag": dpv_non_delivery_day_flag,
                "dpv_non_delivery_day_values": dpv_non_delivery_day_values,
                "dpv_no_secure_location": dpv_no_secure_location,
                "dpv_door_not_accessible": dpv_door_not_accessible,
                "dpv_footnotes": dpv_footnotes,
                "ews_match": ews_match,
                "lacs_indicator": lacs_indicator,
                "lacs_return_code": lacs_return_code,
                "suite_return_code": suite_return_code,
            }
    
    dpv_throwback: MetaOapg.properties.dpv_throwback
    lacs_indicator: MetaOapg.properties.lacs_indicator
    suite_return_code: MetaOapg.properties.suite_return_code
    dpv_door_not_accessible: MetaOapg.properties.dpv_door_not_accessible
    ews_match: MetaOapg.properties.ews_match
    dpv_inactive_reason: MetaOapg.properties.dpv_inactive_reason
    dpv_non_delivery_day_flag: MetaOapg.properties.dpv_non_delivery_day_flag
    dpv_active: MetaOapg.properties.dpv_active
    dpv_non_delivery_day_values: MetaOapg.properties.dpv_non_delivery_day_values
    dpv_no_secure_location: MetaOapg.properties.dpv_no_secure_location
    dpv_confirmation: MetaOapg.properties.dpv_confirmation
    dpv_vacant: MetaOapg.properties.dpv_vacant
    dpv_cmra: MetaOapg.properties.dpv_cmra
    lacs_return_code: MetaOapg.properties.lacs_return_code
    dpv_footnotes: MetaOapg.properties.dpv_footnotes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_confirmation"]) -> MetaOapg.properties.dpv_confirmation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_cmra"]) -> MetaOapg.properties.dpv_cmra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_vacant"]) -> MetaOapg.properties.dpv_vacant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_active"]) -> MetaOapg.properties.dpv_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_inactive_reason"]) -> MetaOapg.properties.dpv_inactive_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_throwback"]) -> MetaOapg.properties.dpv_throwback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_non_delivery_day_flag"]) -> MetaOapg.properties.dpv_non_delivery_day_flag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_non_delivery_day_values"]) -> MetaOapg.properties.dpv_non_delivery_day_values: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_no_secure_location"]) -> MetaOapg.properties.dpv_no_secure_location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_door_not_accessible"]) -> MetaOapg.properties.dpv_door_not_accessible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dpv_footnotes"]) -> MetaOapg.properties.dpv_footnotes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ews_match"]) -> MetaOapg.properties.ews_match: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lacs_indicator"]) -> MetaOapg.properties.lacs_indicator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lacs_return_code"]) -> MetaOapg.properties.lacs_return_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suite_return_code"]) -> MetaOapg.properties.suite_return_code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dpv_confirmation", "dpv_cmra", "dpv_vacant", "dpv_active", "dpv_inactive_reason", "dpv_throwback", "dpv_non_delivery_day_flag", "dpv_non_delivery_day_values", "dpv_no_secure_location", "dpv_door_not_accessible", "dpv_footnotes", "ews_match", "lacs_indicator", "lacs_return_code", "suite_return_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_confirmation"]) -> MetaOapg.properties.dpv_confirmation: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_cmra"]) -> MetaOapg.properties.dpv_cmra: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_vacant"]) -> MetaOapg.properties.dpv_vacant: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_active"]) -> MetaOapg.properties.dpv_active: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_inactive_reason"]) -> MetaOapg.properties.dpv_inactive_reason: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_throwback"]) -> MetaOapg.properties.dpv_throwback: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_non_delivery_day_flag"]) -> MetaOapg.properties.dpv_non_delivery_day_flag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_non_delivery_day_values"]) -> MetaOapg.properties.dpv_non_delivery_day_values: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_no_secure_location"]) -> MetaOapg.properties.dpv_no_secure_location: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_door_not_accessible"]) -> MetaOapg.properties.dpv_door_not_accessible: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dpv_footnotes"]) -> MetaOapg.properties.dpv_footnotes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ews_match"]) -> MetaOapg.properties.ews_match: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lacs_indicator"]) -> MetaOapg.properties.lacs_indicator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lacs_return_code"]) -> MetaOapg.properties.lacs_return_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suite_return_code"]) -> MetaOapg.properties.suite_return_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dpv_confirmation", "dpv_cmra", "dpv_vacant", "dpv_active", "dpv_inactive_reason", "dpv_throwback", "dpv_non_delivery_day_flag", "dpv_non_delivery_day_values", "dpv_no_secure_location", "dpv_door_not_accessible", "dpv_footnotes", "ews_match", "lacs_indicator", "lacs_return_code", "suite_return_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        dpv_throwback: typing.Union[MetaOapg.properties.dpv_throwback, str, ],
        lacs_indicator: typing.Union[MetaOapg.properties.lacs_indicator, str, ],
        suite_return_code: typing.Union[MetaOapg.properties.suite_return_code, str, ],
        dpv_door_not_accessible: typing.Union[MetaOapg.properties.dpv_door_not_accessible, str, ],
        ews_match: typing.Union[MetaOapg.properties.ews_match, bool, ],
        dpv_inactive_reason: typing.Union[MetaOapg.properties.dpv_inactive_reason, str, ],
        dpv_non_delivery_day_flag: typing.Union[MetaOapg.properties.dpv_non_delivery_day_flag, str, ],
        dpv_active: typing.Union[MetaOapg.properties.dpv_active, str, ],
        dpv_non_delivery_day_values: typing.Union[MetaOapg.properties.dpv_non_delivery_day_values, str, ],
        dpv_no_secure_location: typing.Union[MetaOapg.properties.dpv_no_secure_location, str, ],
        dpv_confirmation: typing.Union[MetaOapg.properties.dpv_confirmation, str, ],
        dpv_vacant: typing.Union[MetaOapg.properties.dpv_vacant, str, ],
        dpv_cmra: typing.Union[MetaOapg.properties.dpv_cmra, str, ],
        lacs_return_code: typing.Union[MetaOapg.properties.lacs_return_code, str, ],
        dpv_footnotes: typing.Union[MetaOapg.properties.dpv_footnotes, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DeliverabilityAnalysis':
        return super().__new__(
            cls,
            *args,
            dpv_throwback=dpv_throwback,
            lacs_indicator=lacs_indicator,
            suite_return_code=suite_return_code,
            dpv_door_not_accessible=dpv_door_not_accessible,
            ews_match=ews_match,
            dpv_inactive_reason=dpv_inactive_reason,
            dpv_non_delivery_day_flag=dpv_non_delivery_day_flag,
            dpv_active=dpv_active,
            dpv_non_delivery_day_values=dpv_non_delivery_day_values,
            dpv_no_secure_location=dpv_no_secure_location,
            dpv_confirmation=dpv_confirmation,
            dpv_vacant=dpv_vacant,
            dpv_cmra=dpv_cmra,
            lacs_return_code=lacs_return_code,
            dpv_footnotes=dpv_footnotes,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.dpv_footnote import DpvFootnote
