DROP TABLE IF EXISTS episodes;
DROP TABLE IF EXISTS series;

CREATE TABLE series (
    tconst TEXT PRIMARY KEY,
    titleType TEXT NOT NULL,
    primaryTitle TEXT NOT NULL,
    originalTitle TEXT NOT NULL,
    isAdult BOOLEAN NOT NULL,
    startYear INT NULL,
    endYear INT NULL,
    runtimeMinutes INT NULL,
    genres TEXT NULL,
    averageRating DECIMAL(3,1) NOT NULL,
    numVotes INT NOT NULL
);

CREATE TABLE episodes (
    tconst TEXT PRIMARY KEY,
    parentTconst TEXT NOT NULL,
    seasonNumber INT NOT NULL,
    episodeNumber INT NOT NULL,
    titleType TEXT NOT NULL,
    primaryTitle TEXT NOT NULL,
    originalTitle TEXT NOT NULL,
    isAdult BOOLEAN NOT NULL,
    startYear INT NULL,
    endYear INT NULL,
    runtimeMinutes INT NULL,
    genres TEXT NULL,
    averageRating DECIMAL(3,1) NOT NULL,
    numVotes INT NOT NULL,
    FOREIGN KEY (parentTconst) REFERENCES series(tconst) ON DELETE CASCADE
);

\copy series (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, numVotes) FROM 'preprocessed/series.csv' DELIMITER ',' CSV HEADER;

\copy episodes (tconst, parentTconst, seasonNumber, episodeNumber, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres, averageRating, numVotes) FROM 'preprocessed/episodes.csv' DELIMITER ',' CSV HEADER;


