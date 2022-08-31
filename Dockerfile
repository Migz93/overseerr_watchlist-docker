FROM python:latest

LABEL Maintainer="miguel1993"

RUN pip install requests plexapi flask

WORKDIR /app

COPY overseerr_watchlist.py ./

CMD [ "python","-u","./overseerr_watchlist.py"]