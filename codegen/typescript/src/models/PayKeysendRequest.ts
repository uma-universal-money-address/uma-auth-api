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
import type { PayKeysendRequestTlvRecordsInner } from './PayKeysendRequestTlvRecordsInner';
import {
    PayKeysendRequestTlvRecordsInnerFromJSON,
    PayKeysendRequestTlvRecordsInnerFromJSONTyped,
    PayKeysendRequestTlvRecordsInnerToJSON,
} from './PayKeysendRequestTlvRecordsInner';

/**
 * 
 * @export
 * @interface PayKeysendRequest
 */
export interface PayKeysendRequest {
    /**
     * The amount to pay in msats.
     * @type {number}
     * @memberof PayKeysendRequest
     */
    amount: number;
    /**
     * The public key of the receiver's node.
     * @type {string}
     * @memberof PayKeysendRequest
     */
    pubkey: string;
    /**
     * Preimage of the payment.
     * @type {string}
     * @memberof PayKeysendRequest
     */
    preimage?: string;
    /**
     * The tlv records.
     * @type {Array<PayKeysendRequestTlvRecordsInner>}
     * @memberof PayKeysendRequest
     */
    tlvRecords?: Array<PayKeysendRequestTlvRecordsInner>;
    /**
     * The code of the currency the sender used to set budget.  Optional if the budget is set to SAT.
     * @type {string}
     * @memberof PayKeysendRequest
     */
    budgetCurrencyCode?: string;
}

/**
 * Check if a given object implements the PayKeysendRequest interface.
 */
export function instanceOfPayKeysendRequest(value: object): value is PayKeysendRequest {
    if (!('amount' in value) || value['amount'] === undefined) return false;
    if (!('pubkey' in value) || value['pubkey'] === undefined) return false;
    return true;
}

export function PayKeysendRequestFromJSON(json: any): PayKeysendRequest {
    return PayKeysendRequestFromJSONTyped(json, false);
}

export function PayKeysendRequestFromJSONTyped(json: any, ignoreDiscriminator: boolean): PayKeysendRequest {
    if (json == null) {
        return json;
    }
    return {
        
        'amount': json['amount'],
        'pubkey': json['pubkey'],
        'preimage': json['preimage'] == null ? undefined : json['preimage'],
        'tlvRecords': json['tlv_records'] == null ? undefined : ((json['tlv_records'] as Array<any>).map(PayKeysendRequestTlvRecordsInnerFromJSON)),
        'budgetCurrencyCode': json['budget_currency_code'] == null ? undefined : json['budget_currency_code'],
    };
}

export function PayKeysendRequestToJSON(value?: PayKeysendRequest | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'amount': value['amount'],
        'pubkey': value['pubkey'],
        'preimage': value['preimage'],
        'tlv_records': value['tlvRecords'] == null ? undefined : ((value['tlvRecords'] as Array<any>).map(PayKeysendRequestTlvRecordsInnerToJSON)),
        'budget_currency_code': value['budgetCurrencyCode'],
    };
}

