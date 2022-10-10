# Speedtest

[![MIT License](https://img.shields.io/badge/License-MIT-success.svg)](https://choosealicense.com/licenses/mit/)

A little CLI program who prints the speed and some informations about your connection.

## Details:

Some little toy project: a speedtest who also prints some informations about your connection (IP, City, Country and ISP). 
I used this project to learn the usage of an API, here the *ipgeolocation.abstractapi.com* API.
I also learn more about Json.

## Tools Used:

![Logo](https://img.shields.io/badge/Python-v3.10.6-success?style=flat&logo=python&logoColor=white)
![Logo](https://img.shields.io/badge/PyPI-v22.2.2-success?style=flat&logo=pypi&logoColor=white)
![Logo](https://img.shields.io/badge/Speedtest-v2.1.3-success?style=flat&logo=speedtest&logoColor=white)
![Logo](https://img.shields.io/badge/Requests-v2.28.1-success?style=flat&logo=curl&logoColor=white)
![Logo](https://img.shields.io/badge/JSON-v3.10.6-success?style=flat&logo=json&logoColor=white)
![Logo](https://img.shields.io/badge/Dotenv-v0.21.0-success?style=flat&logo=hack-the-box&logoColor=white)
![Logo](https://img.shields.io/badge/VisualStudioCode-v1.71.2-success?style=flat&logo=visual-studio-code&logoColor=white)


## Demo

![Demo Speedtest](speedtest.gif)

## Installation

Install my-project with pip

```bash
  git clone git@github.com:tt-bb/cli-scripts.git
  cd cli-scripts/speedtest
  pip install requirements.txt
  python3 main.py
```

### API

- Get an API key on [abstractapi.com](https://app.abstractapi.com/api/ip-geolocation/)
- Create a filename `.env`

```python
API_KEY = "your_api_key"
```
    
## License

[MIT](https://choosealicense.com/licenses/mit/)


