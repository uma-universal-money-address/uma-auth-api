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
 * @interface ErrorResponse
 */
export interface ErrorResponse {
    /**
     * The error code.
     * @type {string}
     * @memberof ErrorResponse
     */
    code: string;
    /**
     * The error message.
     * @type {string}
     * @memberof ErrorResponse
     */
    message: string;
}

/**
 * Check if a given object implements the ErrorResponse interface.
 */
export function instanceOfErrorResponse(value: object): value is ErrorResponse {
    if (!('code' in value) || value['code'] === undefined) return false;
    if (!('message' in value) || value['message'] === undefined) return false;
    return true;
}

export function ErrorResponseFromJSON(json: any): ErrorResponse {
    return ErrorResponseFromJSONTyped(json, false);
}

export function ErrorResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): ErrorResponse {
    if (json == null) {
        return json;
    }
    return {
        
        'code': json['code'],
        'message': json['message'],
    };
}

export function ErrorResponseToJSON(value?: ErrorResponse | null): any {
    if (value == null) {
        return value;
    }
    return {
        
        'code': value['code'],
        'message': value['message'],
    };
}

