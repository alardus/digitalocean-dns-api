# DigitalOcean Dynamic DNS

- Преполагается, что управление DNS записями для домена делегировано DigitalOcean.
- Получите ключ для управления доменом. Для этого откройте:

`https://cloud.digitalocean.com/account/api`

авторизуйтесь и получите токен. Копируйте его в поле `TOKEN` в файле `.env`.

- Укажите `DOMAIN` и `SUBDOMAIN`, которыми хотите управлять, в файле `.env`:

```
DOMAIN = 'host.com'
SUBDOMAIN = 'subdomain'
```

- Установите необходимые модули:

`pip install -r req.txt`

- Чтобы добавить поддомен:

`./ddns --add hostname ip`

- Чтобы удалить поддомен:

`./ddns --delete hostname`

- Чтобы обновить адрес поддомена вручную:

`./ddns --update hostname ip`

- Чтобы автоматически раз в 30 минут обновлять адрес для поддомена указанного в .env:

`./ddns --auto`

Для последнего случая удобно положить скрипт в Docker:

```
docker build -t alardus/dodns .
docker run --dns 8.8.8.8 -d --restart=always --name dodns alardus/dodns
```
