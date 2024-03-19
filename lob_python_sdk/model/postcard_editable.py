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


class PostcardEditable(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_3(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "use_type",
                    "back",
                    "front",
                    "to",
                }
                
                class properties:
                
                    @staticmethod
                    def front() -> typing.Type['PscFront']:
                        return PscFront
                
                    @staticmethod
                    def back() -> typing.Type['PscBack']:
                        return PscBack
                    billing_group_id = schemas.StrSchema
                
                    @staticmethod
                    def qr_code() -> typing.Type['QrCode']:
                        return QrCode
                
                    @staticmethod
                    def use_type() -> typing.Type['PscUseType']:
                        return PscUseType
                    fsc = schemas.BoolSchema
                    __annotations__ = {
                        "front": front,
                        "back": back,
                        "billing_group_id": billing_group_id,
                        "qr_code": qr_code,
                        "use_type": use_type,
                        "fsc": fsc,
                    }
            
            use_type: 'PscUseType'
            back: 'PscBack'
            front: 'PscFront'
            to: schemas.AnyTypeSchema
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["front"]) -> 'PscFront': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["back"]) -> 'PscBack': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["billing_group_id"]) -> MetaOapg.properties.billing_group_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["qr_code"]) -> 'QrCode': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["use_type"]) -> 'PscUseType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fsc"]) -> MetaOapg.properties.fsc: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["front", "back", "billing_group_id", "qr_code", "use_type", "fsc", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["front"]) -> 'PscFront': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["back"]) -> 'PscBack': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["billing_group_id"]) -> typing.Union[MetaOapg.properties.billing_group_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["qr_code"]) -> typing.Union['QrCode', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["use_type"]) -> 'PscUseType': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fsc"]) -> typing.Union[MetaOapg.properties.fsc, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["front", "back", "billing_group_id", "qr_code", "use_type", "fsc", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                use_type: 'PscUseType',
                back: 'PscBack',
                front: 'PscFront',
                to: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                billing_group_id: typing.Union[MetaOapg.properties.billing_group_id, str, schemas.Unset] = schemas.unset,
                qr_code: typing.Union['QrCode', schemas.Unset] = schemas.unset,
                fsc: typing.Union[MetaOapg.properties.fsc, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *args,
                    use_type=use_type,
                    back=back,
                    front=front,
                    to=to,
                    billing_group_id=billing_group_id,
                    qr_code=qr_code,
                    fsc=fsc,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                PostcardBase,
                InputTo,
                InputFromUs,
                cls.all_of_3,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PostcardEditable':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.input_from_us import InputFromUs
from lob_python_sdk.model.input_to import InputTo
from lob_python_sdk.model.postcard_base import PostcardBase
from lob_python_sdk.model.psc_back import PscBack
from lob_python_sdk.model.psc_front import PscFront
from lob_python_sdk.model.psc_use_type import PscUseType
from lob_python_sdk.model.qr_code import QrCode