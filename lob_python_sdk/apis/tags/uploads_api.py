# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.uploads.post import Create
from lob_python_sdk.paths.uploads_upl_id_exports.post import CreateExportFile
from lob_python_sdk.paths.uploads_upl_id.delete import Delete
from lob_python_sdk.paths.uploads_upl_id_file.post import File
from lob_python_sdk.paths.uploads.get import List
from lob_python_sdk.paths.uploads_upl_id.get import Retrieve
from lob_python_sdk.paths.uploads_upl_id_report.get import Retrieve0
from lob_python_sdk.paths.uploads_upl_id_exports_ex_id.get import Retrieve1
from lob_python_sdk.paths.uploads_upl_id.patch import Update
from lob_python_sdk.apis.tags.uploads_api_raw import UploadsApiRaw


class UploadsApi(
    Create,
    CreateExportFile,
    Delete,
    File,
    List,
    Retrieve,
    Retrieve0,
    Retrieve1,
    Update,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: UploadsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = UploadsApiRaw(api_client)
