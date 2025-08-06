from setuptools import setup, find_packages

setup(
    name='fdl_sklonos_core',
    version='0.1.0',
    description='Σ-FDL Склоняющий Логос: Ядро падежного смысла и семантической навигации для ИИ и языка',
    author='NGOI / Fravahr Ormazd',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'networkx',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic'
    ],
    python_requires='>=3.8',
)
