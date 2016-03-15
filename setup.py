from setuptools import setup

setup(name='fabrisunto',
      version='0.1',
      description='',
      url='https://github.com/buxur/fabrisunto',
      author='buxur',
      author_email='info@buxur.com',
      license='MIT',
      packages=['fabrisunto'],
      install_requires=[
          'boto3', 'argparse', 'sh', 'requests', 'gitpython', 'awscli', 'fabric'
      ],
      zip_safe=False)