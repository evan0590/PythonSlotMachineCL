from setuptools import setup

requirements = [
      'emoji',
]

setup(name="slotmachine",
      version="0.4",
      description="Basic command line slot machine.",
      url="",
      author="Evan Byrnes",
      author_email="evan.byrnes@ucdconnect.ie",
      licence="GPL3",
      packages=['slotmachine'],
      install_requires=requirements,
      entry_points={
        'console_scripts':['run_slotmachine=slotmachine.main:main']
        }
      )