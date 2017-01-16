import io
from setuptools import setup

# Version
version = open('VERSION.txt').read()

# Long description
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r", "")
except OSError:
    print("Pandoc not found. Long_description conversion failure.")
    with io.open('README.md', encoding="utf-8") as f:
        long_description = f.read()

# Setup
setup(name='intrinio',
      version=version,
      description='Intrinio API client',
      long_description=long_description,
      keywords=['intrinio', 'API', 'data', 'client', 'quant', 'finance'],
      url='https://github.com/nhedlund/intrinio',
      author='nhedlund',
      license='MIT',
      packages=['intrinio'],
      zip_safe=False,
      install_requires=[
          'pandas >= 0.14',
          'numpy >= 1.8',
          'requests >= 2.7.0']
      )
