#!/usr/bin/env bash

# Run original model
mkdir Output
python growth.py Input/photosynthesis_rate.txt Output/growth_rate.txt

# Run integrations with files
yggrun tests/test_growth.yml
yggrun tests/test_light.yml
yggrun tests/test_photosynthesis.yml
yggrun tests/test_canopy.yml

# Run complete integration network
yggrun tests/test_network.yml
