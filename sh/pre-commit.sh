#!/bin/bash

set -e

pytest
pylint src
