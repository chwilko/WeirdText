# UlamLab_Test
Recruiting task for Ulam Lab Intern. Encoder and Decoder of Weird Text.
The app is written in framework django.
## Heroku API
link to heroku API:
[test-ulamlab.herokuapp.com](https://test-ulamlab.herokuapp.com)

## CirceCi project
[app.circleci.com/pipelines/github/chwilko/WeirdText](https://app.circleci.com/pipelines/github/chwilko/WeirdText)
<br>
project id:
cd143c77-1f92-4beb-b581-79a45fb531d9

### Author
Bartłomiej Chwiłkowski (github: chwilko)


## Installation
### Ubuntu bash

```bash
# clone from github
git clone https://github.com/chwilko/WeirdText.git

# install Virtualenv
sudo apt install python3-virtualenv

#make virtualenv
virtualenv WeirdTextAPP

# go to virtualenv
source WeirdTextAPP/bin/activate

# chancge current directory
cd WeirdText/

# install required dependence
pip install -r requirements.txt

```

## Usage

```bash
# type in bash
python3 manage.py runserver
```

Next paste to your browser:
```
http://127.0.0.1:8000/
```




