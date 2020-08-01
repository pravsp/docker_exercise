FROM centos:8
ARG requirements
RUN yum -y install python3
RUN python3 --version
RUN mkdir user_registration 
#RUN pip3 install -r ${requirements}
COPY ${requirements} user_registration/requirements.txt
RUN ls /user_registration
#COPY /code /tests
RUN pip3 install -r user_registration/requirements.txt 
#RUN ls /tests && cat tests/flaskapp.py
CMD python3 user_registration/userregistrationapp.py
