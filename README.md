# soa-serialization

This is an application that tests serialization time and memory overhead for different data formats in Python. 

Now it supports Pickle, JSON, XML, Protobuf, Apache Avro, YAML, MessagePack. 

It is [available on Docker Hub](https://hub.docker.com/repository/docker/haidaansko/soa-serialization/general).

## Usage

```bash
pip3 install -r requirements.txt
chmod +x run.sh
./run.sh
```

or

```bash
docker run -it haidaansko/soa-serialization
```