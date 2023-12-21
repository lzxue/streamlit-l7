import setuptools

setuptools.setup(
    name="streamlit-l7",
    version="0.1.2",
    author="lzxue",
    author_email="lzx199065@gmail.com",
    description="Render L7 Map in Streamlit",
    long_description="Render Map charts in Streamlit",
    long_description_content_type="text/plain",
    url="https://github.com/lzxue/streamlit-l7",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
