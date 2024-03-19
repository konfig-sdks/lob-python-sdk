# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from lob_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNTS = "/accounts"
    ADDRESSES = "/addresses"
    ADDRESSES_ADR_ID = "/addresses/{adr_id}"
    BANK_ACCOUNTS_BANK_ID_VERIFY = "/bank_accounts/{bank_id}/verify"
    BANK_ACCOUNTS_BANK_ID = "/bank_accounts/{bank_id}"
    BANK_ACCOUNTS = "/bank_accounts"
    BILLING_GROUPS_BG_ID = "/billing_groups/{bg_id}"
    BILLING_GROUPS = "/billing_groups"
    BUCKSLIPS = "/buckslips"
    BUCKSLIPS_BUCKSLIP_ID = "/buckslips/{buckslip_id}"
    BUCKSLIPS_BUCKSLIP_ID_ORDERS = "/buckslips/{buckslip_id}/orders"
    BULK_US_VERIFICATIONS = "/bulk/us_verifications"
    BULK_INTL_VERIFICATIONS = "/bulk/intl_verifications"
    CAMPAIGNS = "/campaigns"
    CAMPAIGNS_CMP_ID = "/campaigns/{cmp_id}"
    CAMPAIGNS_CMP_ID_SEND = "/campaigns/{cmp_id}/send"
    CARDS = "/cards"
    CARDS_CARD_ID = "/cards/{card_id}"
    CARDS_CARD_ID_ORDERS = "/cards/{card_id}/orders"
    CHECKS = "/checks"
    CHECKS_CHK_ID = "/checks/{chk_id}"
    CREATIVES = "/creatives"
    CREATIVES_CRV_ID = "/creatives/{crv_id}"
    IDENTITY_VALIDATION = "/identity_validation"
    INTL_AUTOCOMPLETIONS = "/intl_autocompletions"
    INTL_VERIFICATIONS = "/intl_verifications"
    LETTERS_LTR_ID = "/letters/{ltr_id}"
    LETTERS = "/letters"
    POSTCARDS_PSC_ID = "/postcards/{psc_id}"
    POSTCARDS = "/postcards"
    QR_CODE_ANALYTICS = "/qr_code_analytics"
    DOMAINS_DOMAIN_ID = "/domains/{domain_id}"
    DOMAINS = "/domains"
    DOMAINS_DOMAIN_ID_LINKS = "/domains/{domain_id}/links"
    LINKS = "/links"
    LINKS_LINK_ID = "/links/{link_id}"
    LINKS_SHORTEN = "/links/shorten"
    LINKS_SHORTEN_BULK = "/links/shorten/bulk"
    SELF_MAILERS_SFM_ID = "/self_mailers/{sfm_id}"
    SELF_MAILERS = "/self_mailers"
    SNAP_PACKS = "/snap_packs"
    TEMPLATES_TMPL_ID_VERSIONS_VRSN_ID = "/templates/{tmpl_id}/versions/{vrsn_id}"
    TEMPLATES_TMPL_ID_VERSIONS = "/templates/{tmpl_id}/versions"
    TEMPLATES_TMPL_ID = "/templates/{tmpl_id}"
    TEMPLATES = "/templates"
    UPLOADS = "/uploads"
    UPLOADS_UPL_ID = "/uploads/{upl_id}"
    UPLOADS_UPL_ID_FILE = "/uploads/{upl_id}/file"
    UPLOADS_UPL_ID_EXPORTS = "/uploads/{upl_id}/exports"
    UPLOADS_UPL_ID_REPORT = "/uploads/{upl_id}/report"
    UPLOADS_UPL_ID_EXPORTS_EX_ID = "/uploads/{upl_id}/exports/{ex_id}"
    US_AUTOCOMPLETIONS = "/us_autocompletions"
    US_REVERSE_GEOCODE_LOOKUPS = "/us_reverse_geocode_lookups"
    US_VERIFICATIONS = "/us_verifications"
    US_ZIP_LOOKUPS = "/us_zip_lookups"
