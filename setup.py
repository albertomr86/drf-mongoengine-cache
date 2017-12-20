from setuptools import setup

import drf_mongoengine_cache


github_url = "https://github.com/albertomr86/drf-mongoengine-cache"

setup(
    name="drf-mongoengine-cache",
    version=drf_mongoengine_cache.__version__,
    author=drf_mongoengine_cache.__author__,
    author_email=drf_mongoengine_cache.__email__,
    description="Easy to use cache framework for django-rest-framwork with MongoEngine models",
    license="GPLv3",
    keywords="drf_mongoengine_cache",
    url=github_url,
    packages=['drf_mongoengine_cache'],
    namespace_packages=['drf_mongoengine_cache'],
    package_dir={'drf_mongoengine_cache': 'drf_mongoengine_cache'},
    download_url="{}/tarball/master".format(github_url),
    test_suite='tests',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Topic :: Utilities",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
