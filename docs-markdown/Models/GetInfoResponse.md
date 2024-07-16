# GetInfoResponse
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **alias** | **String** | The alias of the user&#39;s node. | [optional] [default to null] |
| **color** | **String** | The color of the user&#39;s node. | [optional] [default to null] |
| **pubkey** | **String** | The pubkey of the user&#39;s node. | [default to null] |
| **network** | **String** | The bitcoin network of the user&#39;s node. | [default to null] |
| **block\_height** | **BigDecimal** | The current block height of the user&#39;s node. | [optional] [default to null] |
| **block\_hash** | **String** | The current block hash of the user&#39;s node. | [optional] [default to null] |
| **methods** | **List** | A list of supported methods for this connection. | [default to null] |
| **lud16** | **String** | The lightning or UMA address for the user. | [optional] [default to null] |
| **currencies** | [**List**](CurrencyPreference.md) | The currencies the user&#39;s wallet supports. Ordered by preference. If not provided, assume this user only supports BTC. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

