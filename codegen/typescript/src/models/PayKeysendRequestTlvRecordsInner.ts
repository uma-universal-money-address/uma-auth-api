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
 * The tlv record.
 * @export
 * @interface PayKeysendRequestTlvRecordsInner
 */
export interface PayKeysendRequestTlvRecordsInner {
    /**
     * The tlv type
     * @type {number}
     * @memberof PayKeysendRequestTlvRecordsInner
     */
    type: number;
    /**
     * The hex encoded tlv value.
     * @type {string}
     * @memberof PayKeysendRequestTlvRecordsInner
     */
    value: string;
}

/**
 * Check if a given object implements the PayKeysendRequestTlvRecordsInner interface.
 */
export function instanceOfPayKeysendRequestTlvRecordsInner(value: object): value is PayKeysendRequestTlvRecordsInner {
    if (!('type' in value) || value['type'] === undefined) return false;
    if (!('value' in value) || value['value'] === undefined) return false;
    return true;
}

export function PayKeysendRequestTlvRecordsInnerFromJSON(json: any): PayKeysendRequestTlvRecordsInner {
    return PayKeysendRequestTlvRecordsInnerFromJSONTyped(json, false);
}

export function PayKeysendRequestTlvRecordsInnerFromJSONTyped(json: any, ignoreDiscriminator: boolean): PayKeysendRequestTlvRecordsInner {
    if (json == null) {
        return json;
    }
    return {
        
        'type': json['type'],
        'value': json['value'],
    };
}

export function PayKeysendRequestTlvRecordsInnerToJSON(value?: PayKeysendRequestTlvRecordsInner | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'type': value['type'],
        'value': value['value'],
    };
}
