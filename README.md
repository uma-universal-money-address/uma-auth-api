# UMA Auth OpenAPI Spec

Contains the OpenAPI schema and codegen for the UMA Auth API for actions taken on a user's wallet. This will be wrapped in an NWC proxy to be consumed via Nostr Wallet Connect client apps.

See [markdown docs](./docs-markdown/README.md) or [html docs](./docs/index.html) for more information.

## Development

The schema is defined in `uma-auth-api.yaml`. To regenerate the docs and generated libs, run:

```bash
./generate-all.sh
```

## Usage

The [`codegen/`](./codegen/) folder contains generated models libraries for Go, Kotlin/Java, Python and TypeScript. If you are using a different framework or language, you can generate the library yourself using the schema defined in `uma-auth-api.yaml`. See the full list of OpenAPI generators [here](https://openapi-generator.tech/docs/generators).

Refer to the [full API spec documentation](https://uma-universal-money-address.github.io/uma-auth-api/) or in [markdown](https://github.com/uma-universal-money-address/uma-auth-api/tree/main/docs-markdown) for details on the API endpoints and models. You'll need to implement these in your server to handle UMA Auth requests. The generated libraries provide most of the foundational code, and you'll connect them with your existing UMA implementation. It is not mandatory to support all of the endpoints, but doing so will provide the best experience to your users.

See the detailed implementation guide [here](https://docs.uma.me/uma-auth/vasp-open-api-schema).
