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
	"context"
	"net/http"
)



// UmaAuthAPIRouter defines the required methods for binding the api requests to a responses for the UmaAuthAPI
// The UmaAuthAPIRouter implementation should parse necessary information from the http request,
// pass the data to a UmaAuthAPIServicer to perform the required actions, then write the service results to the http response.
type UmaAuthAPIRouter interface { 
	ExecuteQuote(http.ResponseWriter, *http.Request)
	FetchQuoteForLud16(http.ResponseWriter, *http.Request)
	GetBalance(http.ResponseWriter, *http.Request)
	GetBudgetEstimate(http.ResponseWriter, *http.Request)
	GetInfo(http.ResponseWriter, *http.Request)
	ListTransactions(http.ResponseWriter, *http.Request)
	LookupInvoice(http.ResponseWriter, *http.Request)
	LookupUserByLud16(http.ResponseWriter, *http.Request)
	MakeInvoice(http.ResponseWriter, *http.Request)
	PayInvoice(http.ResponseWriter, *http.Request)
	PayKeysend(http.ResponseWriter, *http.Request)
	PayToLud16Address(http.ResponseWriter, *http.Request)
}


// UmaAuthAPIServicer defines the api actions for the UmaAuthAPI service
// This interface intended to stay up to date with the openapi yaml used to generate it,
// while the service implementation can be ignored with the .openapi-generator-ignore file
// and updated with the logic required for the API.
type UmaAuthAPIServicer interface { 
	ExecuteQuote(context.Context, string, ExecuteQuoteRequest) (ImplResponse, error)
	FetchQuoteForLud16(context.Context, string, string, int64, LockedCurrencySide, string) (ImplResponse, error)
	GetBalance(context.Context, string) (ImplResponse, error)
	GetBudgetEstimate(context.Context, string, int64, string) (ImplResponse, error)
	GetInfo(context.Context) (ImplResponse, error)
	ListTransactions(context.Context, int64, int64, int32, int32, bool, TransactionType) (ImplResponse, error)
	LookupInvoice(context.Context, string) (ImplResponse, error)
	LookupUserByLud16(context.Context, string, string) (ImplResponse, error)
	MakeInvoice(context.Context, MakeInvoiceRequest) (ImplResponse, error)
	PayInvoice(context.Context, PayInvoiceRequest) (ImplResponse, error)
	PayKeysend(context.Context, PayKeysendRequest) (ImplResponse, error)
	PayToLud16Address(context.Context, PayToAddressRequest) (ImplResponse, error)
}
