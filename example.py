import krypto.__main__ as krypto
import argparse


# encrypt a value in the DEFAULT section
args = argparse.Namespace(option='test')
myVar = krypto.encrypt_value(args)

# encrypt a value in mysection and set a value
args = argparse.Namespace(section='mysection', option='myoption', value='myvalue')
myVar = krypto.encrypt_value(args)


# encrypt a value in mysection and prompt for a value to set
args = argparse.Namespace(section='mysection', option='myoption')
myVar = krypto.decrypt_value(args)
print(myVar)

# Encrypt a file my_secret_file.txt with a key prefix of dev
args = argparse.Namespace(file='my_secret_file.txt', key='rsa')
myVar = krypto.encrypt_file(args)

# Set an unencrypted value in the configuration file
krypto.set_value_config('url', b'htps://...', '')

# Retreive the unencrypted value
enc_data = krypto.get_value_config('url')
print(enc_data)
