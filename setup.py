"""
Creating PIPY package instruction:

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist
python3 -m pip install --user --upgrade twine
twine check dist/*
twine upload dist/*
"""

from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(name = 'pybeach',
          author            = "Tomas Beuzen",
          author_email      = "https://tomasbeuzen.github.io/",
          url               = "https://github.com/TomasBeuzen/pybeach",
          version           = "0.1.1",
          description       = "Coastal Processes, Environments & Systems.",
          long_description  = long_description,
          long_description_content_type='text/markdown',
          packages          = ['pybeach','pybeach.support','pybeach.classifiers'],
          install_requires  = [
                        'numpy>=1.16.3',
                        'scikit-learn>=0.20.3',
                        'pandas>=0.25',
                        'pytz==2019.1',
                        'scipy>=1.2.1',
                        'joblib==0.13.2',
                        ],
          python_requires   = '>=3.7',
          # package_data      = {'pybeach': ['Notebooks/notebooks/*ipynb',
          #                                 'Notebooks/notebooks/*py'] },
          include_package_data = True,
          classifiers       = ['Programming Language :: Python :: 3.7']
          )
