from setuptools import setup,find_packages
from typing import List

def get_requirements()->List[str]:
    
    """
    This function will return list of requirements
    """
    requirement_list:List[str]=[]
    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
   
    return requirement_list
    

setup(
    name="sensor",
    version="0.0.0",
    author="jiyamaryjoseph",
    author_email="jiyamaryjoseph@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements(), #["pymongo==4.2.0"],
)