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

import me.uma.auth.models.Currency

/**
 * 
 * @param currency 
 * @param multiplier Estimated number of milli-sats per smallest unit of this currency (eg. cents) If base_sending_currency_code was specified, this is the rate relative to that currency instead of milli-sats.
 * @param min The minimum amount that can be received in this currency.
 * @param max The maximum amount that can be received in this currency.
 */
data class CurrencyPreference(
    val currency: Currency,
    /* Estimated number of milli-sats per smallest unit of this currency (eg. cents) If base_sending_currency_code was specified, this is the rate relative to that currency instead of milli-sats. */
    val multiplier: java.math.BigDecimal,
    /* The minimum amount that can be received in this currency. */
    val min: kotlin.Long,
    /* The maximum amount that can be received in this currency. */
    val max: kotlin.Long
) 

