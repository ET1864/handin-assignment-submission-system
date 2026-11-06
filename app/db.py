"""Database helper: one SQLite connection per request, plus init-db support."""
import os
import sqlite3

import click
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row          # rows behave like dicts: row["name"]
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def _run_sql_file(db, filename):
    path = os.path.join(current_app.root_path, "..", "database", filename)
    with open(path, encoding="utf-8") as f:
        db.executescript(f.read())


def init_db(seed=True):
    """Create all tables from schema.sql and (optionally) load seed.sql."""
    db = get_db()
    _run_sql_file(db, "schema.sql")
    if seed:
        _run_sql_file(db, "seed.sql")
    db.commit()


@click.command("init-db")
@click.option("--no-seed", is_flag=True, help="Create empty tables without sample data.")
def init_db_command(no_seed):
    """Rebuild the local database. WARNING: deletes existing data."""
    init_db(seed=not no_seed)
    click.echo("Database initialised" + (" (no seed data)." if no_seed else " with seed data."))


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
