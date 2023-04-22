from setuptools import find_packages,setup
from typing import List

HYPHEN_DOT_E = '-e .'

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of required libraries

    Args:
        file_path (str): file path of requirements.txt file

    Returns:
        List[str]: list of string objects conating required libraries
    """
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [requirement.split('==')[0].replace('\n','') for requirement in requirements]
        if(HYPHEN_DOT_E in requirements):
            requirements.remove(HYPHEN_DOT_E)
    return requirements            

setup(
    name="End-2-End MLProject",
    version="0.0.1",
    author="Paritosh Sharma",
    author_email="paritoshsharma0707@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)

#whenever we want to install requirements.txt at that point of time setup.py file should also trigger for that add 
    #       -e.