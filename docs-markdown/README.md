# Documentation for UMA Auth API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *http://localhost*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *UmaAuthApi* | [**executeQuote**](Apis/UmaAuthApi.md#executequote) | **POST** /quote | execute_quote: Execute a quote |
*UmaAuthApi* | [**fetchQuote**](Apis/UmaAuthApi.md#fetchquote) | **GET** /quote | fetch_quote: Get a quote for a payment |
*UmaAuthApi* | [**getBalance**](Apis/UmaAuthApi.md#getbalance) | **GET** /balance | get_balance: Get the balance of the user's wallet |
*UmaAuthApi* | [**getInfo**](Apis/UmaAuthApi.md#getinfo) | **GET** /info | get_info: Get information about the user's wallet connection |
*UmaAuthApi* | [**lookupInvoice**](Apis/UmaAuthApi.md#lookupinvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
*UmaAuthApi* | [**lookupUser**](Apis/UmaAuthApi.md#lookupuser) | **GET** /receiver/uma/{receiver_uma} | lookup_user: Get receiver info by UMA |
*UmaAuthApi* | [**makeInvoice**](Apis/UmaAuthApi.md#makeinvoice) | **POST** /invoice | make_invoice: Create a new invoice |
*UmaAuthApi* | [**payInvoice**](Apis/UmaAuthApi.md#payinvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
*UmaAuthApi* | [**payToAddress**](Apis/UmaAuthApi.md#paytoaddress) | **POST** /payments/lnurl | pay_to_address: Pay to an LNURL address |


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
