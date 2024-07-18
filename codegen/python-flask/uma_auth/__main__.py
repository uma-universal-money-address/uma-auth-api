#!/usr/bin/env python3

import connexion
import connexion.jsonifier

from uma_auth import encoder


def main():
    app = connexion.FlaskApp(__name__, specification_dir="./openapi/")
    app.add_api(
        "openapi.yaml",
        arguments={"title": "UMA Auth API"},
        pythonic_params=True,
        jsonifier=connexion.jsonifier.Jsonifier(cls=encoder.JSONEncoder),
    )

    app.run(port=8080)


if __name__ == "__main__":
    main()
