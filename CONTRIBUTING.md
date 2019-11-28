# Contributing

Thanks for reading this document and thinking about contributing.

I tried to make it as easy as possible.

## Setting up your development environment

You will need to have installed virtualenv and python 3.7

Create then a local environment by using `make setup`.

This will run:

*   setup-virtual-env: will create a virtualenv for you
*   setup-hooks: Will setup the pre-push hook (to easily integrate with bumpversion)
*   install-requirements: Will install the requirements

Note, you can access those commands directly.

Remember to activate your virtual environment by running `source .env/bin/activate`

## Pushing a change

Create a PR. If you have followed the previous steps, it will ask you what type fo change are you contributing. This will automatically generate a new version.

Once the PR is approved, the merge will trigger a release.

Any questions, just drop me an email or write an issue.

Thanks again and happy contributing!!
