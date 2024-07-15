# UMA Auth OpenAPI Spec

Contains the OpenAPI schema and codegen for the UMA Auth API for actions taken on a user's wallet.

See [markdown docs](./docs-markdown/README.md) or [html docs](./docs/index.html) for more information.

## Development

The schema is defined in `uma-auth-api.yaml`. To generate the docs, run:

Markdown:

```bash
# If needed, first run `brew install openapi-generator`
openapi-generator generate -g markdown -i uma-auth-api.yml -o docs-markdown
```

HTML:

```bash
npx @redocly/cli build-docs uma-auth-api.yml -o docs/index.html
```
