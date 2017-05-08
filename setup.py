from distutils.core import setup

setup(name='CrackMyARS',
        version='0.1',
        description='Robust RSA Cracking Tool',
        author='Joshua Jacob, Harrison Wilco',
        url='https://github.com/jacobj10/CrackMyARS',

        requires=['FactorDB', 'Crypto', 'gmpy'],
        provides=['CrackMyARS'],
        packages=['CrackMyARS', 'CrackMyARS.utils', 'CrackMyARS.attacks'],
        package_dir={'': 'lib'}
    )
