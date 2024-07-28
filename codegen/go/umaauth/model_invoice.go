// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * UMA Auth API
 *
 * This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
 *
 * API version: 0.1
 */

package umaauth


import (
	"time"
)



type Invoice struct {

	// The full, encoded payment request.
	PaymentRequest string `json:"payment_request"`

	// The amount of the invoice in msats.
	Amount int64 `json:"amount"`

	// The payment hash of the invoice.
	PaymentHash string `json:"payment_hash"`

	// A memo attached to the invoice.
	Memo *string `json:"memo,omitempty"`

	// Additional metadata attached to the invoice.
	Metadata *map[string]interface{} `json:"metadata,omitempty"`

	// The payment preimage of the invoice.
	Preimage *string `json:"preimage,omitempty"`

	// The time the invoice expires.
	ExpiresAt *time.Time `json:"expires_at,omitempty"`

	// The time the invoice was created.
	CreatedAt time.Time `json:"created_at"`

	// The time the invoice was settled.
	SettledAt *time.Time `json:"settled_at,omitempty"`

	// Whether the invoice is incoming (created by this user) or outgoing (created by another user).
	Type string `json:"type"`
}

// AssertInvoiceRequired checks if the required fields are not zero-ed
func AssertInvoiceRequired(obj Invoice) error {
	elements := map[string]interface{}{
		"payment_request": obj.PaymentRequest,
		"amount": obj.Amount,
		"payment_hash": obj.PaymentHash,
		"created_at": obj.CreatedAt,
		"type": obj.Type,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertInvoiceConstraints checks if the values respects the defined constraints
func AssertInvoiceConstraints(obj Invoice) error {
	return nil
}
