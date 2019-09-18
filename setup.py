import setuptools

reqs = [
    'requests >= 2.5.1'
]

setuptools.setup(
    name="ManyRequests",
    version="0.0.4",
    author="Kyle Beauregard",
    author_email="kylembeauregard@gmail.com",
    description="A library to make many requests concurrently.",
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