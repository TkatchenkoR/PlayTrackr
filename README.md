# PlayTrackr
Personal IT project, football highlights


# Repo Structure
playtrackr/
├── README.md
├── LICENSE
├── .gitignore
├── pyproject.toml          # or requirements.txt + setup.cfg
├── docker-compose.yml      # later: API + maybe DB
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py         # FastAPI entrypoint
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── v1/
│   │   │       ├── __init__.py
│   │   │       ├── routes_jobs.py     # submit/check jobs
│   │   │       └── routes_health.py   # healthcheck
│   │   ├── core/
│   │   │   ├── config.py    # settings: paths, models, etc.
│   │   │   └── logging.py   # log setup
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── video_ingest.py      # download/normalise video
│   │   │   ├── detection.py         # YOLO wrapper
│   │   │   ├── tracking.py          # ByteTrack/DeepSORT wrapper
│   │   │   ├── player_id.py         # selecting "you"
│   │   │   ├── touch_detection.py   # ball–player interaction logic
│   │   │   └── jobs.py              # orchestrates full pipeline for one match
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── job.py       # Pydantic models for job requests/responses
│   │   │   └── events.py    # Pydantic models for touch events
│   │   └── db/
│   │       ├── __init__.py
│       │   ├── base.py      # database connection (can be SQLite at start)
│       │   └── schemas.py   # ORM models (Job, Match, Event) – optional for MVP
│   └── tests/
│       ├── __init__.py
│       ├── test_detection.py
│       ├── test_tracking.py
│       └── test_touch_detection.py
├── ml/
│   ├── notebooks/
│   │   ├── 01_yolo_detection_dev.ipynb
│   │   ├── 02_tracking_experiments.ipynb
│   │   └── 03_touch_logic_experiments.ipynb
│   ├── scripts/
│   │   ├── run_detection.py      # quick CLI to test detector on a video
│   │   ├── run_tracking.py       # test tracker end-to-end
│   │   └── visualise_events.py   # overlay detected touches on video
│   └── models/
│       └── README.md             # notes/links about weights (not checked in)
├── data/
│   ├── raw/          # original test videos (ignored in git)
│   ├── processed/    # extracted frames / intermediate outputs
│   └── outputs/      # result JSONs, event lists, sample clips
├── scripts/
│   ├── dev_run_api.sh           # run backend locally
│   └── format_check.sh          # black/ruff/mypy etc – optional
└── frontend/                    # you can add this later
    ├── packa
