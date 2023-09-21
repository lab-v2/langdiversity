from setuptools import find_packages, setup

# Read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='langdiversity',
    packages=find_packages(exclude=['tests']),
    version='1.0.1',
    description='A tool to elevate your language models with insightful diversity metrics.',
    long_description=long_description,  
    long_description_content_type="text/markdown",  
    author='Noel Ngu, Nathaniel Lee',                        
    author_email='nngu2@asu.edu, nlee51@asu.edu',             
    url='https://github.com/lab-v2/diversity_package',  
    license='BSD 3-clause',
    install_requires=[
        'aiohttp==3.8.5',
        'aiosignal==1.3.1',
        'annotated-types==0.5.0',
        'async-timeout==4.0.3',
        'attrs==23.1.0',
        'certifi==2023.7.22',
        'charset-normalizer==3.2.0',
        'dataclasses-json==0.5.14',
        'frozenlist==1.4.0',
        'greenlet==2.0.2',
        'idna==3.4',
        'langchain==0.0.281',
        'langsmith==0.0.33',
        'marshmallow==3.20.1',
        'multidict==6.0.4',
        'mypy-extensions==1.0.0',
        'numexpr==2.8.5',
        'numpy==1.25.2',
        'packaging==23.1',
        'pydantic==2.3.0',
        'pydantic_core==2.6.3',
        'PyYAML==6.0.1',
        'requests==2.31.0',
        'SQLAlchemy==2.0.20',
        'tenacity==8.2.3',
        'typing-inspect==0.9.0',
        'typing_extensions==4.7.1',
        'urllib3==2.0.4',
        'yarl==1.9.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

    ],
    python_requires='>=3.9',
)
