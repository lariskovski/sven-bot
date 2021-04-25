FROM centos:7

WORKDIR /app

RUN yum update -y &&  yum install gcc python36 python36-pip python36-setuptools \
    python3-devel epel-release libevent-devel -y && \
    yum localinstall -y --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm && \
    yum install ffmpeg ffmpeg-devel -y &&\
    yum clean all && \
    rm -rf /var/cache/yum

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "./main.py"]
