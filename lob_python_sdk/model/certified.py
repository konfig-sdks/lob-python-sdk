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


class Certified(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_0(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "color",
                    "tracking_events",
                    "extra_service",
                }
                
                class properties:
                
                    @staticmethod
                    def description() -> typing.Type['ResourceDescription']:
                        return ResourceDescription
                    
                    
                    class extra_service(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "certified": "CERTIFIED",
                                "certified_return_receipt": "CERTIFIED_RETURN_RECEIPT",
                            }
                        
                        @schemas.classproperty
                        def CERTIFIED(cls):
                            return cls("certified")
                        
                        @schemas.classproperty
                        def CERTIFIED_RETURN_RECEIPT(cls):
                            return cls("certified_return_receipt")
                    
                    
                    class tracking_number(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'tracking_number':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                    
                    
                    class tracking_events(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TrackingEventCertified']:
                                return TrackingEventCertified
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TrackingEventCertified'], typing.List['TrackingEventCertified']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'tracking_events':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TrackingEventCertified':
                            return super().__getitem__(i)
                
                    @staticmethod
                    def return_address() -> typing.Type['ReturnAddress']:
                        return ReturnAddress
                
                    @staticmethod
                    def metadata() -> typing.Type['Metadata']:
                        return Metadata
                
                    @staticmethod
                    def merge_variables() -> typing.Type['MergeVariables']:
                        return MergeVariables
                
                    @staticmethod
                    def send_date() -> typing.Type['SendDate']:
                        return SendDate
                
                    @staticmethod
                    def mail_type() -> typing.Type['MailType']:
                        return MailType
                    color = schemas.BoolSchema
                    double_sided = schemas.BoolSchema
                
                    @staticmethod
                    def address_placement() -> typing.Type['AddressPlacement']:
                        return AddressPlacement
                
                    @staticmethod
                    def return_envelope() -> typing.Type['ReturnEnvelopeReturned']:
                        return ReturnEnvelopeReturned
                    
                    
                    class perforated_page(
                        schemas.IntBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneDecimalMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[None, decimal.Decimal, int, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'perforated_page':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                            )
                
                    @staticmethod
                    def custom_envelope() -> typing.Type['CustomEnvelopeReturned']:
                        return CustomEnvelopeReturned
                    __annotations__ = {
                        "description": description,
                        "extra_service": extra_service,
                        "tracking_number": tracking_number,
                        "tracking_events": tracking_events,
                        "return_address": return_address,
                        "metadata": metadata,
                        "merge_variables": merge_variables,
                        "send_date": send_date,
                        "mail_type": mail_type,
                        "color": color,
                        "double_sided": double_sided,
                        "address_placement": address_placement,
                        "return_envelope": return_envelope,
                        "perforated_page": perforated_page,
                        "custom_envelope": custom_envelope,
                    }
            
            color: MetaOapg.properties.color
            tracking_events: MetaOapg.properties.tracking_events
            extra_service: MetaOapg.properties.extra_service
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["description"]) -> 'ResourceDescription': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["extra_service"]) -> MetaOapg.properties.extra_service: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tracking_number"]) -> MetaOapg.properties.tracking_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["tracking_events"]) -> MetaOapg.properties.tracking_events: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["return_address"]) -> 'ReturnAddress': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> 'Metadata': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["merge_variables"]) -> 'MergeVariables': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["send_date"]) -> 'SendDate': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["mail_type"]) -> 'MailType': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["double_sided"]) -> MetaOapg.properties.double_sided: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["address_placement"]) -> 'AddressPlacement': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["return_envelope"]) -> 'ReturnEnvelopeReturned': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["perforated_page"]) -> MetaOapg.properties.perforated_page: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_envelope"]) -> 'CustomEnvelopeReturned': ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "extra_service", "tracking_number", "tracking_events", "return_address", "metadata", "merge_variables", "send_date", "mail_type", "color", "double_sided", "address_placement", "return_envelope", "perforated_page", "custom_envelope", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union['ResourceDescription', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["extra_service"]) -> MetaOapg.properties.extra_service: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tracking_number"]) -> typing.Union[MetaOapg.properties.tracking_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["tracking_events"]) -> MetaOapg.properties.tracking_events: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["return_address"]) -> typing.Union['ReturnAddress', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union['Metadata', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["merge_variables"]) -> typing.Union['MergeVariables', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["send_date"]) -> typing.Union['SendDate', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["mail_type"]) -> typing.Union['MailType', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["color"]) -> MetaOapg.properties.color: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["double_sided"]) -> typing.Union[MetaOapg.properties.double_sided, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["address_placement"]) -> typing.Union['AddressPlacement', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["return_envelope"]) -> typing.Union['ReturnEnvelopeReturned', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["perforated_page"]) -> typing.Union[MetaOapg.properties.perforated_page, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_envelope"]) -> typing.Union['CustomEnvelopeReturned', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "extra_service", "tracking_number", "tracking_events", "return_address", "metadata", "merge_variables", "send_date", "mail_type", "color", "double_sided", "address_placement", "return_envelope", "perforated_page", "custom_envelope", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                color: typing.Union[MetaOapg.properties.color, bool, ],
                tracking_events: typing.Union[MetaOapg.properties.tracking_events, list, tuple, ],
                extra_service: typing.Union[MetaOapg.properties.extra_service, str, ],
                description: typing.Union['ResourceDescription', schemas.Unset] = schemas.unset,
                tracking_number: typing.Union[MetaOapg.properties.tracking_number, None, str, schemas.Unset] = schemas.unset,
                return_address: typing.Union['ReturnAddress', schemas.Unset] = schemas.unset,
                metadata: typing.Union['Metadata', schemas.Unset] = schemas.unset,
                merge_variables: typing.Union['MergeVariables', schemas.Unset] = schemas.unset,
                send_date: typing.Union['SendDate', schemas.Unset] = schemas.unset,
                mail_type: typing.Union['MailType', schemas.Unset] = schemas.unset,
                double_sided: typing.Union[MetaOapg.properties.double_sided, bool, schemas.Unset] = schemas.unset,
                address_placement: typing.Union['AddressPlacement', schemas.Unset] = schemas.unset,
                return_envelope: typing.Union['ReturnEnvelopeReturned', schemas.Unset] = schemas.unset,
                perforated_page: typing.Union[MetaOapg.properties.perforated_page, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                custom_envelope: typing.Union['CustomEnvelopeReturned', schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_0':
                return super().__new__(
                    cls,
                    *args,
                    color=color,
                    tracking_events=tracking_events,
                    extra_service=extra_service,
                    description=description,
                    tracking_number=tracking_number,
                    return_address=return_address,
                    metadata=metadata,
                    merge_variables=merge_variables,
                    send_date=send_date,
                    mail_type=mail_type,
                    double_sided=double_sided,
                    address_placement=address_placement,
                    return_envelope=return_envelope,
                    perforated_page=perforated_page,
                    custom_envelope=custom_envelope,
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
                cls.all_of_0,
                LetterGeneratedBase,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Certified':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.address_placement import AddressPlacement
from lob_python_sdk.model.custom_envelope_returned import CustomEnvelopeReturned
from lob_python_sdk.model.letter_generated_base import LetterGeneratedBase
from lob_python_sdk.model.mail_type import MailType
from lob_python_sdk.model.merge_variables import MergeVariables
from lob_python_sdk.model.metadata import Metadata
from lob_python_sdk.model.resource_description import ResourceDescription
from lob_python_sdk.model.return_address import ReturnAddress
from lob_python_sdk.model.return_envelope_returned import ReturnEnvelopeReturned
from lob_python_sdk.model.send_date import SendDate
from lob_python_sdk.model.tracking_event_certified import TrackingEventCertified
