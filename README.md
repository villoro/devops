# DevOps

[![Build Status](https://travis-ci.com/villoro/devops.svg?branch=master)](https://travis-ci.com/villoro/devops)
[![codecov](https://codecov.io/gh/villoro/devops/branch/master/graph/badge.svg)](https://codecov.io/gh/villoro/devops)

This repository is a basic example of how to implement DevOps in a python project. It shows how to achive Continuous Integration (CI) and Continuous Deployment (CD).

![DevOps](assets/DevOps.png)

The code is a simple [Dash](https://plot.ly/products/dash/) app. Every time a commit is made [Travis CI](https://travis-ci.com/) starts the app and performs some tests:
1. Unittesting using nosetests and [selenium](https://www.seleniumhq.org/)
2. Static code analysis with [pylint](https://www.pylint.org/) (only for critial and errors)

If a commit in the master branch passes all the tests then it is automatically deployed to [Heroku](https://www.heroku.com/).

It has also integration with [Codecov](https://codecov.io/) to watch the coverage achived by the tests.

## Authors
* [Arnau Villoro](villoro.com)

## License
The content of this repository is licensed under a [MIT](https://opensource.org/licenses/MIT).
