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


class ErrorError(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "code",
            "status_code",
            "message",
        }
        
        class properties:
            message = schemas.StrSchema
        
            @staticmethod
            def status_code() -> typing.Type['FailureStatusCode']:
                return FailureStatusCode
            
            
            class code(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def BAD_REQUEST(cls):
                    return cls("bad_request")
                
                @schemas.classproperty
                def CONFLICT(cls):
                    return cls("conflict")
                
                @schemas.classproperty
                def FEATURE_LIMIT_REACHED(cls):
                    return cls("feature_limit_reached")
                
                @schemas.classproperty
                def INTERNAL_SERVER_ERROR(cls):
                    return cls("internal_server_error")
                
                @schemas.classproperty
                def INVALID(cls):
                    return cls("invalid")
                
                @schemas.classproperty
                def NOT_DELETABLE(cls):
                    return cls("not_deletable")
                
                @schemas.classproperty
                def NOT_FOUND(cls):
                    return cls("not_found")
                
                @schemas.classproperty
                def REQUEST_TIMEOUT(cls):
                    return cls("request_timeout")
                
                @schemas.classproperty
                def SERVICE_UNAVAILABLE(cls):
                    return cls("service_unavailable")
                
                @schemas.classproperty
                def UNRECOGNIZED_ENDPOINT(cls):
                    return cls("unrecognized_endpoint")
                
                @schemas.classproperty
                def UNSUPPORTED_LOB_VERSION(cls):
                    return cls("unsupported_lob_version")
                
                @schemas.classproperty
                def ADDRESS_LENGTH_EXCEEDS_LIMIT(cls):
                    return cls("address_length_exceeds_limit")
                
                @schemas.classproperty
                def BANK_ACCOUNT_ALREADY_VERIFIED(cls):
                    return cls("bank_account_already_verified")
                
                @schemas.classproperty
                def BANK_ERROR(cls):
                    return cls("bank_error")
                
                @schemas.classproperty
                def BILLING_ADDRESS_REQUIRED(cls):
                    return cls("billing_address_required")
                
                @schemas.classproperty
                def CUSTOM_ENVELOPE_INVENTORY_DEPLETED(cls):
                    return cls("custom_envelope_inventory_depleted")
                
                @schemas.classproperty
                def DELETED_BANK_ACCOUNT(cls):
                    return cls("deleted_bank_account")
                
                @schemas.classproperty
                def FAILED_DELIVERABILITY_STRICTNESS(cls):
                    return cls("failed_deliverability_strictness")
                
                @schemas.classproperty
                def FILE_PAGES_BELOW_MIN(cls):
                    return cls("file_pages_below_min")
                
                @schemas.classproperty
                def FILE_PAGES_EXCEED_MAX(cls):
                    return cls("file_pages_exceed_max")
                
                @schemas.classproperty
                def FILE_SIZE_EXCEEDS_LIMIT(cls):
                    return cls("file_size_exceeds_limit")
                
                @schemas.classproperty
                def FOREIGN_RETURN_ADDRESS(cls):
                    return cls("foreign_return_address")
                
                @schemas.classproperty
                def INCONSISTENT_PAGE_DIMENSIONS(cls):
                    return cls("inconsistent_page_dimensions")
                
                @schemas.classproperty
                def INVALID_BANK_ACCOUNT(cls):
                    return cls("invalid_bank_account")
                
                @schemas.classproperty
                def INVALID_BANK_ACCOUNT_VERIFICATION(cls):
                    return cls("invalid_bank_account_verification")
                
                @schemas.classproperty
                def INVALID_CHECK_INTERNATIONAL(cls):
                    return cls("invalid_check_international")
                
                @schemas.classproperty
                def INVALID_COUNTRY_COVID(cls):
                    return cls("invalid_country_covid")
                
                @schemas.classproperty
                def INVALID_FILE(cls):
                    return cls("invalid_file")
                
                @schemas.classproperty
                def INVALID_FILE_DIMENSIONS(cls):
                    return cls("invalid_file_dimensions")
                
                @schemas.classproperty
                def INVALID_FILE_DOWNLOAD_TIME(cls):
                    return cls("invalid_file_download_time")
                
                @schemas.classproperty
                def INVALID_FILE_URL(cls):
                    return cls("invalid_file_url")
                
                @schemas.classproperty
                def INVALID_IMAGE_DPI(cls):
                    return cls("invalid_image_dpi")
                
                @schemas.classproperty
                def INVALID_INTERNATIONAL_FEATURE(cls):
                    return cls("invalid_international_feature")
                
                @schemas.classproperty
                def INVALID_PERFORATION_RETURN_ENVELOPE(cls):
                    return cls("invalid_perforation_return_envelope")
                
                @schemas.classproperty
                def INVALID_TEMPLATE_HTML(cls):
                    return cls("invalid_template_html")
                
                @schemas.classproperty
                def MAIL_USE_TYPE_CAN_NOT_BE_NULL(cls):
                    return cls("mail_use_type_can_not_be_null")
                
                @schemas.classproperty
                def MERGE_VARIABLE_REQUIRED(cls):
                    return cls("merge_variable_required")
                
                @schemas.classproperty
                def MERGE_VARIABLE_WHITESPACE(cls):
                    return cls("merge_variable_whitespace")
                
                @schemas.classproperty
                def PAYMENT_METHOD_UNVERIFIED(cls):
                    return cls("payment_method_unverified")
                
                @schemas.classproperty
                def PDF_ENCRYPTED(cls):
                    return cls("pdf_encrypted")
                
                @schemas.classproperty
                def SPECIAL_CHARACTERS_RESTRICTED(cls):
                    return cls("special_characters_restricted")
                
                @schemas.classproperty
                def UNEMBEDDED_FONTS(cls):
                    return cls("unembedded_fonts")
                
                @schemas.classproperty
                def EMAIL_REQUIRED(cls):
                    return cls("email_required")
                
                @schemas.classproperty
                def INVALID_API_KEY(cls):
                    return cls("invalid_api_key")
                
                @schemas.classproperty
                def PUBLISHABLE_KEY_NOT_ALLOWED(cls):
                    return cls("publishable_key_not_allowed")
                
                @schemas.classproperty
                def RATE_LIMIT_EXCEEDED(cls):
                    return cls("rate_limit_exceeded")
                
                @schemas.classproperty
                def UNAUTHORIZED(cls):
                    return cls("unauthorized")
                
                @schemas.classproperty
                def UNAUTHORIZED_TOKEN(cls):
                    return cls("unauthorized_token")
            __annotations__ = {
                "message": message,
                "status_code": status_code,
                "code": code,
            }
    
    code: MetaOapg.properties.code
    status_code: 'FailureStatusCode'
    message: MetaOapg.properties.message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_code"]) -> 'FailureStatusCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "status_code", "code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_code"]) -> 'FailureStatusCode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "status_code", "code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, ],
        status_code: 'FailureStatusCode',
        message: typing.Union[MetaOapg.properties.message, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ErrorError':
        return super().__new__(
            cls,
            *args,
            code=code,
            status_code=status_code,
            message=message,
            _configuration=_configuration,
            **kwargs,
        )

from lob_python_sdk.model.failure_status_code import FailureStatusCode
