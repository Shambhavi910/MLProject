from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> list[str]:
    '''
    
    this function will return a list of requirements from the requirements.txt file.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        requirements=[req.replace("\n","")for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)            

    return requirements

setup(    
    name='MLProject',
    version='0.0.1',
    author='Shambhavi Roy',
    author_email='r.shambhavi@op.iitg.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A Machine Learning Project Template',

)