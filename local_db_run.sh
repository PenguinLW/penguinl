#!/usr/bin/env bash

sudo systemctl restart postgresql.service

source ~/venv/bin/activate
sudo pgadmin4 #pgadmin4