#!/bin/zsh

source env.sh
pipenv shell
sleep 4
exec python main.py