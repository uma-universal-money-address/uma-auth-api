# Documentation for UMA Auth API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://vasp.net/umanwc/v1*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *UmaAuthApi* | [**executeQuote**](Apis/UmaAuthApi.md#executequote) | **POST** /quote/{payment_hash} | execute_quote: Execute a quote |
*UmaAuthApi* | [**fetchQuoteForLud16**](Apis/UmaAuthApi.md#fetchquoteforlud16) | **GET** /quote/lud16 | fetch_quote_for_lud16: Get a quote for a payment to an LUD16 address |
*UmaAuthApi* | [**getBalance**](Apis/UmaAuthApi.md#getbalance) | **GET** /balance | get_balance: Get the balance of the user's wallet |
*UmaAuthApi* | [**getBudgetEstimate**](Apis/UmaAuthApi.md#getbudgetestimate) | **GET** /budget_estimate | get_budget_estimate: Estimate the total cost of the payment to complete the payment in the currency of sender's budget. |
*UmaAuthApi* | [**getInfo**](Apis/UmaAuthApi.md#getinfo) | **GET** /info | get_info: Get information about the user's wallet connection |
*UmaAuthApi* | [**listTransactions**](Apis/UmaAuthApi.md#listtransactions) | **GET** /transactions | list_transactions: Lists invoices and payments |
*UmaAuthApi* | [**lookupInvoice**](Apis/UmaAuthApi.md#lookupinvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
*UmaAuthApi* | [**lookupUserByLud16**](Apis/UmaAuthApi.md#lookupuserbylud16) | **GET** /receiver/lud16/{receiver_address} | lookup_user_by_lud16: Get receiver info by LUD16 address. |
*UmaAuthApi* | [**makeInvoice**](Apis/UmaAuthApi.md#makeinvoice) | **POST** /invoice | make_invoice: Create a new invoice |
*UmaAuthApi* | [**payInvoice**](Apis/UmaAuthApi.md#payinvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
*UmaAuthApi* | [**payKeysend**](Apis/UmaAuthApi.md#paykeysend) | **POST** /payments/keysend | pay_keysend: Pay directly to the pubkey of the receiver node based on a fixed receiving amount |
*UmaAuthApi* | [**payToLud16Address**](Apis/UmaAuthApi.md#paytolud16address) | **POST** /payments/lud16 | pay_to_lud16_address: Pay directly to an LNURL address based on a fixed sending amount. |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [BudgetEstimateResponse](./Models/BudgetEstimateResponse.md)
 - [Currency](./Models/Currency.md)
 - [CurrencyPreference](./Models/CurrencyPreference.md)
 - [ErrorCode](./Models/ErrorCode.md)
 - [ErrorResponse](./Models/ErrorResponse.md)
 - [ExecuteQuoteRequest](./Models/ExecuteQuoteRequest.md)
 - [ExecuteQuoteResponse](./Models/ExecuteQuoteResponse.md)
 - [GetBalanceResponse](./Models/GetBalanceResponse.md)
 - [GetInfoResponse](./Models/GetInfoResponse.md)
 - [ListTransactionsResponse](./Models/ListTransactionsResponse.md)
 - [LockedCurrencySide](./Models/LockedCurrencySide.md)
 - [LookupUserResponse](./Models/LookupUserResponse.md)
 - [MakeInvoiceRequest](./Models/MakeInvoiceRequest.md)
 - [PayInvoiceRequest](./Models/PayInvoiceRequest.md)
 - [PayInvoiceResponse](./Models/PayInvoiceResponse.md)
 - [PayKeysendRequest](./Models/PayKeysendRequest.md)
 - [PayKeysendRequest_tlv_records_inner](./Models/PayKeysendRequest_tlv_records_inner.md)
 - [PayKeysendResponse](./Models/PayKeysendResponse.md)
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

