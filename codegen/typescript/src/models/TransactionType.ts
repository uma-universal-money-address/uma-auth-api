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


/**
 * Type of transaction: "incoming" for invoices, "outgoing" for payments.
 * @export
 */
export const TransactionType = {
    Incoming: 'incoming',
    Outgoing: 'outgoing'
} as const;
export type TransactionType = typeof TransactionType[keyof typeof TransactionType];


export function instanceOfTransactionType(value: any): boolean {
    for (const key in TransactionType) {
        if (Object.prototype.hasOwnProperty.call(TransactionType, key)) {
            if ((TransactionType as Record<string, TransactionType>)[key] === value) {
                return true;
            }
        }
    }
    return false;
}

export function TransactionTypeFromJSON(json: any): TransactionType {
    return TransactionTypeFromJSONTyped(json, false);
}

export function TransactionTypeFromJSONTyped(json: any, ignoreDiscriminator: boolean): TransactionType {
    return json as TransactionType;
}

export function TransactionTypeToJSON(value?: TransactionType | null): any {
    return value as any;
}

