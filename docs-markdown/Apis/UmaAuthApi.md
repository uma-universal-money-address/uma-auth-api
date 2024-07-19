# UmaAuthApi

All URIs are relative to *https://vasp.net/umanwc/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**executeQuote**](UmaAuthApi.md#executeQuote) | **POST** /quote | execute_quote: Execute a quote |
| [**fetchQuote**](UmaAuthApi.md#fetchQuote) | **GET** /quote | fetch_quote: Get a quote for a payment |
| [**getBalance**](UmaAuthApi.md#getBalance) | **GET** /balance | get_balance: Get the balance of the user&#39;s wallet |
| [**getInfo**](UmaAuthApi.md#getInfo) | **GET** /info | get_info: Get information about the user&#39;s wallet connection |
| [**lookupInvoice**](UmaAuthApi.md#lookupInvoice) | **GET** /invoices/{payment_hash} | lookup_invoice: Get an invoice by its payment hash |
| [**lookupUser**](UmaAuthApi.md#lookupUser) | **GET** /receiver/uma/{receiver_uma} | lookup_user: Get receiver info by UMA |
| [**makeInvoice**](UmaAuthApi.md#makeInvoice) | **POST** /invoice | make_invoice: Create a new invoice |
| [**payInvoice**](UmaAuthApi.md#payInvoice) | **POST** /payments/bolt11 | pay_invoice: Pay a bolt11 invoice |
| [**payToAddress**](UmaAuthApi.md#payToAddress) | **POST** /payments/lnurl | pay_to_address: Pay to an LNURL address |


<a name="executeQuote"></a>
# **executeQuote**
> ExecuteQuoteResponse executeQuote(ExecuteQuoteRequest)

execute_quote: Execute a quote

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ExecuteQuoteRequest** | [**ExecuteQuoteRequest**](../Models/ExecuteQuoteRequest.md)|  | [optional] |

### Return type

[**ExecuteQuoteResponse**](../Models/ExecuteQuoteResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

<a name="fetchQuote"></a>
# **fetchQuote**
> Quote fetchQuote(sending\_currency\_code, receiving\_currency\_code, locked\_currency\_amount, locked\_currency\_side, receiving\_address)

fetch_quote: Get a quote for a payment

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **sending\_currency\_code** | **String**| The currency code being sent from the sender&#39;s wallet. | [default to null] |
| **receiving\_currency\_code** | **String**| The currency code of the currency that the receiver will receive. | [default to null] |
| **locked\_currency\_amount** | **Integer**| The amount to send/receive in the smallest unit of the locked currency (eg. cents). See &#x60;locked_currency_side&#x60; for more information. | [default to null] |
| **locked\_currency\_side** | **String**| The side of the quote which should be locked and specified in the &#x60;locked_currency_amount&#x60;. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \&quot;sending\&quot;, and the &#x60;locked_currency_amount&#x60; to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \&quot;receiving\&quot; and the &#x60;locked_currency_amount&#x60; to 10000 (in cents). | [default to null] [enum: sending, receiving] |
| **receiving\_address** | **String**| The UMA address to send the payment to. | [default to null] |

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

<a name="lookupInvoice"></a>
# **lookupInvoice**
> Invoice lookupInvoice(payment\_hash)

lookup_invoice: Get an invoice by its payment hash

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **payment\_hash** | **String**| The payment hash of the invoice. | [default to null] |

### Return type

[**Invoice**](../Models/Invoice.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

<a name="lookupUser"></a>
# **lookupUser**
> LookupUserResponse lookupUser(receiver\_uma, base\_sending\_currency\_code)

lookup_user: Get receiver info by UMA

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **receiver\_uma** | **String**| The receiver&#39;s UMA. | [default to null] |
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
> Invoice makeInvoice(MakeInvoiceRequest)

make_invoice: Create a new invoice

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **MakeInvoiceRequest** | [**MakeInvoiceRequest**](../Models/MakeInvoiceRequest.md)|  | [optional] |

### Return type

[**Invoice**](../Models/Invoice.md)

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

<a name="payToAddress"></a>
# **payToAddress**
> PayToAddressResponse payToAddress(PayToAddressRequest)

pay_to_address: Pay to an LNURL address

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

