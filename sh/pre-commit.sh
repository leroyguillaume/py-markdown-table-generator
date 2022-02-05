#!/bin/bash

set -e

pytest
pylint markdown_table_generator
