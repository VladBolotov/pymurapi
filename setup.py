from setuptools import setup

setup(name='pymurapi',
      version='0.0.2',
      description='murSimulator/murAUV API for python',
      url='https://github.com/murproject/pymurapi',
      author='Vladislav Bolotov',
      author_email='support@robocenter.org',
      license='MIT',
      packages=['pymurapi'],
      zip_safe=False, install_requires=['opencv-python', 'pyzmq', 'numpy', 'opencv-contrib-python'])
