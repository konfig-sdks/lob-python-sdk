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


class CampaignWritable(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "use_type",
            "schedule_type",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def schedule_type() -> typing.Type['CmpScheduleType']:
                return CmpScheduleType
        
            @staticmethod
            def use_type() -> typing.Type['CmpUseType']:
                return CmpUseType
        
            @staticmethod
            def description() -> typing.Type['ResourceDescription']:
                return ResourceDescription
            
            
            class billing_group_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^bg_[a-zA-Z0-9]+$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'billing_group_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class target_delivery_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'target_delivery_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class send_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'send_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class cancel_window_campaign_minutes(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cancel_window_campaign_minutes':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def metadata() -> typing.Type['Metadata']:
                return Metadata
            auto_cancel_if_ncoa = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "schedule_type": schedule_type,
                "use_type": use_type,
                "description": description,
                "billing_group_id": billing_group_id,
                "target_delivery_date": target_delivery_date,
                "send_date": send_date,
                "cancel_window_campaign_minutes": cancel_window_campaign_minutes,
                "metadata": metadata,
                "auto_cancel_if_ncoa": auto_cancel_if_ncoa,
            }
    
    use_type: 'CmpUseType'
    schedule_type: 'CmpScheduleType'
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["schedule_type"]) -> 'CmpScheduleType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["use_type"]) -> 'CmpUseType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billing_group_id"]) -> MetaOapg.properties.billing_group_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["target_delivery_date"]) -> MetaOapg.properties.target_delivery_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["send_date"]) -> MetaOapg.properties.send_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cancel_window_campaign_minutes"]) -> MetaOapg.properties.cancel_window_campaign_minutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["auto_cancel_if_ncoa"]) -> MetaOapg.properties.auto_cancel_if_ncoa: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "schedule_type", "use_type", "description", "billing_group_id", "target_delivery_date", "send_date", "cancel_window_campaign_minutes", "metadata", "auto_cancel_if_ncoa", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["schedule_type"]) -> 'CmpScheduleType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["use_type"]) -> 'CmpUseType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billing_group_id"]) -> typing.Union[MetaOapg.properties.billing_group_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["target_delivery_date"]) -> typing.Union[MetaOapg.properties.target_delivery_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["send_date"]) -> typing.Union[MetaOapg.properties.send_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cancel_window_campaign_minutes"]) -> typing.Union[MetaOapg.properties.cancel_window_campaign_minutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["auto_cancel_if_ncoa"]) -> typing.Union[MetaOapg.properties.auto_cancel_if_ncoa, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "schedule_type", "use_type", "description", "billing_group_id", "target_delivery_date", "send_date", "cancel_window_campaign_minutes", "metadata", "auto_cancel_if_ncoa", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        use_type: 'CmpUseType',
        schedule_type: 'CmpScheduleType',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
        billing_group_id: typing.Union[MetaOapg.properties.billing_group_id, None, str, schemas.Unset] = schemas.unset,
        target_delivery_date: typing.Union[MetaOapg.properties.target_delivery_date, None, str, datetime, schemas.Unset] = schemas.unset,
        send_date: typing.Union[MetaOapg.properties.send_date, None, str, datetime, schemas.Unset] = schemas.unset,
        cancel_window_campaign_minutes: typing.Union[MetaOapg.properties.cancel_window_campaign_minutes, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
        auto_cancel_if_ncoa: typing.Union[MetaOapg.properties.auto_cancel_if_ncoa, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CampaignWritable':
        return super().__new__(
            cls,
            *args,
            use_type=use_type,
            schedule_type=schedule_type,
            name=name,
            description=description,
            billing_group_id=billing_group_id,
            target_delivery_date=target_delivery_date,
            send_date=send_date,
            cancel_window_campaign_minutes=cancel_window_campaign_minutes,
            metadata=metadata,
            auto_cancel_if_ncoa=auto_cancel_if_ncoa,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.cmp_schedule_type import CmpScheduleType
from lob_python_sdk.model.cmp_use_type import CmpUseType
from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription
