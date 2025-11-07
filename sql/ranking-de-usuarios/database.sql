CREATE TABLE IF NOT EXISTS google_gmail_emails (
    id INTEGER PRIMARY KEY,
    from_user TEXT,
    to_user TEXT,
    day INTEGER
);

INSERT INTO google_gmail_emails (id, from_user, to_user, day)
VALUES
    (1, 'ana', 'bruno', 1),
    (2, 'ana', 'carlos', 1),
    (3, 'bruno', 'daniela', 1),
    (4, 'carlos', 'ana', 2),
    (5, 'ana', 'daniela', 2),
    (6, 'bruno', 'carlos', 2),
    (7, 'ana', 'erica', 3);