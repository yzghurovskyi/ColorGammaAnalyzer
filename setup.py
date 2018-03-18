from setuptools import setup

setup(name='color_gamma_analyzer',
      version='0.1',
      description='The best color gamma analyzer',
      author='Yaroslav Zghurovskyi, Maksym Svynarchuk, Andrian Poyda',
      license='MIT',
      packages=['color_gamma_analyzer'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
