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


class Addresses(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def components() -> typing.Type['Components']:
                return Components
        
            @staticmethod
            def location_analysis() -> typing.Type['LocationAnalysis']:
                return LocationAnalysis
            __annotations__ = {
                "components": components,
                "location_analysis": location_analysis,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["components"]) -> 'Components': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_analysis"]) -> 'LocationAnalysis': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["components", "location_analysis", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["components"]) -> typing.Union['Components', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_analysis"]) -> typing.Union['LocationAnalysis', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["components", "location_analysis", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        components: typing.Union['Components', schemas.Unset] = schemas.unset,
        location_analysis: typing.Union['LocationAnalysis', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Addresses':
        return super().__new__(
            cls,
            *args,
            components=components,
            location_analysis=location_analysis,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.components import Components
from lob_python_sdk.model.location_analysis import LocationAnalysis
