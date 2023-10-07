from setuptools import setup, find_namespace_packages

def _read(path):
    with open(path) as f:
        data = f.read()
    f.close()

    return data

README = ''
CHANGES = ''

setup(name='chromadb',
      version='0.1',
      description='Chromadb',
      author='Jeff Huber',
      author_email="jeff@trychroma.com",
      license='Apache License',
      maintainer='Cynepia Technologies',
      maintainer_email='adminsupport@cynepia.com',
      package_data = {'': ['*.ini', 'corpora/stop-words/*', 'common-words', 'stopwords', '*.conf', '*.txt', '*.r', '*.R', 'common/analytics/kungfu/ml_libs/timeseries/regular/R_scripts/*']},
      packages = find_namespace_packages(exclude=['ez_setup', 'tests', 'tests.*', '.git/*', 'enron.mbox']),
      include_package_data=True,
      install_requires=[],
      zip_safe=False)
