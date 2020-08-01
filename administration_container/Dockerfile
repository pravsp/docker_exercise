from centos:8
arg requirements
RUN yum -y install python3
RUN python3 -V
RUN mkdir admin_processing
COPY ${requirements} admin_processing/requirements.txt
RUN ls -l /admin_processing
RUN pip3 install -r admin_processing/requirements.txt
CMD python3 admin_processing/site_administrator_app.py

