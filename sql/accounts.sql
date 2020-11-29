CREATE TABLE 'accounts' (
'id' INTEGER PRIMARY KEY,
'login' VARCHAR(255),
'password' VARCHAR(255),
'name' VARCHAR(255),
'university' VARCHAR(255),
'github' VARCHAR(255)
);

INSERT INTO accounts (login, password, name)
VALUES('daniyar', '1234567', 'Daniyar Aubekerov');



UPDATE accounts
SET 'university' = 'Suffolk University',
    'github' = 'daniyardake'
WHERE
    accounts.id = 1