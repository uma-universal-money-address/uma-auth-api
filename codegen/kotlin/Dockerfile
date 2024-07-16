FROM openjdk:8-jre-alpine

COPY ./build/libs/uma-auth-server.jar /root/uma-auth-server.jar

WORKDIR /root

CMD ["java", "-server", "-Xms4g", "-Xmx4g", "-XX:+UseG1GC", "-XX:MaxGCPauseMillis=100", "-XX:+UseStringDeduplication", "-jar", "uma-auth-server.jar"]