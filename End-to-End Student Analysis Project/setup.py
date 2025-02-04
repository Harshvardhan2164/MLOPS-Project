from setuptools import find_packages, setup
from typing import List

HYPEN_e_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_e_DOT in requirements:
            requirements.remove(HYPEN_e_DOT)

    return requirements
        
setup(
    name='StudentAnalysis',
    version='0.0.1',
    author='Harshvardhan Sharma',
    author_email='harshvardhan22102@iiitnr.edu.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)