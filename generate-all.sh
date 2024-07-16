#!/bin/sh

pushd `dirname $0` > /dev/null

echo "Generating docs..."
openapi-generator generate -g markdown -i uma-auth-api.yml -o docs-markdown
npx @redocly/cli build-docs uma-auth-api.yml -o docs/index.html

echo "Generating clients...\n\n"

echo "Generating Golang library..."
openapi-generator generate -g go-server -i uma-auth-api.yml -o codegen/go --package-name umaauth

echo "Generating Python library..."
openapi-generator generate -g python-flask -i uma-auth-api.yml -o codegen/python --package-name umaauth

echo "Generating Kotlin library..."
openapi-generator generate -g kotlin-server -i uma-auth-api.yml -o codegen/kotlin --package-name me.uma.auth --group-id me.uma --artifact-id uma-auth-server

popd > /dev/null
