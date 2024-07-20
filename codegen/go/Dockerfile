FROM golang:1.19 AS build
WORKDIR /go/src
COPY umaauth ./umaauth
COPY main.go .
COPY go.sum .
COPY go.mod .

ENV CGO_ENABLED=0

RUN go build -o umaauth .

FROM scratch AS runtime
COPY --from=build /go/src/umaauth ./
EXPOSE 8080/tcp
ENTRYPOINT ["./umaauth"]
