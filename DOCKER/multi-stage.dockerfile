# Build stage
FROM alpine:latest as build
WORKDIR /phython_app
RUN apk update && apk add python3 py3-pip git
COPY . /phython_app

# Copy and Run stage
FROM gcr.io/distroless/python3
WORKDIR /app
COPY --from=build /phython_app /app
ENTRYPOINT ["python3"]
CMD ["app.py"]


# Build runs in one stage
# copy the previous stage output
# use it next stage so it reduces overall output image size size
