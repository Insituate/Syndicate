from setuptools import setup, find_packages

setup(
    name="syndicate",
    version="0.1.0",
    author="Insituate",
    author_email="nishant@insituate.ai",
    description="Empowering enterprises, with the power of open source.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Insituate/Syndicate",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
    ],
    classifiers=[
        # Choose your license as you wish
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)

