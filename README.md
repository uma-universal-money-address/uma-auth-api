# [Work In Progress] UMA Auth OpenAPI Spec

**This is a super early alpha and is not yet ready for production use**

Contains the OpenAPI schema and codegen for the UMA Auth API for actions taken on a user's wallet. This will be wrapped in an NWC proxy to be consumed via Nostr Wallet Connect client apps.

See [markdown docs](./docs-markdown/README.md) or [html docs](./docs/index.html) for more information.

## Development

The schema is defined in `uma-auth-api.yaml`. To regenerate the docs and generated libs, run:

```bash
./generate-all.sh
```
