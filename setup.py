import os
from setuptools import setup, find_packages
from setuptools.dist import Distribution
import pkg_resources

add_django_dependency = True

try:
    pkg_resources.get_distribution('Django')
    add_django_dependency = False
except pkg_resources.DistributionNotFound:
    try:
        import django
        if django.VERSION[0] >= 1 and django.VERSION[1] >= 3 and django.VERSION[2] >= 0:
            add_django_dependency = False
    except ImportError:
        pass

    Distribution({
        "setup_requires": add_django_dependency and  ['Django >=1.3.0'] or []
    })

import changelist_ordering

setup(
    name='changelist-ordering',
    version=changelist_ordering.__version__,
    packages = find_packages(),
    url='',
    license='BSD License',
    author='Sergey Kubrak',
    author_email='kartoswko@gmail.com',
    description='',
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        ],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    include_package_data=True,
    zip_safe=False,
)
