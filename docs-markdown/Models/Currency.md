# Currency
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **code** | **String** | The ISO-4217 currency code. | [default to null] |
| **symbol** | **String** | The currency symbol. | [default to null] |
| **name** | **String** | The currency name. | [default to null] |
| **decimals** | **Integer** | Number of digits after the decimal point for display on the sender side, and to add clarity around what the \&quot;smallest unit\&quot; of the currency is. For example, in USD, by convention, there are 2 digits for cents - $5.95. In this case, &#x60;decimals&#x60; would be 2. Note that the multiplier is still always in the smallest unit (cents). In addition to display purposes, this field can be used to resolve ambiguity in what the multiplier means. For example, if the currency is \&quot;BTC\&quot; and the multiplier is 1000, really we&#39;re exchanging in SATs, so &#x60;decimals&#x60; would be 8. | [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

