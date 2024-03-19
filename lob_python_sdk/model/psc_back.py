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


class PscBack(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The artwork to use as the back of your postcard.

Notes:
- HTML merge variables should not include delimiting whitespace.
- PDF, PNG, and JPGs must be sized at 4.25"x6.25", 6.25"x9.25", or 6.25"x11.25" at 300 DPI, while supplied HTML will be rendered to the specified `size`.
- Be sure to leave room for address and postage information by following the templates provided here:
  - <a href="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/postcards/4x6_postcard.pdf" target="_blank">4x6 template</a>
  - <a href="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/postcards/6x9_postcard.pdf" target="_blank">6x9 template</a>
  - <a href="https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/postcards/6x11_postcard.pdf" target="_blank">6x11 template</a>


See [here](#section/HTML-Examples) for HTML examples.

    """


    class MetaOapg:
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                HtmlString,
                TmplId,
                RemoteFileUrl,
                LocalFilePath,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PscBack':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.html_string import HtmlString
from lob_python_sdk.model.local_file_path import LocalFilePath
from lob_python_sdk.model.remote_file_url import RemoteFileUrl
from lob_python_sdk.model.tmpl_id import TmplId
