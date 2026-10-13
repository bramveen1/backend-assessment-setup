# Interview setup check

Thanks for coming to our technical interview! This tiny project checks that your laptop is ready.
It uses exactly the same Python packages as the exercise you'll get on the day, so once this
works, setup on the day takes a minute.

Use your own laptop, editor and OS (macOS, Linux and Windows all work), with your usual tools,
including any AI assistant you normally use.

## What you need

- `git`
- **Either** [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended; it
  installs Python 3.12 for you) **or** Python 3.12 or newer with `pip`
- Your editor or IDE of choice

## Run the check

### Option A: uv

```bash
uv sync
uv run pytest
uv run python manage.py runserver        # then open http://localhost:8000/api/ping/
```

### Option B: pip + venv

```bash
python -m venv .venv
source .venv/bin/activate                # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
pytest
python manage.py runserver               # then open http://localhost:8000/api/ping/
```

You're ready when `pytest` reports **3 passed** and the ping page shows `"status": "ok"`.

If anything fails, just email us the error. We'd rather fix it before the interview than during it.

## On the day

Please arrive 15 minutes early. We'll get you on the wifi and you'll clone the exercise repository
then. You don't need to prepare anything else.
