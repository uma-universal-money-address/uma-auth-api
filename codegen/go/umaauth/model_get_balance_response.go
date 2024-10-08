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



type GetBalanceResponse struct {

	// The balance of the user's wallet.
	Balance float32 `json:"balance"`

	Currency Currency `json:"currency,omitempty"`
}

// AssertGetBalanceResponseRequired checks if the required fields are not zero-ed
func AssertGetBalanceResponseRequired(obj GetBalanceResponse) error {
	elements := map[string]interface{}{
		"balance": obj.Balance,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	if err := AssertCurrencyRequired(obj.Currency); err != nil {
		return err
	}
	return nil
}

// AssertGetBalanceResponseConstraints checks if the values respects the defined constraints
func AssertGetBalanceResponseConstraints(obj GetBalanceResponse) error {
	if obj.Balance < 0 {
		return &ParsingError{Param: "Balance", Err: errors.New(errMsgMinValueConstraint)}
	}
	if err := AssertCurrencyConstraints(obj.Currency); err != nil {
		return err
	}
	return nil
}
