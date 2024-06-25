FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x si_ps_conv_fastcorrs.py

#ENTRYPOINT ["./si_ps_conv_fastcorrs.py"]

#CMD ["$P$R"]

CMD ./si_ps_conv_fastcorrs.py ${P}${R}
