from setuptools import setup, find_packages

setup(
    name="remotenet",
    version="1.0.0",
    description='Distributed Software Defined Network Emulation',
    long_description='Distributed Software Defined Network Emulation',
    keywords=['networking', 'emulator', 'containernet', 'mininet', 'OpenFlow', 'SDN', 'fog'],
    url='https://github.com/EsauM10/remotenet',
    author='Esaú Mascarenhas',
    author_email='esaumasc@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python 3.8',
        'Topic :: System :: Emulators'
        'Operating System :: Ubunbu OS'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'RunCluster = remotenet.server.cluster_app:main',
            'RunWorker = remotenet.server.worker_app:main',
        ]
    },
    zip_safe=False
)