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
import type { TransactionType } from './TransactionType';
import {
    TransactionTypeFromJSON,
    TransactionTypeFromJSONTyped,
    TransactionTypeToJSON,
} from './TransactionType';

/**
 * 
 * @export
 * @interface Transaction
 */
export interface Transaction {
    /**
     * 
     * @type {TransactionType}
     * @memberof Transaction
     */
    type: TransactionType;
    /**
     * The full, encoded invoice.
     * @type {string}
     * @memberof Transaction
     */
    invoice?: string | null;
    /**
     * The invoice's description.
     * @type {string}
     * @memberof Transaction
     */
    description?: string | null;
    /**
     * The invoice's description hash.
     * @type {string}
     * @memberof Transaction
     */
    descriptionHash?: string | null;
    /**
     * The payment preimage, optional if unpaid.
     * @type {string}
     * @memberof Transaction
     */
    preimage?: string | null;
    /**
     * Payment hash for the payment
     * @type {string}
     * @memberof Transaction
     */
    paymentHash: string;
    /**
     * Value in msats.
     * @type {number}
     * @memberof Transaction
     */
    amount: number;
    /**
     * Value in msats.
     * @type {number}
     * @memberof Transaction
     */
    feesPaid?: number | null;
    /**
     * The time the payment/invoice was created.
     * @type {number}
     * @memberof Transaction
     */
    createdAt: number;
    /**
     * The time the invoice expires.
     * @type {number}
     * @memberof Transaction
     */
    expiresAt?: number | null;
    /**
     * Additional metadata attached to the invoice.
     * @type {object}
     * @memberof Transaction
     */
    metadata?: object | null;
}

/**
 * Check if a given object implements the Transaction interface.
 */
export function instanceOfTransaction(value: object): value is Transaction {
    if (!('type' in value) || value['type'] === undefined) return false;
    if (!('paymentHash' in value) || value['paymentHash'] === undefined) return false;
    if (!('amount' in value) || value['amount'] === undefined) return false;
    if (!('createdAt' in value) || value['createdAt'] === undefined) return false;
    return true;
}

export function TransactionFromJSON(json: any): Transaction {
    return TransactionFromJSONTyped(json, false);
}

export function TransactionFromJSONTyped(json: any, ignoreDiscriminator: boolean): Transaction {
    if (json == null) {
        return json;
    }
    return {
        
        'type': TransactionTypeFromJSON(json['type']),
        'invoice': json['invoice'] == null ? undefined : json['invoice'],
        'description': json['description'] == null ? undefined : json['description'],
        'descriptionHash': json['description_hash'] == null ? undefined : json['description_hash'],
        'preimage': json['preimage'] == null ? undefined : json['preimage'],
        'paymentHash': json['payment_hash'],
        'amount': json['amount'],
        'feesPaid': json['fees_paid'] == null ? undefined : json['fees_paid'],
        'createdAt': json['created_at'],
        'expiresAt': json['expires_at'] == null ? undefined : json['expires_at'],
        'metadata': json['metadata'] == null ? undefined : json['metadata'],
    };
}

export function TransactionToJSON(value?: Transaction | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'type': TransactionTypeToJSON(value['type']),
        'invoice': value['invoice'],
        'description': value['description'],
        'description_hash': value['descriptionHash'],
        'preimage': value['preimage'],
        'payment_hash': value['paymentHash'],
        'amount': value['amount'],
        'fees_paid': value['feesPaid'],
        'created_at': value['createdAt'],
        'expires_at': value['expiresAt'],
        'metadata': value['metadata'],
    };
}

