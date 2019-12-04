FROM python:3.8-slim
WORKDIR /usr/app
COPY ./ /usr/app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
