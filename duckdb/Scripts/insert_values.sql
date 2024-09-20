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

INSERT INTO jokes (id, joke_text, rating) VALUES
(5, 'Why don’t some couples go to the gym? Because some relationships don’t work out.', 8),
(6, 'I would avoid the sushi if I was you. It’s a little fishy.', 7),
(7, 'Want to hear a joke about construction? I’m still working on it.', 6),
(8, 'Why don’t programmers like nature? It has too many bugs.', 9),
(9, 'How does a penguin build its house? Igloos it together.', 1),
(10, 'A gothenburg person stands in queue for star wars. When someone cuts the line he says ge daj.', 2);

