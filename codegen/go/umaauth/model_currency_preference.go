// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

/*
 * UMA Auth API
 *
 * This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
 *
 * API version: 0.1
 */

package umaauth




type CurrencyPreference struct {

	// The ISO-4217 currency code.
	Code string `json:"code"`

	// The currency symbol.
	Symbol string `json:"symbol"`

	// The currency name.
	Name string `json:"name"`

	// Estimated number of milli-sats per smallest unit of this currency (eg. cents) If base_sending_currency_code was specified, this is the rate relative to that currency instead of milli-sats.
	Multiplier float32 `json:"multiplier"`

	// Number of digits after the decimal point for display on the sender side, and to add clarity around what the \"smallest unit\" of the currency is. For example, in USD, by convention, there are 2 digits for cents - $5.95. In this case, `decimals` would be 2. Note that the multiplier is still always in the smallest unit (cents). In addition to display purposes, this field can be used to resolve ambiguity in what the multiplier means. For example, if the currency is \"BTC\" and the multiplier is 1000, really we're exchanging in SATs, so `decimals` would be 8.
	Decimals int32 `json:"decimals"`

	// The minimum amount that can be received in this currency.
	Min int32 `json:"min"`

	// The maximum amount that can be received in this currency.
	Max int32 `json:"max"`
}

// AssertCurrencyPreferenceRequired checks if the required fields are not zero-ed
func AssertCurrencyPreferenceRequired(obj CurrencyPreference) error {
	elements := map[string]interface{}{
		"code": obj.Code,
		"symbol": obj.Symbol,
		"name": obj.Name,
		"multiplier": obj.Multiplier,
		"decimals": obj.Decimals,
		"min": obj.Min,
		"max": obj.Max,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertCurrencyPreferenceConstraints checks if the values respects the defined constraints
func AssertCurrencyPreferenceConstraints(obj CurrencyPreference) error {
	return nil
}