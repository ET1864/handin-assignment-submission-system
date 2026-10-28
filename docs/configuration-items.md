# Configuration Items

| ID | Item | Location | Type |
|----|------|----------|------|
| CI-01 | Application source code | app/ | Source code |
| CI-02 | Database schema and seed data | database/ | Database |
| CI-03 | Requirements document | docs/requirements.md | Document |
| CI-04 | Test files | tests/ | Test |
| CI-05 | User guide | docs/user-guide.md | Document |
| CI-06 | Dependency list | requirements.txt | Configuration |
| CI-07 | Application configuration | config.py | Configuration |
| CI-08 | Change request records | docs/change-requests/ | Document |
| CI-09 | Design wireframes | docs/design/ | Document |
| CI-10 | README | README.md | Document |

The SQLite database file itself is not tracked (`*.db` is ignored). The schema
and seed scripts that build it are the configuration items.
