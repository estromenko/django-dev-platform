<h1 align="center">
    Django Dev Platform (WIP)
</h1>
<p align="center">
    Universal collaborative platform that includes
    lots of useful apps for in-team and cross-team communication
</p>

<hr>

# 🎯 Roadmap
- [ ] Chat
- [ ] Video calls
- [ ] Discussions
- [ ] Kanban Deck
- [ ] Knowledge base
- [ ] Password manager
- [ ] Calendar

# ⚡ Getting started

## Development

Requirements:
- python>=3.11
- [poetry](https://python-poetry.org)
- [Tailwind CSS standalone cli](https://tailwindcss.com/blog/standalone-cli)
- docker

## 1. Install dependencies

```bash
poetry install --no-root
```

## 2. Apply migrations
```bash
poetry run ./manage.py migrate
```

## 3. Run redis
```bash
docker run --rm --net host -d redis:7.2.3-alpine3.18
```

## 3. Run server
```bash
poetry run ./manage.py runserver
```

## 4. Create superuser (optional)
```bash
poetry run ./manage.py createsuperuser
```

<hr>

## Production

Soon.
