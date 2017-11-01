from setuptools import setup, find_packages

setup(name='owlpost',
      version='1.0.0',
      description='Send data back and forth from Vivo',
      url='http://github.com/akash314/owl-post',
      author='Akash Agarwal',
      author_email='agarwala989@gmail.com',
      license='MIT',
      packages=find_packages(),
      scripts=['owls.py'],
      zip_safe=False)
