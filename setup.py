from setuptools import setup,find_packages


def get_requirements():
    requirements=[]
    with open("requirements.txt","r") as file:
        for line in file:
            clean_line=line.strip()
            if clean_line == '.e':
                continue
            requirements.append(clean_line)

    return requirements
    

setup(
    name="Hate-Speech-Detection",
    version="1.0",
    author="Muhammad Uzair",
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    install_requires=get_requirements()
)