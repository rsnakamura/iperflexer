from __future__ import print_function

try:
    from setuptools import setup, find_packages
except ImportError as error:
    #print(error)
    #print('setuptools package required')
    #import sys
    #sys.exit()
    from distribute_setup import use_setuptools
    use_setuptools()

# put the readme in for pypi
with open('readme.rst') as reader:
    long_description = reader.read()
    
setup(name='iperflexer',
      version="2014.12.21.2",
      description="A program to parse iperf files",
      long_description=long_description,
      author="russell",
      platforms=['linux'],
      url = 'https://bitbucket.org/cloisteredmonkey-admin/iperflexer',
      author_email="necromuralist@gmail.com",
      license = "MIT",
      packages = find_packages(),
      include_package_data = True,
      package_data = {"":["*.rst", "*.ini"]},
      entry_points = """
	  [console_scripts]
      parseiperf=iperflexer.main:main
	  """

      )

#      install_requires = ['pudb', 'mock'],
# an example last line would be cpm= cpm.main: main

# If you want to require other packages add (to setup parameters):
# install_requires = [<package>],
#version=datetime.today().strftime("%Y.%m.%d"),
# if you have an egg somewhere other than PyPi that needs to be installed as a dependency, point to a page where you can download it:
# dependency_links = ["http://<url>"]
