from setuptools import setup

setup(name='pymurapi',
      version='0.0.1',
      description='murSimulator/murAUV API for python',
      url='http://github.com/',
      author='Vladislav Bolotov',
      author_email='vlad@murproject.com',
      license='MIT',
      packages=['pymurapi'],
      zip_safe=False, install_requires=['opencv-python', 'pyzmq', 'numpy', 'opencv-contrib-python'])
