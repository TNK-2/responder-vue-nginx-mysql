FROM kennethreitz/pipenv
ENV PORT '5042'
WORKDIR /app
COPY . .
CMD python3 app.py
EXPOSE 5042

# docker run -p 5042:5042 -it wisnote-backend 