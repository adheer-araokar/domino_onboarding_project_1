#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from controllers.drift_calculator import api_v1


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.app.register_blueprint(api_v1)
    app.add_api('swagger.yaml', arguments={'title': 'Drift Calculator'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
