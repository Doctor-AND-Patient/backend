FROM nginx:latest

# Копируем пользовательские конфигурации (если есть)
COPY nginx.conf /etc/nginx/nginx.conf
# COPY ./html /usr/share/nginx/html

# Открываем порт 80
EXPOSE 80

# Запускаем Nginx в foreground-режиме
CMD ["nginx", "-g", "daemon off;"]