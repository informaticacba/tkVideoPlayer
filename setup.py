from setuptools import setup

with open("Readme.md", 'r') as f:
    long_description = f.read()

setup(
    name='tkvideoplayer',
    version='1.1.0',
    description="This library helps you play videos in tkinter",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Paul',
    url="https://github.com/PaulleDemon/tkVideoPlayer",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        'Development Status :: 4 - Beta',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    keywords=['tkinter', 'video', 'payer', 'video player', 'tkvideoplayer'],
    packages=["tkVideoPlayer"],
    install_requires=["av", "pillow"],
    include_package_data=True,
    python_requires='>=3.6',
)