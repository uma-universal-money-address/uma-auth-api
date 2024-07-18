# Documentation for UMA Auth API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *DefaultApi* | [**executeQuote**](Apis/DefaultApi.md#executequote) | **POST** /quote | execute_quote: Execute a quote |
*DefaultApi* | [**fetchQuote**](Apis/DefaultApi.md#fetchquote) | **GET** /quote | fetch_quote: Get a quote for a payment |
*DefaultApi* | [**getBalance**](Apis/DefaultApi.md#getbalance) | **GET** /balance | get_balance: Get the balance of the user's wallet |
*DefaultApi* | [**getInfo**](Apis/DefaultApi.md#getinfo) | **GET** /info | get_info: Get information about the user's wallet connection |
*DefaultApi* | [**lookupInvoice**](Apis/DefaultApi.md#lookupinvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
*DefaultApi* | [**lookupUser**](Apis/DefaultApi.md#lookupuser) | **GET** /receiver/uma/{receiver_uma} | lookup_user: Get receiver info by UMA |
*DefaultApi* | [**makeInvoice**](Apis/DefaultApi.md#makeinvoice) | **POST** /invoice | make_invoice: Create a new invoice |
*DefaultApi* | [**payInvoice**](Apis/DefaultApi.md#payinvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
*DefaultApi* | [**payToAddress**](Apis/DefaultApi.md#paytoaddress) | **POST** /payments/lnurl | pay_to_address: Pay to an LNURL address |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [CurrencyPreference](./Models/CurrencyPreference.md)
 - [ExecuteQuoteRequest](./Models/ExecuteQuoteRequest.md)
 - [ExecuteQuoteResponse](./Models/ExecuteQuoteResponse.md)
 - [GetBalanceResponse](./Models/GetBalanceResponse.md)
 - [GetInfoResponse](./Models/GetInfoResponse.md)
 - [Invoice](./Models/Invoice.md)
 - [LookupUserResponse](./Models/LookupUserResponse.md)
 - [MakeInvoiceRequest](./Models/MakeInvoiceRequest.md)
 - [PayInvoiceRequest](./Models/PayInvoiceRequest.md)
 - [PayInvoiceResponse](./Models/PayInvoiceResponse.md)
 - [PayToAddressRequest](./Models/PayToAddressRequest.md)
 - [PayToAddressResponse](./Models/PayToAddressResponse.md)
 - [Quote](./Models/Quote.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

All endpoints do not require authorization.
