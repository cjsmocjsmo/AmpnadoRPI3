FROM amp-build-deps:latest

RUN \
	mkdir -p /usr/share/Ampnado/AmpBackup && \
	chmod -R 0755 /usr/share/Ampnado && \
	chmod -R 0755 /usr/share/Ampnado/AmpBackup

COPY ampnado /usr/share/Ampnado

RUN \
	chmod -R 0755 /usr/share/Ampnado/static && \
	chmod -R 0755 /usr/share/Ampnado/static/images && \
	mkdir -p /usr/share/Ampnado/static/images/thumbnails && \
	chmod -R 0755 /usr/share/Ampnado/static/images/thumbnails

CMD [ "python3", "/usr/share/Ampnado/ampnado.py" ]
