#!/usr/bin/env bash

cd $(dirname $0)/../

protoc \
    protobuf_test/myobject.proto \
    --python_out=.