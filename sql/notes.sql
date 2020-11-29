CREATE TABLE Notes (
    'noteID' INTEGER NOT NULL PRIMARY KEY,
    'content' TEXT(50000),
    'author' INTEGER,
    FOREIGN KEY('author') REFERENCES accounts(id),
    'university' VARCHAR(300),
    'class' VARCHAR(300),
    'lectureName' VARCHAR(300)
); 

INSERT INTO Notes (noteID, content, author, university, class,lectureName)
VALUES(1, 'It was very interesting lecture.', 2, 'Suffolk University', 'Discrete Math', 'Connected Graphs');

SELECT accounts.name FROM Notes
INNER JOIN accounts ON notes.author==accounts.id;

