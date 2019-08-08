# DeOldify Colorizer

<p>
    <a href="https://cloud.docker.com/u/deepaiorg/repository/docker/deepaiorg/colorization">
        <img src='https://img.shields.io/docker/cloud/automated/deepaiorg/colorization.svg?style=plastic' />
        <img src='https://img.shields.io/docker/cloud/build/deepaiorg/colorization.svg' />
    </a>
</p>

This model has been integrated with [ai_integration](https://github.com/deepai-org/ai_integration/blob/master/README.md) for seamless portability across hosting providers.

# Overview

Nvidia-Docker is required to run this image.

# For details see [Colorizer](https://deepai.org/machine-learning-model/colorizer) on [Deep AI](https://deepai.org)

# Quick Start

docker pull deepaiorg/colorization

### HTTP
```bash
nvidia-docker run --rm -it -e MODE=http -p 5000:5000 deepaiorg/colorization
```
Open your browser to localhost:5000 (or the correct IP address)

### Command Line

Save your image as content.jpg in the current directory.
```bash
nvidia-docker run --rm -it -v `pwd`:/shared -e MODE=command_line deepaiorg/colorization --image /shared/content.jpg --output /shared/output.jpg
```
# Docker build
```bash
docker build -t colorization .
```

# Author Credit

Jason Antic: https://twitter.com/citnaj

Based on this implementation:

https://github.com/jantic/DeOldify

Simplification, streamlining, and updating to work in the year 2019 by DeepAI.
