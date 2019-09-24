# Unofficial Memsource CLI client

![GitHub](https://img.shields.io/github/license/unofficial-memsource/memsource-cli-client)
[![Coverage Status](https://coveralls.io/repos/github/unofficial-memsource/memsource-cli-client/badge.svg?branch=master)](https://coveralls.io/github/unofficial-memsource/memsource-cli-client?branch=master)
[![Build Status](https://travis-ci.com/unofficial-memsource/memsource-cli-client.svg?branch=master)](https://travis-ci.com/unofficial-memsource/memsource-cli-client)

<img src="docs/Cloudy_shell.png" border=0 align="right">

**Table of contents**
<!-- TOC depthFrom:1 insertAnchor:true orderedList:true -->

- [Introduction](#introduction)
- [Highlights](#highlights)
- [How does it looks like?](#how-does-it-looks-like)
- [Collaborate](#collaborate)
- [Usage](#usage)
- [Contact us!](#contact-us)

<!-- /TOC -->


<a id="markdown-introduction" name="introduction"></a>
## Introduction

Memsource CLI is a framework to help with automation of Memsource related tasks. This empowers you to automate repetitive tasks such as project, job creation, analysis runs and others. The framework is cabable to talk to Memsource API using REST client and show you the results of the execution on the screen.

Please if you have any idea on any improvements please do not hesitate to open an issue.

<a id="markdown-highlights" name="highlights"></a>
## Highlights
- Extensions are written in Python
- Allows you to use formatter `-f` to choose one of many different formats: csv,json,table,value,yaml
- You can sort by any individual columns or multiple columns using `--sort-column`
- Specify the columns that you are interested in using `-c`

Framework will download additional packages:

- cliff
- certifi>=2017.4.17
- python-dateutil>=2.1
- six>=1.10
- urllib3>=1.23

<a id="markdown-how-does-it-looks-like" name="how-does-it-looks-like"></a>
## How does it looks like?
Check how does it look in an execution at:
[![asciicast](https://asciinema.org/a/270610.png)](https://asciinema.org/a/270610)

<a id="markdown-collaborate" name="collaborate"></a>
## Collaborate

- Open issues/feature requests, etc at <https://github.com/unofficial-memsource/memsource-cli-client/issues>


<a id="markdown-usage" name="usage"></a>
## Usage

```
$ memsource --help
usage: memsource [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
                 [--ms-username <auth-username>]
                 [--ms-password <auth-password>] [--ms-token <auth-token>]

Unofficial Memsource CLI client

optional arguments:
  --version             show program's version number and exit
  -v, --verbose         Increase verbosity of output. Can be repeated.
  -q, --quiet           Suppress output except warnings and errors.
  --log-file LOG_FILE   Specify a file to log output. Disabled by default.
  -h, --help            Show help message and exit.
  --debug               Show tracebacks on errors.
  --ms-username <auth-username>
                        Authentication username (Env: MEMSOURCE_USERNAME)
  --ms-password <auth-password>
                        Authentication password (Env: MEMSOURCE_PASSWORD)
  --ms-token <auth-token>
                        Authentication token (Env: MEMSOURCE_TOKEN)

Commands:
  analyse create  Create analysis
  analyse delete  Delete analysis
  analyse language create  Create analyses by languages
  analyse project list  List analyses by project
  analyse show   Get Analysis
  auth login     Login
  auth whoami    Who am I
  complete       print bash completion command (cliff)
  help           print detailed help for another command (cliff)
  job create     Creates job in project
  job delete     Delete jobs
  job list       List jobs in project
  job show       Get job
  project create  Create new project
  project delete  Deletes a project
  project list   List projects
  project show   Get project
  project template create  Create new project from template
  user create    Create user
  user get       Get user
```

## Getting Started

Requirements for python2 environments:
- package `python-virtualenv`


```
DIRECTORY="$HOME/git/"

if [[ ! -d ${DIRECTORY} ]]; then
  mkdir ${DIRECTORY}
fi
cd ${DIRECTORY}
if [[ ! -d ${DIRECTORY}/memsource-cli-client ]]; then
  git clone https://github.com/unofficial-memsource/memsource-cli-client.git
  cd memsource-cli-client/
  if [[ -f $(which python3) ]];
  then
    python3 -m venv --system-site-packages .memsource
  else
    if [[ ! -f $(which virtualenv) ]];
    then
      sudo yum -y install python-virtualenv
    fi
    virtualenv --system-site-packages .memsource
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -U pip
  pip install -U setuptools
  pip install -e .
  deactivate
else
  cd memsource-cli-client/
  git checkout master
  git reset --hard
  git pull
  if [[ ! -f $(which python3) ]];
  then
    for py in $(find memsource_cli -name "*.py"); do sed -i -e 's#/usr/bin/env python3#/usr/bin/env python#' $py; done
  fi
  source .memsource/bin/activate
  pip install -e .
  deactivate
fi
source ${DIRECTORY}/memsource-cli-client/.memsource/bin/activate
clear
memsource --help
```
And that's it!

## Configuration
This way you can configure your username/password and set up memsource token for faster authentication:

```
export MEMSOURCE_USERNAME=<username>
export MEMSOURCE_PASSWORD=<password>
export MEMSOURCE_TOKEN=$(memsource auth login --user-name $MEMSOURCE_USERNAME --password "${MEMSOURCE_PASSWORD}" -c token -f value)
source ${HOME}/git/memsource-cli-client/.memsource/bin/activate
```

Or you can create a file:

```
vi ~/.memsourcerc

export MEMSOURCE_USERNAME=<username>
export MEMSOURCE_PASSWORD=<password>
export MEMSOURCE_TOKEN=$(memsource auth login --user-name $MEMSOURCE_USERNAME --password "${MEMSOURCE_PASSWORD}" -c token -f value)
source ${HOME}/git/memsource-cli-client/.memsource/bin/activate
```

Then only source that file to start using memsource-cli:

```
source ~/.memsourcerc
```

Requirements:
- `jq`

## Autocompletion
To add autocompletion to your shell so you can type:

`mem[tab] pr[tab] cr[tab]` which will translate to:

`memsource project create`
```
memsource complete | sudo tee /etc/bash_completion.d/memsource > /dev/null
. /etc/bash_completion.d/memsource
```

Now you should be fine to use `memsource`

<a id="markdown-contact" name="contact-us"></a>
## Contact us!

This project is maintained on Github. Please contact us by submitting [issue](#collaborate)
