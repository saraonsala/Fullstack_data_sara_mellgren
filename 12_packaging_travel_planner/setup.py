from setuptools import setup
from setuptools import find_packages


# find_packages will find all the packages with __init__.py
print(find_packages())

setup(
    name="travel-planner",
    version="0.0.1",
    description="""
    This package is used for travel planning in public transport. 
    It has backend code, frontend code and utils.  
    """,
    author="Sara Mellgren",
    author_email="info@saramellgren.com",
    install_requires=["streamlit", "pandas", "folium", "requests", "python-dotenv"],
    packages=find_packages(exclude=("test*", "explorations")),
    entry_points={"console_scripts": ["dashboard = utils.run_dashboard:run_dashboard"]},
)
