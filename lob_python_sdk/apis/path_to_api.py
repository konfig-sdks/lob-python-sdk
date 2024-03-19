import typing_extensions

from lob_python_sdk.paths import PathValues
from lob_python_sdk.apis.paths.accounts import Accounts
from lob_python_sdk.apis.paths.addresses import Addresses
from lob_python_sdk.apis.paths.addresses_adr_id import AddressesAdrId
from lob_python_sdk.apis.paths.bank_accounts_bank_id_verify import BankAccountsBankIdVerify
from lob_python_sdk.apis.paths.bank_accounts_bank_id import BankAccountsBankId
from lob_python_sdk.apis.paths.bank_accounts import BankAccounts
from lob_python_sdk.apis.paths.billing_groups_bg_id import BillingGroupsBgId
from lob_python_sdk.apis.paths.billing_groups import BillingGroups
from lob_python_sdk.apis.paths.buckslips import Buckslips
from lob_python_sdk.apis.paths.buckslips_buckslip_id import BuckslipsBuckslipId
from lob_python_sdk.apis.paths.buckslips_buckslip_id_orders import BuckslipsBuckslipIdOrders
from lob_python_sdk.apis.paths.bulk_us_verifications import BulkUsVerifications
from lob_python_sdk.apis.paths.bulk_intl_verifications import BulkIntlVerifications
from lob_python_sdk.apis.paths.campaigns import Campaigns
from lob_python_sdk.apis.paths.campaigns_cmp_id import CampaignsCmpId
from lob_python_sdk.apis.paths.campaigns_cmp_id_send import CampaignsCmpIdSend
from lob_python_sdk.apis.paths.cards import Cards
from lob_python_sdk.apis.paths.cards_card_id import CardsCardId
from lob_python_sdk.apis.paths.cards_card_id_orders import CardsCardIdOrders
from lob_python_sdk.apis.paths.checks import Checks
from lob_python_sdk.apis.paths.checks_chk_id import ChecksChkId
from lob_python_sdk.apis.paths.creatives import Creatives
from lob_python_sdk.apis.paths.creatives_crv_id import CreativesCrvId
from lob_python_sdk.apis.paths.identity_validation import IdentityValidation
from lob_python_sdk.apis.paths.intl_autocompletions import IntlAutocompletions
from lob_python_sdk.apis.paths.intl_verifications import IntlVerifications
from lob_python_sdk.apis.paths.letters_ltr_id import LettersLtrId
from lob_python_sdk.apis.paths.letters import Letters
from lob_python_sdk.apis.paths.postcards_psc_id import PostcardsPscId
from lob_python_sdk.apis.paths.postcards import Postcards
from lob_python_sdk.apis.paths.qr_code_analytics import QrCodeAnalytics
from lob_python_sdk.apis.paths.domains_domain_id import DomainsDomainId
from lob_python_sdk.apis.paths.domains import Domains
from lob_python_sdk.apis.paths.domains_domain_id_links import DomainsDomainIdLinks
from lob_python_sdk.apis.paths.links import Links
from lob_python_sdk.apis.paths.links_link_id import LinksLinkId
from lob_python_sdk.apis.paths.links_shorten import LinksShorten
from lob_python_sdk.apis.paths.links_shorten_bulk import LinksShortenBulk
from lob_python_sdk.apis.paths.self_mailers_sfm_id import SelfMailersSfmId
from lob_python_sdk.apis.paths.self_mailers import SelfMailers
from lob_python_sdk.apis.paths.snap_packs import SnapPacks
from lob_python_sdk.apis.paths.templates_tmpl_id_versions_vrsn_id import TemplatesTmplIdVersionsVrsnId
from lob_python_sdk.apis.paths.templates_tmpl_id_versions import TemplatesTmplIdVersions
from lob_python_sdk.apis.paths.templates_tmpl_id import TemplatesTmplId
from lob_python_sdk.apis.paths.templates import Templates
from lob_python_sdk.apis.paths.uploads import Uploads
from lob_python_sdk.apis.paths.uploads_upl_id import UploadsUplId
from lob_python_sdk.apis.paths.uploads_upl_id_file import UploadsUplIdFile
from lob_python_sdk.apis.paths.uploads_upl_id_exports import UploadsUplIdExports
from lob_python_sdk.apis.paths.uploads_upl_id_report import UploadsUplIdReport
from lob_python_sdk.apis.paths.uploads_upl_id_exports_ex_id import UploadsUplIdExportsExId
from lob_python_sdk.apis.paths.us_autocompletions import UsAutocompletions
from lob_python_sdk.apis.paths.us_reverse_geocode_lookups import UsReverseGeocodeLookups
from lob_python_sdk.apis.paths.us_verifications import UsVerifications
from lob_python_sdk.apis.paths.us_zip_lookups import UsZipLookups

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ADDRESSES: Addresses,
        PathValues.ADDRESSES_ADR_ID: AddressesAdrId,
        PathValues.BANK_ACCOUNTS_BANK_ID_VERIFY: BankAccountsBankIdVerify,
        PathValues.BANK_ACCOUNTS_BANK_ID: BankAccountsBankId,
        PathValues.BANK_ACCOUNTS: BankAccounts,
        PathValues.BILLING_GROUPS_BG_ID: BillingGroupsBgId,
        PathValues.BILLING_GROUPS: BillingGroups,
        PathValues.BUCKSLIPS: Buckslips,
        PathValues.BUCKSLIPS_BUCKSLIP_ID: BuckslipsBuckslipId,
        PathValues.BUCKSLIPS_BUCKSLIP_ID_ORDERS: BuckslipsBuckslipIdOrders,
        PathValues.BULK_US_VERIFICATIONS: BulkUsVerifications,
        PathValues.BULK_INTL_VERIFICATIONS: BulkIntlVerifications,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_CMP_ID: CampaignsCmpId,
        PathValues.CAMPAIGNS_CMP_ID_SEND: CampaignsCmpIdSend,
        PathValues.CARDS: Cards,
        PathValues.CARDS_CARD_ID: CardsCardId,
        PathValues.CARDS_CARD_ID_ORDERS: CardsCardIdOrders,
        PathValues.CHECKS: Checks,
        PathValues.CHECKS_CHK_ID: ChecksChkId,
        PathValues.CREATIVES: Creatives,
        PathValues.CREATIVES_CRV_ID: CreativesCrvId,
        PathValues.IDENTITY_VALIDATION: IdentityValidation,
        PathValues.INTL_AUTOCOMPLETIONS: IntlAutocompletions,
        PathValues.INTL_VERIFICATIONS: IntlVerifications,
        PathValues.LETTERS_LTR_ID: LettersLtrId,
        PathValues.LETTERS: Letters,
        PathValues.POSTCARDS_PSC_ID: PostcardsPscId,
        PathValues.POSTCARDS: Postcards,
        PathValues.QR_CODE_ANALYTICS: QrCodeAnalytics,
        PathValues.DOMAINS_DOMAIN_ID: DomainsDomainId,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DOMAIN_ID_LINKS: DomainsDomainIdLinks,
        PathValues.LINKS: Links,
        PathValues.LINKS_LINK_ID: LinksLinkId,
        PathValues.LINKS_SHORTEN: LinksShorten,
        PathValues.LINKS_SHORTEN_BULK: LinksShortenBulk,
        PathValues.SELF_MAILERS_SFM_ID: SelfMailersSfmId,
        PathValues.SELF_MAILERS: SelfMailers,
        PathValues.SNAP_PACKS: SnapPacks,
        PathValues.TEMPLATES_TMPL_ID_VERSIONS_VRSN_ID: TemplatesTmplIdVersionsVrsnId,
        PathValues.TEMPLATES_TMPL_ID_VERSIONS: TemplatesTmplIdVersions,
        PathValues.TEMPLATES_TMPL_ID: TemplatesTmplId,
        PathValues.TEMPLATES: Templates,
        PathValues.UPLOADS: Uploads,
        PathValues.UPLOADS_UPL_ID: UploadsUplId,
        PathValues.UPLOADS_UPL_ID_FILE: UploadsUplIdFile,
        PathValues.UPLOADS_UPL_ID_EXPORTS: UploadsUplIdExports,
        PathValues.UPLOADS_UPL_ID_REPORT: UploadsUplIdReport,
        PathValues.UPLOADS_UPL_ID_EXPORTS_EX_ID: UploadsUplIdExportsExId,
        PathValues.US_AUTOCOMPLETIONS: UsAutocompletions,
        PathValues.US_REVERSE_GEOCODE_LOOKUPS: UsReverseGeocodeLookups,
        PathValues.US_VERIFICATIONS: UsVerifications,
        PathValues.US_ZIP_LOOKUPS: UsZipLookups,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNTS: Accounts,
        PathValues.ADDRESSES: Addresses,
        PathValues.ADDRESSES_ADR_ID: AddressesAdrId,
        PathValues.BANK_ACCOUNTS_BANK_ID_VERIFY: BankAccountsBankIdVerify,
        PathValues.BANK_ACCOUNTS_BANK_ID: BankAccountsBankId,
        PathValues.BANK_ACCOUNTS: BankAccounts,
        PathValues.BILLING_GROUPS_BG_ID: BillingGroupsBgId,
        PathValues.BILLING_GROUPS: BillingGroups,
        PathValues.BUCKSLIPS: Buckslips,
        PathValues.BUCKSLIPS_BUCKSLIP_ID: BuckslipsBuckslipId,
        PathValues.BUCKSLIPS_BUCKSLIP_ID_ORDERS: BuckslipsBuckslipIdOrders,
        PathValues.BULK_US_VERIFICATIONS: BulkUsVerifications,
        PathValues.BULK_INTL_VERIFICATIONS: BulkIntlVerifications,
        PathValues.CAMPAIGNS: Campaigns,
        PathValues.CAMPAIGNS_CMP_ID: CampaignsCmpId,
        PathValues.CAMPAIGNS_CMP_ID_SEND: CampaignsCmpIdSend,
        PathValues.CARDS: Cards,
        PathValues.CARDS_CARD_ID: CardsCardId,
        PathValues.CARDS_CARD_ID_ORDERS: CardsCardIdOrders,
        PathValues.CHECKS: Checks,
        PathValues.CHECKS_CHK_ID: ChecksChkId,
        PathValues.CREATIVES: Creatives,
        PathValues.CREATIVES_CRV_ID: CreativesCrvId,
        PathValues.IDENTITY_VALIDATION: IdentityValidation,
        PathValues.INTL_AUTOCOMPLETIONS: IntlAutocompletions,
        PathValues.INTL_VERIFICATIONS: IntlVerifications,
        PathValues.LETTERS_LTR_ID: LettersLtrId,
        PathValues.LETTERS: Letters,
        PathValues.POSTCARDS_PSC_ID: PostcardsPscId,
        PathValues.POSTCARDS: Postcards,
        PathValues.QR_CODE_ANALYTICS: QrCodeAnalytics,
        PathValues.DOMAINS_DOMAIN_ID: DomainsDomainId,
        PathValues.DOMAINS: Domains,
        PathValues.DOMAINS_DOMAIN_ID_LINKS: DomainsDomainIdLinks,
        PathValues.LINKS: Links,
        PathValues.LINKS_LINK_ID: LinksLinkId,
        PathValues.LINKS_SHORTEN: LinksShorten,
        PathValues.LINKS_SHORTEN_BULK: LinksShortenBulk,
        PathValues.SELF_MAILERS_SFM_ID: SelfMailersSfmId,
        PathValues.SELF_MAILERS: SelfMailers,
        PathValues.SNAP_PACKS: SnapPacks,
        PathValues.TEMPLATES_TMPL_ID_VERSIONS_VRSN_ID: TemplatesTmplIdVersionsVrsnId,
        PathValues.TEMPLATES_TMPL_ID_VERSIONS: TemplatesTmplIdVersions,
        PathValues.TEMPLATES_TMPL_ID: TemplatesTmplId,
        PathValues.TEMPLATES: Templates,
        PathValues.UPLOADS: Uploads,
        PathValues.UPLOADS_UPL_ID: UploadsUplId,
        PathValues.UPLOADS_UPL_ID_FILE: UploadsUplIdFile,
        PathValues.UPLOADS_UPL_ID_EXPORTS: UploadsUplIdExports,
        PathValues.UPLOADS_UPL_ID_REPORT: UploadsUplIdReport,
        PathValues.UPLOADS_UPL_ID_EXPORTS_EX_ID: UploadsUplIdExportsExId,
        PathValues.US_AUTOCOMPLETIONS: UsAutocompletions,
        PathValues.US_REVERSE_GEOCODE_LOOKUPS: UsReverseGeocodeLookups,
        PathValues.US_VERIFICATIONS: UsVerifications,
        PathValues.US_ZIP_LOOKUPS: UsZipLookups,
    }
)
