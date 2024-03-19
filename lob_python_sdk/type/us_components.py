# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lob_python_sdk.type.city import City
from lob_python_sdk.type.county_fips import CountyFips
from lob_python_sdk.type.state import State
from lob_python_sdk.type.zip_code_plus4 import ZipCodePlus4
from lob_python_sdk.type.zip_code_type import ZipCodeType

class RequiredUsComponents(TypedDict):
    # The numeric or alphanumeric part of an address preceding the street name. Often the house, building, or PO Box number.
    primary_number: str

    # Geographic direction preceding a street name (`N`, `S`, `E`, `W`, `NE`, `SW`, `SE`, `NW`). 
    street_predirection: str

    # The name of the street.
    street_name: str

    # The standard USPS abbreviation for the street suffix (`ST`, `AVE`, `BLVD`, etc). 
    street_suffix: str

    # Geographic direction following a street name (`N`, `S`, `E`, `W`, `NE`, `SW`, `SE`, `NW`). 
    street_postdirection: str

    # The standard USPS abbreviation describing the `components[secondary_number]` (`STE`, `APT`, `BLDG`, etc). 
    secondary_designator: str

    # Number of the apartment/unit/etc. 
    secondary_number: str

    # Designator of a <a href=\"https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency\" target=\"_blank\">CMRA-authorized</a> private mailbox. 
    pmb_designator: str

    # Number of a <a href=\"https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency\" target=\"_blank\">CMRA-authorized</a> private mailbox. 
    pmb_number: str

    # An extra (often unnecessary) secondary designator provided with the input address. 
    extra_secondary_designator: str

    # An extra (often unnecessary) secondary number provided with the input address. 
    extra_secondary_number: str

    city: City

    state: State

    # The 5-digit ZIP code
    zip_code: str

    zip_code_plus_4: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    zip_code_type: ZipCodeType

    # A 12-digit identifier that uniquely identifies a delivery point (location where mail can be sent and received). It consists of the 5-digit ZIP code (`zip_code`), 4-digit ZIP+4 add-on (`zip_code_plus_4`), 2-digit delivery point, and 1-digit delivery point check digit. 
    delivery_point_barcode: str

    # Uses USPS's <a href=\"https://www.usps.com/nationalpremieraccounts/rdi.htm\" target=\"_blank\">Residential Delivery Indicator (RDI)</a> to identify whether an address is classified as residential or business. Possible values are: * `residential` –– The address is residential or a PO Box. * `commercial` –– The address is commercial. * `''` –– Not enough information provided to be determined. 
    address_type: str

    # A description of the type of address. Populated if a DPV match is made (`deliverability_analysis[dpv_confirmation]` is `Y`, `S`, or `D`). For more detailed information about each record type, see [US Verification Details](#tag/US-Verification-Types). 
    record_type: str

    # Designates whether or not the address is the default address for a building containing multiple delivery points. 
    default_building_address: bool

    # County name of the address city.
    county: str

    county_fips: CountyFips

    # A 4-character code assigned to a mail delivery route within a ZIP code. 
    carrier_route: str

    # The type of `components[carrier_route]`. For more detailed information about each carrier route type, see [US Verification Details](#tag/US-Verification-Types). 
    carrier_route_type: str

    # Indicates the mailing facility for an address only supports PO Box deliveries and other forms of mail delivery are not available. 
    po_box_only_flag: str

class OptionalUsComponents(TypedDict, total=False):
    # A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be used with `longitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). 
    latitude: typing.Optional[typing.Union[int, float]]

    # A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be used with `latitude` to pinpoint locations on a map. Will not be returned for undeliverable addresses or military addresses (state is `AA`, `AE`, or `AP`). 
    longitude: typing.Optional[typing.Union[int, float]]

class UsComponents(RequiredUsComponents, OptionalUsComponents):
    pass
