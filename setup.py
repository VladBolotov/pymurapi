from setuptools import setup

setup(name='pymurapi',
      version='0.0.1',
      description='murSimulator/murAUV API for python',
      url='https://github.com/VladBolotov/pymurapi',
      author='Vladislav Bolotov',
      author_email='vlad@murproject.com',
      license='MIT',
      packages=['pymurapi'],
      zip_safe=False, install_requires=['pyzmq', 'numpy'])
