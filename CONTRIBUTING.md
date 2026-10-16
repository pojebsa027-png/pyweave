# Contributing

## Setup

```bash
git clone https://github.com/pojebsa027-png/pyweave.git
cd pyweave
```

Per-stack install, nothing is shared at the root:

```bash
pip install -r django/requirements.txt
pip install -r flask/10-taskapp/requirements.txt
```

## Running the checks

```bash
make test        # Django test suite + Flask import check
make lint        # compileall over both trees
```

## House rules

- One concept per Flask step directory. If you add a step, renumber nothing —
  append.
- Django stays a single app. New functionality goes into `core`, not into a new
  app.
- No committed databases, no committed secrets. `db.sqlite3`, `tasks.db` and
  `*_settings.py` are gitignored on purpose.
- Pin dependencies. The whole point of this repo is that it boots a year later.
