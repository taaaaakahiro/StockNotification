FROM python:3.9-alpine
ADD . /code
WORKDIR /code
RUN apk --no-cache add libstdc++ \
  && apk --no-cache --virtual pydeps add gcc \
    g++ \
    python3-dev \
    musl-dev \
    cython \
  && pip install --upgrade pip \ 
    pip install openpyxl \
    pip install requests \
    pip install bs4
CMD ["python", "src/app.py"]