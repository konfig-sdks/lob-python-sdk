# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.uploads.post import CreateRaw
from lob_python_sdk.paths.uploads_upl_id_exports.post import CreateExportFileRaw
from lob_python_sdk.paths.uploads_upl_id.delete import DeleteRaw
from lob_python_sdk.paths.uploads_upl_id_file.post import FileRaw
from lob_python_sdk.paths.uploads.get import ListRaw
from lob_python_sdk.paths.uploads_upl_id.get import RetrieveRaw
from lob_python_sdk.paths.uploads_upl_id_report.get import Retrieve0Raw
from lob_python_sdk.paths.uploads_upl_id_exports_ex_id.get import Retrieve1Raw
from lob_python_sdk.paths.uploads_upl_id.patch import UpdateRaw


class UploadsApiRaw(
    CreateRaw,
    CreateExportFileRaw,
    DeleteRaw,
    FileRaw,
    ListRaw,
    RetrieveRaw,
    Retrieve0Raw,
    Retrieve1Raw,
    UpdateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass