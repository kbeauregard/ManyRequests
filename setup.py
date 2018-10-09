import setuptools

with open("ReadMe.md", "r") as fh:
    long_description = fh.read()

reqs = [
    'requests >= 2.5.1'
]

setuptools.setup(
    name="ManyRequests",
    version="0.0.2",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="A library to make many requests concurrently.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kbeauregard/ManyRequests',
    packages=setuptools.find_packages(
        include=[
            'ManyRequests*',
        ]
    ),
    py_modules=[
        'ManyRequests.__init__',
    ],
    install_requires=reqs,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ],
)