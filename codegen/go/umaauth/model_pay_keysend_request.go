// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * UMA Auth API
 *
 * This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
 *
 * API version: 0.1
 */

package umaauth




type PayKeysendRequest struct {

	// The amount to pay in msats.
	Amount int64 `json:"amount"`

	// The public key of the receiver's node.
	Pubkey string `json:"pubkey"`

	// Preimage of the payment.
	Preimage string `json:"preimage,omitempty"`

	// The tlv records.
	TlvRecords []PayKeysendRequestTlvRecordsInner `json:"tlv_records,omitempty"`
}

// AssertPayKeysendRequestRequired checks if the required fields are not zero-ed
func AssertPayKeysendRequestRequired(obj PayKeysendRequest) error {
	elements := map[string]interface{}{
		"amount": obj.Amount,
		"pubkey": obj.Pubkey,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	for _, el := range obj.TlvRecords {
		if err := AssertPayKeysendRequestTlvRecordsInnerRequired(el); err != nil {
			return err
		}
	}
	return nil
}

// AssertPayKeysendRequestConstraints checks if the values respects the defined constraints
func AssertPayKeysendRequestConstraints(obj PayKeysendRequest) error {
	for _, el := range obj.TlvRecords {
		if err := AssertPayKeysendRequestTlvRecordsInnerConstraints(el); err != nil {
			return err
		}
	}
	return nil
}
