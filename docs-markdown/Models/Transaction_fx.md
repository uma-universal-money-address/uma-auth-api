# Transaction_fx
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **receiving\_currency** | [**Currency**](Currency.md) |  | [optional] [default to null] |
| **sending\_currency** | [**Currency**](Currency.md) |  | [optional] [default to null] |
| **total\_receiving\_amount** | **Long** | The total amount that will be received in the smallest unit of the receiving currency (eg. cents). | [optional] [default to null] |
| **total\_sending\_amount** | **Long** | The total amount that will be sent in the smallest unit of the sending currency (eg. cents). | [optional] [default to null] |
| **multiplier** | **BigDecimal** | Number of sending currency units per receiving currency unit. | [optional] [default to null] |
| **fees** | **Long** | The fees associated with the quote in the smallest unit of the sending currency (eg. cents). | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

