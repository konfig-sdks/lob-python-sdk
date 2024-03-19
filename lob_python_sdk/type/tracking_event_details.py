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


class RequiredTrackingEventDetails(TypedDict):
    # The description as listed in the description for event.
    description: str

    # Find the full table [here](#tag/Tracking-Events). A detailed substatus about the event: * `package_accepted` - Package has been accepted into the carrier network for delivery. * `package_arrived` - Package has arrived at an intermediate location in the carrier network. * `package_departed` - Package has departed from an intermediate location in the carrier network. * `package_processing` - Package is processing at an intermediate location in the carrier network. * `package_processed` - Package has been processed at an intermediate location. * `package_in_local_area` - Package is at a location near the end destination. * `delivery_scheduled` - Package is scheduled for delivery. * `out_for_delivery` - Package is out for delivery. * `pickup_available` - Package is available for pickup at carrier location. * `delivered` - Package has been delivered. * `package_forwarded` - Package has been forwarded. * `returned_to_sender` - Package is to be returned to sender. * `address_issue` - Address information is incorrect. Contact carrier to ensure delivery. * `contact_carrier` - Contact the carrier for more information. * `delayed` - Delivery of package is delayed. * `delivery_attempted` - Delivery of package has been attempted. Contact carrier to ensure delivery. * `delivery_rescheduled` - Delivery of package has been rescheduled. * `location_inaccessible` - Delivery location inaccessible to carrier. Contact carrier to ensure delivery. * `notice_left` - Carrier left notice during attempted delivery. Follow carrier instructions on notice. * `package_damaged` - Package has been damaged. Contact carrier for more details. * `package_disposed` - Package has been disposed. * `package_held` - Package held at carrier location. Contact carrier for more details. * `package_lost` - Package has been lost. Contact carrier for more details. * `package_unclaimed` - Package is unclaimed. * `package_undeliverable` - Package is not able to be delivered. * `reschedule_delivery` - Contact carrier to reschedule delivery. * `other` - Unrecognized carrier status. 
    event: str

    # `true` if action is required by the end recipient, `false` otherwise. 
    action_required: bool

class OptionalTrackingEventDetails(TypedDict, total=False):
    # Event-specific notes from USPS about the tracking event.
    notes: str

class TrackingEventDetails(RequiredTrackingEventDetails, OptionalTrackingEventDetails):
    pass