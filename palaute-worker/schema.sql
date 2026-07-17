-- Suomen Paras — customer feedback (Anna oma arvio)
CREATE TABLE IF NOT EXISTS arviot (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vertical TEXT NOT NULL,
  slug TEXT NOT NULL,
  fiilis INTEGER NOT NULL CHECK (fiilis BETWEEN 1 AND 5),
  luotettava INTEGER NOT NULL DEFAULT 0,
  hintansa INTEGER NOT NULL DEFAULT 0,
  suosittelisin INTEGER NOT NULL DEFAULT 0,
  uudelleen INTEGER NOT NULL DEFAULT 0,
  nimi TEXT,
  teksti TEXT,
  ip_hash TEXT,
  created_at TEXT NOT NULL,
  approved INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_arviot_company ON arviot (vertical, slug, approved);
CREATE INDEX IF NOT EXISTS idx_arviot_pending ON arviot (approved);
