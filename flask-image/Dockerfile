FROM python:3.6


# 构建在服务器上的工作路径
WORKDIR /Project/Demo

ARG version=v3
ENV imageVersion=$version
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
# 拷贝本地文件到镜像中
COPY ./ ./
# 构建镜像需要执行的操作

RUN pip install -r requirements.txt;


#CMD ["gunicorn","wsgi:app","-c","./gunicorn.conf.py"]
#CMD ["flask","run","--host=0.0.0.0","--port=80"]
CMD ["uwsgi","./uwsgi.ini"]