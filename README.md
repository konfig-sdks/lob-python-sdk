<div align="left">

[![Visit Lob](./header.png)](https://lob.com)

# Lob<a id="lob"></a>

The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p>



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`lob.accounts.get_credits_balance`](#lobaccountsget_credits_balance)
  * [`lob.addresses.create`](#lobaddressescreate)
  * [`lob.addresses.delete`](#lobaddressesdelete)
  * [`lob.addresses.list`](#lobaddresseslist)
  * [`lob.addresses.retrieve`](#lobaddressesretrieve)
  * [`lob.bank_accounts.create_new_bank_account`](#lobbank_accountscreate_new_bank_account)
  * [`lob.bank_accounts.delete_bank_account`](#lobbank_accountsdelete_bank_account)
  * [`lob.bank_accounts.get_details`](#lobbank_accountsget_details)
  * [`lob.bank_accounts.get_list`](#lobbank_accountsget_list)
  * [`lob.bank_accounts.verify_bank_account`](#lobbank_accountsverify_bank_account)
  * [`lob.billing_groups.create_new_group`](#lobbilling_groupscreate_new_group)
  * [`lob.billing_groups.get_details`](#lobbilling_groupsget_details)
  * [`lob.billing_groups.list`](#lobbilling_groupslist)
  * [`lob.billing_groups.update_attributes`](#lobbilling_groupsupdate_attributes)
  * [`lob.buckslip_orders.create_new_order`](#lobbuckslip_orderscreate_new_order)
  * [`lob.buckslip_orders.get_by_buckslip_id`](#lobbuckslip_ordersget_by_buckslip_id)
  * [`lob.buckslips.create`](#lobbuckslipscreate)
  * [`lob.buckslips.delete`](#lobbuckslipsdelete)
  * [`lob.buckslips.list`](#lobbuckslipslist)
  * [`lob.buckslips.retrieve`](#lobbuckslipsretrieve)
  * [`lob.buckslips.update`](#lobbuckslipsupdate)
  * [`lob.campaigns.create`](#lobcampaignscreate)
  * [`lob.campaigns.delete`](#lobcampaignsdelete)
  * [`lob.campaigns.list`](#lobcampaignslist)
  * [`lob.campaigns.retrieve`](#lobcampaignsretrieve)
  * [`lob.campaigns.send`](#lobcampaignssend)
  * [`lob.campaigns.update`](#lobcampaignsupdate)
  * [`lob.card_orders.create_new_order`](#lobcard_orderscreate_new_order)
  * [`lob.card_orders.get`](#lobcard_ordersget)
  * [`lob.cards.create`](#lobcardscreate)
  * [`lob.cards.delete`](#lobcardsdelete)
  * [`lob.cards.list`](#lobcardslist)
  * [`lob.cards.retrieve`](#lobcardsretrieve)
  * [`lob.cards.update`](#lobcardsupdate)
  * [`lob.checks.cancel`](#lobcheckscancel)
  * [`lob.checks.create`](#lobcheckscreate)
  * [`lob.checks.list`](#lobcheckslist)
  * [`lob.checks.retrieve`](#lobchecksretrieve)
  * [`lob.creatives.create`](#lobcreativescreate)
  * [`lob.creatives.retrieve`](#lobcreativesretrieve)
  * [`lob.creatives.update`](#lobcreativesupdate)
  * [`lob.identity_validation.validation`](#lobidentity_validationvalidation)
  * [`lob.intl_autocompletions.autocompletions`](#lobintl_autocompletionsautocompletions)
  * [`lob.intl_verifications.verification`](#lobintl_verificationsverification)
  * [`lob.intl_verifications.verify_bulk_addresses`](#lobintl_verificationsverify_bulk_addresses)
  * [`lob.letters.cancel`](#lobletterscancel)
  * [`lob.letters.create`](#lobletterscreate)
  * [`lob.letters.list`](#lobletterslist)
  * [`lob.letters.retrieve`](#loblettersretrieve)
  * [`lob.lob_credits.get_credits_balance`](#loblob_creditsget_credits_balance)
  * [`lob.postcards.create`](#lobpostcardscreate)
  * [`lob.postcards.delete`](#lobpostcardsdelete)
  * [`lob.postcards.list`](#lobpostcardslist)
  * [`lob.postcards.retrieve`](#lobpostcardsretrieve)
  * [`lob.qr_codes.get_sorted_qr_codes`](#lobqr_codesget_sorted_qr_codes)
  * [`lob.reverse_geocode_lookups.us_location_with_live_api_key`](#lobreverse_geocode_lookupsus_location_with_live_api_key)
  * [`lob.self_mailers.create_new_self_mailer`](#lobself_mailerscreate_new_self_mailer)
  * [`lob.self_mailers.get_details`](#lobself_mailersget_details)
  * [`lob.self_mailers.get_list`](#lobself_mailersget_list)
  * [`lob.self_mailers.remove_self_mailer`](#lobself_mailersremove_self_mailer)
  * [`lob.snap_packs.create_new_snap_pack`](#lobsnap_packscreate_new_snap_pack)
  * [`lob.template_versions.create_new_version`](#lobtemplate_versionscreate_new_version)
  * [`lob.template_versions.delete_version`](#lobtemplate_versionsdelete_version)
  * [`lob.template_versions.get`](#lobtemplate_versionsget)
  * [`lob.template_versions.get_list`](#lobtemplate_versionsget_list)
  * [`lob.template_versions.update_template_version`](#lobtemplate_versionsupdate_template_version)
  * [`lob.templates.delete`](#lobtemplatesdelete)
  * [`lob.templates.list`](#lobtemplateslist)
  * [`lob.templates.retrieve`](#lobtemplatesretrieve)
  * [`lob.templates.template`](#lobtemplatestemplate)
  * [`lob.templates.update`](#lobtemplatesupdate)
  * [`lob.url_shortener.bulk_shorten_links`](#loburl_shortenerbulk_shorten_links)
  * [`lob.url_shortener.create`](#loburl_shortenercreate)
  * [`lob.url_shortener.create_0`](#loburl_shortenercreate_0)
  * [`lob.url_shortener.delete`](#loburl_shortenerdelete)
  * [`lob.url_shortener.delete_0`](#loburl_shortenerdelete_0)
  * [`lob.url_shortener.delete_all_links_for_domain`](#loburl_shortenerdelete_all_links_for_domain)
  * [`lob.url_shortener.get`](#loburl_shortenerget)
  * [`lob.url_shortener.get_0`](#loburl_shortenerget_0)
  * [`lob.url_shortener.list`](#loburl_shortenerlist)
  * [`lob.url_shortener.list_0`](#loburl_shortenerlist_0)
  * [`lob.url_shortener.update`](#loburl_shortenerupdate)
  * [`lob.us_autocompletions.get_suggestions`](#lobus_autocompletionsget_suggestions)
  * [`lob.us_verifications.bulk_verify_addresses`](#lobus_verificationsbulk_verify_addresses)
  * [`lob.us_verifications.verification`](#lobus_verificationsverification)
  * [`lob.uploads.create`](#lobuploadscreate)
  * [`lob.uploads.create_export_file`](#lobuploadscreate_export_file)
  * [`lob.uploads.delete`](#lobuploadsdelete)
  * [`lob.uploads.file`](#lobuploadsfile)
  * [`lob.uploads.list`](#lobuploadslist)
  * [`lob.uploads.retrieve`](#lobuploadsretrieve)
  * [`lob.uploads.retrieve_0`](#lobuploadsretrieve_0)
  * [`lob.uploads.retrieve_1`](#lobuploadsretrieve_1)
  * [`lob.uploads.update`](#lobuploadsupdate)
  * [`lob.zip_lookups.lookup`](#lobzip_lookupslookup)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Lob&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from lob_python_sdk import Lob, ApiException

lob = Lob(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Get Lob Credits Balance
    get_credits_balance_response = lob.accounts.get_credits_balance()
    print(get_credits_balance_response)
except ApiException as e:
    print("Exception when calling AccountsApi.get_credits_balance: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from lob_python_sdk import Lob, ApiException

lob = Lob(username="YOUR_USERNAME", password="YOUR_PASSWORD")


async def main():
    try:
        # Get Lob Credits Balance
        get_credits_balance_response = await lob.accounts.aget_credits_balance()
        print(get_credits_balance_response)
    except ApiException as e:
        print("Exception when calling AccountsApi.get_credits_balance: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from lob_python_sdk import Lob, ApiException

lob = Lob(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Get Lob Credits Balance
    get_credits_balance_response = lob.accounts.raw.get_credits_balance()
    pprint(get_credits_balance_response.body)
    pprint(get_credits_balance_response.body["balance"])
    pprint(get_credits_balance_response.headers)
    pprint(get_credits_balance_response.status)
    pprint(get_credits_balance_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccountsApi.get_credits_balance: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `lob.accounts.get_credits_balance`<a id="lobaccountsget_credits_balance"></a>

Returns the account's current balance of Lob Credits.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_credits_balance_response = lob.accounts.get_credits_balance()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LobCreditsBalance`](./lob_python_sdk/pydantic/lob_credits_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.addresses.create`<a id="lobaddressescreate"></a>

Creates a new address given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.addresses.create(
    body=None,
    address_line1="string_example",
    address_line2="string_example",
    address_city="string_example",
    address_state="string_example",
    address_zip="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address_line1: `str`<a id="address_line1-str"></a>

The primary number, street name, and directional information.

##### address_line2: `Optional[str]`<a id="address_line2-optionalstr"></a>

An optional field containing any information which can't fit into line 1.

##### address_city: `Optional[str]`<a id="address_city-optionalstr"></a>

##### address_state: `Optional[str]`<a id="address_state-optionalstr"></a>

##### address_zip: `Optional[str]`<a id="address_zip-optionalstr"></a>

Optional postal code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddressEditable`](./lob_python_sdk/type/address_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Address`](./lob_python_sdk/pydantic/address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.addresses.delete`<a id="lobaddressesdelete"></a>

Deletes the details of an existing address. You need only supply the unique identifier that was returned upon address creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.addresses.delete(
    adr_id="adr_e68217bd744d65c8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### adr_id: [`AdrId`](./lob_python_sdk/type/.py)<a id="adr_id-adridlob_python_sdktypepy"></a>

id of the address

#### 🔄 Return<a id="🔄-return"></a>

[`AddressDeletion`](./lob_python_sdk/pydantic/address_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/addresses/{adr_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.addresses.list`<a id="lobaddresseslist"></a>

Returns a list of your addresses. The addresses are returned sorted by creation date, with the most recently created addresses appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.addresses.list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

#### 🔄 Return<a id="🔄-return"></a>

[`AddressesListResponse`](./lob_python_sdk/pydantic/addresses_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.addresses.retrieve`<a id="lobaddressesretrieve"></a>

Retrieves the details of an existing address. You need only supply the unique identifier that was returned upon address creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.addresses.retrieve(
    adr_id="adr_e68217bd744d65c8",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### adr_id: [`AdrId`](./lob_python_sdk/type/.py)<a id="adr_id-adridlob_python_sdktypepy"></a>

id of the address

#### 🔄 Return<a id="🔄-return"></a>

[`Address`](./lob_python_sdk/pydantic/address.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/addresses/{adr_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.bank_accounts.create_new_bank_account`<a id="lobbank_accountscreate_new_bank_account"></a>

Creates a new bank account with the provided properties. Bank accounts created in live mode will need to be verified via micro deposits before being able to send live checks. The deposits will appear in the bank account in 2-3 business days and have the description "VERIFICATION".

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_bank_account_response = lob.bank_accounts.create_new_bank_account(
    routing_number="aaaaaaaaa",
    account_number="string_example",
    account_type="company",
    signatory="string_example",
    description="Harry - Office",
    check_template="common",
    fractional_routing_number="string_example",
    city="string_example",
    state="string_example",
    zipcode="string_example",
    metadata={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### routing_number: `str`<a id="routing_number-str"></a>

Must be a <a href=\\\"https://www.frbservices.org/index.html\\\" target=\\\"_blank\\\">valid US routing number</a>.

##### account_number: `str`<a id="account_number-str"></a>

##### account_type: `str`<a id="account_type-str"></a>

The type of entity that holds the account.

##### signatory: `str`<a id="signatory-str"></a>

The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the <a href=\\\"https://dashboard.lob.com/#/login\\\" target=\\\"_blank\\\">Dashboard</a>.

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### check_template: `str`<a id="check_template-str"></a>

The check template used for printing. The defualt value is `common`. If you bank with JP Morgan Chase and wish to use Positive Pay use the `jpm` template. `jpm` requires additional information to be provided.

##### fractional_routing_number: `str`<a id="fractional_routing_number-str"></a>

The fractional routing number for your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the fractional routing number associated with your home bank institution.

##### city: `str`<a id="city-str"></a>

The city associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the city associated with your home bank institution.

##### state: `str`<a id="state-str"></a>

The state associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the state associated with your home bank institution.

##### zipcode: `str`<a id="zipcode-str"></a>

The zipcode associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the zipcode associated with your home bank institution.

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountBase`](./lob_python_sdk/type/bank_account_base.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccount`](./lob_python_sdk/pydantic/bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank_accounts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.bank_accounts.delete_bank_account`<a id="lobbank_accountsdelete_bank_account"></a>

Permanently deletes a bank account. It cannot be undone.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_bank_account_response = lob.bank_accounts.delete_bank_account(
    bank_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_id: `BankId`<a id="bank_id-bankid"></a>

id of the bank account

#### 🔄 Return<a id="🔄-return"></a>

[`BankDeletion`](./lob_python_sdk/pydantic/bank_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank_accounts/{bank_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.bank_accounts.get_details`<a id="lobbank_accountsget_details"></a>

Retrieves the details of an existing bank account. You need only supply the unique bank account identifier that was returned upon bank account creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = lob.bank_accounts.get_details(
    bank_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bank_id: `BankId`<a id="bank_id-bankid"></a>

id of the bank account

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccount`](./lob_python_sdk/pydantic/bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank_accounts/{bank_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.bank_accounts.get_list`<a id="lobbank_accountsget_list"></a>

Returns a list of your bank accounts. The bank accounts are returned sorted by creation date, with the most recently created bank accounts appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lob.bank_accounts.get_list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

#### 🔄 Return<a id="🔄-return"></a>

[`BankAccountsGetListResponse`](./lob_python_sdk/pydantic/bank_accounts_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank_accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.bank_accounts.verify_bank_account`<a id="lobbank_accountsverify_bank_account"></a>

Verify a bank account in order to create a check.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_bank_account_response = lob.bank_accounts.verify_bank_account(
    amounts=[1],
    bank_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amounts: List[`Cents`]<a id="amounts-listcents"></a>

In live mode, an array containing the two micro deposits (in cents) placed in the bank account. In test mode, no micro deposits will be placed, so any two integers between `1` and `100` will work.

##### bank_id: `BankId`<a id="bank_id-bankid"></a>

id of the bank account to be verified

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BankAccountVerify`](./lob_python_sdk/type/bank_account_verify.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BankAccount`](./lob_python_sdk/pydantic/bank_account.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bank_accounts/{bank_id}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.billing_groups.create_new_group`<a id="lobbilling_groupscreate_new_group"></a>

Creates a new billing_group with the provided properties.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_group_response = lob.billing_groups.create_new_group(
    body=None,
    description="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`BgDescription`](./lob_python_sdk/type/bg_description.py)<a id="description-bgdescriptionlob_python_sdktypebg_descriptionpy"></a>

##### name: [`Name`](./lob_python_sdk/type/name.py)<a id="name-namelob_python_sdktypenamepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BillingGroupEditable`](./lob_python_sdk/type/billing_group_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BillingGroup`](./lob_python_sdk/pydantic/billing_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing_groups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.billing_groups.get_details`<a id="lobbilling_groupsget_details"></a>

Retrieves the details of an existing billing_group. You need only supply the unique billing_group identifier that was returned upon billing_group creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = lob.billing_groups.get_details(
    bg_id="bg_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bg_id: [`BgId`](./lob_python_sdk/type/.py)<a id="bg_id-bgidlob_python_sdktypepy"></a>

id of the billing_group

#### 🔄 Return<a id="🔄-return"></a>

[`BillingGroup`](./lob_python_sdk/pydantic/billing_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing_groups/{bg_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.billing_groups.list`<a id="lobbilling_groupslist"></a>

Returns a list of your billing_groups. The billing_groups are returned sorted by creation date, with the most recently created billing_groups appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.billing_groups.list(
    limit=10,
    offset=0,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    date_modified={
        "key": "string_example",
    },
    sort_by=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### date_modified: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_modified-datefilterlob_python_sdktypepy"></a>

Filter by date modified. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### sort_by: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="sort_by-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Sorts items by ascending or descending dates. Use either `date_created` or `date_modified`, not both. 

#### 🔄 Return<a id="🔄-return"></a>

[`BillingGroupsListResponse`](./lob_python_sdk/pydantic/billing_groups_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing_groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.billing_groups.update_attributes`<a id="lobbilling_groupsupdate_attributes"></a>

Updates all editable attributes of the billing_group with the given id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_attributes_response = lob.billing_groups.update_attributes(
    bg_id="bg_C",
    description="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### bg_id: [`BgId`](./lob_python_sdk/type/.py)<a id="bg_id-bgidlob_python_sdktypepy"></a>

id of the billing_group

##### description: [`BgDescription`](./lob_python_sdk/type/bg_description.py)<a id="description-bgdescriptionlob_python_sdktypebg_descriptionpy"></a>

##### name: [`Name`](./lob_python_sdk/type/name.py)<a id="name-namelob_python_sdktypenamepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BillingGroupBase`](./lob_python_sdk/type/billing_group_base.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BillingGroup`](./lob_python_sdk/pydantic/billing_group.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/billing_groups/{bg_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslip_orders.create_new_order`<a id="lobbuckslip_orderscreate_new_order"></a>

Creates a new buckslip order given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_order_response = lob.buckslip_orders.create_new_order(
    quantity=5000,
    buckslip_id="bck_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quantity: `int`<a id="quantity-int"></a>

The quantity of buckslips in the order (minimum 5,000).

##### buckslip_id: [`BuckslipId`](./lob_python_sdk/type/.py)<a id="buckslip_id-buckslipidlob_python_sdktypepy"></a>

The ID of the buckslip to which the buckslip orders belong.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BuckslipOrderEditable`](./lob_python_sdk/type/buckslip_order_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BuckslipOrder`](./lob_python_sdk/pydantic/buckslip_order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips/{buckslip_id}/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslip_orders.get_by_buckslip_id`<a id="lobbuckslip_ordersget_by_buckslip_id"></a>

Retrieves the buckslip orders associated with the given buckslip id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_buckslip_id_response = lob.buckslip_orders.get_by_buckslip_id(
    buckslip_id="bck_C",
    limit=10,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### buckslip_id: [`BuckslipId`](./lob_python_sdk/type/.py)<a id="buckslip_id-buckslipidlob_python_sdktypepy"></a>

The ID of the buckslip to which the buckslip orders belong.

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

#### 🔄 Return<a id="🔄-return"></a>

[`BuckslipOrdersGetByBuckslipIdResponse`](./lob_python_sdk/pydantic/buckslip_orders_get_by_buckslip_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips/{buckslip_id}/orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslips.create`<a id="lobbuckslipscreate"></a>

Creates a new buckslip given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.buckslips.create(
    body=None,
    description="string_example",
    size="8.75x3.75",
    front=None,
    back=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`BuckslipDescription`](./lob_python_sdk/type/buckslip_description.py)<a id="description-buckslipdescriptionlob_python_sdktypebuckslip_descriptionpy"></a>

##### size: `str`<a id="size-str"></a>

The size of the buckslip

##### front: Union[`RemoteFileUrl`, `LocalFilePath`]<a id="front-unionremotefileurl-localfilepath"></a>


A PDF template for the front of the buckslip

##### back: Union[`RemoteFileUrl`, `LocalFilePath`]<a id="back-unionremotefileurl-localfilepath"></a>


A PDF template for the back of the buckslip

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BuckslipEditable`](./lob_python_sdk/type/buckslip_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Buckslip`](./lob_python_sdk/pydantic/buckslip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslips.delete`<a id="lobbuckslipsdelete"></a>

Delete an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.buckslips.delete(
    buckslip_id="bck_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### buckslip_id: [`BuckslipId`](./lob_python_sdk/type/.py)<a id="buckslip_id-buckslipidlob_python_sdktypepy"></a>

id of the buckslip

#### 🔄 Return<a id="🔄-return"></a>

[`BuckslipDeletion`](./lob_python_sdk/pydantic/buckslip_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips/{buckslip_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslips.list`<a id="lobbuckslipslist"></a>

Returns a list of your buckslips. The buckslips are returned sorted by creation date, with the most recently created buckslips appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.buckslips.list(
    limit=10,
    before_after=None,
    include=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

#### 🔄 Return<a id="🔄-return"></a>

[`BuckslipsListResponse`](./lob_python_sdk/pydantic/buckslips_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslips.retrieve`<a id="lobbuckslipsretrieve"></a>

Retrieves the details of an existing buckslip. You need only supply the unique customer identifier that was returned upon buckslip creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.buckslips.retrieve(
    buckslip_id="bck_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### buckslip_id: [`BuckslipId`](./lob_python_sdk/type/.py)<a id="buckslip_id-buckslipidlob_python_sdktypepy"></a>

id of the buckslip

#### 🔄 Return<a id="🔄-return"></a>

[`Buckslip`](./lob_python_sdk/pydantic/buckslip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips/{buckslip_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.buckslips.update`<a id="lobbuckslipsupdate"></a>

Update the details of an existing buckslip. You need only supply the unique identifier that was returned upon buckslip creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.buckslips.update(
    buckslip_id="bck_C",
    description="string_example",
    auto_reorder=True,
    reorder_quantity=5000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### buckslip_id: [`BuckslipId`](./lob_python_sdk/type/.py)<a id="buckslip_id-buckslipidlob_python_sdktypepy"></a>

id of the buckslip

##### description: [`BuckslipDescription`](./lob_python_sdk/type/buckslip_description.py)<a id="description-buckslipdescriptionlob_python_sdktypebuckslip_descriptionpy"></a>

##### auto_reorder: `bool`<a id="auto_reorder-bool"></a>

Allows for auto reordering

##### reorder_quantity: `Union[int, float]`<a id="reorder_quantity-unionint-float"></a>

The quantity of items to be reordered (only required when auto_reorder is true).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BuckslipUpdatable`](./lob_python_sdk/type/buckslip_updatable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Buckslip`](./lob_python_sdk/pydantic/buckslip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/buckslips/{buckslip_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.create`<a id="lobcampaignscreate"></a>

Creates a new campaign with the provided properties. See how to launch your first campaign [here](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/launch-your-first-campaign).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.campaigns.create(
    name="string_example",
    schedule_type="immediate",
    use_type="marketing",
    description="Harry - Office",
    billing_group_id="bg_C",
    target_delivery_date="1970-01-01T00:00:00.00Z",
    send_date="1970-01-01T00:00:00.00Z",
    cancel_window_campaign_minutes=1,
    metadata={
        "key": "string_example",
    },
    auto_cancel_if_ncoa=True,
    x_lang_output="native",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

Name of the campaign.

##### schedule_type: [`CmpScheduleType`](./lob_python_sdk/type/cmp_schedule_type.py)<a id="schedule_type-cmpscheduletypelob_python_sdktypecmp_schedule_typepy"></a>

##### use_type: [`CmpUseType`](./lob_python_sdk/type/cmp_use_type.py)<a id="use_type-cmpusetypelob_python_sdktypecmp_use_typepy"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### billing_group_id: `Optional[str]`<a id="billing_group_id-optionalstr"></a>

Unique identifier prefixed with `bg_`.

##### target_delivery_date: `Optional[datetime]`<a id="target_delivery_date-optionaldatetime"></a>

If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign.

##### send_date: `Optional[datetime]`<a id="send_date-optionaldatetime"></a>

If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign.

##### cancel_window_campaign_minutes: `Optional[int]`<a id="cancel_window_campaign_minutes-optionalint"></a>

A window, in minutes, within which the campaign can be canceled.

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### auto_cancel_if_ncoa: `bool`<a id="auto_cancel_if_ncoa-bool"></a>

Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA.

##### x_lang_output: `str`<a id="x_lang_output-str"></a>

* `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CampaignWritable`](./lob_python_sdk/type/campaign_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Campaign`](./lob_python_sdk/pydantic/campaign.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.delete`<a id="lobcampaignsdelete"></a>

Delete an existing campaign. You need only supply the unique identifier that was returned upon campaign creation. Deleting a campaign also deletes any associated mail pieces that have been created but not sent. A campaign's `send_date` matches its associated mail pieces' `send_date`s.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.campaigns.delete(
    cmp_id="cmp_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cmp_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="cmp_id-cmpidlob_python_sdktypepy"></a>

id of the campaign

#### 🔄 Return<a id="🔄-return"></a>

[`CampaignDeleteResponse`](./lob_python_sdk/pydantic/campaign_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns/{cmp_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.list`<a id="lobcampaignslist"></a>

Returns a list of your campaigns. The campaigns are returned sorted by creation date, with the most recently created campaigns appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.campaigns.list(
    limit=10,
    include=["string_example"],
    before_after=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

#### 🔄 Return<a id="🔄-return"></a>

[`CampaignsListResponse`](./lob_python_sdk/pydantic/campaigns_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.retrieve`<a id="lobcampaignsretrieve"></a>

Retrieves the details of an existing campaign. You need only supply the unique campaign identifier that was returned upon campaign creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.campaigns.retrieve(
    cmp_id="cmp_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cmp_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="cmp_id-cmpidlob_python_sdktypepy"></a>

id of the campaign

#### 🔄 Return<a id="🔄-return"></a>

[`Campaign`](./lob_python_sdk/pydantic/campaign.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns/{cmp_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.send`<a id="lobcampaignssend"></a>

Sends a campaign. You need only supply the unique campaign identifier that was returned upon campaign creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_response = lob.campaigns.send(
    cmp_id="cmp_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cmp_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="cmp_id-cmpidlob_python_sdktypepy"></a>

id of the campaign

#### 🔄 Return<a id="🔄-return"></a>

[`Campaign`](./lob_python_sdk/pydantic/campaign.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns/{cmp_id}/send` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.campaigns.update`<a id="lobcampaignsupdate"></a>

Update the details of an existing campaign. You need only supply the unique identifier that was returned upon campaign creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.campaigns.update(
    cmp_id="cmp_C",
    description="Harry - Office",
    name="string_example",
    schedule_type="immediate",
    target_delivery_date="1970-01-01T00:00:00.00Z",
    send_date="1970-01-01T00:00:00.00Z",
    cancel_window_campaign_minutes=1,
    metadata={
        "key": "string_example",
    },
    is_draft=True,
    use_type="marketing",
    auto_cancel_if_ncoa=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cmp_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="cmp_id-cmpidlob_python_sdktypepy"></a>

id of the campaign

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### name: `str`<a id="name-str"></a>

##### schedule_type: [`CmpScheduleType`](./lob_python_sdk/type/cmp_schedule_type.py)<a id="schedule_type-cmpscheduletypelob_python_sdktypecmp_schedule_typepy"></a>

##### target_delivery_date: `datetime`<a id="target_delivery_date-datetime"></a>

If `schedule_type` is `target_delivery_date`, provide a targeted delivery date for mail pieces in this campaign.

##### send_date: `datetime`<a id="send_date-datetime"></a>

If `schedule_type` is `scheduled_send_date`, provide a date to send this campaign.

##### cancel_window_campaign_minutes: `int`<a id="cancel_window_campaign_minutes-int"></a>

A window, in minutes, within which the campaign can be canceled.

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### is_draft: `bool`<a id="is_draft-bool"></a>

Whether or not the campaign is still a draft. Can either be excluded or `false`.

##### use_type: [`CmpUseType`](./lob_python_sdk/type/cmp_use_type.py)<a id="use_type-cmpusetypelob_python_sdktypecmp_use_typepy"></a>

##### auto_cancel_if_ncoa: `bool`<a id="auto_cancel_if_ncoa-bool"></a>

Whether or not a mail piece should be automatically canceled and not sent if the address is updated via NCOA.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CampaignUpdatable`](./lob_python_sdk/type/campaign_updatable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Campaign`](./lob_python_sdk/pydantic/campaign.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/campaigns/{cmp_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.card_orders.create_new_order`<a id="lobcard_orderscreate_new_order"></a>

Creates a new card order given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_order_response = lob.card_orders.create_new_order(
    quantity=10000,
    card_id="card_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### quantity: `int`<a id="quantity-int"></a>

The quantity of cards in the order (minimum 10,000).

##### card_id: [`CardId`](./lob_python_sdk/type/.py)<a id="card_id-cardidlob_python_sdktypepy"></a>

The ID of the card to which the card orders belong.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardOrderEditable`](./lob_python_sdk/type/card_order_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CardOrder`](./lob_python_sdk/pydantic/card_order.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{card_id}/orders` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.card_orders.get`<a id="lobcard_ordersget"></a>

Retrieves the card orders associated with the given card id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = lob.card_orders.get(
    card_id="card_C",
    limit=10,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_id: [`CardId`](./lob_python_sdk/type/.py)<a id="card_id-cardidlob_python_sdktypepy"></a>

The ID of the card to which the card orders belong.

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

#### 🔄 Return<a id="🔄-return"></a>

[`CardOrdersGetResponse`](./lob_python_sdk/pydantic/card_orders_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{card_id}/orders` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.cards.create`<a id="lobcardscreate"></a>

Creates a new card given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.cards.create(
    body=None,
    description="string_example",
    size="2.125x3.375",
    front=None,
    back=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`CardDescription`](./lob_python_sdk/type/card_description.py)<a id="description-carddescriptionlob_python_sdktypecard_descriptionpy"></a>

##### size: `str`<a id="size-str"></a>

The size of the card

##### front: Union[`RemoteFileUrl`, `LocalFilePath`]<a id="front-unionremotefileurl-localfilepath"></a>


A PDF template for the front of the card

##### back: Union[`RemoteFileUrl`, `LocalFilePath`]<a id="back-unionremotefileurl-localfilepath"></a>


A PDF template for the back of the card

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardEditable`](./lob_python_sdk/type/card_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Card`](./lob_python_sdk/pydantic/card.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.cards.delete`<a id="lobcardsdelete"></a>

Delete an existing card. You need only supply the unique identifier that was returned upon card creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.cards.delete(
    card_id="card_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_id: [`CardId`](./lob_python_sdk/type/.py)<a id="card_id-cardidlob_python_sdktypepy"></a>

id of the card

#### 🔄 Return<a id="🔄-return"></a>

[`CardDeletion`](./lob_python_sdk/pydantic/card_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{card_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.cards.list`<a id="lobcardslist"></a>

Returns a list of your cards. The cards are returned sorted by creation date, with the most recently created addresses appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.cards.list(
    limit=10,
    before_after=None,
    include=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

#### 🔄 Return<a id="🔄-return"></a>

[`CardsListResponse`](./lob_python_sdk/pydantic/cards_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.cards.retrieve`<a id="lobcardsretrieve"></a>

Retrieves the details of an existing card. You need only supply the unique customer identifier that was returned upon card creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.cards.retrieve(
    card_id="card_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_id: [`CardId`](./lob_python_sdk/type/.py)<a id="card_id-cardidlob_python_sdktypepy"></a>

id of the card

#### 🔄 Return<a id="🔄-return"></a>

[`Card`](./lob_python_sdk/pydantic/card.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{card_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.cards.update`<a id="lobcardsupdate"></a>

Update the details of an existing card. You need only supply the unique identifier that was returned upon card creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.cards.update(
    card_id="card_C",
    description="string_example",
    auto_reorder=True,
    reorder_quantity=10000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_id: [`CardId`](./lob_python_sdk/type/.py)<a id="card_id-cardidlob_python_sdktypepy"></a>

id of the card

##### description: [`CardDescription`](./lob_python_sdk/type/card_description.py)<a id="description-carddescriptionlob_python_sdktypecard_descriptionpy"></a>

##### auto_reorder: `bool`<a id="auto_reorder-bool"></a>

Allows for auto reordering

##### reorder_quantity: `Union[int, float]`<a id="reorder_quantity-unionint-float"></a>

The quantity of items to be reordered (only required when auto_reorder is true).

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardUpdatable`](./lob_python_sdk/type/card_updatable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Card`](./lob_python_sdk/pydantic/card.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{card_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.checks.cancel`<a id="lobcheckscancel"></a>

Completely removes a check from production. This can only be done if the check has a `send_date` and the `send_date` has not yet passed. If the check is successfully canceled, you will not be charged for it. Read more on [cancellation windows](#section/Cancellation-Windows) and [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation is a premium feature. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_response = lob.checks.cancel(
    chk_id="chk_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chk_id: [`ChkId`](./lob_python_sdk/type/.py)<a id="chk_id-chkidlob_python_sdktypepy"></a>

id of the check

#### 🔄 Return<a id="🔄-return"></a>

[`CheckDeletion`](./lob_python_sdk/pydantic/check_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks/{chk_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.checks.create`<a id="lobcheckscreate"></a>

Creates a new check with the provided properties.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.checks.create(
    body=None,
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    merge_variables={},
    send_date="string_example",
    mail_type="usps_first_class",
    memo="string_example",
    check_number=1,
    message="string_example",
    use_type="marketing",
    to=None,
    _from=None,
    bank_account=None,
    amount=3.14,
    logo=None,
    check_bottom=None,
    attachment=None,
    billing_group_id="string_example",
    idempotency_key="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    idempotency_key2="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### merge_variables: [`MergeVariables`](./lob_python_sdk/type/merge_variables.py)<a id="merge_variables-mergevariableslob_python_sdktypemerge_variablespy"></a>


##### send_date: `SendDate`<a id="send_date-senddate"></a>

##### mail_type: `str`<a id="mail_type-str"></a>

Checks must be sent `usps_first_class`

##### memo: `Optional[str]`<a id="memo-optionalstr"></a>

Text to include on the memo line of the check.

##### check_number: `int`<a id="check_number-int"></a>

An integer that designates the check number. If `check_number` is not provided, checks created from a new `bank_account` will start at `10000` and increment with each check created with the `bank_account`. A provided `check_number` overrides the defaults. Subsequent checks created with the same `bank_account` will increment from the provided check number.

##### message: `str`<a id="message-str"></a>

Max of 400 characters to be included at the bottom of the check page.

##### use_type: [`ChkUseType`](./lob_python_sdk/type/chk_use_type.py)<a id="use_type-chkusetypelob_python_sdktypechk_use_typepy"></a>

##### to: Union[`AdrId`, `InlineAddressUsChk`]<a id="to-unionadrid-inlineaddressuschk"></a>


Must either be an address ID or an inline object with correct address parameters. Checks cannot be sent internationally (`address_country` must be `US`). The total string of the sum of `address_line1` and `address_line2` must be no longer than 50 characters combined. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine, and returned back with an ID. Depending on your <a href=\\\"https://dashboard.lob.com/#/settings/editions\\\" target=\\\"_blank\\\">Print & Mail Edition</a>, addresses may also be run through [National Change of Address (NCOALink)](#tag/National-Change-of-Address). If an address used does not meet your account’s <a href=\\\"https://dashboard.lob.com/#/settings/account\\\" target=\\\"_blank\\\">US Mail Strictness Setting</a>, the request will fail. <a href=\\\"https://help.lob.com/print-and-mail/all-about-addresses\\\" target=\\\"_blank\\\">More about verification of mailing addresses</a>

##### _from: Union[`AdrId`, `InlineAddressUs`]<a id="_from-unionadrid-inlineaddressus"></a>


Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.

##### bank_account: Union[`BankIdNoDescription`, `str`]<a id="bank_account-unionbankidnodescription-str"></a>


##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The payment amount to be sent in US dollars. Amounts will be rounded to two decimal places.

##### logo: Union[`str`, `str`]<a id="logo-unionstr-str"></a>


Accepts a remote URL or local file upload to an image to print (in grayscale) in the upper-left corner of your check. Image requirements:    * RGB or CMYK    * square    * minimum size: 100px x 100px    * transparent backgrond    * `png` or `jpg`

##### check_bottom: `CheckBottom`<a id="check_bottom-checkbottom"></a>

##### attachment: Union[`HtmlString`, `TmplId`, `RemoteFileUrl`, `LocalFilePath`]<a id="attachment-unionhtmlstring-tmplid-remotefileurl-localfilepath"></a>


A document to include with the check.  Notes: - HTML merge variables should not include delimiting whitespace. - All pages of PDF, PNG, and JPGs must be sized at 8.5\\\"x11\\\" at 300 DPI, while supplied HTML will be rendered and trimmed to as many 8.5\\\"x11\\\" pages as necessary. - If a PDF is provided, it must be 6 pages or fewer. - The attachment will be printed double-sided in black & white and will be included in the envelope after the check page. - Please follow these <a href=\\\"https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_attachment_template.pdf\\\" target=\\\"_blank\\\">design guidelines</a>.  See <a href=\\\"https://lob.com/pricing/print-mail#compare\\\" target=\\\"_blank\\\">pricing</a> for extra costs incurred. Need more help? Consult our [HTML examples](#section/HTML-Examples).

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### idempotency_key2: `str`<a id="idempotency_key2-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckEditable`](./lob_python_sdk/type/check_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Check`](./lob_python_sdk/pydantic/check.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.checks.list`<a id="lobcheckslist"></a>

Returns a list of your checks. The checks are returned sorted by creation date, with the most recently created checks appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.checks.list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
    scheduled=True,
    send_date="string_example",
    mail_type="usps_first_class",
    sort_by=None,
    status="processed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

##### scheduled: `bool`<a id="scheduled-bool"></a>

* `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created` 

##### send_date: `SendDate`<a id="send_date-senddate"></a>

Filter by ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. 

##### mail_type: [`MailType`](./lob_python_sdk/type/.py)<a id="mail_type-mailtypelob_python_sdktypepy"></a>

A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href=\"https://lob.com/pricing/print-mail#compare\" target=\"_blank\">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. 

##### sort_by: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="sort_by-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. 

##### status: [`Status`](./lob_python_sdk/type/.py)<a id="status-statuslob_python_sdktypepy"></a>

A string describing the render status: * `processed` - the rendering process is currently underway. * `rendered` - the rendering process has completed successfully. * `failed` - the rendering process has failed. 

#### 🔄 Return<a id="🔄-return"></a>

[`ChecksListResponse`](./lob_python_sdk/pydantic/checks_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.checks.retrieve`<a id="lobchecksretrieve"></a>

Retrieves the details of an existing check. You need only supply the unique check identifier that was returned upon check creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.checks.retrieve(
    chk_id="chk_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### chk_id: [`ChkId`](./lob_python_sdk/type/.py)<a id="chk_id-chkidlob_python_sdktypepy"></a>

id of the check

#### 🔄 Return<a id="🔄-return"></a>

[`Check`](./lob_python_sdk/pydantic/check.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checks/{chk_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.creatives.create`<a id="lobcreativescreate"></a>

Creates a new creative with the provided properties

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.creatives.create(
    body=None,
    resource_type="self_mailer",
    campaign_id="cmp_C",
    front=None,
    back=None,
    details=None,
    description="Harry - Office",
    _from=None,
    metadata={
        "key": "string_example",
    },
    file=None,
    inside=None,
    outside=None,
    x_lang_output="native",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### resource_type: `str`<a id="resource_type-str"></a>

Mailpiece type for the creative

##### campaign_id: [`CmpId`](./lob_python_sdk/type/cmp_id.py)<a id="campaign_id-cmpidlob_python_sdktypecmp_idpy"></a>

##### front: `CrvFront`<a id="front-crvfront"></a>

##### back: `CrvBack`<a id="back-crvback"></a>

##### details: [`SelfMailerDetailsWritable`](./lob_python_sdk/type/self_mailer_details_writable.py)<a id="details-selfmailerdetailswritablelob_python_sdktypeself_mailer_details_writablepy"></a>


##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### _from: `FromAttribute`<a id="_from-fromattribute"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### file: `CrvFile`<a id="file-crvfile"></a>

##### inside: `CrvInside`<a id="inside-crvinside"></a>

##### outside: `CrvOutside`<a id="outside-crvoutside"></a>

##### x_lang_output: `str`<a id="x_lang_output-str"></a>

* `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreativeWritable`](./lob_python_sdk/type/creative_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Creative`](./lob_python_sdk/pydantic/creative.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/creatives` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.creatives.retrieve`<a id="lobcreativesretrieve"></a>

Retrieves the details of an existing creative. You need only supply the unique creative identifier that was returned upon creative creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.creatives.retrieve(
    crv_id="crv_2a3b096c409b32c",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### crv_id: [`CrvId`](./lob_python_sdk/type/.py)<a id="crv_id-crvidlob_python_sdktypepy"></a>

id of the creative

#### 🔄 Return<a id="🔄-return"></a>

[`Creative`](./lob_python_sdk/pydantic/creative.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/creatives/{crv_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.creatives.update`<a id="lobcreativesupdate"></a>

Update the details of an existing creative. You need only supply the unique identifier that was returned upon creative creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.creatives.update(
    crv_id="crv_2a3b096c409b32c",
    description="Harry - Office",
    _from=None,
    metadata={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### crv_id: [`CrvId`](./lob_python_sdk/type/.py)<a id="crv_id-crvidlob_python_sdktypepy"></a>

id of the creative

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### _from: `FromAttribute`<a id="_from-fromattribute"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreativeBase`](./lob_python_sdk/type/creative_base.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Creative`](./lob_python_sdk/pydantic/creative.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/creatives/{crv_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.identity_validation.validation`<a id="lobidentity_validationvalidation"></a>

Validates whether a given name is associated with an address.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validation_response = lob.identity_validation.validation(
    body=None,
    recipient="string_example",
    primary_line="string_example",
    secondary_line="string_example",
    urbanization="string_example",
    city=None,
    state="string_example",
    zip_code=None,
    company="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient: [`Recipient`](./lob_python_sdk/type/recipient.py)<a id="recipient-recipientlob_python_sdktyperecipientpy"></a>

##### primary_line: [`PrimaryLineUs`](./lob_python_sdk/type/primary_line_us.py)<a id="primary_line-primarylineuslob_python_sdktypeprimary_line_uspy"></a>

##### secondary_line: [`SecondaryLine`](./lob_python_sdk/type/secondary_line.py)<a id="secondary_line-secondarylinelob_python_sdktypesecondary_linepy"></a>

##### urbanization: [`Urbanization`](./lob_python_sdk/type/urbanization.py)<a id="urbanization-urbanizationlob_python_sdktypeurbanizationpy"></a>

##### city: Union[`CityNoDescription`, `str`]<a id="city-unioncitynodescription-str"></a>


##### state: `str`<a id="state-str"></a>

The <a href=\\\"https://en.wikipedia.org/wiki/ISO_3166-2:US\\\" target=\\\"_blank\\\">ISO 3166-2</a> two letter code or subdivision name for the state. `city` and `state` are required if no `zip_code` is passed.

##### zip_code: Union[`str`, `ZipCode`]<a id="zip_code-unionstr-zipcode"></a>


##### company: [`IdentityValidationCompany`](./lob_python_sdk/type/identity_validation_company.py)<a id="company-identityvalidationcompanylob_python_sdktypeidentity_validation_companypy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IdentityValidationWritable`](./lob_python_sdk/type/identity_validation_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IdentityValidation`](./lob_python_sdk/pydantic/identity_validation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/identity_validation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.intl_autocompletions.autocompletions`<a id="lobintl_autocompletionsautocompletions"></a>

Given an address prefix consisting of a partial primary line and country, as well as optional input of city, state, and zip code, this functionality returns up to 10 full International address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/intl_verification).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
autocompletions_response = lob.intl_autocompletions.autocompletions(
    address_prefix="string_example",
    country="AD",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    geo_ip_sort=True,
    x_lang_output="native",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address_prefix: `str`<a id="address_prefix-str"></a>

Only accepts numbers and street names in an alphanumeric format. 

##### country: [`CountryExtended`](./lob_python_sdk/type/country_extended.py)<a id="country-countryextendedlob_python_sdktypecountry_extendedpy"></a>

##### city: `str`<a id="city-str"></a>

An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. 

##### state: `str`<a id="state-str"></a>

An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. 

##### zip_code: `str`<a id="zip_code-str"></a>

An optional Zip Code input used to filter suggestions. Matches partial entries. 

##### geo_ip_sort: `bool`<a id="geo_ip_sort-bool"></a>

If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. 

##### x_lang_output: `str`<a id="x_lang_output-str"></a>

* `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntlAutocompletionsWritable`](./lob_python_sdk/type/intl_autocompletions_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IntlAutocompletions`](./lob_python_sdk/pydantic/intl_autocompletions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/intl_autocompletions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.intl_verifications.verification`<a id="lobintl_verificationsverification"></a>

Verify an international (except US or US territories) address _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verification_response = lob.intl_verifications.verification(
    body=None,
    recipient="string_example",
    primary_line="string_example",
    secondary_line="string_example",
    city=None,
    state="string_example",
    postal_code="string_example",
    country="AD",
    address="string_example",
    x_lang_output="native",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient: [`Recipient`](./lob_python_sdk/type/recipient.py)<a id="recipient-recipientlob_python_sdktyperecipientpy"></a>

##### primary_line: [`PrimaryLine`](./lob_python_sdk/type/primary_line.py)<a id="primary_line-primarylinelob_python_sdktypeprimary_linepy"></a>

##### secondary_line: [`SecondaryLine`](./lob_python_sdk/type/secondary_line.py)<a id="secondary_line-secondarylinelob_python_sdktypesecondary_linepy"></a>

##### city: `City`<a id="city-city"></a>

##### state: `str`<a id="state-str"></a>

The name of the state.

##### postal_code: [`PostalCode`](./lob_python_sdk/type/postal_code.py)<a id="postal_code-postalcodelob_python_sdktypepostal_codepy"></a>

##### country: [`CountryExtended`](./lob_python_sdk/type/country_extended.py)<a id="country-countryextendedlob_python_sdktypecountry_extendedpy"></a>

##### address: `str`<a id="address-str"></a>

The entire address in one string (e.g., \\\"370 Water St C1N 1C4\\\"). 

##### x_lang_output: `str`<a id="x_lang_output-str"></a>

* `native` - Translate response to the native language of the country in the request * `match` - match the response to the language in the request  Default response is in English. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntlVerificationWritable`](./lob_python_sdk/type/intl_verification_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IntlVerification`](./lob_python_sdk/pydantic/intl_verification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/intl_verifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.intl_verifications.verify_bulk_addresses`<a id="lobintl_verificationsverify_bulk_addresses"></a>

Verify a list of international (except US or US territories) address _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_bulk_addresses_response = lob.intl_verifications.verify_bulk_addresses(
    addresses=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### addresses: List[`MultipleComponentsIntl`]<a id="addresses-listmultiplecomponentsintl"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IntlVerificationsPayload`](./lob_python_sdk/type/intl_verifications_payload.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IntlVerifications`](./lob_python_sdk/pydantic/intl_verifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bulk/intl_verifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.letters.cancel`<a id="lobletterscancel"></a>

Completely removes a letter from production. This can only be done if the letter has a `send_date` and the `send_date` has not yet passed. If the letter is successfully canceled, you will not be charged for it. Read more on [cancellation windows](#section/Cancellation-Windows) and [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation is a premium feature. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_response = lob.letters.cancel(
    ltr_id="ltr_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ltr_id: [`LtrId`](./lob_python_sdk/type/.py)<a id="ltr_id-ltridlob_python_sdktypepy"></a>

id of the letter

#### 🔄 Return<a id="🔄-return"></a>

[`LetterDeletion`](./lob_python_sdk/pydantic/letter_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/letters/{ltr_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.letters.create`<a id="lobletterscreate"></a>

Creates a new letter given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.letters.create(
    body=None,
    to=None,
    _from=None,
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    mail_type="usps_first_class",
    merge_variables={},
    send_date="string_example",
    file=None,
    extra_service="certified",
    cards=["card_C"],
    color=None,
    double_sided=True,
    address_placement="top_first_page",
    return_envelope=None,
    perforated_page=1,
    custom_envelope="env_C",
    billing_group_id="string_example",
    qr_code={
        "position": "relative",
        "redirect_url": "redirect_url_example",
        "width": "width_example",
    },
    use_type="marketing",
    fsc=False,
    size="us_letter",
    idempotency_key="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    idempotency_key2="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    lob_version="2024-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### to: Union[`AdrId`, `InlineAddress`]<a id="to-unionadrid-inlineaddress"></a>


Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your <a href=\\\"https://dashboard.lob.com/#/settings/editions\\\" target=\\\"_blank\\\">Print & Mail Edition</a>, US addresses may also be run through <a href=\\\"#tag/National-Change-of-Address\\\">National Change of Address Linkage(NCOALink)</a>. Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account’s <a href=\\\"https://dashboard.lob.com/#/settings/account\\\" target=\\\"_blank\\\">US Mail strictness setting</a>, the request will fail. <a href=\\\"https://help.lob.com/print-and-mail/all-about-addresses\\\" target=\\\"_blank\\\">Lob Guide: Verification of Mailing Addresses</a>

##### _from: Union[`AdrId`, `InlineAddress`]<a id="_from-unionadrid-inlineaddress"></a>


Must either be an address ID or an inline object with correct address parameters. Must be a US address unless using a `custom_envelope`. All addresses will be standardized into uppercase without being modified by verification.

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### mail_type: [`MailType`](./lob_python_sdk/type/mail_type.py)<a id="mail_type-mailtypelob_python_sdktypemail_typepy"></a>

##### merge_variables: [`MergeVariables`](./lob_python_sdk/type/merge_variables.py)<a id="merge_variables-mergevariableslob_python_sdktypemerge_variablespy"></a>


##### send_date: `SendDate`<a id="send_date-senddate"></a>

##### file: `LtrFile`<a id="file-ltrfile"></a>

##### extra_service: [`ExtraService`](./lob_python_sdk/type/extra_service.py)<a id="extra_service-extraservicelob_python_sdktypeextra_servicepy"></a>

##### cards: List[`CardId`]<a id="cards-listcardid"></a>

A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information. Not available for `us_legal` letter size.

##### color: Union[`bool`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lob_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="color-unionbool-unionbool-date-datetime-dict-float-int-list-str-nonelob_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### double_sided: `bool`<a id="double_sided-bool"></a>

Set this attribute to `true` for double sided printing, or `false` for for single sided printing. Defaults to `true`.

##### address_placement: [`AddressPlacement`](./lob_python_sdk/type/address_placement.py)<a id="address_placement-addressplacementlob_python_sdktypeaddress_placementpy"></a>

##### return_envelope: `ReturnEnvelopeUserProvided`<a id="return_envelope-returnenvelopeuserprovided"></a>

##### perforated_page: `Optional[int]`<a id="perforated_page-optionalint"></a>

Required if `return_envelope` is `true`. The number of the page that should be perforated for use with the return envelope. Must be greater than or equal to `1`. The blank page added by `address_placement=insert_blank_page` will be ignored when considering the perforated page number. To see how perforation will impact your letter design, view our <a href=\\\"https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/letter_perf_template.pdf\\\" target=\\\"_blank\\\">perforation guide</a>.

##### custom_envelope: [`UserProvided`](./lob_python_sdk/type/user_provided.py)<a id="custom_envelope-userprovidedlob_python_sdktypeuser_providedpy"></a>

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

##### qr_code: [`QrCode`](./lob_python_sdk/type/qr_code.py)<a id="qr_code-qrcodelob_python_sdktypeqr_codepy"></a>


##### use_type: [`LtrUseType`](./lob_python_sdk/type/ltr_use_type.py)<a id="use_type-ltrusetypelob_python_sdktypeltr_use_typepy"></a>

##### fsc: `bool`<a id="fsc-bool"></a>

This is in beta. Contact support@lob.com or your account contact to learn more. Not available for `A4` and `us_legal` letter size.

##### size: [`LtrSize`](./lob_python_sdk/type/ltr_size.py)<a id="size-ltrsizelob_python_sdktypeltr_sizepy"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### idempotency_key2: `str`<a id="idempotency_key2-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### lob_version: `str`<a id="lob_version-str"></a>

A string representing the version of the API being used. For more information on versioning, refer to our [Versioning and Changelog](https://docs.lob.com/#tag/Versioning-and-Changelog) documentation. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LetterEditable`](./lob_python_sdk/type/letter_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Letter`](./lob_python_sdk/pydantic/letter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/letters` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.letters.list`<a id="lobletterslist"></a>

Returns a list of your letters. The letters are returned sorted by creation date, with the most recently created letters appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.letters.list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
    campaign_id="camp_u2LC4",
    status="processed",
    color=True,
    scheduled=True,
    send_date="string_example",
    mail_type="usps_first_class",
    sort_by=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

##### campaign_id: [`CampaignId`](./lob_python_sdk/type/.py)<a id="campaign_id-campaignidlob_python_sdktypepy"></a>

Filters resources created by the provided campaign id, prefixed with `cmp_`.

##### status: [`Status`](./lob_python_sdk/type/.py)<a id="status-statuslob_python_sdktypepy"></a>

A string describing the render status: * `processed` - the rendering process is currently underway. * `rendered` - the rendering process has completed successfully. * `failed` - the rendering process has failed. 

##### color: `bool`<a id="color-bool"></a>

Set to `true` to return only color letters. Set to `false` to return only black & white letters.

##### scheduled: `bool`<a id="scheduled-bool"></a>

* `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created` 

##### send_date: `SendDate`<a id="send_date-senddate"></a>

Filter by ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. 

##### mail_type: [`MailType`](./lob_python_sdk/type/.py)<a id="mail_type-mailtypelob_python_sdktypepy"></a>

A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href=\"https://lob.com/pricing/print-mail#compare\" target=\"_blank\">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. 

##### sort_by: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="sort_by-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. 

#### 🔄 Return<a id="🔄-return"></a>

[`LettersListResponse`](./lob_python_sdk/pydantic/letters_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/letters` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.letters.retrieve`<a id="loblettersretrieve"></a>

Retrieves the details of an existing letter. You need only supply the unique letter identifier that was returned upon letter creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.letters.retrieve(
    ltr_id="ltr_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ltr_id: [`LtrId`](./lob_python_sdk/type/.py)<a id="ltr_id-ltridlob_python_sdktypepy"></a>

id of the letter

#### 🔄 Return<a id="🔄-return"></a>

[`Letter`](./lob_python_sdk/pydantic/letter.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/letters/{ltr_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.lob_credits.get_credits_balance`<a id="loblob_creditsget_credits_balance"></a>

Returns the account's current balance of Lob Credits.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_credits_balance_response = lob.lob_credits.get_credits_balance()
```

#### 🔄 Return<a id="🔄-return"></a>

[`LobCreditsBalance`](./lob_python_sdk/pydantic/lob_credits_balance.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/accounts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.postcards.create`<a id="lobpostcardscreate"></a>

Creates a new postcard given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.postcards.create(
    body=None,
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    mail_type="usps_first_class",
    merge_variables={},
    send_date="string_example",
    items="4x6",
    to=None,
    _from=None,
    front=None,
    back=None,
    billing_group_id="string_example",
    qr_code={
        "position": "relative",
        "redirect_url": "redirect_url_example",
        "width": "width_example",
    },
    use_type="marketing",
    fsc=False,
    idempotency_key="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    idempotency_key2="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### mail_type: [`MailType`](./lob_python_sdk/type/mail_type.py)<a id="mail_type-mailtypelob_python_sdktypemail_typepy"></a>

##### merge_variables: [`MergeVariables`](./lob_python_sdk/type/merge_variables.py)<a id="merge_variables-mergevariableslob_python_sdktypemerge_variablespy"></a>


##### send_date: `SendDate`<a id="send_date-senddate"></a>

##### items: [`PostcardSize`](./lob_python_sdk/type/postcard_size.py)<a id="items-postcardsizelob_python_sdktypepostcard_sizepy"></a>

##### to: Union[`AdrId`, `InlineAddress`]<a id="to-unionadrid-inlineaddress"></a>


Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your <a href=\\\"https://dashboard.lob.com/#/settings/editions\\\" target=\\\"_blank\\\">Print & Mail Edition</a>, US addresses may also be run through <a href=\\\"#tag/National-Change-of-Address\\\">National Change of Address Linkage(NCOALink)</a>. Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account’s <a href=\\\"https://dashboard.lob.com/#/settings/account\\\" target=\\\"_blank\\\">US Mail strictness setting</a>, the request will fail. <a href=\\\"https://help.lob.com/print-and-mail/all-about-addresses\\\" target=\\\"_blank\\\">Lob Guide: Verification of Mailing Addresses</a>

##### _from: Union[`AdrId`, `InlineAddressUs`]<a id="_from-unionadrid-inlineaddressus"></a>


*Required* if `to` address is international. Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.

##### front: `PscFront`<a id="front-pscfront"></a>

##### back: `PscBack`<a id="back-pscback"></a>

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

##### qr_code: [`QrCode`](./lob_python_sdk/type/qr_code.py)<a id="qr_code-qrcodelob_python_sdktypeqr_codepy"></a>


##### use_type: [`PscUseType`](./lob_python_sdk/type/psc_use_type.py)<a id="use_type-pscusetypelob_python_sdktypepsc_use_typepy"></a>

##### fsc: `bool`<a id="fsc-bool"></a>

This is in beta. Contact support@lob.com or your account contact to learn more. Not available for `4x6` or `A5` postcard sizes.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### idempotency_key2: `str`<a id="idempotency_key2-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostcardEditable`](./lob_python_sdk/type/postcard_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Postcard`](./lob_python_sdk/pydantic/postcard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/postcards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.postcards.delete`<a id="lobpostcardsdelete"></a>

Completely removes a postcard from production. This can only be done if the postcard has a `send_date` and the `send_date` has not yet passed. If the postcard is successfully canceled, you will not be charged for it. Read more on [cancellation windows](#section/Cancellation-Windows) and [scheduling](#section/Scheduled-Mailings). Scheduling and cancellation is a premium feature. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.postcards.delete(
    psc_id="psc_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### psc_id: [`PscId`](./lob_python_sdk/type/.py)<a id="psc_id-pscidlob_python_sdktypepy"></a>

id of the postcard

#### 🔄 Return<a id="🔄-return"></a>

[`PostcardDeletion`](./lob_python_sdk/pydantic/postcard_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/postcards/{psc_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.postcards.list`<a id="lobpostcardslist"></a>

Returns a list of your postcards. The addresses are returned sorted by creation date, with the most recently created addresses appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.postcards.list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
    campaign_id="camp_u2LC4",
    status="processed",
    size=["string_example"],
    scheduled=True,
    send_date="string_example",
    mail_type="usps_first_class",
    sort_by=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

##### campaign_id: [`CampaignId`](./lob_python_sdk/type/.py)<a id="campaign_id-campaignidlob_python_sdktypepy"></a>

Filters resources created by the provided campaign id, prefixed with `cmp_`.

##### status: [`Status`](./lob_python_sdk/type/.py)<a id="status-statuslob_python_sdktypepy"></a>

A string describing the render status: * `processed` - the rendering process is currently underway. * `rendered` - the rendering process has completed successfully. * `failed` - the rendering process has failed. 

##### size: List[[`PostcardSize`](./lob_python_sdk/type/postcard_size.py)]<a id="size-listpostcardsizelob_python_sdktypepostcard_sizepy"></a>

Specifies the size of the postcard. Only `4x6` postcards can be sent to international destinations.

##### scheduled: `bool`<a id="scheduled-bool"></a>

* `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created` 

##### send_date: `SendDate`<a id="send_date-senddate"></a>

Filter by ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. 

##### mail_type: [`MailType`](./lob_python_sdk/type/.py)<a id="mail_type-mailtypelob_python_sdktypepy"></a>

A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href=\"https://lob.com/pricing/print-mail#compare\" target=\"_blank\">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. 

##### sort_by: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="sort_by-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. 

#### 🔄 Return<a id="🔄-return"></a>

[`PostcardsListResponse`](./lob_python_sdk/pydantic/postcards_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/postcards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.postcards.retrieve`<a id="lobpostcardsretrieve"></a>

Retrieves the details of an existing postcard. You need only supply the unique customer identifier that was returned upon postcard creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.postcards.retrieve(
    psc_id="psc_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### psc_id: [`PscId`](./lob_python_sdk/type/.py)<a id="psc_id-pscidlob_python_sdktypepy"></a>

id of the postcard

#### 🔄 Return<a id="🔄-return"></a>

[`Postcard`](./lob_python_sdk/pydantic/postcard.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/postcards/{psc_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.qr_codes.get_sorted_qr_codes`<a id="lobqr_codesget_sorted_qr_codes"></a>

Returns a list of your QR codes. The QR codes are returned sorted by scan date, with the most recently scanned QR codes appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sorted_qr_codes_response = lob.qr_codes.get_sorted_qr_codes(
    limit=10,
    offset=0,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    scanned=True,
    resource_ids=[],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### scanned: `bool`<a id="scanned-bool"></a>

Filter list of responses to only include QR codes with at least one scan event.

##### resource_ids: [`list`](./lob_python_sdk/type/.py)<a id="resource_ids-listlob_python_sdktypepy"></a>

Filter by the resource ID.

#### 🔄 Return<a id="🔄-return"></a>

[`QrCodesGetSortedQrCodesResponse`](./lob_python_sdk/pydantic/qr_codes_get_sorted_qr_codes_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/qr_code_analytics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.reverse_geocode_lookups.us_location_with_live_api_key`<a id="lobreverse_geocode_lookupsus_location_with_live_api_key"></a>

Reverse geocode a valid US location with a live API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
us_location_with_live_api_key_response = (
    lob.reverse_geocode_lookups.us_location_with_live_api_key(
        latitude=-90,
        longitude=-180,
        size=5,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### latitude: `Optional[Union[int, float]]`<a id="latitude-optionalunionint-float"></a>

A positive or negative decimal indicating the geographic latitude of the address, specifying the north-to-south position of a location. This should be input with `longitude` to pinpoint locations on a map. 

##### longitude: `Optional[Union[int, float]]`<a id="longitude-optionalunionint-float"></a>

A positive or negative decimal indicating the geographic longitude of the address, specifying the north-to-south position of a location. This should be input with `latitude` to pinpoint locations on a map. 

##### size: `int`<a id="size-int"></a>

Determines the number of locations returned. Possible values are between 1 and 50 and any number higher will be rounded down to 50. Default size is a list of 5 reverse geocoded locations.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Location`](./lob_python_sdk/type/location.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ReverseGeocode`](./lob_python_sdk/pydantic/reverse_geocode.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/us_reverse_geocode_lookups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.self_mailers.create_new_self_mailer`<a id="lobself_mailerscreate_new_self_mailer"></a>

Creates a new self_mailer given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_self_mailer_response = lob.self_mailers.create_new_self_mailer(
    body=None,
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    mail_type="usps_first_class",
    merge_variables={},
    send_date="string_example",
    items="6x18_bifold",
    to=None,
    _from=None,
    inside=None,
    outside=None,
    billing_group_id="string_example",
    qr_code={
        "position": "relative",
        "redirect_url": "redirect_url_example",
        "width": "width_example",
    },
    use_type="marketing",
    fsc=False,
    idempotency_key="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    idempotency_key2="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### mail_type: [`MailType`](./lob_python_sdk/type/mail_type.py)<a id="mail_type-mailtypelob_python_sdktypemail_typepy"></a>

##### merge_variables: [`MergeVariables`](./lob_python_sdk/type/merge_variables.py)<a id="merge_variables-mergevariableslob_python_sdktypemerge_variablespy"></a>


##### send_date: `SendDate`<a id="send_date-senddate"></a>

##### items: [`SelfMailerSize`](./lob_python_sdk/type/self_mailer_size.py)<a id="items-selfmailersizelob_python_sdktypeself_mailer_sizepy"></a>

##### to: Union[`AdrId`, `InlineAddress`]<a id="to-unionadrid-inlineaddress"></a>


Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your <a href=\\\"https://dashboard.lob.com/#/settings/editions\\\" target=\\\"_blank\\\">Print & Mail Edition</a>, US addresses may also be run through <a href=\\\"#tag/National-Change-of-Address\\\">National Change of Address Linkage(NCOALink)</a>. Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account’s <a href=\\\"https://dashboard.lob.com/#/settings/account\\\" target=\\\"_blank\\\">US Mail strictness setting</a>, the request will fail. <a href=\\\"https://help.lob.com/print-and-mail/all-about-addresses\\\" target=\\\"_blank\\\">Lob Guide: Verification of Mailing Addresses</a>

##### _from: Union[`AdrId`, `InlineAddressUs`]<a id="_from-unionadrid-inlineaddressus"></a>


*Required* if `to` address is international. Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.

##### inside: Union[`HtmlString`, `TmplId`, `RemoteFileUrl`, `LocalFilePath`]<a id="inside-unionhtmlstring-tmplid-remotefileurl-localfilepath"></a>


The artwork to use as the inside of your self mailer.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 6\\\"x18\\\" at 300 DPI, while supplied HTML will be rendered to the specified `size`. - Be sure to leave room for address and postage information by following the templates provided here:   - <a href=\\\"https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/6x18_sfm_bifold_template.pdf\\\" target=\\\"_blank\\\">6x18 bifold template</a>   - <a href=\\\"https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/12x9_sfm_bifold_template.pdf\\\" target=\\\"_blank\\\">12x9 bifold template</a>   - <a href=\\\"https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/self_mailers/17_75x9_trifold_sfm_template.pdf\\\" target=\\\"_blank\\\">17.75x9 trifold template</a>   See [here](#section/HTML-Examples) for HTML examples. 

##### outside: Union[`HtmlString`, `TmplId`, `RemoteFileUrl`, `LocalFilePath`]<a id="outside-unionhtmlstring-tmplid-remotefileurl-localfilepath"></a>


The artwork to use as the outside of your self mailer.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 6\\\"x18\\\" at 300 DPI, while supplied HTML will be rendered to the specified `size`.  See [here](#section/HTML-Examples) for HTML examples. 

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

##### qr_code: [`QrCode`](./lob_python_sdk/type/qr_code.py)<a id="qr_code-qrcodelob_python_sdktypeqr_codepy"></a>


##### use_type: [`SfmUseType`](./lob_python_sdk/type/sfm_use_type.py)<a id="use_type-sfmusetypelob_python_sdktypesfm_use_typepy"></a>

##### fsc: `bool`<a id="fsc-bool"></a>

This is in beta. Contact support@lob.com or your account contact to learn more. Not available for `11x9_bifold` self-mailer size.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### idempotency_key2: `str`<a id="idempotency_key2-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SelfMailerEditable`](./lob_python_sdk/type/self_mailer_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SelfMailer`](./lob_python_sdk/pydantic/self_mailer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/self_mailers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.self_mailers.get_details`<a id="lobself_mailersget_details"></a>

Retrieves the details of an existing self_mailer. You need only supply the unique self_mailer identifier that was returned upon self_mailer creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = lob.self_mailers.get_details(
    sfm_id="sfm_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sfm_id: [`SfmId`](./lob_python_sdk/type/.py)<a id="sfm_id-sfmidlob_python_sdktypepy"></a>

id of the self_mailer

#### 🔄 Return<a id="🔄-return"></a>

[`SelfMailer`](./lob_python_sdk/pydantic/self_mailer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/self_mailers/{sfm_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.self_mailers.get_list`<a id="lobself_mailersget_list"></a>

Returns a list of your self_mailers. The self_mailers are returned sorted by creation date, with the most recently created self_mailers appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lob.self_mailers.get_list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
    size=["string_example"],
    scheduled=True,
    send_date="string_example",
    mail_type="usps_first_class",
    sort_by=None,
    campaign_id="camp_u2LC4",
    status="processed",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

##### size: List[[`SelfMailerSize`](./lob_python_sdk/type/self_mailer_size.py)]<a id="size-listselfmailersizelob_python_sdktypeself_mailer_sizepy"></a>

The self mailer sizes to be returned.

##### scheduled: `bool`<a id="scheduled-bool"></a>

* `true` - only return orders (past or future) where `send_date` is greater than `date_created` * `false` - only return orders where `send_date` is equal to `date_created` 

##### send_date: `SendDate`<a id="send_date-senddate"></a>

Filter by ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤. 

##### mail_type: [`MailType`](./lob_python_sdk/type/.py)<a id="mail_type-mailtypelob_python_sdktypepy"></a>

A string designating the mail postage type: * `usps_first_class` - (default) * `usps_standard` - a <a href=\"https://lob.com/pricing/print-mail#compare\" target=\"_blank\">cheaper option</a> which is less predictable and takes longer to deliver. `usps_standard` cannot be used with `4x6` postcards or for any postcards sent outside of the United States. 

##### sort_by: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="sort_by-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


Sorts items by ascending or descending dates. Use either `date_created` or `send_date`, not both. 

##### campaign_id: [`CampaignId`](./lob_python_sdk/type/.py)<a id="campaign_id-campaignidlob_python_sdktypepy"></a>

Filters resources created by the provided campaign id, prefixed with `cmp_`.

##### status: [`Status`](./lob_python_sdk/type/.py)<a id="status-statuslob_python_sdktypepy"></a>

A string describing the render status: * `processed` - the rendering process is currently underway. * `rendered` - the rendering process has completed successfully. * `failed` - the rendering process has failed. 

#### 🔄 Return<a id="🔄-return"></a>

[`SelfMailersGetListResponse`](./lob_python_sdk/pydantic/self_mailers_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/self_mailers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.self_mailers.remove_self_mailer`<a id="lobself_mailersremove_self_mailer"></a>

Completely removes a self mailer from production. This can only be done if the self mailer's `send_date` has not yet passed. If the self mailer is successfully canceled, you will not be charged for it. This feature is exclusive to certain customers. Upgrade to the appropriate <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a> to gain access.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_self_mailer_response = lob.self_mailers.remove_self_mailer(
    sfm_id="sfm_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### sfm_id: [`SfmId`](./lob_python_sdk/type/.py)<a id="sfm_id-sfmidlob_python_sdktypepy"></a>

id of the self_mailer

#### 🔄 Return<a id="🔄-return"></a>

[`SelfMailerDeletion`](./lob_python_sdk/pydantic/self_mailer_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/self_mailers/{sfm_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.snap_packs.create_new_snap_pack`<a id="lobsnap_packscreate_new_snap_pack"></a>

Creates a new snap_pack given information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_snap_pack_response = lob.snap_packs.create_new_snap_pack(
    body=None,
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    mail_type="usps_first_class",
    merge_variables={},
    send_date="string_example",
    size="8.5x11",
    to=None,
    _from=None,
    inside=None,
    outside=None,
    billing_group_id="string_example",
    use_type="marketing",
    color=None,
    idempotency_key="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
    idempotency_key2="026e7634-24d7-486c-a0bb-4a17fd0eebc5",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### mail_type: [`MailType`](./lob_python_sdk/type/mail_type.py)<a id="mail_type-mailtypelob_python_sdktypemail_typepy"></a>

##### merge_variables: [`MergeVariables`](./lob_python_sdk/type/merge_variables.py)<a id="merge_variables-mergevariableslob_python_sdktypemerge_variablespy"></a>


##### send_date: `SendDate`<a id="send_date-senddate"></a>

##### size: [`SnapPackSize`](./lob_python_sdk/type/snap_pack_size.py)<a id="size-snappacksizelob_python_sdktypesnap_pack_sizepy"></a>

##### to: Union[`AdrId`, `InlineAddress`]<a id="to-unionadrid-inlineaddress"></a>


Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your <a href=\\\"https://dashboard.lob.com/#/settings/editions\\\" target=\\\"_blank\\\">Print & Mail Edition</a>, US addresses may also be run through <a href=\\\"#tag/National-Change-of-Address\\\">National Change of Address Linkage(NCOALink)</a>. Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account’s <a href=\\\"https://dashboard.lob.com/#/settings/account\\\" target=\\\"_blank\\\">US Mail strictness setting</a>, the request will fail. <a href=\\\"https://help.lob.com/print-and-mail/all-about-addresses\\\" target=\\\"_blank\\\">Lob Guide: Verification of Mailing Addresses</a>

##### _from: Union[`AdrId`, `InlineAddressUs`]<a id="_from-unionadrid-inlineaddressus"></a>


*Required* if `to` address is international. Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.

##### inside: Union[`HtmlString`, `TmplId`, `RemoteFileUrl`, `LocalFilePath`]<a id="inside-unionhtmlstring-tmplid-remotefileurl-localfilepath"></a>


The artwork to use as the inside of your snap pack.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 8.5\\\"x11\\\" at 300 DPI, while supplied HTML will be rendered to the specified `size`. - Be sure to leave room for address and postage information by following the template provided here:   - <a href=\\\"https://s3.us-west-2.amazonaws.com/public.lob.com/assets/8.5x11_Snappack_template_address.pdf\\\" target=\\\"_blank\\\">8.5x11 snap pack template</a>   See [here](#section/HTML-Examples) for HTML examples. 

##### outside: Union[`HtmlString`, `TmplId`, `RemoteFileUrl`, `LocalFilePath`]<a id="outside-unionhtmlstring-tmplid-remotefileurl-localfilepath"></a>


The artwork to use as the outside of your snap pack.  Notes: - HTML merge variables should not include delimiting whitespace. - PDF, PNG, and JPGs must be sized at 6\\\"x18\\\" at 300 DPI, while supplied HTML will be rendered to the specified `size`.  See [here](#section/HTML-Examples) for HTML examples. 

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

##### use_type: [`SnapPackUseType`](./lob_python_sdk/type/snap_pack_use_type.py)<a id="use_type-snappackusetypelob_python_sdktypesnap_pack_use_typepy"></a>

##### color: Union[`bool`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lob_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="color-unionbool-unionbool-date-datetime-dict-float-int-list-str-nonelob_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### idempotency_key: `str`<a id="idempotency_key-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

##### idempotency_key2: `str`<a id="idempotency_key2-str"></a>

A string of no longer than 256 characters that uniquely identifies this resource. For more help integrating idempotency keys, refer to our <a href=\"https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings#idempotent-requests-12\" target=\"_blank\">implementation guide</a>. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SnapPackEditable`](./lob_python_sdk/type/snap_pack_editable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SnapPack`](./lob_python_sdk/pydantic/snap_pack.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/snap_packs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.template_versions.create_new_version`<a id="lobtemplate_versionscreate_new_version"></a>

Creates a new template version attached to the specified template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_version_response = lob.template_versions.create_new_version(
    html="string_example",
    tmpl_id="tmpl_C",
    description="Harry - Office",
    engine="legacy",
    required_vars=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### html: [`TemplateHtml`](./lob_python_sdk/type/template_html.py)<a id="html-templatehtmllob_python_sdktypetemplate_htmlpy"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

The ID of the template the new version will be attached to

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### engine: [`Engine`](./lob_python_sdk/type/engine.py)<a id="engine-enginelob_python_sdktypeenginepy"></a>

##### required_vars: [`TemplateRequiredVars`](./lob_python_sdk/type/template_required_vars.py)<a id="required_vars-templaterequiredvarslob_python_sdktypetemplate_required_varspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TemplateVersionWritable`](./lob_python_sdk/type/template_version_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TemplateVersion`](./lob_python_sdk/pydantic/template_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}/versions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.template_versions.delete_version`<a id="lobtemplate_versionsdelete_version"></a>

Permanently deletes a template version. A template's `published_version` can not be deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_version_response = lob.template_versions.delete_version(
    tmpl_id="tmpl_C",
    vrsn_id="vrsn_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

The ID of the template to which the version belongs.

##### vrsn_id: [`VrsnId`](./lob_python_sdk/type/.py)<a id="vrsn_id-vrsnidlob_python_sdktypepy"></a>

id of the template_version

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateVersionDeletion`](./lob_python_sdk/pydantic/template_version_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}/versions/{vrsn_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.template_versions.get`<a id="lobtemplate_versionsget"></a>

Retrieves the template version with the given template and version ids.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = lob.template_versions.get(
    tmpl_id="tmpl_C",
    vrsn_id="vrsn_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

The ID of the template to which the version belongs.

##### vrsn_id: [`VrsnId`](./lob_python_sdk/type/.py)<a id="vrsn_id-vrsnidlob_python_sdktypepy"></a>

id of the template_version

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateVersion`](./lob_python_sdk/pydantic/template_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}/versions/{vrsn_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.template_versions.get_list`<a id="lobtemplate_versionsget_list"></a>

Returns a list of template versions for the given template ID. The template versions are sorted by creation date, with the most recently created appearing first.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = lob.template_versions.get_list(
    tmpl_id="tmpl_C",
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

The ID of the template associated with the retrieved versions

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateVersionsGetListResponse`](./lob_python_sdk/pydantic/template_versions_get_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}/versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.template_versions.update_template_version`<a id="lobtemplate_versionsupdate_template_version"></a>

Updates the template version with the given template and version ids.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_template_version_response = lob.template_versions.update_template_version(
    tmpl_id="tmpl_C",
    vrsn_id="vrsn_C",
    description="Harry - Office",
    engine="legacy",
    required_vars=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

The ID of the template to which the version belongs.

##### vrsn_id: [`VrsnId`](./lob_python_sdk/type/.py)<a id="vrsn_id-vrsnidlob_python_sdktypepy"></a>

id of the template_version

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### engine: [`Engine`](./lob_python_sdk/type/engine.py)<a id="engine-enginelob_python_sdktypeenginepy"></a>

##### required_vars: [`TemplateRequiredVars`](./lob_python_sdk/type/template_required_vars.py)<a id="required_vars-templaterequiredvarslob_python_sdktypetemplate_required_varspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TemplateVersionUpdatable`](./lob_python_sdk/type/template_version_updatable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TemplateVersion`](./lob_python_sdk/pydantic/template_version.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}/versions/{vrsn_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.templates.delete`<a id="lobtemplatesdelete"></a>

Permanently deletes a template. Deleting a template also deletes its associated versions. Deleted templates can not be used to create postcard, letter, or check resources.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.templates.delete(
    tmpl_id="tmpl_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

id of the template

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateDeletion`](./lob_python_sdk/pydantic/template_deletion.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.templates.list`<a id="lobtemplateslist"></a>

Returns a list of your templates. The templates are returned sorted by creation date, with the most recently created templates appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.templates.list(
    limit=10,
    before_after=None,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### before_after: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Union[Union[bool, date, datetime, dict, float, int, list, str, None], Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="before_after-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-unionunionbool-date-datetime-dict-float-int-list-str-none-unionbool-date-datetime-dict-float-int-list-str-none"></a>


`before` and `after` are both optional but only one of them can be in the query at a time. 

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

#### 🔄 Return<a id="🔄-return"></a>

[`TemplatesListResponse`](./lob_python_sdk/pydantic/templates_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.templates.retrieve`<a id="lobtemplatesretrieve"></a>

Retrieves the details of an existing template. You need only supply the unique template identifier that was returned upon template creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.templates.retrieve(
    tmpl_id="tmpl_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

id of the template

#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./lob_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.templates.template`<a id="lobtemplatestemplate"></a>

Creates a new template for use with the Print & Mail API. In Live mode, you can only have as many non-deleted templates as allotted in your current <a href="https://dashboard.lob.com/#/settings/editions" target="_blank">Print & Mail Edition</a>. If you attempt to create a template past your limit, you will receive a `403` error. There is no limit in Test mode.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
template_response = lob.templates.template(
    html="string_example",
    description="Harry - Office",
    metadata={
        "key": "string_example",
    },
    engine="legacy",
    required_vars=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### html: [`TemplateHtml`](./lob_python_sdk/type/template_html.py)<a id="html-templatehtmllob_python_sdktypetemplate_htmlpy"></a>

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### metadata: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata-metadatalob_python_sdktypemetadatapy"></a>

##### engine: [`Engine`](./lob_python_sdk/type/engine.py)<a id="engine-enginelob_python_sdktypeenginepy"></a>

##### required_vars: [`TemplateRequiredVars`](./lob_python_sdk/type/template_required_vars.py)<a id="required_vars-templaterequiredvarslob_python_sdktypetemplate_required_varspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TemplateWritable`](./lob_python_sdk/type/template_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./lob_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.templates.update`<a id="lobtemplatesupdate"></a>

Updates the description and/or published version of the template with the given id. To update the template's html, create a new version of the template.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.templates.update(
    tmpl_id="tmpl_C",
    description="Harry - Office",
    published_version=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tmpl_id: [`TmplId`](./lob_python_sdk/type/.py)<a id="tmpl_id-tmplidlob_python_sdktypepy"></a>

id of the template

##### description: [`ResourceDescription`](./lob_python_sdk/type/resource_description.py)<a id="description-resourcedescriptionlob_python_sdktyperesource_descriptionpy"></a>

##### published_version: Union[`str`, `VrsnId`]<a id="published_version-unionstr-vrsnid"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TemplateUpdate`](./lob_python_sdk/type/template_update.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Template`](./lob_python_sdk/pydantic/template.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{tmpl_id}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.bulk_shorten_links`<a id="loburl_shortenerbulk_shorten_links"></a>

Shortens a list of links in a single request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_shorten_links_response = lob.url_shortener.bulk_shorten_links(
    body=[
        [
            {"redirect_link": "https://www.lob.com", "slug": "a1b2c3"},
            {"redirect_link": "https://www.lob.com", "slug": "a1b2c3"},
        ]
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LinkList`](./lob_python_sdk/type/link_list.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LinksResponse`](./lob_python_sdk/pydantic/links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/shorten/bulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.create`<a id="loburl_shortenercreate"></a>

Add a new custom domain that can be used to create custom links.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.url_shortener.create(
    domain="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain: `str`<a id="domain-str"></a>

The registered domain/hostname.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Domains`](./lob_python_sdk/type/domains.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DomainResponse`](./lob_python_sdk/pydantic/domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.create_0`<a id="loburl_shortenercreate_0"></a>

Given a long URL, shorten your URL either by using a custom domain or Lob's own short domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_0_response = lob.url_shortener.create_0(
    redirect_link="string_example",
    domain="string_example",
    slug="string_example",
    metadata_tag={
        "key": "string_example",
    },
    billing_group_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### redirect_link: `str`<a id="redirect_link-str"></a>

The original target URL.

##### domain: `str`<a id="domain-str"></a>

The registered domain to be used for the short URL.

##### slug: `str`<a id="slug-str"></a>

The unique path for the shortened URL, if empty a unique path will be used.

##### metadata_tag: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata_tag-metadatalob_python_sdktypemetadatapy"></a>

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LinkSingle`](./lob_python_sdk/type/link_single.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./lob_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/shorten` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.delete`<a id="loburl_shortenerdelete"></a>

Delete a registered domain. This operation can only be performed if all associated links with the domain are deleted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_response = lob.url_shortener.delete(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

Unique identifier for a domain.

#### 🔄 Return<a id="🔄-return"></a>

[`DomainResponse`](./lob_python_sdk/pydantic/domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.delete_0`<a id="loburl_shortenerdelete_0"></a>

Delete the shortened link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_0_response = lob.url_shortener.delete_0(
    link_id="link_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_id: `str`<a id="link_id-str"></a>

Unique identifier for a link.

#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./lob_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.delete_all_links_for_domain`<a id="loburl_shortenerdelete_all_links_for_domain"></a>

Delete all associated links for a domain

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_all_links_for_domain_response = lob.url_shortener.delete_all_links_for_domain(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

Unique identifier for a domain.

#### 🔄 Return<a id="🔄-return"></a>

[`DomainsResponse`](./lob_python_sdk/pydantic/domains_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}/links` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.get`<a id="loburl_shortenerget"></a>

Retrieve details for a single domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = lob.url_shortener.get(
    domain_id="domain_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### domain_id: `str`<a id="domain_id-str"></a>

Unique identifier for a domain.

#### 🔄 Return<a id="🔄-return"></a>

[`DomainResponse`](./lob_python_sdk/pydantic/domain_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains/{domain_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.get_0`<a id="loburl_shortenerget_0"></a>

Retrievs a single shortened link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_0_response = lob.url_shortener.get_0(
    link_id="link_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link_id: `str`<a id="link_id-str"></a>

Unique identifier for a link.

#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./lob_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.list`<a id="loburl_shortenerlist"></a>

Retrieve a list of all created domains.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.url_shortener.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DomainsResponse`](./lob_python_sdk/pydantic/domains_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/domains` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.list_0`<a id="loburl_shortenerlist_0"></a>

Retrieves a list of shortened links. The list is sorted by  creation date, with the most recently created appearing first.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_0_response = lob.url_shortener.list_0(
    limit=10,
    offset=0,
    include=["string_example"],
    date_created={
        "key": "string_example",
    },
    metadata={
        "key": "string_example",
    },
    campaign_id="cmp_C",
    clicked=True,
    billing_group_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

##### include: List[`str`]<a id="include-liststr"></a>

Request that the response include the total count by specifying `include=[\"total_count\"]`. 

##### date_created: [`DateFilter`](./lob_python_sdk/type/.py)<a id="date_created-datefilterlob_python_sdktypepy"></a>

Filter by date created. Accepted formats are ISO-8601 date or datetime, e.g. `{ \"gt\": \"2012-01-01\", \"lt\": \"2012-01-31T12:34:56Z\" }` where `gt` is >, `lt` is <, `gte` is ≥, and `lte` is ≤.

##### metadata: [`Metadata`](./lob_python_sdk/type/.py)<a id="metadata-metadatalob_python_sdktypepy"></a>

Filter by metadata key-value pair`.

##### campaign_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="campaign_id-cmpidlob_python_sdktypepy"></a>

Filter the links generated for a particular campaign using its campaign id.

##### clicked: `bool`<a id="clicked-bool"></a>

Retrieve the list of links that have been opened.

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

Filter the links generated for a particular billing group id.

#### 🔄 Return<a id="🔄-return"></a>

[`LinksResponse`](./lob_python_sdk/pydantic/links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.url_shortener.update`<a id="loburl_shortenerupdate"></a>

Update any of the properties of a shortened link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.url_shortener.update(
    redirect_link="string_example",
    link_id="link_id_example",
    domain="string_example",
    slug="string_example",
    metadata_tag={
        "key": "string_example",
    },
    billing_group_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### redirect_link: `str`<a id="redirect_link-str"></a>

The original target URL.

##### link_id: `str`<a id="link_id-str"></a>

Unique identifier for a link.

##### domain: `str`<a id="domain-str"></a>

The registered domain to be used for the short URL.

##### slug: `str`<a id="slug-str"></a>

The unique path for the shortened URL, if empty a unique path will be used.

##### metadata_tag: [`Metadata`](./lob_python_sdk/type/metadata.py)<a id="metadata_tag-metadatalob_python_sdktypemetadatapy"></a>

##### billing_group_id: `str`<a id="billing_group_id-str"></a>

An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\\\"#tag/Billing-Groups\\\">Billing Group API</a> for more information.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LinkSingle`](./lob_python_sdk/type/link_single.py)
#### 🔄 Return<a id="🔄-return"></a>

[`LinkResponse`](./lob_python_sdk/pydantic/link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/links/{link_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.us_autocompletions.get_suggestions`<a id="lobus_autocompletionsget_suggestions"></a>

Given an address prefix consisting of a partial primary line, as well as optional input of city, state, and zip code, this functionality returns up to 10 full US address suggestions. Not all of them will turn out to be valid addresses; they'll need to be [verified](#operation/verification_us).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_suggestions_response = lob.us_autocompletions.get_suggestions(
    address_prefix="string_example",
    city="string_example",
    state="string_example",
    zip_code="string_example",
    geo_ip_sort=True,
    case="upper",
    valid_addresses=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### address_prefix: `str`<a id="address_prefix-str"></a>

Only accepts numbers and street names in an alphanumeric format. 

##### city: `str`<a id="city-str"></a>

An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. 

##### state: `str`<a id="state-str"></a>

An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. 

##### zip_code: `str`<a id="zip_code-str"></a>

An optional ZIP Code input used to filter suggestions. Matches partial entries. 

##### geo_ip_sort: `bool`<a id="geo_ip_sort-bool"></a>

If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. 

##### case: `str`<a id="case-str"></a>

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. \"PO BOX\") and proper-cased (e.g. \"PO Box\"), respectively. Only affects `primary_line`, `city`, and `state`. Default casing is `upper`.

##### valid_addresses: `bool`<a id="valid_addresses-bool"></a>

Possible values are `true` and `false`. If false, not all of the suggestions in the response will be valid addresses; they'll need to be verified in order to determine the deliverability. The valid_addresses flag will greatly reduce the number of keystrokes needed before reaching an intended address.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsAutocompletionsWritable`](./lob_python_sdk/type/us_autocompletions_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsAutocompletions`](./lob_python_sdk/pydantic/us_autocompletions.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/us_autocompletions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.us_verifications.bulk_verify_addresses`<a id="lobus_verificationsbulk_verify_addresses"></a>

Verify a list of US or US territory addresses _with a live API key_. Requests to this endpoint with a test API key will return a dummy response based on the primary line you input.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
bulk_verify_addresses_response = lob.us_verifications.bulk_verify_addresses(
    addresses=[None],
    case="upper",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### addresses: List[`MultipleComponents`]<a id="addresses-listmultiplecomponents"></a>

##### case: `str`<a id="case-str"></a>

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. \"PO BOX\") and proper-cased (e.g. \"PO Box\"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MultipleComponentsList`](./lob_python_sdk/type/multiple_components_list.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsVerifications`](./lob_python_sdk/pydantic/us_verifications.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/bulk/us_verifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.us_verifications.verification`<a id="lobus_verificationsverification"></a>

Verify a US or US territory address _with a live API key_. The address can be in components (e.g. `primary_line` is "210 King Street", `zip_code` is "94107") or as a single string (e.g. "210 King Street 94107"), but not as both. Requests using a test API key validate required fields but return empty values unless specific `primary_line` values are provided. See the [US Verifications Test Environment](#section/US-Verifications-Test-Env) for details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verification_response = lob.us_verifications.verification(
    body=None,
    recipient="string_example",
    primary_line="string_example",
    secondary_line="string_example",
    urbanization="string_example",
    city=None,
    state="string_example",
    zip_code=None,
    address="string_example",
    case="upper",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### recipient: [`Recipient`](./lob_python_sdk/type/recipient.py)<a id="recipient-recipientlob_python_sdktyperecipientpy"></a>

##### primary_line: [`PrimaryLineUs`](./lob_python_sdk/type/primary_line_us.py)<a id="primary_line-primarylineuslob_python_sdktypeprimary_line_uspy"></a>

##### secondary_line: [`SecondaryLine`](./lob_python_sdk/type/secondary_line.py)<a id="secondary_line-secondarylinelob_python_sdktypesecondary_linepy"></a>

##### urbanization: [`Urbanization`](./lob_python_sdk/type/urbanization.py)<a id="urbanization-urbanizationlob_python_sdktypeurbanizationpy"></a>

##### city: Union[`CityNoDescription`, `str`]<a id="city-unioncitynodescription-str"></a>


##### state: `str`<a id="state-str"></a>

The <a href=\\\"https://en.wikipedia.org/wiki/ISO_3166-2:US\\\" target=\\\"_blank\\\">ISO 3166-2</a> two letter code or subdivision name for the state. `city` and `state` are required if no `zip_code` is passed.

##### zip_code: Union[[`Union[bool, date, datetime, dict, float, int, list, str, None]`](./lob_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py), `ZipCode`]<a id="zip_code-unionunionbool-date-datetime-dict-float-int-list-str-nonelob_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy-zipcode"></a>


##### address: `str`<a id="address-str"></a>

The entire address in one string (e.g., \\\"210 King Street 94107\\\"). _Does not support a recipient and will error when other payload parameters are provided._ 

##### case: `str`<a id="case-str"></a>

Casing of the verified address. Possible values are `upper` and `proper` for uppercased (e.g. \"PO BOX\") and proper-cased (e.g. \"PO Box\"), respectively. Only affects `recipient`, `primary_line`, `secondary_line`, `urbanization`, and `last_line`. Default casing is `upper`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsVerificationsWritable`](./lob_python_sdk/type/us_verifications_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsVerification`](./lob_python_sdk/pydantic/us_verification.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/us_verifications` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.create`<a id="lobuploadscreate"></a>

Creates a new upload with the provided properties.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = lob.uploads.create(
    campaign_id=None,
    required_address_column_mapping={
        "name": "name_example",
        "address_line1": "address_line1_example",
        "address_city": "address_city_example",
        "address_state": "address_state_example",
        "address_zip": "address_zip_example",
    },
    optional_address_column_mapping={
        "address_line2": "address_line2_example",
        "company": "company_example",
        "address_country": "address_country_example",
    },
    metadata={
        "columns": [],
    },
    merge_variable_column_mapping={
        "name": "recipient_name",
        "gift_code": "code",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### campaign_id: Union[`CmpId`, `str`]<a id="campaign_id-unioncmpid-str"></a>


##### required_address_column_mapping: [`RequiredAddressColumnMapping`](./lob_python_sdk/type/required_address_column_mapping.py)<a id="required_address_column_mapping-requiredaddresscolumnmappinglob_python_sdktyperequired_address_column_mappingpy"></a>


##### optional_address_column_mapping: [`OptionalAddressColumnMapping`](./lob_python_sdk/type/optional_address_column_mapping.py)<a id="optional_address_column_mapping-optionaladdresscolumnmappinglob_python_sdktypeoptional_address_column_mappingpy"></a>


##### metadata: [`UploadsMetadata`](./lob_python_sdk/type/uploads_metadata.py)<a id="metadata-uploadsmetadatalob_python_sdktypeuploads_metadatapy"></a>


##### merge_variable_column_mapping: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="merge_variable_column_mapping-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The mapping of column headers in your file to the merge variables present in your creative. See our <a href=\\\"https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#step-3-map-merge-variable-data-if-applicable-7\\\" target=\\\"_blank\\\">Campaign Audience Guide</a> for additional details. <br />If a merge variable has the same \\\"name\\\" as a \\\"key\\\" in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects, then they **CANNOT** have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects. If using customized QR code redirect from the Audience file, then a `qr_code_redirect_url` must be mapped to the column header as used in the CSV.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadWritable`](./lob_python_sdk/type/upload_writable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Upload`](./lob_python_sdk/pydantic/upload.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.create_export_file`<a id="lobuploadscreate_export_file"></a>

Campaign Exports can help you understand exactly which records in a campaign could not be created. By initiating and retrieving an export, you will get row-by-row errors for your campaign. For a step-by-step walkthrough of creating a campaign and exporting failures, see our [Campaigns Guide](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/launch-your-first-campaign).

Create an export file associated with an upload.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_export_file_response = lob.uploads.create_export_file(
    upl_id="upl_C",
    type="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

ID of the upload

##### type: `str`<a id="type-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadsCreateExportFileRequest`](./lob_python_sdk/type/uploads_create_export_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadCreateExport`](./lob_python_sdk/pydantic/upload_create_export.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}/exports` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.delete`<a id="lobuploadsdelete"></a>

Delete an existing upload. You need only supply the unique identifier that was returned upon upload creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lob.uploads.delete(
    upl_id="upl_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

id of the upload

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.file`<a id="lobuploadsfile"></a>

Upload an [audience file](https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide) and associate it with an upload.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
file_response = lob.uploads.file(
    upl_id="upl_C",
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

ID of the upload

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadFileRequest`](./lob_python_sdk/type/upload_file_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadFile`](./lob_python_sdk/pydantic/upload_file.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}/file` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.list`<a id="lobuploadslist"></a>

Returns a list of your uploads. Optionally, filter uploads by campaign.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = lob.uploads.list(
    campaign_id="cmp_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### campaign_id: [`CmpId`](./lob_python_sdk/type/.py)<a id="campaign_id-cmpidlob_python_sdktypepy"></a>

id of the campaign

#### 🔄 Return<a id="🔄-return"></a>

[`UploadsListResponse`](./lob_python_sdk/pydantic/uploads_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.retrieve`<a id="lobuploadsretrieve"></a>

Retrieves the details of an existing upload. You need only supply the unique upload identifier that was returned upon upload creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_response = lob.uploads.retrieve(
    upl_id="upl_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

id of the upload

#### 🔄 Return<a id="🔄-return"></a>

[`Upload`](./lob_python_sdk/pydantic/upload.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.retrieve_0`<a id="lobuploadsretrieve_0"></a>

Retrieves the line item data for each row from the csv file associated with the upload id record. NOTE: This endpoint is currently feature flagged. Please reach out to Lob's support team if you  would like access to this API endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_0_response = lob.uploads.retrieve_0(
    upl_id="upl_C",
    status="Validated",
    limit=10,
    offset=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

ID of the upload

##### status: `str`<a id="status-str"></a>

The status of line items to filter and retrieve. By default all line items are returned.

##### limit: `int`<a id="limit-int"></a>

How many results to return.

##### offset: `int`<a id="offset-int"></a>

An integer that designates the offset at which to begin returning results. Defaults to 0.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportRetrieveResponse`](./lob_python_sdk/pydantic/report_retrieve_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}/report` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.retrieve_1`<a id="lobuploadsretrieve_1"></a>

Retrieves the details of an existing export. You need only supply the unique export identifier that was returned upon export creation. If you try retrieving an export immediately after creating one (i.e., before we're done processing the export), you will get back an export object with `state = in_progress`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retrieve_1_response = lob.uploads.retrieve_1(
    upl_id="upl_C",
    ex_id="ex_C",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

ID of the upload

##### ex_id: [`ExId`](./lob_python_sdk/type/.py)<a id="ex_id-exidlob_python_sdktypepy"></a>

ID of the export

#### 🔄 Return<a id="🔄-return"></a>

[`ExportRetrieveResponse`](./lob_python_sdk/pydantic/export_retrieve_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}/exports/{ex_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.uploads.update`<a id="lobuploadsupdate"></a>

Update the details of an existing upload. You need only supply the unique identifier that was returned upon upload creation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_response = lob.uploads.update(
    upl_id="upl_C",
    original_filename="string_example",
    required_address_column_mapping={
        "name": "name_example",
        "address_line1": "address_line1_example",
        "address_city": "address_city_example",
        "address_state": "address_state_example",
        "address_zip": "address_zip_example",
    },
    optional_address_column_mapping={
        "address_line2": "address_line2_example",
        "company": "company_example",
        "address_country": "address_country_example",
    },
    metadata={
        "columns": [],
    },
    merge_variable_column_mapping={
        "name": "recipient_name",
        "gift_code": "code",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### upl_id: [`UplId`](./lob_python_sdk/type/.py)<a id="upl_id-uplidlob_python_sdktypepy"></a>

id of the upload

##### original_filename: `str`<a id="original_filename-str"></a>

Original filename provided when the upload is created.

##### required_address_column_mapping: [`RequiredAddressColumnMapping`](./lob_python_sdk/type/required_address_column_mapping.py)<a id="required_address_column_mapping-requiredaddresscolumnmappinglob_python_sdktyperequired_address_column_mappingpy"></a>


##### optional_address_column_mapping: [`OptionalAddressColumnMapping`](./lob_python_sdk/type/optional_address_column_mapping.py)<a id="optional_address_column_mapping-optionaladdresscolumnmappinglob_python_sdktypeoptional_address_column_mappingpy"></a>


##### metadata: [`UploadsMetadata`](./lob_python_sdk/type/uploads_metadata.py)<a id="metadata-uploadsmetadatalob_python_sdktypeuploads_metadatapy"></a>


##### merge_variable_column_mapping: `Optional[Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]]`<a id="merge_variable_column_mapping-optionaldictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

The mapping of column headers in your file to the merge variables present in your creative. See our <a href=\\\"https://help.lob.com/print-and-mail/building-a-mail-strategy/campaign-or-triggered-sends/campaign-audience-guide#step-3-map-merge-variable-data-if-applicable-7\\\" target=\\\"_blank\\\">Campaign Audience Guide</a> for additional details. <br />If a merge variable has the same \\\"name\\\" as a \\\"key\\\" in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects, then they **CANNOT** have a different value in this object. If a different value is provided, then when the campaign is processing it will get overwritten with the mapped value present in the `requiredAddressColumnMapping` or `optionalAddressColumnMapping` objects. If using customized QR code redirect from the Audience file, then a `qr_code_redirect_url` must be mapped to the column header as used in the CSV.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadUpdatable`](./lob_python_sdk/type/upload_updatable.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Upload`](./lob_python_sdk/pydantic/upload.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploads/{upl_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `lob.zip_lookups.lookup`<a id="lobzip_lookupslookup"></a>

Returns information about a ZIP code

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_response = lob.zip_lookups.lookup(
    zip_code="94107",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zip_code: `str`<a id="zip_code-str"></a>

A 5-digit ZIP code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Zip5`](./lob_python_sdk/type/zip5.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Zip`](./lob_python_sdk/pydantic/zip.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/us_zip_lookups` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
