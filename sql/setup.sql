CREATE TABLE 'accounts' (
'id' INTEGER PRIMARY KEY,
'login' VARCHAR(255),
'password' VARCHAR(255),
'name' VARCHAR(255)
);

INSERT INTO accounts (login, password, name)
VALUES('daniyar', '1234567', 'Daniyar Aubekerov');