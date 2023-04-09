from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'an unofficial python API interface for Vajirayana'
LONG_DESCRIPTION = 'Vajirayana Scraper an unofficial python API interface for Vajirayana'

# Setting up
setup(
        name="vajirayana", 
        version=VERSION,
        author="hrnph",
        author_email="hrnph@protonmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['beautifulsoup4', 'requests', 'pandas', 'numpy', 'lxml'], # add any additional packages that 
        keywords=['python', 'api', 'scraper', 'vajirayana', 'vajirayana-scraper'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)