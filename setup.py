import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid>=1.0.2',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'ziggurat_form'
]

setup(name='ziggurat_form_demo',
      version='0.0',
      description='ziggurat_form_demo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="ziggurat_form_demo",
      entry_points="""\
      [paste.app_factory]
      main = ziggurat_form_demo:main
      """,
      paster_plugins=['pyramid'],
      )
