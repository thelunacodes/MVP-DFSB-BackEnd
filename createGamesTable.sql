CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    gameImage VARCHAR(2083),
    gameName VARCHAR(50) NOT NULL,
    developer VARCHAR(50),
    publisher VARCHAR(50),
    platform VARCHAR(30) NOT NULL,
    link VARCHAR(2083),
    startedAtDate DATE,
    startedAtTime TIME,
    finishedAtDate DATE,
    finishedAtTime TIME,
    score FLOAT,

    -- CONSTRAINT pk_id 
    --     PRIMARY KEY (id),

    CONSTRAINT ck_score
        CHECK (score BETWEEN 0.0 AND 5.0),

    CONSTRAINT ck_date
        CHECK (startedAtDate < finishedAtDate)
);