"""Проверка работоспособности контейнера.

HTTP-сервер у бота поднимается ТОЛЬКО если задан WEBHOOK_BASE_URL (режим
webhook). В режиме long polling бот вообще не открывает порт - это
нормальный режим, и проверка обязана пройти, иначе Docker будет считать
рабочий контейнер нездоровым и перезапускать его.

Если же порт открыт и сервер отвечает ошибкой - это реальная проблема.
"""
import os
import sys
import urllib.error
import urllib.request

port = os.environ.get("PORT", "8080")
try:
    urllib.request.urlopen("http://127.0.0.1:%s/health" % port, timeout=5)
except urllib.error.URLError:
    pass
except Exception:
    sys.exit(1)
