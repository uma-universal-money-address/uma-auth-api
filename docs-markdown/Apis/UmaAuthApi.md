# UmaAuthApi

All URIs are relative to *https://vasp.net/umanwc/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**executeQuote**](UmaAuthApi.md#executeQuote) | **POST** /quote/{payment_hash} | execute_quote: Execute a quote |
| [**fetchQuoteForLud16**](UmaAuthApi.md#fetchQuoteForLud16) | **GET** /quote/lud16 | fetch_quote_for_lud16: Get a quote for a payment to an LUD16 address |
| [**getBalance**](UmaAuthApi.md#getBalance) | **GET** /balance | get_balance: Get the balance of the user&#39;s wallet |
| [**getInfo**](UmaAuthApi.md#getInfo) | **GET** /info | get_info: Get information about the user&#39;s wallet connection |
| [**listTransactions**](UmaAuthApi.md#listTransactions) | **GET** /transactions | list_transactions: Lists invoices and payments |
| [**lookupInvoice**](UmaAuthApi.md#lookupInvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
| [**lookupUserByLud16**](UmaAuthApi.md#lookupUserByLud16) | **GET** /receiver/lud16/{receiver_address} | lookup_user_by_lud16: Get receiver info by LUD16 address. |
| [**makeInvoice**](UmaAuthApi.md#makeInvoice) | **POST** /invoice | make_invoice: Create a new invoice |
| [**payInvoice**](UmaAuthApi.md#payInvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
| [**payToLud16Address**](UmaAuthApi.md#payToLud16Address) | **POST** /payments/lud16 | pay_to_lud16_address: Pay to an LNURL address |


<a name="executeQuote"></a>
# **executeQuote**
> ExecuteQuoteResponse executeQuote(payment\_hash)

execute_quote: Execute a quote

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **payment\_hash** | **String**| The payment hash of the quote to execute. | [default to null] |

### Return type

[**ExecuteQuoteResponse**](../Models/ExecuteQuoteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="fetchQuoteForLud16"></a>
# **fetchQuoteForLud16**
> Quote fetchQuoteForLud16(sending\_currency\_code, receiving\_currency\_code, locked\_currency\_amount, locked\_currency\_side, receiver\_address)

fetch_quote_for_lud16: Get a quote for a payment to an LUD16 address

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sending\_currency\_code** | **String**| The currency code being sent from the sender&#39;s wallet. | [default to null] |
| **receiving\_currency\_code** | **String**| The currency code of the currency that the receiver will receive. | [default to null] |
| **locked\_currency\_amount** | **Long**| The amount to send/receive in the smallest unit of the locked currency (eg. cents). See &#x60;locked_currency_side&#x60; for more information. | [default to null] |
| **locked\_currency\_side** | **String**| The side of the quote which should be locked and specified in the &#x60;locked_currency_amount&#x60;. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \&quot;sending\&quot;, and the &#x60;locked_currency_amount&#x60; to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \&quot;receiving\&quot; and the &#x60;locked_currency_amount&#x60; to 10000 (in cents). | [default to null] [enum: sending, receiving] |
| **receiver\_address** | **String**| The LUD16 address to send the payment to. | [default to null] |

### Return type

[**Quote**](../Models/Quote.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getBalance"></a>
# **getBalance**
> GetBalanceResponse getBalance(currency\_code)

get_balance: Get the balance of the user&#39;s wallet

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **currency\_code** | **String**| The currency code of the balance. Assumed to be in msats if not provided.  | [optional] [default to null] |

### Return type

[**GetBalanceResponse**](../Models/GetBalanceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="getInfo"></a>
# **getInfo**
> GetInfoResponse getInfo()

get_info: Get information about the user&#39;s wallet connection

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInfoResponse**](../Models/GetInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="listTransactions"></a>
# **listTransactions**
> ListTransactionsResponse listTransactions(from, until, limit, offset, unpaid, type)

list_transactions: Lists invoices and payments

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **from** | **Integer**| Starting timestamp in seconds since epoch (inclusive). | [optional] [default to null] |
| **until** | **Integer**| Ending timestamp in seconds since epoch (inclusive). | [optional] [default to null] |
| **limit** | **Integer**| Maximum number of transactions to return. | [optional] [default to null] |
| **offset** | **Integer**| Offset of the first transaction to return. | [optional] [default to null] |
| **unpaid** | **Boolean**| Whether to include unpaid invoices. | [optional] [default to null] |
| **type** | [**TransactionType**](../Models/.md)| Type of transactions to return: \&quot;incoming\&quot; for invoices, \&quot;outgoing\&quot; for payments, undefined for both. | [optional] [default to null] [enum: incoming, outgoing] |

### Return type

[**ListTransactionsResponse**](../Models/ListTransactionsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="lookupInvoice"></a>
# **lookupInvoice**
> Transaction lookupInvoice(payment\_hash)

lookup_invoice: Get an invoice by its payment hash

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **payment\_hash** | **String**| The payment hash of the invoice. | [default to null] |

### Return type

[**Transaction**](../Models/Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="lookupUserByLud16"></a>
# **lookupUserByLud16**
> LookupUserResponse lookupUserByLud16(receiver\_address, base\_sending\_currency\_code)

lookup_user_by_lud16: Get receiver info by LUD16 address.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **receiver\_address** | **String**| The receiver&#39;s LUD16 address. | [default to null] |
| **base\_sending\_currency\_code** | **String**| The currency code of the sender&#39;s balance. Assumed to be in msats if not provided.  This is used to calculate the multiplier for the receiver&#39;s currencies. | [optional] [default to null] |

### Return type

[**LookupUserResponse**](../Models/LookupUserResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="makeInvoice"></a>
# **makeInvoice**
> Transaction makeInvoice(MakeInvoiceRequest)

make_invoice: Create a new invoice

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MakeInvoiceRequest** | [**MakeInvoiceRequest**](../Models/MakeInvoiceRequest.md)|  | [optional] |

### Return type

[**Transaction**](../Models/Transaction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="payInvoice"></a>
# **payInvoice**
> PayInvoiceResponse payInvoice(PayInvoiceRequest)

pay_invoice: Pay a bolt11 invoice

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PayInvoiceRequest** | [**PayInvoiceRequest**](../Models/PayInvoiceRequest.md)|  | [optional] |

### Return type

[**PayInvoiceResponse**](../Models/PayInvoiceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="payToLud16Address"></a>
# **payToLud16Address**
> PayToAddressResponse payToLud16Address(PayToAddressRequest)

pay_to_lud16_address: Pay to an LNURL address

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **PayToAddressRequest** | [**PayToAddressRequest**](../Models/PayToAddressRequest.md)|  | [optional] |

### Return type

[**PayToAddressResponse**](../Models/PayToAddressResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

