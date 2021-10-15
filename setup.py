from setuptools import setup

VERSION = '1.0.2'

setup(
    name='krypto',
    version=VERSION,

    description='Encrypt and decrypt data using RSA certificates.',
    url='https://github.com/Christophe-Gauge/krypto',

    author='Christophe Gauge',
    author_email='chris@videre.us',

    packages=['krypto'],

    install_requires=['pycryptodome'],

    entry_points={
        'console_scripts': [
            'krypto = krypto.__main__:main'
        ]
    },

)
