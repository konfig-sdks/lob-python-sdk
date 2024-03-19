# coding: utf-8
"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

import typing
import inspect
from datetime import date, datetime
from lob_python_sdk.client_custom import ClientCustom
from lob_python_sdk.configuration import Configuration
from lob_python_sdk.api_client import ApiClient
from lob_python_sdk.type_util import copy_signature
from lob_python_sdk.apis.tags.accounts_api import AccountsApi
from lob_python_sdk.apis.tags.addresses_api import AddressesApi
from lob_python_sdk.apis.tags.bank_accounts_api import BankAccountsApi
from lob_python_sdk.apis.tags.billing_groups_api import BillingGroupsApi
from lob_python_sdk.apis.tags.buckslip_orders_api import BuckslipOrdersApi
from lob_python_sdk.apis.tags.buckslips_api import BuckslipsApi
from lob_python_sdk.apis.tags.campaigns_api import CampaignsApi
from lob_python_sdk.apis.tags.card_orders_api import CardOrdersApi
from lob_python_sdk.apis.tags.cards_api import CardsApi
from lob_python_sdk.apis.tags.checks_api import ChecksApi
from lob_python_sdk.apis.tags.creatives_api import CreativesApi
from lob_python_sdk.apis.tags.identity_validation_api import IdentityValidationApi
from lob_python_sdk.apis.tags.intl_autocompletions_api import IntlAutocompletionsApi
from lob_python_sdk.apis.tags.intl_verifications_api import IntlVerificationsApi
from lob_python_sdk.apis.tags.letters_api import LettersApi
from lob_python_sdk.apis.tags.lob_credits_api import LobCreditsApi
from lob_python_sdk.apis.tags.postcards_api import PostcardsApi
from lob_python_sdk.apis.tags.qr_codes_api import QRCodesApi
from lob_python_sdk.apis.tags.reverse_geocode_lookups_api import ReverseGeocodeLookupsApi
from lob_python_sdk.apis.tags.self_mailers_api import SelfMailersApi
from lob_python_sdk.apis.tags.snap_packs_api import SnapPacksApi
from lob_python_sdk.apis.tags.template_versions_api import TemplateVersionsApi
from lob_python_sdk.apis.tags.templates_api import TemplatesApi
from lob_python_sdk.apis.tags.url_shortener_api import URLShortenerApi
from lob_python_sdk.apis.tags.us_autocompletions_api import USAutocompletionsApi
from lob_python_sdk.apis.tags.us_verifications_api import USVerificationsApi
from lob_python_sdk.apis.tags.uploads_api import UploadsApi
from lob_python_sdk.apis.tags.zip_lookups_api import ZipLookupsApi



class Lob(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.accounts: AccountsApi = AccountsApi(api_client)
        self.addresses: AddressesApi = AddressesApi(api_client)
        self.bank_accounts: BankAccountsApi = BankAccountsApi(api_client)
        self.billing_groups: BillingGroupsApi = BillingGroupsApi(api_client)
        self.buckslip_orders: BuckslipOrdersApi = BuckslipOrdersApi(api_client)
        self.buckslips: BuckslipsApi = BuckslipsApi(api_client)
        self.campaigns: CampaignsApi = CampaignsApi(api_client)
        self.card_orders: CardOrdersApi = CardOrdersApi(api_client)
        self.cards: CardsApi = CardsApi(api_client)
        self.checks: ChecksApi = ChecksApi(api_client)
        self.creatives: CreativesApi = CreativesApi(api_client)
        self.identity_validation: IdentityValidationApi = IdentityValidationApi(api_client)
        self.intl_autocompletions: IntlAutocompletionsApi = IntlAutocompletionsApi(api_client)
        self.intl_verifications: IntlVerificationsApi = IntlVerificationsApi(api_client)
        self.letters: LettersApi = LettersApi(api_client)
        self.lob_credits: LobCreditsApi = LobCreditsApi(api_client)
        self.postcards: PostcardsApi = PostcardsApi(api_client)
        self.qr_codes: QRCodesApi = QRCodesApi(api_client)
        self.reverse_geocode_lookups: ReverseGeocodeLookupsApi = ReverseGeocodeLookupsApi(api_client)
        self.self_mailers: SelfMailersApi = SelfMailersApi(api_client)
        self.snap_packs: SnapPacksApi = SnapPacksApi(api_client)
        self.template_versions: TemplateVersionsApi = TemplateVersionsApi(api_client)
        self.templates: TemplatesApi = TemplatesApi(api_client)
        self.url_shortener: URLShortenerApi = URLShortenerApi(api_client)
        self.us_autocompletions: USAutocompletionsApi = USAutocompletionsApi(api_client)
        self.us_verifications: USVerificationsApi = USVerificationsApi(api_client)
        self.uploads: UploadsApi = UploadsApi(api_client)
        self.zip_lookups: ZipLookupsApi = ZipLookupsApi(api_client)
