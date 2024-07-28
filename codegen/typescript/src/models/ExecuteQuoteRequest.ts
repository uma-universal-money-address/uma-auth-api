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
 * @interface ExecuteQuoteRequest
 */
export interface ExecuteQuoteRequest {
    /**
     * The payment hash of the quote to execute.
     * @type {string}
     * @memberof ExecuteQuoteRequest
     */
    paymentHash: string;
}

/**
 * Check if a given object implements the ExecuteQuoteRequest interface.
 */
export function instanceOfExecuteQuoteRequest(value: object): value is ExecuteQuoteRequest {
    if (!('paymentHash' in value) || value['paymentHash'] === undefined) return false;
    return true;
}

export function ExecuteQuoteRequestFromJSON(json: any): ExecuteQuoteRequest {
    return ExecuteQuoteRequestFromJSONTyped(json, false);
}

export function ExecuteQuoteRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): ExecuteQuoteRequest {
    if (json == null) {
        return json;
    }
    return {
        
        'paymentHash': json['payment_hash'],
    };
}

export function ExecuteQuoteRequestToJSON(value?: ExecuteQuoteRequest | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'payment_hash': value['paymentHash'],
    };
}
