FROM python:3.9-bullseye

RUN apt update
RUN apt install default-jre -y

RUN pip install tika==2.6.0
RUN pip install pyexcel-ods3==0.6.1
RUN pip install sentence-transformers==2.2.2
RUN pip install pandas==1.5.3

COPY app/lib_java/tika-server-standard-2.6.0.jar /tmp/tika-server.jar
COPY app/lib_java/tika-server-standard-2.6.0.jar.md5 /tmp/tika-server.jar.md5

RUN pip install networkx==3.0
RUN pip install python-sqlite-cache==0.0.2

CMD ["bash"]