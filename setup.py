from setuptools import setup, find_packages

version = "1.0dev"

setup(name                  = "z3c.caching",
      version               = version,
      description           = "Caching infrastructure for web apps",
      long_description      = open("README.txt").read(),
      classifiers           = [
            "Environment :: Web Environment",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Zope Public License",
            "Programming Language :: Python",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords              = "",
      author                = "Wichert Akkerman",
      author_email          = "zope-dev@zope.org",
      url                   = "",
      license               = "ZPL",
      namespace_packages    = ["z3c"],
      packages              = find_packages(exclude=["ez_setup"]),
      include_package_data  = True,
      zip_safe              = False,
      install_requires      = [
          "setuptools",
          "zope.interface",
          "zope.component",
          ],
      tests_require         = "nose >=0.10.0b1",
      test_suite            = "nose.collector",
      )