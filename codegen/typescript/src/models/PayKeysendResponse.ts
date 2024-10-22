/* tslint:disable */
/* eslint-disable */
/**
 * UMA Auth API
 * This API allows you to authenticate with the UMA server to take actions on a user\'s wallet. It\'s the exposed communication layer between the NWC server and the main UMA server.
 *
 * The version of the OpenAPI document: 0.1
 * Contact: info@lightspark.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { mapValues } from '../runtime';
/**
 * 
 * @export
 * @interface PayKeysendResponse
 */
export interface PayKeysendResponse {
    /**
     * The preimage of the payment.
     * @type {string}
     * @memberof PayKeysendResponse
     */
    preimage: string;
    /**
     * The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null. 
     * @type {number}
     * @memberof PayKeysendResponse
     */
    totalBudgetCurrencyAmount?: number;
}

/**
 * Check if a given object implements the PayKeysendResponse interface.
 */
export function instanceOfPayKeysendResponse(value: object): value is PayKeysendResponse {
    if (!('preimage' in value) || value['preimage'] === undefined) return false;
    return true;
}

export function PayKeysendResponseFromJSON(json: any): PayKeysendResponse {
    return PayKeysendResponseFromJSONTyped(json, false);
}

export function PayKeysendResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): PayKeysendResponse {
    if (json == null) {
        return json;
    }
    return {
        
        'preimage': json['preimage'],
        'totalBudgetCurrencyAmount': json['total_budget_currency_amount'] == null ? undefined : json['total_budget_currency_amount'],
    };
}

export function PayKeysendResponseToJSON(value?: PayKeysendResponse | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'preimage': value['preimage'],
        'total_budget_currency_amount': value['totalBudgetCurrencyAmount'],
    };
}

