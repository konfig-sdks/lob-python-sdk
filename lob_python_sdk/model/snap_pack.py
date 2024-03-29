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


class SnapPack(
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
                    "id",
                    "url",
                }
                
                class properties:
                
                    @staticmethod
                    def id() -> typing.Type['SnapPackId']:
                        return SnapPackId
                    
                    
                    class outside_template_id(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
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
                                    TmplId,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'outside_template_id':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class inside_template_id(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
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
                                    TmplId,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'inside_template_id':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class outside_template_version_id(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
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
                                    VrsnId,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'outside_template_version_id':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class inside_template_version_id(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class all_of_1(
                                schemas.StrBase,
                                schemas.NoneBase,
                                schemas.Schema,
                                schemas.NoneStrMixin
                            ):
                            
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[None, str, ],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'all_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        _configuration=_configuration,
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
                                    VrsnId,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'inside_template_version_id':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    
                    
                    class object(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "snap_pack": "SNAP_PACK",
                            }
                        
                        @schemas.classproperty
                        def SNAP_PACK(cls):
                            return cls("snap_pack")
                    
                    
                    class tracking_events(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TrackingEventNormal']:
                                return TrackingEventNormal
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TrackingEventNormal'], typing.List['TrackingEventNormal']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'tracking_events':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TrackingEventNormal':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def use_type() -> typing.Type['SnapPackUseType']:
                        return SnapPackUseType
                
                    @staticmethod
                    def url() -> typing.Type['SignedLink']:
                        return SignedLink
                    fsc = schemas.BoolSchema
                
                    @staticmethod
                    def status() -> typing.Type['Status']:
                        return Status
                
                    @staticmethod
                    def campaign_id() -> typing.Type['CampaignId']:
                        return CampaignId
                    
                    
                    class failure_reason(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            all_of_1 = schemas.AnyTypeSchema
                            
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
                                    FailureReason,
                                    cls.all_of_1,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'failure_reason':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    color = schemas.BoolSchema
                    __annotations__ = {
                        "id": id,
                        "outside_template_id": outside_template_id,
                        "inside_template_id": inside_template_id,
                        "outside_template_version_id": outside_template_version_id,
                        "inside_template_version_id": inside_template_version_id,
                        "object": object,
                        "tracking_events": tracking_events,
                        "use_type": use_type,
                        "url": url,
                        "fsc": fsc,
                        "status": status,
                        "campaign_id": campaign_id,
                        "failure_reason": failure_reason,
                        "color": color,
                    }
            
            use_type: 'SnapPackUseType'
            id: 'SnapPackId'
            url: 'SignedLink'
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> 'SnapPackId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["outside_template_id"]) -> MetaOapg.properties.outside_template_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inside_template_id"]) -> MetaOapg.properties.inside_template_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["outside_template_version_id"]) -> MetaOapg.properties.outside_template_version_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["inside_template_version_id"]) -> MetaOapg.properties.inside_template_version_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["object"]) -> MetaOapg.properties.object: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tracking_events"]) -> MetaOapg.properties.tracking_events: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["use_type"]) -> 'SnapPackUseType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["url"]) -> 'SignedLink': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["fsc"]) -> MetaOapg.properties.fsc: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'Status': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["campaign_id"]) -> 'CampaignId': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["failure_reason"]) -> MetaOapg.properties.failure_reason: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "outside_template_id", "inside_template_id", "outside_template_version_id", "inside_template_version_id", "object", "tracking_events", "use_type", "url", "fsc", "status", "campaign_id", "failure_reason", "color", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> 'SnapPackId': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["outside_template_id"]) -> typing.Union[MetaOapg.properties.outside_template_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inside_template_id"]) -> typing.Union[MetaOapg.properties.inside_template_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["outside_template_version_id"]) -> typing.Union[MetaOapg.properties.outside_template_version_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["inside_template_version_id"]) -> typing.Union[MetaOapg.properties.inside_template_version_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["object"]) -> typing.Union[MetaOapg.properties.object, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tracking_events"]) -> typing.Union[MetaOapg.properties.tracking_events, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["use_type"]) -> 'SnapPackUseType': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> 'SignedLink': ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["fsc"]) -> typing.Union[MetaOapg.properties.fsc, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['Status', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["campaign_id"]) -> typing.Union['CampaignId', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["failure_reason"]) -> typing.Union[MetaOapg.properties.failure_reason, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> typing.Union[MetaOapg.properties.color, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "outside_template_id", "inside_template_id", "outside_template_version_id", "inside_template_version_id", "object", "tracking_events", "use_type", "url", "fsc", "status", "campaign_id", "failure_reason", "color", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                use_type: 'SnapPackUseType',
                id: 'SnapPackId',
                url: 'SignedLink',
                outside_template_id: typing.Union[MetaOapg.properties.outside_template_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                inside_template_id: typing.Union[MetaOapg.properties.inside_template_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                outside_template_version_id: typing.Union[MetaOapg.properties.outside_template_version_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                inside_template_version_id: typing.Union[MetaOapg.properties.inside_template_version_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                object: typing.Union[MetaOapg.properties.object, str, schemas.Unset] = schemas.unset,
                tracking_events: typing.Union[MetaOapg.properties.tracking_events, list, tuple, schemas.Unset] = schemas.unset,
                fsc: typing.Union[MetaOapg.properties.fsc, bool, schemas.Unset] = schemas.unset,
                status: typing.Union['Status', schemas.Unset] = schemas.unset,
                campaign_id: typing.Union['CampaignId', schemas.Unset] = schemas.unset,
                failure_reason: typing.Union[MetaOapg.properties.failure_reason, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                color: typing.Union[MetaOapg.properties.color, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_3':
                return super().__new__(
                    cls,
                    *args,
                    use_type=use_type,
                    id=id,
                    url=url,
                    outside_template_id=outside_template_id,
                    inside_template_id=inside_template_id,
                    outside_template_version_id=outside_template_version_id,
                    inside_template_version_id=inside_template_version_id,
                    object=object,
                    tracking_events=tracking_events,
                    fsc=fsc,
                    status=status,
                    campaign_id=campaign_id,
                    failure_reason=failure_reason,
                    color=color,
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
                SnapPackBase,
                Generated,
                FromUs,
                cls.all_of_3,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SnapPack':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.campaign_id import CampaignId
from lob_python_sdk.model.failure_reason import FailureReason
from lob_python_sdk.model.from_us import FromUs
from lob_python_sdk.model.generated import Generated
from lob_python_sdk.model.signed_link import SignedLink
from lob_python_sdk.model.snap_pack_base import SnapPackBase
from lob_python_sdk.model.snap_pack_id import SnapPackId
from lob_python_sdk.model.snap_pack_use_type import SnapPackUseType
from lob_python_sdk.model.status import Status
from lob_python_sdk.model.tmpl_id import TmplId
from lob_python_sdk.model.tracking_event_normal import TrackingEventNormal
from lob_python_sdk.model.vrsn_id import VrsnId
