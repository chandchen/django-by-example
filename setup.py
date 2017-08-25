from setuptools import setup, find_packages

setup(
    name="website",
    version="1.0",
    url="https://github.com/changduchen/Social-Website.git",
    license="BSD",
    description="Develop a website",
    author="changduchen",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
)
