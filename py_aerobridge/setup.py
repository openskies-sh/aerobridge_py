from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='pyaerobridge',
    version='0.0.1',
    description='Useful tools to work with Aerobridge APIs in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='Apache-2.0',
    packages=find_packages(),
    author='Dr. Hrishikesh Ballal',
    author_email='hrishikeshballal@yahoo.com',
    keywords=['Managmeent Server', 'Aerobridge', 'Drones', 'Drone'],
    url='https://github.com/openskies-sh/py_aerobridge',
    download_url='https://pypi.org/project/py_aerobridge/'
)

install_requires = [
    'requests==2.27.1'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)