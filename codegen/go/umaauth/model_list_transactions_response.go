// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * UMA Auth API
 *
 * This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
 *
 * API version: 0.1
 */

package umaauth




type ListTransactionsResponse struct {

	// A list of transactions including invoices and payments.
	Transactions []Transaction `json:"transactions"`
}

// AssertListTransactionsResponseRequired checks if the required fields are not zero-ed
func AssertListTransactionsResponseRequired(obj ListTransactionsResponse) error {
	elements := map[string]interface{}{
		"transactions": obj.Transactions,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	for _, el := range obj.Transactions {
		if err := AssertTransactionRequired(el); err != nil {
			return err
		}
	}
	return nil
}

// AssertListTransactionsResponseConstraints checks if the values respects the defined constraints
func AssertListTransactionsResponseConstraints(obj ListTransactionsResponse) error {
	for _, el := range obj.Transactions {
		if err := AssertTransactionConstraints(el); err != nil {
			return err
		}
	}
	return nil
}
