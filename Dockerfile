FROM centos:7
MAINTAINER "Sravani"
ENV PYTHON_VERSION "3.6.4"

RUN yum -y install epel-release
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm
RUN yum -y install python36u python36-setuptools
RUN easy_install-3.6 pip

WORKDIR /weather
COPY . .

RUN pip install -r requirements.txt
RUN pip install -e .

EXPOSE 5000

CMD python3.6 /weather/weather/__init__.py

