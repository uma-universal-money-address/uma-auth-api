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
package me.uma.auth

import io.ktor.resources.*
import kotlinx.serialization.*
import me.uma.auth.models.*

object Paths {
    /**
     * execute_quote: Execute a quote
     * 
     * @param paymentHash The payment hash of the quote to execute. 
     */
    @Serializable @Resource("/quote/{payment_hash}") class executeQuote(val paymentHash: kotlin.String)

    /**
     * fetch_quote_for_lud16: Get a quote for a payment to an LUD16 address
     * 
     * @param sendingCurrencyCode The currency code being sent from the sender&#39;s wallet. 
     * @param receivingCurrencyCode The currency code of the currency that the receiver will receive. 
     * @param lockedCurrencyAmount The amount to send/receive in the smallest unit of the locked currency (eg. cents). See &#x60;locked_currency_side&#x60; for more information. 
     * @param lockedCurrencySide The side of the quote which should be locked and specified in the &#x60;locked_currency_amount&#x60;. For example, if I want to send exactly $5 MXN from my wallet, I would set this to \&quot;sending\&quot;, and the &#x60;locked_currency_amount&#x60; to 500 (in cents). If I want the receiver to receive exactly $10 USD, I would set this to \&quot;receiving\&quot; and the &#x60;locked_currency_amount&#x60; to 10000 (in cents). 
     * @param receiverAddress The LUD16 address to send the payment to. 
     */
    @Serializable @Resource("/quote/lud16") class fetchQuoteForLud16(val sendingCurrencyCode: kotlin.String, val receivingCurrencyCode: kotlin.String, val lockedCurrencyAmount: kotlin.Long, val lockedCurrencySide: kotlin.String, val receiverAddress: kotlin.String)

    /**
     * get_balance: Get the balance of the user&#39;s wallet
     * 
     * @param currencyCode The currency code of the balance. Assumed to be in msats if not provided.  (optional)
     */
    @Serializable @Resource("/balance") class getBalance(val currencyCode: kotlin.String? = null)

    /**
     * get_info: Get information about the user&#39;s wallet connection
     * 
     */
    @Serializable @Resource("/info") class getInfo

    /**
     * list_transactions: Lists invoices and payments
     * 
     * @param from Starting timestamp in seconds since epoch (inclusive). (optional)
     * @param until Ending timestamp in seconds since epoch (inclusive). (optional)
     * @param limit Maximum number of transactions to return. (optional)
     * @param offset Offset of the first transaction to return. (optional)
     * @param unpaid Whether to include unpaid invoices. (optional)
     * @param type Type of transactions to return: \&quot;incoming\&quot; for invoices, \&quot;outgoing\&quot; for payments, undefined for both. (optional)
     */
    @Serializable @Resource("/transactions") class listTransactions(val from: kotlin.Int? = null, val until: kotlin.Int? = null, val limit: kotlin.Int? = null, val offset: kotlin.Int? = null, val unpaid: kotlin.Boolean? = null, val type: TransactionType? = null)

    /**
     * lookup_invoice: Get an invoice by its payment hash
     * 
     * @param paymentHash The payment hash of the invoice. 
     */
    @Serializable @Resource("/invoices/{payment_hash}") class lookupInvoice(val paymentHash: kotlin.String)

    /**
     * lookup_user_by_lud16: Get receiver info by LUD16 address.
     * 
     * @param receiverAddress The receiver&#39;s LUD16 address. 
     * @param baseSendingCurrencyCode The currency code of the sender&#39;s balance. Assumed to be in msats if not provided.  This is used to calculate the multiplier for the receiver&#39;s currencies. (optional)
     */
    @Serializable @Resource("/receiver/lud16/{receiver_address}") class lookupUserByLud16(val receiverAddress: kotlin.String, val baseSendingCurrencyCode: kotlin.String? = null)

    /**
     * make_invoice: Create a new invoice
     * 
     * @param makeInvoiceRequest  (optional)
     */
    @Serializable @Resource("/invoice") class makeInvoice(val makeInvoiceRequest: MakeInvoiceRequest? = null)

    /**
     * pay_invoice: Pay a bolt11 invoice
     * 
     * @param payInvoiceRequest  (optional)
     */
    @Serializable @Resource("/payments/bolt11") class payInvoice(val payInvoiceRequest: PayInvoiceRequest? = null)

    /**
     * pay_keysend: Pay directly to the pubkey of the receiver node based on a fixed receiving amount
     * 
     * @param payKeysendRequest  (optional)
     */
    @Serializable @Resource("/payments/keysend") class payKeysend(val payKeysendRequest: PayKeysendRequest? = null)

    /**
     * pay_to_lud16_address: Pay directly to an LNURL address based on a fixed sending amount.
     * 
     * @param payToAddressRequest  (optional)
     */
    @Serializable @Resource("/payments/lud16") class payToLud16Address(val payToAddressRequest: PayToAddressRequest? = null)

}
