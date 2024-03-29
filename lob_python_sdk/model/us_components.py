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


class UsComponents(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A nested object containing a breakdown of each component of an address.
    """


    class MetaOapg:
        required = {
            "pmb_number",
            "primary_number",
            "city",
            "street_postdirection",
            "county",
            "carrier_route",
            "street_name",
            "zip_code",
            "street_suffix",
            "county_fips",
            "default_building_address",
            "extra_secondary_number",
            "street_predirection",
            "delivery_point_barcode",
            "zip_code_plus_4",
            "state",
            "zip_code_type",
            "secondary_designator",
            "address_type",
            "carrier_route_type",
            "record_type",
            "secondary_number",
            "po_box_only_flag",
            "extra_secondary_designator",
            "pmb_designator",
        }
        
        class properties:
            primary_number = schemas.StrSchema
            
            
            class street_predirection(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "N": "N",
                        "S": "S",
                        "E": "E",
                        "W": "W",
                        "NE": "NE",
                        "SW": "SW",
                        "SE": "SE",
                        "NW": "NW",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def S(cls):
                    return cls("S")
                
                @schemas.classproperty
                def E(cls):
                    return cls("E")
                
                @schemas.classproperty
                def W(cls):
                    return cls("W")
                
                @schemas.classproperty
                def NE(cls):
                    return cls("NE")
                
                @schemas.classproperty
                def SW(cls):
                    return cls("SW")
                
                @schemas.classproperty
                def SE(cls):
                    return cls("SE")
                
                @schemas.classproperty
                def NW(cls):
                    return cls("NW")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            street_name = schemas.StrSchema
            street_suffix = schemas.StrSchema
            
            
            class street_postdirection(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "N": "N",
                        "S": "S",
                        "E": "E",
                        "W": "W",
                        "NE": "NE",
                        "SW": "SW",
                        "SE": "SE",
                        "NW": "NW",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
                
                @schemas.classproperty
                def S(cls):
                    return cls("S")
                
                @schemas.classproperty
                def E(cls):
                    return cls("E")
                
                @schemas.classproperty
                def W(cls):
                    return cls("W")
                
                @schemas.classproperty
                def NE(cls):
                    return cls("NE")
                
                @schemas.classproperty
                def SW(cls):
                    return cls("SW")
                
                @schemas.classproperty
                def SE(cls):
                    return cls("SE")
                
                @schemas.classproperty
                def NW(cls):
                    return cls("NW")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            secondary_designator = schemas.StrSchema
            secondary_number = schemas.StrSchema
            pmb_designator = schemas.StrSchema
            pmb_number = schemas.StrSchema
            extra_secondary_designator = schemas.StrSchema
            extra_secondary_number = schemas.StrSchema
        
            @staticmethod
            def city() -> typing.Type['City']:
                return City
        
            @staticmethod
            def state() -> typing.Type['State']:
                return State
            
            
            class zip_code(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^\d{5}$',
                    }]
            
            
            class zip_code_plus_4(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_0 = schemas.AnyTypeSchema
                    
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
                            ZipCodePlus4,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'zip_code_plus_4':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def zip_code_type() -> typing.Type['ZipCodeType']:
                return ZipCodeType
            delivery_point_barcode = schemas.StrSchema
            
            
            class address_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "residential": "RESIDENTIAL",
                        "commercial": "COMMERCIAL",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def RESIDENTIAL(cls):
                    return cls("residential")
                
                @schemas.classproperty
                def COMMERCIAL(cls):
                    return cls("commercial")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class record_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "street": "STREET",
                        "highrise": "HIGHRISE",
                        "firm": "FIRM",
                        "po_box": "PO_BOX",
                        "rural_route": "RURAL_ROUTE",
                        "general_delivery": "GENERAL_DELIVERY",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def STREET(cls):
                    return cls("street")
                
                @schemas.classproperty
                def HIGHRISE(cls):
                    return cls("highrise")
                
                @schemas.classproperty
                def FIRM(cls):
                    return cls("firm")
                
                @schemas.classproperty
                def PO_BOX(cls):
                    return cls("po_box")
                
                @schemas.classproperty
                def RURAL_ROUTE(cls):
                    return cls("rural_route")
                
                @schemas.classproperty
                def GENERAL_DELIVERY(cls):
                    return cls("general_delivery")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            default_building_address = schemas.BoolSchema
            county = schemas.StrSchema
        
            @staticmethod
            def county_fips() -> typing.Type['CountyFips']:
                return CountyFips
            carrier_route = schemas.StrSchema
            
            
            class carrier_route_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "city_delivery": "CITY_DELIVERY",
                        "rural_route": "RURAL_ROUTE",
                        "highway_contract": "HIGHWAY_CONTRACT",
                        "po_box": "PO_BOX",
                        "general_delivery": "GENERAL_DELIVERY",
                    }
                
                @schemas.classproperty
                def CITY_DELIVERY(cls):
                    return cls("city_delivery")
                
                @schemas.classproperty
                def RURAL_ROUTE(cls):
                    return cls("rural_route")
                
                @schemas.classproperty
                def HIGHWAY_CONTRACT(cls):
                    return cls("highway_contract")
                
                @schemas.classproperty
                def PO_BOX(cls):
                    return cls("po_box")
                
                @schemas.classproperty
                def GENERAL_DELIVERY(cls):
                    return cls("general_delivery")
            
            
            class po_box_only_flag(
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
            
            
            class latitude(
                schemas.Float32Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'float'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'latitude':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class longitude(
                schemas.Float32Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'float'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'longitude':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "primary_number": primary_number,
                "street_predirection": street_predirection,
                "street_name": street_name,
                "street_suffix": street_suffix,
                "street_postdirection": street_postdirection,
                "secondary_designator": secondary_designator,
                "secondary_number": secondary_number,
                "pmb_designator": pmb_designator,
                "pmb_number": pmb_number,
                "extra_secondary_designator": extra_secondary_designator,
                "extra_secondary_number": extra_secondary_number,
                "city": city,
                "state": state,
                "zip_code": zip_code,
                "zip_code_plus_4": zip_code_plus_4,
                "zip_code_type": zip_code_type,
                "delivery_point_barcode": delivery_point_barcode,
                "address_type": address_type,
                "record_type": record_type,
                "default_building_address": default_building_address,
                "county": county,
                "county_fips": county_fips,
                "carrier_route": carrier_route,
                "carrier_route_type": carrier_route_type,
                "po_box_only_flag": po_box_only_flag,
                "latitude": latitude,
                "longitude": longitude,
            }
    
    pmb_number: MetaOapg.properties.pmb_number
    primary_number: MetaOapg.properties.primary_number
    city: 'City'
    street_postdirection: MetaOapg.properties.street_postdirection
    county: MetaOapg.properties.county
    carrier_route: MetaOapg.properties.carrier_route
    street_name: MetaOapg.properties.street_name
    zip_code: MetaOapg.properties.zip_code
    street_suffix: MetaOapg.properties.street_suffix
    county_fips: 'CountyFips'
    default_building_address: MetaOapg.properties.default_building_address
    extra_secondary_number: MetaOapg.properties.extra_secondary_number
    street_predirection: MetaOapg.properties.street_predirection
    delivery_point_barcode: MetaOapg.properties.delivery_point_barcode
    zip_code_plus_4: MetaOapg.properties.zip_code_plus_4
    state: 'State'
    zip_code_type: 'ZipCodeType'
    secondary_designator: MetaOapg.properties.secondary_designator
    address_type: MetaOapg.properties.address_type
    carrier_route_type: MetaOapg.properties.carrier_route_type
    record_type: MetaOapg.properties.record_type
    secondary_number: MetaOapg.properties.secondary_number
    po_box_only_flag: MetaOapg.properties.po_box_only_flag
    extra_secondary_designator: MetaOapg.properties.extra_secondary_designator
    pmb_designator: MetaOapg.properties.pmb_designator
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_number"]) -> MetaOapg.properties.primary_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_predirection"]) -> MetaOapg.properties.street_predirection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_name"]) -> MetaOapg.properties.street_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_suffix"]) -> MetaOapg.properties.street_suffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_postdirection"]) -> MetaOapg.properties.street_postdirection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondary_designator"]) -> MetaOapg.properties.secondary_designator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondary_number"]) -> MetaOapg.properties.secondary_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pmb_designator"]) -> MetaOapg.properties.pmb_designator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pmb_number"]) -> MetaOapg.properties.pmb_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra_secondary_designator"]) -> MetaOapg.properties.extra_secondary_designator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra_secondary_number"]) -> MetaOapg.properties.extra_secondary_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> 'City': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> 'State': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip_code"]) -> MetaOapg.properties.zip_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip_code_plus_4"]) -> MetaOapg.properties.zip_code_plus_4: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip_code_type"]) -> 'ZipCodeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delivery_point_barcode"]) -> MetaOapg.properties.delivery_point_barcode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_type"]) -> MetaOapg.properties.address_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["record_type"]) -> MetaOapg.properties.record_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_building_address"]) -> MetaOapg.properties.default_building_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["county"]) -> MetaOapg.properties.county: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["county_fips"]) -> 'CountyFips': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carrier_route"]) -> MetaOapg.properties.carrier_route: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["carrier_route_type"]) -> MetaOapg.properties.carrier_route_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["po_box_only_flag"]) -> MetaOapg.properties.po_box_only_flag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latitude"]) -> MetaOapg.properties.latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["longitude"]) -> MetaOapg.properties.longitude: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["primary_number", "street_predirection", "street_name", "street_suffix", "street_postdirection", "secondary_designator", "secondary_number", "pmb_designator", "pmb_number", "extra_secondary_designator", "extra_secondary_number", "city", "state", "zip_code", "zip_code_plus_4", "zip_code_type", "delivery_point_barcode", "address_type", "record_type", "default_building_address", "county", "county_fips", "carrier_route", "carrier_route_type", "po_box_only_flag", "latitude", "longitude", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_number"]) -> MetaOapg.properties.primary_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_predirection"]) -> MetaOapg.properties.street_predirection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_name"]) -> MetaOapg.properties.street_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_suffix"]) -> MetaOapg.properties.street_suffix: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_postdirection"]) -> MetaOapg.properties.street_postdirection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondary_designator"]) -> MetaOapg.properties.secondary_designator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondary_number"]) -> MetaOapg.properties.secondary_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pmb_designator"]) -> MetaOapg.properties.pmb_designator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pmb_number"]) -> MetaOapg.properties.pmb_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra_secondary_designator"]) -> MetaOapg.properties.extra_secondary_designator: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra_secondary_number"]) -> MetaOapg.properties.extra_secondary_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> 'City': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> 'State': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip_code"]) -> MetaOapg.properties.zip_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip_code_plus_4"]) -> MetaOapg.properties.zip_code_plus_4: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip_code_type"]) -> 'ZipCodeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delivery_point_barcode"]) -> MetaOapg.properties.delivery_point_barcode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_type"]) -> MetaOapg.properties.address_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["record_type"]) -> MetaOapg.properties.record_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_building_address"]) -> MetaOapg.properties.default_building_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["county"]) -> MetaOapg.properties.county: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["county_fips"]) -> 'CountyFips': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carrier_route"]) -> MetaOapg.properties.carrier_route: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["carrier_route_type"]) -> MetaOapg.properties.carrier_route_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["po_box_only_flag"]) -> MetaOapg.properties.po_box_only_flag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latitude"]) -> typing.Union[MetaOapg.properties.latitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["longitude"]) -> typing.Union[MetaOapg.properties.longitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primary_number", "street_predirection", "street_name", "street_suffix", "street_postdirection", "secondary_designator", "secondary_number", "pmb_designator", "pmb_number", "extra_secondary_designator", "extra_secondary_number", "city", "state", "zip_code", "zip_code_plus_4", "zip_code_type", "delivery_point_barcode", "address_type", "record_type", "default_building_address", "county", "county_fips", "carrier_route", "carrier_route_type", "po_box_only_flag", "latitude", "longitude", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pmb_number: typing.Union[MetaOapg.properties.pmb_number, str, ],
        primary_number: typing.Union[MetaOapg.properties.primary_number, str, ],
        city: 'City',
        street_postdirection: typing.Union[MetaOapg.properties.street_postdirection, str, ],
        county: typing.Union[MetaOapg.properties.county, str, ],
        carrier_route: typing.Union[MetaOapg.properties.carrier_route, str, ],
        street_name: typing.Union[MetaOapg.properties.street_name, str, ],
        zip_code: typing.Union[MetaOapg.properties.zip_code, str, ],
        street_suffix: typing.Union[MetaOapg.properties.street_suffix, str, ],
        county_fips: 'CountyFips',
        default_building_address: typing.Union[MetaOapg.properties.default_building_address, bool, ],
        extra_secondary_number: typing.Union[MetaOapg.properties.extra_secondary_number, str, ],
        street_predirection: typing.Union[MetaOapg.properties.street_predirection, str, ],
        delivery_point_barcode: typing.Union[MetaOapg.properties.delivery_point_barcode, str, ],
        zip_code_plus_4: typing.Union[MetaOapg.properties.zip_code_plus_4, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        state: 'State',
        zip_code_type: 'ZipCodeType',
        secondary_designator: typing.Union[MetaOapg.properties.secondary_designator, str, ],
        address_type: typing.Union[MetaOapg.properties.address_type, str, ],
        carrier_route_type: typing.Union[MetaOapg.properties.carrier_route_type, str, ],
        record_type: typing.Union[MetaOapg.properties.record_type, str, ],
        secondary_number: typing.Union[MetaOapg.properties.secondary_number, str, ],
        po_box_only_flag: typing.Union[MetaOapg.properties.po_box_only_flag, str, ],
        extra_secondary_designator: typing.Union[MetaOapg.properties.extra_secondary_designator, str, ],
        pmb_designator: typing.Union[MetaOapg.properties.pmb_designator, str, ],
        latitude: typing.Union[MetaOapg.properties.latitude, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        longitude: typing.Union[MetaOapg.properties.longitude, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsComponents':
        return super().__new__(
            cls,
            *args,
            pmb_number=pmb_number,
            primary_number=primary_number,
            city=city,
            street_postdirection=street_postdirection,
            county=county,
            carrier_route=carrier_route,
            street_name=street_name,
            zip_code=zip_code,
            street_suffix=street_suffix,
            county_fips=county_fips,
            default_building_address=default_building_address,
            extra_secondary_number=extra_secondary_number,
            street_predirection=street_predirection,
            delivery_point_barcode=delivery_point_barcode,
            zip_code_plus_4=zip_code_plus_4,
            state=state,
            zip_code_type=zip_code_type,
            secondary_designator=secondary_designator,
            address_type=address_type,
            carrier_route_type=carrier_route_type,
            record_type=record_type,
            secondary_number=secondary_number,
            po_box_only_flag=po_box_only_flag,
            extra_secondary_designator=extra_secondary_designator,
            pmb_designator=pmb_designator,
            latitude=latitude,
            longitude=longitude,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.city import City
from lob_python_sdk.model.county_fips import CountyFips
from lob_python_sdk.model.state import State
from lob_python_sdk.model.zip_code_plus4 import ZipCodePlus4
from lob_python_sdk.model.zip_code_type import ZipCodeType
