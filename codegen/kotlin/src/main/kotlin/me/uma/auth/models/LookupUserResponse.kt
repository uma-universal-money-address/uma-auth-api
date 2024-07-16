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

import me.uma.auth.models.CurrencyPreference

/**
 * 
 * @param currencies The currencies the receiver accepts in order of preference.
 */
data class LookupUserResponse(
    /* The currencies the receiver accepts in order of preference. */
    val currencies: kotlin.collections.List<CurrencyPreference>? = null
) 

