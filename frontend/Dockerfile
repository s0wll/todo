FROM node:18-slim

WORKDIR /app

COPY frontend/package.json frontend/package-lock.json* ./
COPY frontend/ .

RUN npm install --legacy-peer-deps
RUN npm install axios --legacy-peer-deps   

RUN npm run build

EXPOSE 4173

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0"]
