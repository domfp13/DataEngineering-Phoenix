# DataEngineering-Phoenix

This is the DataEngineering-Phoenix project, this is a Serverless application that is being triggered by a Pub/Sub notification after a file is finalize/create in a bucket, the function transforms and cleans various different Excel files in a unified standard CSV format, the final result is inserted into another bucket and another Serverless application picks it up from there. This uses a decoupled architecture where processes are independent.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
conda create -n phoenix python=3.7
pip install --upgrade -r requirements.txt
```

## Usage
For local testing please comment out the decorators

## Authors
* **Luis Fuentes** - *2019-10-05*

## License
[MIT](https://choosealicense.com/licenses/mit/)