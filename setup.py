from setuptools import setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

AUTHOR_NAME  = 'NOEL ZIN'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = [
    'streamlit',
    'pandas',
    'scikit-learn',
    'nltk',
    'requests',
    'beautifulsoup4'
]

setup(
    name = SRC_REPO,
    version = '0.0.1',
    author = AUTHOR_NAME,
    author_email = 'channyeinzin.fl@gmail.com',
    description = 'perfume recommendation small package',
    long_description = long_description,
    long_description_content_type= 'text/markdown',
    packages = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS,
)
