FROM tensorflow/tensorflow:1.14.0-gpu-py3

RUN apt-get -y update

RUN apt-get install -y software-properties-common wget libsm6 libxext6 libxrender-dev


RUN mkdir -p /data/models


RUN wget -q -O /data/models/ColorizeArtistic_gen.pth https://deepai-opensource-codebases-models.s3-us-west-2.amazonaws.com/deoldify/ColorizeArtistic_gen.pth
RUN wget -q -O /data/models/ColorizeVideo_gen.pth https://deepai-opensource-codebases-models.s3-us-west-2.amazonaws.com/deoldify/ColorizeVideo_gen.pth

ADD . /data/

WORKDIR /data

RUN pip install -r requirements.txt

RUN pip install ai-integration==1.0.14

RUN mkdir -p /root/.cache/torch/checkpoints/
RUN wget -q -O /root/.cache/torch/checkpoints/vgg16_bn-6c64b313.pth https://deepai-opensource-codebases-models.s3-us-west-2.amazonaws.com/deoldify/vgg16_bn-6c64b313.pth
RUN wget -q -O /root/.cache/torch/checkpoints/resnet34-333f7ec4.pth https://deepai-opensource-codebases-models.s3-us-west-2.amazonaws.com/deoldify/resnet34-333f7ec4.pth
RUN wget -q -O /root/.cache/torch/checkpoints/resnet101-5d3b4d8f.pth https://deepai-opensource-codebases-models.s3-us-west-2.amazonaws.com/deoldify/resnet101-5d3b4d8f.pth

# This dumb conda installation breaks all sanity in the world
RUN rm /usr/bin/pip3 && ln -s /opt/conda/bin/pip /usr/bin/pip3

CMD []
ENTRYPOINT ["python3", "app.py"]
