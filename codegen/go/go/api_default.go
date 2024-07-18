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
	"encoding/json"
	"net/http"
	"strings"

	"github.com/gorilla/mux"
)

// DefaultAPIController binds http requests to an api service and writes the service results to the http response
type DefaultAPIController struct {
	service DefaultAPIServicer
	errorHandler ErrorHandler
}

// DefaultAPIOption for how the controller is set up.
type DefaultAPIOption func(*DefaultAPIController)

// WithDefaultAPIErrorHandler inject ErrorHandler into controller
func WithDefaultAPIErrorHandler(h ErrorHandler) DefaultAPIOption {
	return func(c *DefaultAPIController) {
		c.errorHandler = h
	}
}

// NewDefaultAPIController creates a default api controller
func NewDefaultAPIController(s DefaultAPIServicer, opts ...DefaultAPIOption) *DefaultAPIController {
	controller := &DefaultAPIController{
		service:      s,
		errorHandler: DefaultErrorHandler,
	}

	for _, opt := range opts {
		opt(controller)
	}

	return controller
}

// Routes returns all the api routes for the DefaultAPIController
func (c *DefaultAPIController) Routes() Routes {
	return Routes{
		"ExecuteQuote": Route{
			strings.ToUpper("Post"),
			"/quote",
			c.ExecuteQuote,
		},
		"FetchQuote": Route{
			strings.ToUpper("Get"),
			"/quote",
			c.FetchQuote,
		},
		"GetBalance": Route{
			strings.ToUpper("Get"),
			"/balance",
			c.GetBalance,
		},
		"GetInfo": Route{
			strings.ToUpper("Get"),
			"/info",
			c.GetInfo,
		},
		"LookupInvoice": Route{
			strings.ToUpper("Get"),
			"/invoices/{payment_hash}",
			c.LookupInvoice,
		},
		"LookupUser": Route{
			strings.ToUpper("Get"),
			"/receiver/uma/{receiver_uma}",
			c.LookupUser,
		},
		"MakeInvoice": Route{
			strings.ToUpper("Post"),
			"/invoice",
			c.MakeInvoice,
		},
		"PayInvoice": Route{
			strings.ToUpper("Post"),
			"/payments/bolt11",
			c.PayInvoice,
		},
		"PayToAddress": Route{
			strings.ToUpper("Post"),
			"/payments/lnurl",
			c.PayToAddress,
		},
	}
}

// ExecuteQuote - execute_quote: Execute a quote
func (c *DefaultAPIController) ExecuteQuote(w http.ResponseWriter, r *http.Request) {
	executeQuoteRequestParam := ExecuteQuoteRequest{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(&executeQuoteRequestParam); err != nil && !errors.Is(err, io.EOF) {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertExecuteQuoteRequestRequired(executeQuoteRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertExecuteQuoteRequestConstraints(executeQuoteRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.ExecuteQuote(r.Context(), executeQuoteRequestParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// FetchQuote - fetch_quote: Get a quote for a payment
func (c *DefaultAPIController) FetchQuote(w http.ResponseWriter, r *http.Request) {
	query, err := parseQuery(r.URL.RawQuery)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	var sendingCurrencyCodeParam string
	if query.Has("sending_currency_code") {
		param := query.Get("sending_currency_code")

		sendingCurrencyCodeParam = param
	} else {
		c.errorHandler(w, r, &RequiredError{Field: "sending_currency_code"}, nil)
		return
	}
	var receivingCurrencyCodeParam string
	if query.Has("receiving_currency_code") {
		param := query.Get("receiving_currency_code")

		receivingCurrencyCodeParam = param
	} else {
		c.errorHandler(w, r, &RequiredError{Field: "receiving_currency_code"}, nil)
		return
	}
	var lockedCurrencyAmountParam int32
	if query.Has("locked_currency_amount") {
		param, err := parseNumericParameter[int32](
			query.Get("locked_currency_amount"),
			WithParse[int32](parseInt32),
		)
		if err != nil {
			c.errorHandler(w, r, &ParsingError{Param: "locked_currency_amount", Err: err}, nil)
			return
		}

		lockedCurrencyAmountParam = param
	} else {
		c.errorHandler(w, r, &RequiredError{Field: "locked_currency_amount"}, nil)
		return
	}
	var lockedCurrencySideParam string
	if query.Has("locked_currency_side") {
		param := query.Get("locked_currency_side")

		lockedCurrencySideParam = param
	} else {
		c.errorHandler(w, r, &RequiredError{Field: "locked_currency_side"}, nil)
		return
	}
	var receivingAddressParam string
	if query.Has("receiving_address") {
		param := query.Get("receiving_address")

		receivingAddressParam = param
	} else {
		c.errorHandler(w, r, &RequiredError{Field: "receiving_address"}, nil)
		return
	}
	result, err := c.service.FetchQuote(r.Context(), sendingCurrencyCodeParam, receivingCurrencyCodeParam, lockedCurrencyAmountParam, lockedCurrencySideParam, receivingAddressParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// GetBalance - get_balance: Get the balance of the user's wallet
func (c *DefaultAPIController) GetBalance(w http.ResponseWriter, r *http.Request) {
	query, err := parseQuery(r.URL.RawQuery)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	var currencyCodeParam string
	if query.Has("currency_code") {
		param := query.Get("currency_code")

		currencyCodeParam = param
	} else {
	}
	result, err := c.service.GetBalance(r.Context(), currencyCodeParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// GetInfo - get_info: Get information about the user's wallet connection
func (c *DefaultAPIController) GetInfo(w http.ResponseWriter, r *http.Request) {
	result, err := c.service.GetInfo(r.Context())
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// LookupInvoice - lookup_invoice: Get an invoice by its payment hash
func (c *DefaultAPIController) LookupInvoice(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	paymentHashParam := params["payment_hash"]
	if paymentHashParam == "" {
		c.errorHandler(w, r, &RequiredError{"payment_hash"}, nil)
		return
	}
	result, err := c.service.LookupInvoice(r.Context(), paymentHashParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// LookupUser - lookup_user: Get receiver info by UMA
func (c *DefaultAPIController) LookupUser(w http.ResponseWriter, r *http.Request) {
	params := mux.Vars(r)
	query, err := parseQuery(r.URL.RawQuery)
	if err != nil {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	receiverUmaParam := params["receiver_uma"]
	if receiverUmaParam == "" {
		c.errorHandler(w, r, &RequiredError{"receiver_uma"}, nil)
		return
	}
	var baseSendingCurrencyCodeParam string
	if query.Has("base_sending_currency_code") {
		param := query.Get("base_sending_currency_code")

		baseSendingCurrencyCodeParam = param
	} else {
	}
	result, err := c.service.LookupUser(r.Context(), receiverUmaParam, baseSendingCurrencyCodeParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// MakeInvoice - make_invoice: Create a new invoice
func (c *DefaultAPIController) MakeInvoice(w http.ResponseWriter, r *http.Request) {
	makeInvoiceRequestParam := MakeInvoiceRequest{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(&makeInvoiceRequestParam); err != nil && !errors.Is(err, io.EOF) {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertMakeInvoiceRequestRequired(makeInvoiceRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertMakeInvoiceRequestConstraints(makeInvoiceRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.MakeInvoice(r.Context(), makeInvoiceRequestParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// PayInvoice - pay_invoice: Pay a bolt11 invoice
func (c *DefaultAPIController) PayInvoice(w http.ResponseWriter, r *http.Request) {
	payInvoiceRequestParam := PayInvoiceRequest{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(&payInvoiceRequestParam); err != nil && !errors.Is(err, io.EOF) {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertPayInvoiceRequestRequired(payInvoiceRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertPayInvoiceRequestConstraints(payInvoiceRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.PayInvoice(r.Context(), payInvoiceRequestParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}

// PayToAddress - pay_to_address: Pay to an LNURL address
func (c *DefaultAPIController) PayToAddress(w http.ResponseWriter, r *http.Request) {
	payToAddressRequestParam := PayToAddressRequest{}
	d := json.NewDecoder(r.Body)
	d.DisallowUnknownFields()
	if err := d.Decode(&payToAddressRequestParam); err != nil && !errors.Is(err, io.EOF) {
		c.errorHandler(w, r, &ParsingError{Err: err}, nil)
		return
	}
	if err := AssertPayToAddressRequestRequired(payToAddressRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	if err := AssertPayToAddressRequestConstraints(payToAddressRequestParam); err != nil {
		c.errorHandler(w, r, err, nil)
		return
	}
	result, err := c.service.PayToAddress(r.Context(), payToAddressRequestParam)
	// If an error occurred, encode the error with the status code
	if err != nil {
		c.errorHandler(w, r, err, &result)
		return
	}
	// If no error, encode the body and the result code
	_ = EncodeJSONResponse(result.Body, &result.Code, w)
}
