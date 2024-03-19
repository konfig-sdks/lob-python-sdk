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

from lob_python_sdk.type.dpv_footnote import DpvFootnote

class RequiredDeliverabilityAnalysis(TypedDict):
    # Result of Delivery Point Validation (DPV), which determines whether or not the address is deliverable by the USPS. Possible values are: * `Y` –– The address is deliverable by the USPS. * `S` –– The address is deliverable by removing the provided secondary unit designator. This information may be incorrect or unnecessary. * `D` –– The address is deliverable to the building's default address but is missing a secondary unit designator and/or number.   There is a chance the mail will not reach the intended recipient. * `N` –– The address is not deliverable according to the USPS, but parts of the address are valid (such as the street and ZIP code). * `''` –– This address is not deliverable. No matching street could be found within the city or ZIP code. 
    dpv_confirmation: str

    # Indicates whether or not the address is <a href=\"https://en.wikipedia.org/wiki/Commercial_mail_receiving_agency\" target=\"_blank\">CMRA-authorized</a>. Possible values are: * `Y` –– Address is CMRA-authorized. * `N` –– Address is not CMRA-authorized. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_cmra: str

    # Indicates that an address was once deliverable, but has become vacant and is no longer receiving deliveries. Possible values are: * `Y` –– Address is vacant. * `N` –– Address is not vacant. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_vacant: str

    # Corresponds to the USPS field `dpv_no_stat`. Indicates that an address has been vacated in the recent past, and is no longer receiving deliveries. If it's been unoccupied for 90+ days, or temporarily vacant, this will be flagged. Possible values are: * `Y` –– Address is active. * `N` –– Address is not active. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_active: str

    # Indicates the reason why an address is vacant or no longer receiving deliveries. Possible values are: * `01` –– Address does not receive mail from the USPS directly, but is serviced by a drop address. * `02` –– Address not yet deliverable. * `03` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). * `04` –– Address is a College, Military Zone, or other type. * `05` –– Address no longer receives deliveries. * `06` –– Address is missing required secondary information. * `''` –– A DPV match is not made or the address is active. 
    dpv_inactive_reason: str

    # Indicates a street address for which mail is delivered to a PO Box. Possible values are: * `Y` –– Address is a PO Box throwback delivery point. * `N` –– Address is not a PO Box throwback delivery point. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_throwback: str

    # Indicates whether deliveries are not performed on one or more days of the week at an address. Possible values are: * `Y` –– Mail delivery does not occur on some days of the week. * `N` –– Mail delivery occurs every day of the week. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_non_delivery_day_flag: str

    # Indicates days of the week (starting on Sunday) deliveries are not performed at an address. For example: * `YNNNNNN` –– Mail delivery does not occur on Sunday's. * `NYNNNYN` –– Mail delivery does not occur on Monday's or Friday's. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string) or address receives mail every day of the week (`deliverability_analysis[dpv_non_delivery_day_flag]` is `N` or an empty string). 
    dpv_non_delivery_day_values: str

    # Indicates packages to this address will not be left due to security concerns. Possible values are: * `Y` –– Address does not have a secure mailbox. * `N` –– Address has a secure mailbox. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_no_secure_location: str

    # Indicates the door of the address is not accessible for mail delivery. Possible values are: * `Y` –– Door is not accessible. * `N` –– Door is accessible. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    dpv_door_not_accessible: str

    # An array of 2-character strings that gives more insight into how `deliverability_analysis[dpv_confirmation]` was determined. Will always include at least 1 string, and can include up to 3. For details, see [US Verification Details](#tag/US-Verification-Types). 
    dpv_footnotes: typing.List[DpvFootnote]

    # Indicates whether or not an address has been flagged in the <a href=\"https://docs.informatica.com/data-engineering/data-engineering-quality/10-4-0/address-validator-port-reference/postal-carrier-certification-data-ports/early-warning-system-return-code.html\" target=\"_blank\">Early Warning System</a>, meaning the address is under development and not yet ready to receive mail. However, it should become available in a few months. 
    ews_match: bool

    # Indicates whether this address has been converted by <a href=\"https://postalpro.usps.com/address-quality/lacslink\" target=\"_blank\">LACS<sup>Link</sup></a>. LACS<sup>Link</sup> corrects outdated addresses into their modern counterparts. Possible values are: * `Y` –– New address produced with a matching record in LACS<sup>Link</sup>. * `N` –– New address could not be produced with a matching record in LACS<sup>Link</sup>. * `''` –– A DPV match is not made (`deliverability_analysis[dpv_confirmation]` is `N` or an empty string). 
    lacs_indicator: str

    # A code indicating how `deliverability_analysis[lacs_indicator]` was determined. Possible values are: * `A` — A new address was produced because a match was found in LACS<sup>Link</sup>. * `92` — A LACS<sup>Link</sup> record was matched after dropping secondary information. * `14` — A match was found in LACS<sup>Link</sup>, but could not be converted to a deliverable address. * `00` — A match was not found in LACS<sup>Link</sup>, and no new address was produced. * `''` — LACS<sup>Link</sup> was not attempted. 
    lacs_return_code: str

    # A return code that indicates whether the address was matched and corrected by <a href=\"https://postalpro.usps.com/address-quality-solutions/suitelink\" target=\"_blank\">Suite<sup>Link</sup></a>. Suite<sup>Link</sup> attempts to provide secondary information to business addresses. Possible values are: * `A` –– A Suite<sup>Link</sup> match was found and secondary information was added. * `00` –– A Suite<sup>Link</sup> match could not be found and no secondary information was added. * `''` –– Suite<sup>Link</sup> lookup was not attempted. 
    suite_return_code: str

class OptionalDeliverabilityAnalysis(TypedDict, total=False):
    pass

class DeliverabilityAnalysis(RequiredDeliverabilityAnalysis, OptionalDeliverabilityAnalysis):
    pass
