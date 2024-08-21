# First stage: Build the JAR
FROM gradle:7.5.1-jdk17 AS build
COPY --chown=gradle:gradle . /home/gradle/project
WORKDIR /home/gradle/project
RUN gradle build --no-daemon

# Second stage: Create the final image
FROM eclipse-temurin:17-jdk
RUN groupadd -r spring && useradd -r -g spring spring
USER spring:spring
ARG JAR_FILE=/home/gradle/project/build/libs/cart-1.0.0.jar
COPY --from=build ${JAR_FILE} app.jar

# Environment variables
ENV SPRING_REDIS_HOST=localhost
ENV SPRING_REDIS_PORT=6379
ENV SPRING_REDIS_PASSWORD=

ENTRYPOINT ["java","-jar","/app.jar"]