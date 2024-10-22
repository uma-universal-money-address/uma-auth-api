## @uma-universal-money-address/uma-auth-api@0.0.1

This generator creates TypeScript/JavaScript model types for UMA Auth API

### Building

To build and compile the typescript sources to javascript use:
```
npm install
npm run build
```

### Publishing

First build the package then run ```npm publish```

### Consuming

Navigate to the folder of your consuming project and run one of the following commands.

_published:_

```
npm install @uma-universal-money-address/uma-auth-api@0.0.1 --save
```

_unPublished (not recommended):_

```
npm install PATH_TO_GENERATED_PACKAGE --save
```

### Usage

This is an example of how to use these models in an UMA express server:

```
import { PayInvoiceRequestFromJSON, PayInvoiceResponse } from '@uma-universal-money-address/uma-auth-api';

app.post('/payments/bolt11', (req, res) => {
    try {
        const requestData = PayInvoiceRequestFromJSON(req.body);
    } catch (e) {
        res.status(400).send(`Invalid request: ${e}`);
        return;
    }

    const invoice = requestData.invoice;
    const amount = requestData.amount;

    // ... actually pay the invoice ...
    const response: PayInvoiceResponse = {
        preimage: paymentResult.preimage
    };
    return response;
});
```

Note that this library only contains request and response model types to help with type safety and encoding/decoding of requests and responses.
If you want something more custom for a specific API framework, you can generate your own code using the
[OpenAPI Generator CLI](https://openapi-generator.tech/docs/generators). 