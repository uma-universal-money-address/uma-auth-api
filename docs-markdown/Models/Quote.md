# Quote
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **sending\_currency\_code** | **String** | The currency code of the sender&#39;s balance. | [default to null] |
| **receiving\_currency** | [**Currency**](Currency.md) |  | [default to null] |
| **payment\_hash** | **String** | The payment hash of the quote. Used as an identifier to execute the quote. | [default to null] |
| **expires\_at** | **Long** | The time the quote expires in unix timestamp. | [default to null] |
| **multiplier** | **BigDecimal** | Number of sending currency units per receiving currency unit. | [default to null] |
| **fees** | **Long** | The fees associated with the quote in the smallest unit of the sending currency (eg. cents). | [default to null] |
| **total\_sending\_amount** | **Long** | The total amount that will be sent in the smallest unit of the sending currency (eg. cents). | [default to null] |
| **total\_receiving\_amount** | **Long** | The total amount that will be received in the smallest unit of the receiving currency (eg. cents). | [default to null] |
| **created\_at** | **Long** | The time the quote was created in unix timestamp. | [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

