FROM python

ARG wd=/home/miniserver
WORKDIR $wd

ADD main.py $wd/
ADD requirement.txt $wd/

RUN ["ls"]
RUN ["pip","install","-r","requirement.txt"]

ENTRYPOINT ["python","main.py"]
