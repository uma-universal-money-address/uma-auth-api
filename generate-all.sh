#!/bin/sh

pushd `dirname $0` > /dev/null

echo "Generating docs..."
openapi-generator generate -g markdown -i uma-auth-api.yml -o docs-markdown
npx @redocly/cli build-docs uma-auth-api.yml -o docs/index.html

echo "Generating clients...\n\n"

echo "Generating Golang library..."
openapi-generator generate -g go-server -i uma-auth-api.yml -o codegen/go --package-name umaauth -c codegen-config/go/config.yml

echo "Generating Python Models library..."
openapi-generator generate -g python-fastapi -i uma-auth-api.yml -o codegen/python-models -c codegen-config/python-fastapi-models/config.yml --global-property=models,supportingFiles

echo "Generating Python Flask library..."
openapi-generator generate -g python-flask -i uma-auth-api.yml -o codegen/python-flask -c codegen-config/python-flask/config.yml

echo "Generating Kotlin library..."
openapi-generator generate -g kotlin-server -i uma-auth-api.yml -o codegen/kotlin --package-name me.uma.auth --group-id me.uma --artifact-id uma-auth-server

echo "Generating Typescript library..."
openapi-generator generate -g typescript-fetch -i uma-auth-api.yml -o codegen/typescript --global-property=models,supportingFiles -c codegen-config/typescript/config.yaml

popd > /dev/null
