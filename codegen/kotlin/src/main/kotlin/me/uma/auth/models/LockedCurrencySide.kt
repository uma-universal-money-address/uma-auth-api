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
package me.uma.auth.models


/**
* The side of the quote which should be locked and specified in the `locked_currency_amount`. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \"sending\", and the `locked_currency_amount` to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \"receiving\" and the `locked_currency_amount` to 10000 (in cents).
* Values: sending,receiving
*/
enum class LockedCurrencySide(val value: kotlin.String) {

    sending("sending"),

    receiving("receiving");

}

