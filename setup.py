from setuptools import setup

setup(
    name='trash',
    version='1.0.0',
    description='A tool to show the pickup times of trash in your local area',
    author='trashman',
    author_email='trashman@foo.com',
    packages=['trash'],
    package_data={'trash': ['trashrc']},
    include_package_data=True,
    scripts=['trash-cli'], # when we install the package, setuptools will copy the script to our PATH and make it available for general use.
    install_requires=[
        "astroid==1.6.5",
        # "autopep8==1.3.5",
        "certifi==2022.12.7",
        "chardet==3.0.4",
        "icalendar==4.0.1",
        "idna==2.6",
        "isort==4.3.4",
        "lazy-object-proxy==1.3.1",
        "mccabe==0.6.1",
        # "pycodestyle==2.4.0",
        # "pylint==1.9.2",
        "python-dateutil==2.7.3",
        "pytz==2018.4",
        #"PyYAML==3.12",
        "configobj==5.0.6",
        "requests==2.18.4",
        "rope==0.10.7",
        "six==1.11.0",
        "urllib3==1.22",
        "wrapt==1.10.11"
    ],
)
