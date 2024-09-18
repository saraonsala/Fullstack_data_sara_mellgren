desc;

SELECT * FROM information_schema.schemata;

CREATE TABLE jokes (
    id INTEGER PRIMARY KEY,
    joke_text VARCHAR,
    rating INTEGER
);

desc;
SELECT * FROM main.jokes;

INSERT INTO jokes (id, joke_text, rating) VALUES
(1, 'Why don’t scientists trust atoms? Because they make up everything!', 8),
(2, 'Why did the scarecrow win an award? Because he was outstanding in his field!', 7),
(3, 'I told my wife she was drawing her eyebrows too high. She looked surprised.', 9),
(4, 'Why don’t skeletons fight each other? They don’t have the guts.', 6);

desc first_db.main.jokes;

SELECT * FROM jokes WHERE rating >7;