# yt-manager-multi
# YouTube Manager (Multi-Version CLI Project)

A learning project that evolves from basic Python to SQLite and MongoDB.

---

## Versions

### ✅ Version 1: JSON-based CLI App
- Pure Python, stores data in a `.txt` file using JSON
- Basic CRUD support in terminal
- Folder: `01_basic_version-json`

---

### ✅ Version 2: SQLite-based CLI App
- Uses SQLite (`youtube-vid.db`) instead of flat JSON file
- Stores data in a structured, queryable format
- Built-in table creation and robust data handling
- Still terminal-based, but more production-ready
- Folder: `02_yt_manager_sqlite`

#### Features
- Add, list, update, and delete videos
- Uses `sqlite3` module from Python standard library
- Each video has: `id`, `name`, and `time`
- Prevents data loss via real DB transactions

#### Run the App
```bash
cd 02_yt_manager_sqlite
python yt_manager_db.py
