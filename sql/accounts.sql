CREATE TABLE 'accounts' (
'id' INTEGER PRIMARY KEY,
'login' VARCHAR(255),
'password' VARCHAR(255),
'name' VARCHAR(255),
'university' VARCHAR(255),
'github' VARCHAR(255)
);

INSERT INTO accounts (login, password, name, university, github) VALUES('daniyar', '1234567', 'Daniyar Aubekerov', 'Suffolk University', 'daniyardake');
INSERT INTO accounts (login, password, name, university) VALUES('john', '1234567', 'John Smith', 'Tufts University');
INSERT INTO accounts (login, password, name, university, github) VALUES('george', '1234567', 'George Hunting', 'Boston University', 'george');
INSERT INTO accounts (login, password, name, university) VALUES('madison', '1234567', 'Madison Li', 'Suffolk University');
INSERT INTO accounts (login, password, name, university) VALUES('shlim', '1234567', 'Shin Lim', 'Boston University');
INSERT INTO accounts (login, password, name) VALUES('ptalor', '1234567', 'Pan Taylor');
INSERT INTO accounts (login, password, name, university, github) VALUES('nur001', '1234567', 'Nurbek Nursultan', 'MIT', 'nurd');
INSERT INTO accounts (login, password, name, university, github) VALUES('lucy', '1234567', 'Lucy Lee', 'Harvard College', 'lucy');
INSERT INTO accounts (login, password, name, university, github) VALUES('william', '1234567', 'Will I Am', 'MIT', 'nwill');
INSERT INTO accounts (login, password, name, university) VALUES('pogba', '1234567', 'Paul Pogba', 'Suffolk University');


