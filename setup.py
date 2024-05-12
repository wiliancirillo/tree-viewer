from setuptools import setup, find_packages

setup(
   name='tree-viewer',
   version='0.1.0',
   packages=find_packages(),
   description="Tree-Viewer is a Python library designed to generate customizable visual representations of directory structures, enabling users to clearly and efficiently organize and manage their project layouts. With its user-friendly interface, Tree-Viewer provides a comprehensive view of your directories, presenting all necessary details in a structured and easily accessible format. This tool is ideal for developers seeking to maintain an intuitive overview of complex projects, ensuring all components are logically arranged for optimal navigation and project oversight.",
   long_description=open('README.md', encoding='utf-8').read(),
   long_description_content_type='text/markdown',
   author='Wilian Cirillo',
   author_email='wilian@hey.com',
   url='https://github.com/wiliancirillo/tree-viewer',
   license='MIT',
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
   ],
   entry_points={
      'console_scripts': [
         'tree-viewer = tree-viewer.main:main'
      ]
   }
)
