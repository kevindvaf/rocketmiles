<!--
*** To avoid retyping too much info. Do a search and replace for the following:
*** kevindvaf, rocketmiles, twitter_handle, email
-->

# RocketMiles Interview Project

Can I figure out how to test something I've never seen before?? :)

## Table of Contents

- [RocketMiles Interview Project](#rocketmiles-interview-project)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
      - [Python 3.6+](#python-36)
    - [Installation](#installation)
  - [Usage](#usage)
  - [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

    Using the tool of your choice as an automation framework write as many tests as you 
    think would be sufficient to test the Search functionality on the rocketmiles.com.a  


### Built With

* Windows 10
  * Python 3.7.0
  * behave 1.2.6
  * pipenv 2018.11.26

* Ubuntu 18.04.2 LTS
  * python 3.6.7
  * behave 1.2.6
  * pipenv 2018.11.26



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

#### Python 3.6+

I used the system python3 since the only additional packages I needed there were pip3 and pipenv. Pipenv is used to handle the virtual environments replacing explicit use of pip3, venv, virtualenvwrapper, and activation of the venv.

```sh
apt install python3  # only necessaru of there is an older version on Ubuntu
apt install python3-pip
python3 -m pip install pipenv
```

### Installation
 
1. Clone the repo
```sh
cd <parent of project directory>
git clone https:://github.com/kevindvaf/rocketmiles.git
```
2. Create the virtual environment
```sh
cd rocketmiles
pipenv --three
```
This should also install all necessary packages from the Pipfile.  

4. Verify installation 
```sh
pipenv run python3 --version
pipenv run pip3 --version
pipenv run pipenv --version
pipenv run behave --version
```
The paths should be from the venv and the versions shown should match those specified above.

3. Install Python packages if the verification fails
```sh
pipenv install behave
pipenv install selenium
```

## Usage

Once everything is installed, try a dry-run. This should check the feature files.
```sh
pipenv run behave -d
```
If this works, it's time to give the tests a shot.
```sh
pipenv run behave
```

As you can see, a few of the step implementations are incorrect and fail. This framework suffers from the same issue that many older frameworks have, manual selection of the object locators. Unless steps are taken when a page is first created and specific, non-volatile selectors are chosen, all tests will be "flaky" to a large extent. Selectors can change from one version to the next, even from one build to the net, and, occasionaly, from one job to the next.

## Contact

Kevin Ferguson - kferguson@acm.org

Project Link: [https://github.com/kevindvaf/rocketmiles](https://github.com/kevindvaf/rocketmiles)

