from setuptools import setup

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    requirement_field_name = 'requirement'
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    requirement_field_name = 'req'

with open("requirements.txt") as f:
    dependencies = [line for line in f if "==" in line]

setup(
    name='zemberek_parser',
    version='1.0.1',
    packages=['zemberek_python'],
    url='https://github.com/kemalcanbora/zemberek_parser',
    license='BSD',
    package_data = { '' : ['zemberek-tum-2.0.jar']},
    author='Kemalcan Bora',
    author_email='kemalcanbora@gmail.com',
    description='zemberek kutuphanesinin lite python versiyonu',
    classifiers=[
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=dependencies


)
