import setuptools

setuptools.setup(
    name="sshcolab",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sshcolab = ssh_colab:main',
        ],
    },
    include_package_data=True,
    )