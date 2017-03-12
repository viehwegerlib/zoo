from setuptools import setup

setup(name='zoo',
      version='0.1',
      description='A distributed microbial database',
      url='https://github.com/viehwegerlib/zoo',
      author='Adrian Viehweger',
      author_email='none',
      license='BSD 3-clause',
      packages=['zoo'],
      install_requires=[
          'numpy'
      ],
      zip_safe=False)
