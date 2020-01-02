import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder

from controllers.drift_calculator import api_v1


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.register_blueprint(api_v1)
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
