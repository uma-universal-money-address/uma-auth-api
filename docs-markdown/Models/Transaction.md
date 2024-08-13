# Transaction
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **type** | [**TransactionType**](TransactionType.md) |  | [default to null] |
| **invoice** | **String** | The full, encoded invoice. | [optional] [default to null] |
| **description** | **String** | The invoice&#39;s description. | [optional] [default to null] |
| **description\_hash** | **String** | The invoice&#39;s description hash. | [optional] [default to null] |
| **preimage** | **String** | The payment preimage, optional if unpaid. | [optional] [default to null] |
| **payment\_hash** | **String** | Payment hash for the payment | [default to null] |
| **amount** | **Long** | Value in msats. | [default to null] |
| **fees\_paid** | **Long** | Value in msats. | [optional] [default to null] |
| **created\_at** | **Integer** | The time the payment/invoice was created. | [default to null] |
| **expires\_at** | **Integer** | The time the invoice expires. | [optional] [default to null] |
| **metadata** | [**Object**](.md) | Additional metadata attached to the invoice. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

