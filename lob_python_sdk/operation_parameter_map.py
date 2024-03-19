operation_parameter_map = {
    '/accounts-GET': {
        'parameters': [
        ]
    },
    '/addresses-POST': {
        'parameters': [
            {
                'name': 'address_line1'
            },
            {
                'name': 'address_line2'
            },
            {
                'name': 'address_city'
            },
            {
                'name': 'address_state'
            },
            {
                'name': 'address_zip'
            },
        ]
    },
    '/addresses/{adr_id}-DELETE': {
        'parameters': [
            {
                'name': 'adr_id'
            },
        ]
    },
    '/addresses-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/addresses/{adr_id}-GET': {
        'parameters': [
            {
                'name': 'adr_id'
            },
        ]
    },
    '/bank_accounts-POST': {
        'parameters': [
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'signatory'
            },
            {
                'name': 'description'
            },
            {
                'name': 'check_template'
            },
            {
                'name': 'fractional_routing_number'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zipcode'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/bank_accounts/{bank_id}-DELETE': {
        'parameters': [
            {
                'name': 'bank_id'
            },
        ]
    },
    '/bank_accounts/{bank_id}-GET': {
        'parameters': [
            {
                'name': 'bank_id'
            },
        ]
    },
    '/bank_accounts-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/bank_accounts/{bank_id}/verify-POST': {
        'parameters': [
            {
                'name': 'amounts'
            },
            {
                'name': 'bank_id'
            },
        ]
    },
    '/billing_groups-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/billing_groups/{bg_id}-GET': {
        'parameters': [
            {
                'name': 'bg_id'
            },
        ]
    },
    '/billing_groups-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'date_modified'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/billing_groups/{bg_id}-POST': {
        'parameters': [
            {
                'name': 'bg_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/buckslips/{buckslip_id}/orders-POST': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'buckslip_id'
            },
        ]
    },
    '/buckslips/{buckslip_id}/orders-GET': {
        'parameters': [
            {
                'name': 'buckslip_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/buckslips-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'size'
            },
            {
                'name': 'front'
            },
            {
                'name': 'back'
            },
        ]
    },
    '/buckslips/{buckslip_id}-DELETE': {
        'parameters': [
            {
                'name': 'buckslip_id'
            },
        ]
    },
    '/buckslips-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/buckslips/{buckslip_id}-GET': {
        'parameters': [
            {
                'name': 'buckslip_id'
            },
        ]
    },
    '/buckslips/{buckslip_id}-PATCH': {
        'parameters': [
            {
                'name': 'buckslip_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'auto_reorder'
            },
            {
                'name': 'reorder_quantity'
            },
        ]
    },
    '/campaigns-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'schedule_type'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'description'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'target_delivery_date'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'cancel_window_campaign_minutes'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'auto_cancel_if_ncoa'
            },
            {
                'name': 'x-lang-output'
            },
        ]
    },
    '/campaigns/{cmp_id}-DELETE': {
        'parameters': [
            {
                'name': 'cmp_id'
            },
        ]
    },
    '/campaigns-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'include'
            },
            {
                'name': 'before/after'
            },
        ]
    },
    '/campaigns/{cmp_id}-GET': {
        'parameters': [
            {
                'name': 'cmp_id'
            },
        ]
    },
    '/campaigns/{cmp_id}/send-POST': {
        'parameters': [
            {
                'name': 'cmp_id'
            },
        ]
    },
    '/campaigns/{cmp_id}-PATCH': {
        'parameters': [
            {
                'name': 'cmp_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'schedule_type'
            },
            {
                'name': 'target_delivery_date'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'cancel_window_campaign_minutes'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'is_draft'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'auto_cancel_if_ncoa'
            },
        ]
    },
    '/cards/{card_id}/orders-POST': {
        'parameters': [
            {
                'name': 'quantity'
            },
            {
                'name': 'card_id'
            },
        ]
    },
    '/cards/{card_id}/orders-GET': {
        'parameters': [
            {
                'name': 'card_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/cards-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'size'
            },
            {
                'name': 'front'
            },
            {
                'name': 'back'
            },
        ]
    },
    '/cards/{card_id}-DELETE': {
        'parameters': [
            {
                'name': 'card_id'
            },
        ]
    },
    '/cards-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
        ]
    },
    '/cards/{card_id}-GET': {
        'parameters': [
            {
                'name': 'card_id'
            },
        ]
    },
    '/cards/{card_id}-POST': {
        'parameters': [
            {
                'name': 'card_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'auto_reorder'
            },
            {
                'name': 'reorder_quantity'
            },
        ]
    },
    '/checks/{chk_id}-DELETE': {
        'parameters': [
            {
                'name': 'chk_id'
            },
        ]
    },
    '/checks-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'merge_variables'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'check_number'
            },
            {
                'name': 'message'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'to'
            },
            {
                'name': 'from'
            },
            {
                'name': 'bank_account'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'logo'
            },
            {
                'name': 'check_bottom'
            },
            {
                'name': 'attachment'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/checks-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'scheduled'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/checks/{chk_id}-GET': {
        'parameters': [
            {
                'name': 'chk_id'
            },
        ]
    },
    '/creatives-POST': {
        'parameters': [
            {
                'name': 'resource_type'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'front'
            },
            {
                'name': 'back'
            },
            {
                'name': 'details'
            },
            {
                'name': 'description'
            },
            {
                'name': 'from'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'file'
            },
            {
                'name': 'inside'
            },
            {
                'name': 'outside'
            },
            {
                'name': 'x-lang-output'
            },
        ]
    },
    '/creatives/{crv_id}-GET': {
        'parameters': [
            {
                'name': 'crv_id'
            },
        ]
    },
    '/creatives/{crv_id}-PATCH': {
        'parameters': [
            {
                'name': 'crv_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'from'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/identity_validation-POST': {
        'parameters': [
            {
                'name': 'recipient'
            },
            {
                'name': 'primary_line'
            },
            {
                'name': 'secondary_line'
            },
            {
                'name': 'urbanization'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip_code'
            },
            {
                'name': 'company'
            },
        ]
    },
    '/intl_autocompletions-POST': {
        'parameters': [
            {
                'name': 'address_prefix'
            },
            {
                'name': 'country'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip_code'
            },
            {
                'name': 'geo_ip_sort'
            },
            {
                'name': 'x-lang-output'
            },
        ]
    },
    '/intl_verifications-POST': {
        'parameters': [
            {
                'name': 'recipient'
            },
            {
                'name': 'primary_line'
            },
            {
                'name': 'secondary_line'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'postal_code'
            },
            {
                'name': 'country'
            },
            {
                'name': 'address'
            },
            {
                'name': 'x-lang-output'
            },
        ]
    },
    '/bulk/intl_verifications-POST': {
        'parameters': [
            {
                'name': 'addresses'
            },
        ]
    },
    '/letters/{ltr_id}-DELETE': {
        'parameters': [
            {
                'name': 'ltr_id'
            },
        ]
    },
    '/letters-POST': {
        'parameters': [
            {
                'name': 'to'
            },
            {
                'name': 'from'
            },
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'merge_variables'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'file'
            },
            {
                'name': 'extra_service'
            },
            {
                'name': 'cards'
            },
            {
                'name': 'color'
            },
            {
                'name': 'double_sided'
            },
            {
                'name': 'address_placement'
            },
            {
                'name': 'return_envelope'
            },
            {
                'name': 'perforated_page'
            },
            {
                'name': 'custom_envelope'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'qr_code'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'fsc'
            },
            {
                'name': 'size'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'Lob-Version'
            },
        ]
    },
    '/letters-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'color'
            },
            {
                'name': 'scheduled'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/letters/{ltr_id}-GET': {
        'parameters': [
            {
                'name': 'ltr_id'
            },
        ]
    },
    '/accounts-GET': {
        'parameters': [
        ]
    },
    '/postcards-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'merge_variables'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'items'
            },
            {
                'name': 'to'
            },
            {
                'name': 'from'
            },
            {
                'name': 'front'
            },
            {
                'name': 'back'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'qr_code'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'fsc'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/postcards/{psc_id}-DELETE': {
        'parameters': [
            {
                'name': 'psc_id'
            },
        ]
    },
    '/postcards-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'size'
            },
            {
                'name': 'scheduled'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/postcards/{psc_id}-GET': {
        'parameters': [
            {
                'name': 'psc_id'
            },
        ]
    },
    '/qr_code_analytics-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'scanned'
            },
            {
                'name': 'resource_ids'
            },
        ]
    },
    '/us_reverse_geocode_lookups-POST': {
        'parameters': [
            {
                'name': 'latitude'
            },
            {
                'name': 'longitude'
            },
            {
                'name': 'size'
            },
        ]
    },
    '/self_mailers-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'merge_variables'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'items'
            },
            {
                'name': 'to'
            },
            {
                'name': 'from'
            },
            {
                'name': 'inside'
            },
            {
                'name': 'outside'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'qr_code'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'fsc'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/self_mailers/{sfm_id}-GET': {
        'parameters': [
            {
                'name': 'sfm_id'
            },
        ]
    },
    '/self_mailers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'size'
            },
            {
                'name': 'scheduled'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'status'
            },
        ]
    },
    '/self_mailers/{sfm_id}-DELETE': {
        'parameters': [
            {
                'name': 'sfm_id'
            },
        ]
    },
    '/snap_packs-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mail_type'
            },
            {
                'name': 'merge_variables'
            },
            {
                'name': 'send_date'
            },
            {
                'name': 'size'
            },
            {
                'name': 'to'
            },
            {
                'name': 'from'
            },
            {
                'name': 'inside'
            },
            {
                'name': 'outside'
            },
            {
                'name': 'billing_group_id'
            },
            {
                'name': 'use_type'
            },
            {
                'name': 'color'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/templates/{tmpl_id}/versions-POST': {
        'parameters': [
            {
                'name': 'html'
            },
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'engine'
            },
            {
                'name': 'required_vars'
            },
        ]
    },
    '/templates/{tmpl_id}/versions/{vrsn_id}-DELETE': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'vrsn_id'
            },
        ]
    },
    '/templates/{tmpl_id}/versions/{vrsn_id}-GET': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'vrsn_id'
            },
        ]
    },
    '/templates/{tmpl_id}/versions-GET': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
        ]
    },
    '/templates/{tmpl_id}/versions/{vrsn_id}-POST': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'vrsn_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'engine'
            },
            {
                'name': 'required_vars'
            },
        ]
    },
    '/templates/{tmpl_id}-DELETE': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
        ]
    },
    '/templates-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'before/after'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/templates/{tmpl_id}-GET': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
        ]
    },
    '/templates-POST': {
        'parameters': [
            {
                'name': 'html'
            },
            {
                'name': 'description'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'engine'
            },
            {
                'name': 'required_vars'
            },
        ]
    },
    '/templates/{tmpl_id}-POST': {
        'parameters': [
            {
                'name': 'tmpl_id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'published_version'
            },
        ]
    },
    '/links/shorten/bulk-POST': {
        'parameters': [
        ]
    },
    '/domains-POST': {
        'parameters': [
            {
                'name': 'domain'
            },
        ]
    },
    '/links/shorten-POST': {
        'parameters': [
            {
                'name': 'redirect_link'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'metadata_tag'
            },
            {
                'name': 'billing_group_id'
            },
        ]
    },
    '/domains/{domain_id}-DELETE': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/links/{link_id}-DELETE': {
        'parameters': [
            {
                'name': 'link_id'
            },
        ]
    },
    '/domains/{domain_id}/links-DELETE': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/domains/{domain_id}-GET': {
        'parameters': [
            {
                'name': 'domain_id'
            },
        ]
    },
    '/links/{link_id}-GET': {
        'parameters': [
            {
                'name': 'link_id'
            },
        ]
    },
    '/domains-GET': {
        'parameters': [
        ]
    },
    '/links-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'include'
            },
            {
                'name': 'date_created'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'campaign_id'
            },
            {
                'name': 'clicked'
            },
            {
                'name': 'billing_group_id'
            },
        ]
    },
    '/links/{link_id}-PATCH': {
        'parameters': [
            {
                'name': 'redirect_link'
            },
            {
                'name': 'link_id'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'slug'
            },
            {
                'name': 'metadata_tag'
            },
            {
                'name': 'billing_group_id'
            },
        ]
    },
    '/us_autocompletions-POST': {
        'parameters': [
            {
                'name': 'address_prefix'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip_code'
            },
            {
                'name': 'geo_ip_sort'
            },
            {
                'name': 'case'
            },
            {
                'name': 'valid_addresses'
            },
        ]
    },
    '/bulk/us_verifications-POST': {
        'parameters': [
            {
                'name': 'addresses'
            },
            {
                'name': 'case'
            },
        ]
    },
    '/us_verifications-POST': {
        'parameters': [
            {
                'name': 'recipient'
            },
            {
                'name': 'primary_line'
            },
            {
                'name': 'secondary_line'
            },
            {
                'name': 'urbanization'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip_code'
            },
            {
                'name': 'address'
            },
            {
                'name': 'case'
            },
        ]
    },
    '/uploads-POST': {
        'parameters': [
            {
                'name': 'campaignId'
            },
            {
                'name': 'requiredAddressColumnMapping'
            },
            {
                'name': 'optionalAddressColumnMapping'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mergeVariableColumnMapping'
            },
        ]
    },
    '/uploads/{upl_id}/exports-POST': {
        'parameters': [
            {
                'name': 'upl_id'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/uploads/{upl_id}-DELETE': {
        'parameters': [
            {
                'name': 'upl_id'
            },
        ]
    },
    '/uploads/{upl_id}/file-POST': {
        'parameters': [
            {
                'name': 'upl_id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/uploads-GET': {
        'parameters': [
            {
                'name': 'campaignId'
            },
        ]
    },
    '/uploads/{upl_id}-GET': {
        'parameters': [
            {
                'name': 'upl_id'
            },
        ]
    },
    '/uploads/{upl_id}/report-GET': {
        'parameters': [
            {
                'name': 'upl_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/uploads/{upl_id}/exports/{ex_id}-GET': {
        'parameters': [
            {
                'name': 'upl_id'
            },
            {
                'name': 'ex_id'
            },
        ]
    },
    '/uploads/{upl_id}-PATCH': {
        'parameters': [
            {
                'name': 'upl_id'
            },
            {
                'name': 'originalFilename'
            },
            {
                'name': 'requiredAddressColumnMapping'
            },
            {
                'name': 'optionalAddressColumnMapping'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'mergeVariableColumnMapping'
            },
        ]
    },
    '/us_zip_lookups-POST': {
        'parameters': [
            {
                'name': 'zip_code'
            },
        ]
    },
};