from setuptools import setup, find_packages


requires = [
    'typer==0.4.1',
    'pandas==1.4.2',
    'azure-storage-blob==12.12.0',
    'twilio==7.9.0',
]

setup(
    name='DataWrangler',
    version='0.0.1',
    description='A CLI for pulling, pushing, and manipulating data',
    install_requires=requires,
    packages=find_packages(exclude=['tests']),
    entry_points={
        'console_scripts': [
            'wrangle=datawrangler.app',
        ],
    }
)
