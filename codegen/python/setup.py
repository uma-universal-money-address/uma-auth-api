import sys
from setuptools import setup, find_packages

NAME = "uma_auth"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="UMA Auth API",
    author_email="info@lightspark.com",
    url="https://github.com/uma-universal-money-address/uma-auth-api",
    keywords=["OpenAPI", "UMA Auth API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['uma_auth=uma_auth.__main__:main']},
    long_description="""\
    This API allows you to authenticate with the UMA server to take actions on a user&#39;s wallet. It&#39;s the exposed communication layer between the NWC server and the main UMA server.
    """
)

