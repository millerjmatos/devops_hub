#!/bin/sh

docker run -it -v $PWD:/app -w /app --entrypoint "" hashicorp/terraform:light sh    