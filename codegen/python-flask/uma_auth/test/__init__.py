import logging

import connexion
from connexion.jsonifier import Jsonifier
from flask_testing import TestCase
from uma_auth.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = connexion.App(__name__, specification_dir="../openapi/")
        app.add_api(
            "openapi.yaml",
            arguments={"title": "UMA Auth API"},
            pythonic_params=True,
            jsonifier=Jsonifier(cls=JSONEncoder),
        )
        return app.app
