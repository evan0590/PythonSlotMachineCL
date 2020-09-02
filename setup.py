from setuptools import setup

requirements = [
      'emoji',
]

setup(name="slotmachine",
      version="0.1",
      description="Basic command line slot machine.",
      url="https://github.com/evan0590/SlotMachinesCL",
      author="Evan Byrnes",
      author_email="evan.byrnes@ucdconnect.ie",
      licence="GPL3",
      packages=['slotmachine'],
      install_requires=requirements,
      entry_points={
        'console_scripts': ['run_slotmachine=slotmachine.main:main']
        }
      )
