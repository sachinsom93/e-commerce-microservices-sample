
FROM node:18-alpine
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .

# Env variables
ENV MONGO_URI=mongodb://mongo-root-username:mongo-root-password@host:port/
ENV DATABASE=e-commerce

CMD npm start