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
import type { Quote } from './Quote';
import {
    QuoteFromJSON,
    QuoteFromJSONTyped,
    QuoteToJSON,
} from './Quote';

/**
 * 
 * @export
 * @interface PayToAddressResponse
 */
export interface PayToAddressResponse {
    /**
     * The preimage of the payment.
     * @type {string}
     * @memberof PayToAddressResponse
     */
    preimage: string;
    /**
     * 
     * @type {Quote}
     * @memberof PayToAddressResponse
     */
    quote: Quote;
    /**
     * The total cost of the payment in the smallest unit of `budget_currency_code` in the request. This is the amount that will be deducted from the budget  for this connection. Optional if `budget_currency_code` is null. 
     * @type {number}
     * @memberof PayToAddressResponse
     */
    totalBudgetCurrencyAmount?: number;
}

/**
 * Check if a given object implements the PayToAddressResponse interface.
 */
export function instanceOfPayToAddressResponse(value: object): value is PayToAddressResponse {
    if (!('preimage' in value) || value['preimage'] === undefined) return false;
    if (!('quote' in value) || value['quote'] === undefined) return false;
    return true;
}

export function PayToAddressResponseFromJSON(json: any): PayToAddressResponse {
    return PayToAddressResponseFromJSONTyped(json, false);
}

export function PayToAddressResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): PayToAddressResponse {
    if (json == null) {
        return json;
    }
    return {
        
        'preimage': json['preimage'],
        'quote': QuoteFromJSON(json['quote']),
        'totalBudgetCurrencyAmount': json['total_budget_currency_amount'] == null ? undefined : json['total_budget_currency_amount'],
    };
}

export function PayToAddressResponseToJSON(value?: PayToAddressResponse | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'preimage': value['preimage'],
        'quote': QuoteToJSON(value['quote']),
        'total_budget_currency_amount': value['totalBudgetCurrencyAmount'],
    };
}

