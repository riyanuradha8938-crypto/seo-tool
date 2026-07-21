-- 1. Track Target Websites
CREATE TABLE websites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL,
    domain TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Daily Tasks with Status Toggle
CREATE TABLE daily_tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    task_description TEXT,
    category TEXT,
    impact_level TEXT,
    status TEXT DEFAULT 'pending', -- 'pending' or 'completed'
    FOREIGN KEY(website_id) REFERENCES websites(id)
);

-- 3. Track Minimum 20 Keywords with Locality Settings
CREATE TABLE keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    website_id INTEGER,
    keyword_text TEXT NOT NULL,
    country_code TEXT DEFAULT 'us', -- 'us', 'in', 'uk', etc.
    last_rank INTEGER,
    FOREIGN KEY(website_id) REFERENCES websites(id)
);