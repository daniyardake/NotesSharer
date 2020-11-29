CREATE TABLE Comments (
    'commentID' INTEGER NOT NULL PRIMARY KEY,
    'content' VARCHAR(300),
    'author' INTEGER,
    'note' INTEGER,
    FOREIGN KEY('author') REFERENCES accounts(id),
    FOREIGN KEY('note') REFERENCES notes(noteID)
); 

INSERT INTO Comments (commentID, content, author, note)
VALUES(1, 'Thanks for sharing! It is very helpful!', 5, 1);
