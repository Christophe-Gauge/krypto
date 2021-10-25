from setuptools import setup, find_packages

VERSION = '1.0.3'

setup(
    name='rsa_crypto',
    version=VERSION,

    description='Encrypt and decrypt data using RSA certificates.',
    url='https://github.com/Christophe-Gauge/rsa_crypto',

    author='Christophe Gauge',
    author_email='chris@videre.us',
    license='GNU',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    # packages=[
    #     'rsa_crypto'
    #     ],
    py_modules=['rsa_crypto'],
    install_requires=['pycryptodome'],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3",

    entry_points={
        'console_scripts': [
            'rsa_crypto = rsa_crypto:main'
        ]
    },

)