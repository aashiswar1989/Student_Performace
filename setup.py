from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return list of all libraries requiresd to be installed
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')

    return requirements

setup(
    name = "Student_Performance",
    version = '0.1',
    author = 'Aashish',
    author_email = 'eceaashish.swarnkar@gmail.com',
    packages= find_packages(),
    requires= get_requirements("requirements.txt")
)