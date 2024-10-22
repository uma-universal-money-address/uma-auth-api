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



type PayKeysendResponse struct {

	// The preimage of the payment.
	Preimage string `json:"preimage"`

	// The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null. 
	TotalBudgetCurrencyAmount int64 `json:"total_budget_currency_amount,omitempty"`
}

// AssertPayKeysendResponseRequired checks if the required fields are not zero-ed
func AssertPayKeysendResponseRequired(obj PayKeysendResponse) error {
	elements := map[string]interface{}{
		"preimage": obj.Preimage,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertPayKeysendResponseConstraints checks if the values respects the defined constraints
func AssertPayKeysendResponseConstraints(obj PayKeysendResponse) error {
	if obj.TotalBudgetCurrencyAmount < 0 {
		return &ParsingError{Param: "TotalBudgetCurrencyAmount", Err: errors.New(errMsgMinValueConstraint)}
	}
	return nil
}
