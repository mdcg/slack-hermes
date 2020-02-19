from setuptools import find_packages, setup

requirements = ["slackclient==2.5.0"]

setup(
    name="slackhermes",
    version="1.0.0",
    description="A message notifier for Slack",
    author="mdcg",
    url="https://github.com/mdcg/slack-hermes",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
