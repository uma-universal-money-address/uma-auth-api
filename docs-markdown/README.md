# Documentation for UMA Auth API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://vasp.net/umanwc/v1*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *UmaAuthApi* | [**executeQuote**](Apis/UmaAuthApi.md#executequote) | **POST** /quote/{payment_hash} | execute_quote: Execute a quote |
*UmaAuthApi* | [**fetchQuoteForLud16**](Apis/UmaAuthApi.md#fetchquoteforlud16) | **GET** /quote/lud16 | fetch_quote_for_lud16: Get a quote for a payment to an LUD16 address |
*UmaAuthApi* | [**getBalance**](Apis/UmaAuthApi.md#getbalance) | **GET** /balance | get_balance: Get the balance of the user's wallet |
*UmaAuthApi* | [**getInfo**](Apis/UmaAuthApi.md#getinfo) | **GET** /info | get_info: Get information about the user's wallet connection |
*UmaAuthApi* | [**listTransactions**](Apis/UmaAuthApi.md#listtransactions) | **GET** /transactions | list_transactions: Lists invoices and payments |
*UmaAuthApi* | [**lookupInvoice**](Apis/UmaAuthApi.md#lookupinvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
*UmaAuthApi* | [**lookupUserByLud16**](Apis/UmaAuthApi.md#lookupuserbylud16) | **GET** /receiver/lud16/{receiver_address} | lookup_user_by_lud16: Get receiver info by LUD16 address. |
*UmaAuthApi* | [**makeInvoice**](Apis/UmaAuthApi.md#makeinvoice) | **POST** /invoice | make_invoice: Create a new invoice |
*UmaAuthApi* | [**payInvoice**](Apis/UmaAuthApi.md#payinvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
*UmaAuthApi* | [**payToLud16Address**](Apis/UmaAuthApi.md#paytolud16address) | **POST** /payments/lud16 | pay_to_lud16_address: Pay to an LNURL address |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [CurrencyPreference](./Models/CurrencyPreference.md)
 - [ErrorResponse](./Models/ErrorResponse.md)
 - [ExecuteQuoteResponse](./Models/ExecuteQuoteResponse.md)
 - [GetBalanceResponse](./Models/GetBalanceResponse.md)
 - [GetInfoResponse](./Models/GetInfoResponse.md)
 - [ListTransactionsResponse](./Models/ListTransactionsResponse.md)
 - [LookupUserResponse](./Models/LookupUserResponse.md)
 - [MakeInvoiceRequest](./Models/MakeInvoiceRequest.md)
 - [PayInvoiceRequest](./Models/PayInvoiceRequest.md)
 - [PayInvoiceResponse](./Models/PayInvoiceResponse.md)
 - [PayToAddressRequest](./Models/PayToAddressRequest.md)
 - [PayToAddressResponse](./Models/PayToAddressResponse.md)
 - [Quote](./Models/Quote.md)
 - [Transaction](./Models/Transaction.md)
 - [TransactionType](./Models/TransactionType.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="bearerAuth"></a>
### bearerAuth

- **Type**: HTTP Bearer Token authentication (JWT)

