import setuptools


setuptools.setup(
    name="coccidiosis_chicken_disease_classifier",
    version="0.1.0",
    author="Vishal Sharma",
    description="A package for classifying coccidiosis in chickens using CNN.",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    )


