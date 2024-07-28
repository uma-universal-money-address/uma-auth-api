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
 * @interface PayInvoiceResponse
 */
export interface PayInvoiceResponse {
    /**
     * The preimage of the payment.
     * @type {string}
     * @memberof PayInvoiceResponse
     */
    preimage: string;
}

/**
 * Check if a given object implements the PayInvoiceResponse interface.
 */
export function instanceOfPayInvoiceResponse(value: object): value is PayInvoiceResponse {
    if (!('preimage' in value) || value['preimage'] === undefined) return false;
    return true;
}

export function PayInvoiceResponseFromJSON(json: any): PayInvoiceResponse {
    return PayInvoiceResponseFromJSONTyped(json, false);
}

export function PayInvoiceResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): PayInvoiceResponse {
    if (json == null) {
        return json;
    }
    return {
        
        'preimage': json['preimage'],
    };
}

export function PayInvoiceResponseToJSON(value?: PayInvoiceResponse | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'preimage': value['preimage'],
    };
}
