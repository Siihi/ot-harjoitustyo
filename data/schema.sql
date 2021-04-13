CREATE TABLE Users
(
    id TEXT PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE Accounts
(
    id TEXT PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    date DATE,
    amount INT,
    account TEXT,
    name TEXT,
    currency TEXT
);
