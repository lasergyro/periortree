from setuptools import setup, find_packages
setup(
    name='periortree',
    version='0.0.1',
    url='https://github.com/lasergyro/periortree',
    author='lasergyro',
    author_email='31989178+lasergyro@users.noreply.github.com',
    description='An extension of R-Tree1 for Periodic Boundary Condition.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license='MIT',
    license_files=('LICENSE',),
    python_requires='>=3.8',
    install_requires=['cppyy','numpy'],
    platforms=['Linux'],
)
