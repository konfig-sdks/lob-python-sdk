# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.buckslips_buckslip_id_orders.post import CreateNewOrder
from lob_python_sdk.paths.buckslips_buckslip_id_orders.get import GetByBuckslipId
from lob_python_sdk.apis.tags.buckslip_orders_api_raw import BuckslipOrdersApiRaw


class BuckslipOrdersApi(
    CreateNewOrder,
    GetByBuckslipId,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BuckslipOrdersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BuckslipOrdersApiRaw(api_client)
