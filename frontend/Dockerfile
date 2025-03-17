FROM node:22-alpine AS builder

WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN apk update
RUN npm ci
RUN apk add curl
COPY . .
RUN npm run build

FROM node:22-alpine AS production

WORKDIR /app
COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules
COPY package.json package-lock.json ./
EXPOSE 5173
CMD ["npm", "run", "dev", "--", "--port", "5173", "--host", "0.0.0.0"]