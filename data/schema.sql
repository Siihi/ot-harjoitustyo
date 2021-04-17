CREATE TABLE Users
(
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE Accounts
(
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    date DATE,
    amount INTEGER,
    account TEXT,
    name TEXT,
    currency TEXT
);
