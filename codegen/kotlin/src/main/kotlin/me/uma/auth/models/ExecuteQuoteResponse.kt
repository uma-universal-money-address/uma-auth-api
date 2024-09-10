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
 * @param preimage The preimage of the payment.
 * @param totalBudgetCurrencyAmount The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null. 
 */
data class ExecuteQuoteResponse(
    /* The preimage of the payment. */
    val preimage: kotlin.String,
    /* The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null.  */
    val totalBudgetCurrencyAmount: kotlin.Long? = null
) 

