from setuptools import setup, find_packages

setup(
    name = "ambari",
    version = "0.0.11",
    keywords = ("pip", "ambari", "packone"),
    description = "Amabri python client based on ambari rest api.",
    long_description = open('README.rst').read(),
    license = "Apache-2.0 Licence",
    url = "https://github.com/cas-bigdatalab/packone_remedy",
    author = "Excel Wang",
    author_email = "wanghj@cnic.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests"],
    entry_points = {
        'console_scripts': [
            'ambari = pk1.remedy.ambari.cmd:run',
        ]
    }
)