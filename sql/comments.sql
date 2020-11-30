CREATE TABLE Comments (
    'commentID' INTEGER NOT NULL PRIMARY KEY,
    'content' VARCHAR(300),
    'author' INTEGER,
    'note' INTEGER,
    FOREIGN KEY('author') REFERENCES accounts(id),
    FOREIGN KEY('note') REFERENCES notes(noteID)
); 

INSERT INTO Comments (content, author, note)
VALUES('I will try to upload next lecture!', 1, 1);

INSERT INTO Comments (content, author, note)
VALUES('Thanks for sharing!', 1, 2);

INSERT INTO Comments (content, author, note)
VALUES('I think you have a typo in the 2nd sentence?', 1, 9);

INSERT INTO Comments (content, author, note)
VALUES('Wow! Good job!', 2, 1);

INSERT INTO Comments (content, author, note)
VALUES('What grade did you get for the assignment?', 2, 3);

INSERT INTO Comments (content, author, note)
VALUES('How about Euler paths?', 3, 4);

INSERT INTO Comments (content, author, note)
VALUES('Thanks!', 4, 5);

INSERT INTO Comments (content, author, note)
VALUES('Helpfull!', 5, 6);

INSERT INTO Comments (content, author, note)
VALUES('Like!!!', 6, 7);

INSERT INTO Comments (content, author, note)
VALUES('Amazing! Thanks for contributing!', 8, 2);
