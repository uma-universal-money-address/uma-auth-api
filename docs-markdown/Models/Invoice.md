# Invoice
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **payment\_request** | **String** | The full, encoded payment request. | [optional] [default to null] |
| **amount** | **BigDecimal** | The amount of the invoice in msats. | [optional] [default to null] |
| **payment\_hash** | **String** | The payment hash of the invoice. | [optional] [default to null] |
| **memo** | **String** | A memo attached to the invoice. | [optional] [default to null] |
| **metadata** | [**Object**](.md) | Additional metadata attached to the invoice. | [optional] [default to null] |
| **preimage** | **String** | The payment preimage of the invoice. | [optional] [default to null] |
| **expires\_at** | **Date** | The time the invoice expires. | [optional] [default to null] |
| **created\_at** | **Date** | The time the invoice was created. | [optional] [default to null] |
| **settled\_at** | **Date** | The time the invoice was settled. | [optional] [default to null] |
| **type** | **String** | Whether the invoice is incoming (created by this user) or outgoing (created by another user). | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

