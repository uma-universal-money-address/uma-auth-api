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
 * 
 * @param amount The amount to invoice in msats.
 * @param description A memo to attach to the invoice.
 * @param descriptionHash A hash of a longer description field.
 * @param expiry The number of seconds until the invoice expires.
 */
data class MakeInvoiceRequest(
    /* The amount to invoice in msats. */
    val amount: java.math.BigDecimal,
    /* A memo to attach to the invoice. */
    val description: kotlin.String? = null,
    /* A hash of a longer description field. */
    val descriptionHash: kotlin.String? = null,
    /* The number of seconds until the invoice expires. */
    val expiry: java.math.BigDecimal? = null
) 

