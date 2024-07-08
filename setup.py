from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
#def readme():
#    with open('README.rst', encoding='utf-8') as f:
#        return f.read()
        
#def licensefile():
#    with open('LICENSE.txt') as f:
#        return f.read()
        
setup(name='py2eviews',
      version='1.0.6',
      description='Data import/export and EViews function calls from Python',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Topic :: Scientific/Engineering :: Information Analysis',
                   'Programming Language :: Python :: 3',
                   'Operating System :: Microsoft :: Windows'],
      keywords='eviews econometrics',
      url='https://github.com/eviews-support/py2eviews',
      author='EViews_Support',
      author_email='support@eviews.com',
      license='GPLv3',
      packages=['py2eviews'],
      install_requires=['comtypes','numpy','pandas'],
      include_package_data=True,
      zip_safe=False)
