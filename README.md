# ioregpy

![version](https://img.shields.io/badge/version-0.1.0-blue)

ioregpy is a utility script that allows you to access the values from ioreg as a dictionary/JSON on a Mac. It is useful if you want to access lots of information from ioreg such as creating a basic UI for BitBar (my usecase)

## Prerequisites

* Python 3
* MacOS with ioreg accessible from the terminal

## Using ioregpy

Using the basic functionality will show your io products that have a battery with their product name and percentage of charge remaining.

```bash
# Clone the repo ... then using Python version >= 3
python3 main.py
```

You can also make use of the functionality in `utils.py` using the `IOReg.to_dict(options=[...])` to interact with the output in Python, or print it out to stdout to use it in your shell scripting.

## Contributing to ioregpy

To contribute to ioregpy, follow these steps:

1. Create a fork of the repo
2. Make your changes and commit them
3. Push to the forked repo
4. Create the pull request.
