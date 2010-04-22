from setuptools import setup, find_packages

setup(name="django-wurfl",
           version="0.1",
           description="Equivalent to tera-wurfl for python and django web framework",
           author="Clement Nodet",
           author_email="clement.nodet@gmail.com",
           packages=find_packages(),
           include_package_data=True,
)
