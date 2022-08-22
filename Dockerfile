FROM amp-build-deps:1.4

RUN \
	mkdir /usr/share/Ampnado && \
	chmod -R 0755 /usr/share/Ampnado

COPY ampnado /usr/share/Ampnado

# RUN \
# 	openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
#     -subj "/C=US/ST=Washington/L=PortOrchard/O=CharlieDis/CN=Charlie" \
#     -keyout /usr/share/Ampnado/key.pem  -out /usr/share/Ampnado/cert.pem

RUN \
	chmod -R 0755 /usr/share/Ampnado/static && \
	chmod -R 0755 /usr/share/Ampnado/static/images && \
	mkdir -p /usr/share/Ampnado/static/images/thumbnails && \
	chmod -R 0755 /usr/share/Ampnado/static/images/thumbnails

CMD [ "python3", "/usr/share/Ampnado/ampnado.py" ]
