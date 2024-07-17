// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * UMA Auth API
 *
 * This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
 *
 * API version: 0.1
 */

package umaauth




type PayToAddressRequest struct {

	// The address to pay.
	ReceiverAddress string `json:"receiver_address"`

	// The code of the currency being sent from the sender's wallet.
	SendingCurrencyCode string `json:"sending_currency_code"`

	// The amount to send in the smallest unit of the sending currency (eg. cents).
	SendingCurrencyAmount float32 `json:"sending_currency_amount"`

	// The code of the currency being received by the receiver. If not provided, the receiver's default currency will be used.
	ReceivingCurrencyCode string `json:"receiving_currency_code,omitempty"`
}

// AssertPayToAddressRequestRequired checks if the required fields are not zero-ed
func AssertPayToAddressRequestRequired(obj PayToAddressRequest) error {
	elements := map[string]interface{}{
		"receiver_address": obj.ReceiverAddress,
		"sending_currency_code": obj.SendingCurrencyCode,
		"sending_currency_amount": obj.SendingCurrencyAmount,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertPayToAddressRequestConstraints checks if the values respects the defined constraints
func AssertPayToAddressRequestConstraints(obj PayToAddressRequest) error {
	return nil
}