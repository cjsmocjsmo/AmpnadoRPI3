FROM amp-build-deps:latest

RUN \
	chmod -R 0755 /usr/share/Ampnado && \
	mkdir -p /usr/share/Ampnado/AmpBackup && \
	chmod -R 0755 /usr/share/Ampnado/AmpBackup

COPY ampnado /usr/share/Ampnado

RUN \
	chmod -R 0755 /usr/share/Ampnado/static && \
	chmod -R 0755 /usr/share/Ampnado/static/images && \
	mkdir /usr/share/Ampnado/static/images/thumbnails && \
	chmod -R 0755 /usr/share/Ampnado/static/images/thumbnails

CMD [ "python3", "/usr/share/Ampnado/ampnado.py" ]
