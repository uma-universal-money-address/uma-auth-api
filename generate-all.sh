#!/bin/sh

pushd `dirname $0` > /dev/null

echo "Generating docs..."
openapi-generator generate -g markdown -i uma-auth-api.yml -o docs-markdown
npx @redocly/cli build-docs uma-auth-api.yml -o docs/index.html

echo "Generating clients..."
openapi-generator generate -g go-server -i uma-auth-api.yml -o codegen/go --package-name umaauth

popd > /dev/null
