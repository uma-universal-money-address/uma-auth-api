# PayToAddressRequest
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **receiver\_address** | **String** | The LUD16 address to pay. | [default to null] |
| **sending\_currency\_code** | **String** | The code of the currency being sent from the sender&#39;s wallet. | [default to null] |
| **sending\_currency\_amount** | **Long** | The amount to send in the smallest unit of the sending currency (eg. cents). | [default to null] |
| **receiving\_currency\_code** | **String** | The code of the currency being received by the receiver. If not provided, the receiver&#39;s default currency will be used. | [optional] [default to null] |
| **budget\_currency\_code** | **String** | The code of the currency the sender used to set budget. Optional if it is the same as &#x60;sending_currency_code&#x60;. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

