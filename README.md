# Line Notification Gateway #

Line Notification Gateway for Alertmanager (Promtheus).

## Installation ##

```bash
git clone https://github.com/be99inner/line-notify-gateway.git
cd line-notify-gateway
docker-compose up -d
```

## Usage ##

Set receiver of generic webhook from Alertmanager.

```yaml
receivers:
  - name: 'line'
    webhook_configs:
      - url: 'http://webhook:5000/webhook'
        http_config:
          bearer_token: '« YOUR_LINE_API_TOKEN »'
```
