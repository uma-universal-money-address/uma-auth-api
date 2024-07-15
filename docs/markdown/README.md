# Documentation for UMA Auth API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**executeQuote**](Apis/DefaultApi.md#executequote) | **POST** /quote | [NWC: execute_quote] Execute a quote |
*DefaultApi* | [**fetchQuote**](Apis/DefaultApi.md#fetchquote) | **GET** /quote | [NWC: fetch_quote] Get a quote for a payment |
*DefaultApi* | [**getBalance**](Apis/DefaultApi.md#getbalance) | **GET** /balance | [NWC: get_balance] Get the balance of the user's wallet |
*DefaultApi* | [**getInfo**](Apis/DefaultApi.md#getinfo) | **GET** /info | [NWC: get_info] Get information about the user's wallet connection |
*DefaultApi* | [**lookupInvoice**](Apis/DefaultApi.md#lookupinvoice) | **GET** /invoices/{payment_hash} | [NWC: lookup_invoice] Get an invoice by its payment hash |
*DefaultApi* | [**lookupUser**](Apis/DefaultApi.md#lookupuser) | **GET** /receiver/uma/{receiver_uma} | [NWC: lookup_user] Get receiver info by UMA |
*DefaultApi* | [**makeInvoice**](Apis/DefaultApi.md#makeinvoice) | **POST** /invoice | [NWC: make_invoice] Create a new invoice |
*DefaultApi* | [**payInvoice**](Apis/DefaultApi.md#payinvoice) | **POST** /payments/bolt11 | [NWC: pay_invoice] Pay a bolt11 invoice |
*DefaultApi* | [**payToAddress**](Apis/DefaultApi.md#paytoaddress) | **POST** /payments/lnurl | [NWC: pay_to_address] Pay to an LNURL address |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [Invoice](./Models/Invoice.md)
 - [Quote](./Models/Quote.md)
 - [execute_quote_request](./Models/execute_quote_request.md)
 - [get_balance_200_response](./Models/get_balance_200_response.md)
 - [get_balance_request](./Models/get_balance_request.md)
 - [get_info_200_response](./Models/get_info_200_response.md)
 - [get_info_200_response_currencies_inner](./Models/get_info_200_response_currencies_inner.md)
 - [lookup_user_200_response](./Models/lookup_user_200_response.md)
 - [lookup_user_200_response_currencies_inner](./Models/lookup_user_200_response_currencies_inner.md)
 - [lookup_user_request](./Models/lookup_user_request.md)
 - [make_invoice_request](./Models/make_invoice_request.md)
 - [pay_invoice_200_response](./Models/pay_invoice_200_response.md)
 - [pay_invoice_request](./Models/pay_invoice_request.md)
 - [pay_to_address_200_response](./Models/pay_to_address_200_response.md)
 - [pay_to_address_request](./Models/pay_to_address_request.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
