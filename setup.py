from setuptools import setup, find_packages

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name = 'hell_analysis',
  packages = find_packages(),
  include_package_data=True,
  version = '0.0.1',
  license='',
  description = 'Hell analysis for Laura',
  author = 'William Finnigan',
  author_email = 'wjafinnigan@gmail.com',
  url = '',
  download_url = '',
  keywords = ['sugar'],
  install_requires=requirements,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'],
)