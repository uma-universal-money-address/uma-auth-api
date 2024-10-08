/**
* UMA Auth API
* This API allows you to authenticate with the UMA server to take actions on a user's wallet. It's the exposed communication layer between the NWC server and the main UMA server.
*
* The version of the OpenAPI document: 0.1
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
package me.uma.auth.apis

import com.google.gson.Gson
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.auth.*
import io.ktor.server.response.*
import me.uma.auth.Paths
import io.ktor.server.resources.options
import io.ktor.server.resources.get
import io.ktor.server.resources.post
import io.ktor.server.resources.put
import io.ktor.server.resources.delete
import io.ktor.server.resources.head
import io.ktor.server.resources.patch
import io.ktor.server.routing.*
import me.uma.auth.infrastructure.ApiPrincipal
import me.uma.auth.models.BudgetEstimateResponse
import me.uma.auth.models.ErrorResponse
import me.uma.auth.models.ExecuteQuoteRequest
import me.uma.auth.models.ExecuteQuoteResponse
import me.uma.auth.models.GetBalanceResponse
import me.uma.auth.models.GetInfoResponse
import me.uma.auth.models.ListTransactionsResponse
import me.uma.auth.models.LockedCurrencySide
import me.uma.auth.models.LookupUserResponse
import me.uma.auth.models.MakeInvoiceRequest
import me.uma.auth.models.PayInvoiceRequest
import me.uma.auth.models.PayInvoiceResponse
import me.uma.auth.models.PayKeysendRequest
import me.uma.auth.models.PayKeysendResponse
import me.uma.auth.models.PayToAddressRequest
import me.uma.auth.models.PayToAddressResponse
import me.uma.auth.models.Quote
import me.uma.auth.models.Transaction
import me.uma.auth.models.TransactionType

fun Route.UmaAuthApi() {
    val gson = Gson()
    val empty = mutableMapOf<String, Any?>()

    authenticate("bearerAuth") {
    post<Paths.executeQuote> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "total_budget_currency_amount" : 1000
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.fetchQuoteForLud16> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "receiving_currency" : {
                "symbol" : "$",
                "code" : "USD",
                "decimals" : 2,
                "name" : "United States Dollar"
              },
              "fees" : 10,
              "expires_at" : 1683148800,
              "total_sending_amount" : 123010,
              "total_receiving_amount" : 1000,
              "sending_currency" : {
                "symbol" : "$",
                "code" : "USD",
                "decimals" : 2,
                "name" : "United States Dollar"
              },
              "multiplier" : 123,
              "created_at" : 1683148800,
              "payment_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15"
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.getBalance> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "balance" : 1000,
              "currency" : {
                "symbol" : "$",
                "code" : "USD",
                "decimals" : 2,
                "name" : "United States Dollar"
              }
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.getBudgetEstimate> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "estimated_budget_currency_amount" : 1000
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.getInfo> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "color" : "#FF0000",
              "methods" : [ "make_invoice", "make_invoice" ],
              "lud16" : "$alice@vasp.net",
              "alias" : "Alice's Wallet",
              "block_hash" : "abcd1234",
              "block_height" : 1000,
              "pubkey" : "abcd1234",
              "network" : "testnet",
              "currencies" : [ {
                "min" : 1,
                "max" : 1000000,
                "multiplier" : 100000000,
                "currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                }
              }, {
                "min" : 1,
                "max" : 1000000,
                "multiplier" : 100000000,
                "currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                }
              } ]
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.listTransactions> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "transactions" : [ {
                "amount" : 1000,
                "fees_paid" : 1000,
                "metadata" : { },
                "expires_at" : 1683148800,
                "description_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",
                "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "description" : "Pay for pizza.",
                "created_at" : 1683148800,
                "invoice" : "lnbcrt1pjrsa37pp50geu5vxkzn4ddc4hmfkz9x308tw9lrrqtktz2hpm0rccjyhcyp5qdqh2d68yetpd45kueeqv3jk6mccqzpgxq9z0rgqsp5ge2rdw0tzvakxslmtvfmqf2fr7eucg9ughps5vdvp6fm2utk20rs9q8pqqqssqjs3k4nzrzg2nu9slu9c3srv2ae8v69ge097q9seukyw2nger8arj93m6erz8u657hfdzztfmc55wjjm9k337krl00fyw6s9nnwaafaspcqp2uv",
                "settled_at" : 1683148800,
                "type" : "incoming",
                "payment_hash" : "7332c2671019264cf0e9b8626bde20c9c3979799c570a276fb9512e22aef1f08"
              }, {
                "amount" : 1000,
                "fees_paid" : 1000,
                "metadata" : { },
                "expires_at" : 1683148800,
                "description_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",
                "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                "description" : "Pay for pizza.",
                "created_at" : 1683148800,
                "invoice" : "lnbcrt1pjrsa37pp50geu5vxkzn4ddc4hmfkz9x308tw9lrrqtktz2hpm0rccjyhcyp5qdqh2d68yetpd45kueeqv3jk6mccqzpgxq9z0rgqsp5ge2rdw0tzvakxslmtvfmqf2fr7eucg9ughps5vdvp6fm2utk20rs9q8pqqqssqjs3k4nzrzg2nu9slu9c3srv2ae8v69ge097q9seukyw2nger8arj93m6erz8u657hfdzztfmc55wjjm9k337krl00fyw6s9nnwaafaspcqp2uv",
                "settled_at" : 1683148800,
                "type" : "incoming",
                "payment_hash" : "7332c2671019264cf0e9b8626bde20c9c3979799c570a276fb9512e22aef1f08"
              } ]
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.lookupInvoice> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "amount" : 1000,
              "fees_paid" : 1000,
              "metadata" : { },
              "expires_at" : 1683148800,
              "description_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",
              "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "description" : "Pay for pizza.",
              "created_at" : 1683148800,
              "invoice" : "lnbcrt1pjrsa37pp50geu5vxkzn4ddc4hmfkz9x308tw9lrrqtktz2hpm0rccjyhcyp5qdqh2d68yetpd45kueeqv3jk6mccqzpgxq9z0rgqsp5ge2rdw0tzvakxslmtvfmqf2fr7eucg9ughps5vdvp6fm2utk20rs9q8pqqqssqjs3k4nzrzg2nu9slu9c3srv2ae8v69ge097q9seukyw2nger8arj93m6erz8u657hfdzztfmc55wjjm9k337krl00fyw6s9nnwaafaspcqp2uv",
              "settled_at" : 1683148800,
              "type" : "incoming",
              "payment_hash" : "7332c2671019264cf0e9b8626bde20c9c3979799c570a276fb9512e22aef1f08"
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    get<Paths.lookupUserByLud16> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "currencies" : [ {
                "min" : 1,
                "max" : 1000000,
                "multiplier" : 100000000,
                "currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                }
              }, {
                "min" : 1,
                "max" : 1000000,
                "multiplier" : 100000000,
                "currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                }
              } ]
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    post<Paths.makeInvoice> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "amount" : 1000,
              "fees_paid" : 1000,
              "metadata" : { },
              "expires_at" : 1683148800,
              "description_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15",
              "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "description" : "Pay for pizza.",
              "created_at" : 1683148800,
              "invoice" : "lnbcrt1pjrsa37pp50geu5vxkzn4ddc4hmfkz9x308tw9lrrqtktz2hpm0rccjyhcyp5qdqh2d68yetpd45kueeqv3jk6mccqzpgxq9z0rgqsp5ge2rdw0tzvakxslmtvfmqf2fr7eucg9ughps5vdvp6fm2utk20rs9q8pqqqssqjs3k4nzrzg2nu9slu9c3srv2ae8v69ge097q9seukyw2nger8arj93m6erz8u657hfdzztfmc55wjjm9k337krl00fyw6s9nnwaafaspcqp2uv",
              "settled_at" : 1683148800,
              "type" : "incoming",
              "payment_hash" : "7332c2671019264cf0e9b8626bde20c9c3979799c570a276fb9512e22aef1f08"
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    post<Paths.payInvoice> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "preimage" : "abcd1234",
              "total_budget_currency_amount" : 1000
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    post<Paths.payKeysend> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "total_budget_currency_amount" : 1000
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

    authenticate("bearerAuth") {
    post<Paths.payToLud16Address> {
        
        val principal = null!!
        
        
        val exampleContentType = "application/json"
            val exampleContentString = """{
              "quote" : {
                "receiving_currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                },
                "fees" : 10,
                "expires_at" : 1683148800,
                "total_sending_amount" : 123010,
                "total_receiving_amount" : 1000,
                "sending_currency" : {
                  "symbol" : "$",
                  "code" : "USD",
                  "decimals" : 2,
                  "name" : "United States Dollar"
                },
                "multiplier" : 123,
                "created_at" : 1683148800,
                "payment_hash" : "f1d2d2f924e986ac86fdf7b36c94bcdf32beec15"
              },
              "preimage" : "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "total_budget_currency_amount" : 1000
            }"""
            
            when (exampleContentType) {
                "application/json" -> call.respond(gson.fromJson(exampleContentString, empty::class.java))
                "application/xml" -> call.respondText(exampleContentString, ContentType.Text.Xml)
                else -> call.respondText(exampleContentString)
            }
        
    }
    }

}
