import typing_extensions

from lob_python_sdk.apis.tags import TagValues
from lob_python_sdk.apis.tags.url_shortener_api import URLShortenerApi
from lob_python_sdk.apis.tags.uploads_api import UploadsApi
from lob_python_sdk.apis.tags.campaigns_api import CampaignsApi
from lob_python_sdk.apis.tags.bank_accounts_api import BankAccountsApi
from lob_python_sdk.apis.tags.buckslips_api import BuckslipsApi
from lob_python_sdk.apis.tags.cards_api import CardsApi
from lob_python_sdk.apis.tags.template_versions_api import TemplateVersionsApi
from lob_python_sdk.apis.tags.templates_api import TemplatesApi
from lob_python_sdk.apis.tags.addresses_api import AddressesApi
from lob_python_sdk.apis.tags.billing_groups_api import BillingGroupsApi
from lob_python_sdk.apis.tags.checks_api import ChecksApi
from lob_python_sdk.apis.tags.letters_api import LettersApi
from lob_python_sdk.apis.tags.postcards_api import PostcardsApi
from lob_python_sdk.apis.tags.self_mailers_api import SelfMailersApi
from lob_python_sdk.apis.tags.creatives_api import CreativesApi
from lob_python_sdk.apis.tags.buckslip_orders_api import BuckslipOrdersApi
from lob_python_sdk.apis.tags.card_orders_api import CardOrdersApi
from lob_python_sdk.apis.tags.intl_verifications_api import IntlVerificationsApi
from lob_python_sdk.apis.tags.us_verifications_api import USVerificationsApi
from lob_python_sdk.apis.tags.identity_validation_api import IdentityValidationApi
from lob_python_sdk.apis.tags.intl_autocompletions_api import IntlAutocompletionsApi
from lob_python_sdk.apis.tags.qr_codes_api import QRCodesApi
from lob_python_sdk.apis.tags.reverse_geocode_lookups_api import ReverseGeocodeLookupsApi
from lob_python_sdk.apis.tags.us_autocompletions_api import USAutocompletionsApi
from lob_python_sdk.apis.tags.zip_lookups_api import ZipLookupsApi
from lob_python_sdk.apis.tags.accounts_api import AccountsApi
from lob_python_sdk.apis.tags.lob_credits_api import LobCreditsApi
from lob_python_sdk.apis.tags.snap_packs_api import SnapPacksApi
from lob_python_sdk.apis.tags.authentication_api import AuthenticationApi
from lob_python_sdk.apis.tags.beta_program_api import BetaProgramApi
from lob_python_sdk.apis.tags.bulk_intl_verifications_api import BulkIntlVerificationsApi
from lob_python_sdk.apis.tags.bulk_us_verifications_api import BulkUSVerificationsApi
from lob_python_sdk.apis.tags.errors_api import ErrorsApi
from lob_python_sdk.apis.tags.events_api import EventsApi
from lob_python_sdk.apis.tags.getting_started_api import GettingStartedApi
from lob_python_sdk.apis.tags.introduction_api import IntroductionApi
from lob_python_sdk.apis.tags.manage_mail_api import ManageMailApi
from lob_python_sdk.apis.tags.national_change_of_address_api import NationalChangeOfAddressApi
from lob_python_sdk.apis.tags.rate_limiting_api import RateLimitingApi
from lob_python_sdk.apis.tags.requests_and_responses_api import RequestsAndResponsesApi
from lob_python_sdk.apis.tags.sdks_and_tools_api import SDKsAndToolsApi
from lob_python_sdk.apis.tags.template_design_api import TemplateDesignApi
from lob_python_sdk.apis.tags.test_and_live_environments_api import TestAndLiveEnvironmentsApi
from lob_python_sdk.apis.tags.tracking_events_api import TrackingEventsApi
from lob_python_sdk.apis.tags.us_verification_types_api import USVerificationTypesApi
from lob_python_sdk.apis.tags.versioning_and_changelog_api import VersioningAndChangelogApi
from lob_python_sdk.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.URL_SHORTENER: URLShortenerApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.BUCKSLIPS: BuckslipsApi,
        TagValues.CARDS: CardsApi,
        TagValues.TEMPLATE_VERSIONS: TemplateVersionsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.ADDRESSES: AddressesApi,
        TagValues.BILLING_GROUPS: BillingGroupsApi,
        TagValues.CHECKS: ChecksApi,
        TagValues.LETTERS: LettersApi,
        TagValues.POSTCARDS: PostcardsApi,
        TagValues.SELF_MAILERS: SelfMailersApi,
        TagValues.CREATIVES: CreativesApi,
        TagValues.BUCKSLIP_ORDERS: BuckslipOrdersApi,
        TagValues.CARD_ORDERS: CardOrdersApi,
        TagValues.INTL_VERIFICATIONS: IntlVerificationsApi,
        TagValues.US_VERIFICATIONS: USVerificationsApi,
        TagValues.IDENTITY_VALIDATION: IdentityValidationApi,
        TagValues.INTL_AUTOCOMPLETIONS: IntlAutocompletionsApi,
        TagValues.QR_CODES: QRCodesApi,
        TagValues.REVERSE_GEOCODE_LOOKUPS: ReverseGeocodeLookupsApi,
        TagValues.US_AUTOCOMPLETIONS: USAutocompletionsApi,
        TagValues.ZIP_LOOKUPS: ZipLookupsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.LOB_CREDITS: LobCreditsApi,
        TagValues.SNAP_PACKS: SnapPacksApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BETA_PROGRAM: BetaProgramApi,
        TagValues.BULK_INTL_VERIFICATIONS: BulkIntlVerificationsApi,
        TagValues.BULK_US_VERIFICATIONS: BulkUSVerificationsApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GETTING_STARTED: GettingStartedApi,
        TagValues.INTRODUCTION: IntroductionApi,
        TagValues.MANAGE_MAIL: ManageMailApi,
        TagValues.NATIONAL_CHANGE_OF_ADDRESS: NationalChangeOfAddressApi,
        TagValues.RATE_LIMITING: RateLimitingApi,
        TagValues.REQUESTS_AND_RESPONSES: RequestsAndResponsesApi,
        TagValues.SDKS_AND_TOOLS: SDKsAndToolsApi,
        TagValues.TEMPLATE_DESIGN: TemplateDesignApi,
        TagValues.TEST_AND_LIVE_ENVIRONMENTS: TestAndLiveEnvironmentsApi,
        TagValues.TRACKING_EVENTS: TrackingEventsApi,
        TagValues.US_VERIFICATION_TYPES: USVerificationTypesApi,
        TagValues.VERSIONING_AND_CHANGELOG: VersioningAndChangelogApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.URL_SHORTENER: URLShortenerApi,
        TagValues.UPLOADS: UploadsApi,
        TagValues.CAMPAIGNS: CampaignsApi,
        TagValues.BANK_ACCOUNTS: BankAccountsApi,
        TagValues.BUCKSLIPS: BuckslipsApi,
        TagValues.CARDS: CardsApi,
        TagValues.TEMPLATE_VERSIONS: TemplateVersionsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.ADDRESSES: AddressesApi,
        TagValues.BILLING_GROUPS: BillingGroupsApi,
        TagValues.CHECKS: ChecksApi,
        TagValues.LETTERS: LettersApi,
        TagValues.POSTCARDS: PostcardsApi,
        TagValues.SELF_MAILERS: SelfMailersApi,
        TagValues.CREATIVES: CreativesApi,
        TagValues.BUCKSLIP_ORDERS: BuckslipOrdersApi,
        TagValues.CARD_ORDERS: CardOrdersApi,
        TagValues.INTL_VERIFICATIONS: IntlVerificationsApi,
        TagValues.US_VERIFICATIONS: USVerificationsApi,
        TagValues.IDENTITY_VALIDATION: IdentityValidationApi,
        TagValues.INTL_AUTOCOMPLETIONS: IntlAutocompletionsApi,
        TagValues.QR_CODES: QRCodesApi,
        TagValues.REVERSE_GEOCODE_LOOKUPS: ReverseGeocodeLookupsApi,
        TagValues.US_AUTOCOMPLETIONS: USAutocompletionsApi,
        TagValues.ZIP_LOOKUPS: ZipLookupsApi,
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.LOB_CREDITS: LobCreditsApi,
        TagValues.SNAP_PACKS: SnapPacksApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.BETA_PROGRAM: BetaProgramApi,
        TagValues.BULK_INTL_VERIFICATIONS: BulkIntlVerificationsApi,
        TagValues.BULK_US_VERIFICATIONS: BulkUSVerificationsApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GETTING_STARTED: GettingStartedApi,
        TagValues.INTRODUCTION: IntroductionApi,
        TagValues.MANAGE_MAIL: ManageMailApi,
        TagValues.NATIONAL_CHANGE_OF_ADDRESS: NationalChangeOfAddressApi,
        TagValues.RATE_LIMITING: RateLimitingApi,
        TagValues.REQUESTS_AND_RESPONSES: RequestsAndResponsesApi,
        TagValues.SDKS_AND_TOOLS: SDKsAndToolsApi,
        TagValues.TEMPLATE_DESIGN: TemplateDesignApi,
        TagValues.TEST_AND_LIVE_ENVIRONMENTS: TestAndLiveEnvironmentsApi,
        TagValues.TRACKING_EVENTS: TrackingEventsApi,
        TagValues.US_VERIFICATION_TYPES: USVerificationTypesApi,
        TagValues.VERSIONING_AND_CHANGELOG: VersioningAndChangelogApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
