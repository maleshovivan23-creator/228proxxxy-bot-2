"""Точка входа для хостингов, которые запускают `python app.py`.

Код бота лежит одним файлом в proxy-shop-bot.pyz; Python импортирует пакеты
из zip-архива напрямую, поэтому достаточно добавить архив в sys.path.

Если платформа позволяет задать команду запуска, можно указать вместо этого:
    python proxy-shop-bot.pyz
"""

import asyncio
import pathlib
import sys

ARCHIVE = pathlib.Path(__file__).with_name("proxy-shop-bot.pyz")
if not ARCHIVE.is_file():
    raise SystemExit(
        f"Не найден {ARCHIVE.name}: загрузите его в репозиторий рядом с app.py"
    )

sys.path.insert(0, str(ARCHIVE))

from app.main import main  # noqa: E402 (импорт после правки sys.path)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
