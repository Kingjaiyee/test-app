FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

ARG user=plan
ARG group=plan
ARG uid=1000
ARG gid=1001
RUN addgroup -g ${gid} ${group}
RUN adduser -u ${uid} -g ${group} -s /bin/sh -S ${user}

# work directory of the app
WORKDIR .:/usr/src/app/
# copy the app packages into the container
COPY requirements.txt ./
# install package requirement package file if present, if not break the build and exit
RUN if [[ -e requirements.txt ]]; then pip install -r requirements.txt  && echo 'Packages installed successfully'; else exit 1; fi

# copy the app contents into the container
COPY . .
# expose port 8000 for the app
EXPOSE 8000
# workdir permission to the user
#RUN chown -R ${user}:${group} /usr/src/app/
# Switch to user
USER ${uid}:${gid}
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

