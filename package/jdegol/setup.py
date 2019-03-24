from setuptools import setup
from distutils.cmd import Command
from distutils.core import setup

def readme():
    with open('README.rst') as f:
        return f.read()
    
setup(name='jdegol',
      version='0.1',
      description='Game of life implementation for GSoC (JDE Robots)',
      long_description=readme(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Topic :: Game'
      ],
      keywords='game life conway jderobots jde robot',
      url='http://github.com/shubhanshu07/jdegol',
      author='Shubhanshu Agarwal',
      author_email='agarwal.shubhanshu07@gmail.com',
      license='MIT',
      packages=['jdegol'],
      zip_safe=False,
      test_suite = 'jdegol.tests.gol_tests'
)
