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
	"errors"
)



type Quote struct {

	// The currency code of the sender's balance.
	SendingCurrencyCode string `json:"sending_currency_code"`

	ReceivingCurrency Currency `json:"receiving_currency"`

	// The payment hash of the quote. Used as an identifier to execute the quote.
	PaymentHash string `json:"payment_hash"`

	// The time the quote expires in unix timestamp.
	ExpiresAt int64 `json:"expires_at"`

	// Number of sending currency units per receiving currency unit.
	Multiplier float32 `json:"multiplier"`

	// The fees associated with the quote in the smallest unit of the sending currency (eg. cents).
	Fees int64 `json:"fees"`

	// The total amount that will be sent in the smallest unit of the sending currency (eg. cents).
	TotalSendingAmount int64 `json:"total_sending_amount"`

	// The total amount that will be received in the smallest unit of the receiving currency (eg. cents).
	TotalReceivingAmount int64 `json:"total_receiving_amount"`

	// The time the quote was created in unix timestamp.
	CreatedAt int64 `json:"created_at"`
}

// AssertQuoteRequired checks if the required fields are not zero-ed
func AssertQuoteRequired(obj Quote) error {
	elements := map[string]interface{}{
		"sending_currency_code": obj.SendingCurrencyCode,
		"receiving_currency": obj.ReceivingCurrency,
		"payment_hash": obj.PaymentHash,
		"expires_at": obj.ExpiresAt,
		"multiplier": obj.Multiplier,
		"fees": obj.Fees,
		"total_sending_amount": obj.TotalSendingAmount,
		"total_receiving_amount": obj.TotalReceivingAmount,
		"created_at": obj.CreatedAt,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	if err := AssertCurrencyRequired(obj.ReceivingCurrency); err != nil {
		return err
	}
	return nil
}

// AssertQuoteConstraints checks if the values respects the defined constraints
func AssertQuoteConstraints(obj Quote) error {
	if err := AssertCurrencyConstraints(obj.ReceivingCurrency); err != nil {
		return err
	}
	if obj.Multiplier < 0 {
		return &ParsingError{Param: "Multiplier", Err: errors.New(errMsgMinValueConstraint)}
	}
	if obj.Fees < 0 {
		return &ParsingError{Param: "Fees", Err: errors.New(errMsgMinValueConstraint)}
	}
	if obj.TotalSendingAmount < 0 {
		return &ParsingError{Param: "TotalSendingAmount", Err: errors.New(errMsgMinValueConstraint)}
	}
	if obj.TotalReceivingAmount < 0 {
		return &ParsingError{Param: "TotalReceivingAmount", Err: errors.New(errMsgMinValueConstraint)}
	}
	return nil
}
