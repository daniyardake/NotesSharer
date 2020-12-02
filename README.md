# Lecture Notes Sharer

This is final project of Intro to Database Design Class, where we learned introduction to SQL. For the final project we had to use any programming language and db to create a single application that executes some SQL commands. I decided to use Flask framework. However, as the main purpose was to use SQL commands I did not use SQLAlchemy to handle ORM.

The web application has landing page and notes page. After user has registered, he will be able to add lecture notes from his university. There is "All Notes" page, which displays all lecture notes uploaded by the users. In addition, every user can edit their profile, edit notes, and leave comments on notes. There is a "search by" functionality on the "All Notes" page.

## Live view

You can check the live version of the website [here](http://daniyardake.pythonanywhere.com/). Please, create an issue or push request if it doesn't work.

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements.

```bash
pip install -r requirements.txt
```

## Usage
 
```bash
python app.py
```

## Sample data

There is an SQL folder, where you can find SQL queries to create sample data. 

- Accounts: 
```SQL 
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
```

- Notes 

```SQL
INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('A connected graph is graph that is connected in the sense of a topological space, i.e., there is a path from any point to any other point in the graph. A graph that is not connected is said to be disconnected. This definition means that the null graph and singleton graph are considered connected, while empty graphs on n>=2 nodes are disconnected. The number of n-node connected unlabeled graphs for n=1, 2, ... are 1, 1, 2, 6, 21, 112, 853, 11117, 261080, ... (OEIS A001349). The total number of (not necessarily connected) unlabeled n-node graphs is given by the Euler transform of the preceding sequence, 1, 2, 4, 11, 34, 156, 1044, 12346, ... (OEIS A000088; Sloane and Plouffe 1995, p. 20). Furthermore, in general, if a_n is the number of unlabeled connected graphs on n nodes satisfying some property, then the Euler transform b_n is the total number of unlabeled graphs (connected or not) with the same property. This application of the Euler transform is called Riddells formula.', 1, 'Suffolk University', 'Discrete Math', 'Connected Graphs');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from. All these objects have a iter() method which is used to get an iterator. To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object. As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created. The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself. The __next__() method also allows you to do operations, and must return the next item in the sequence.', 9, 'MIT', 'Intro to Python', 'Iterators');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('Write a paper in response to the question below.  The paper is due in class on Thursday, 13February.  Late papers will not be accepted (unless there are extenuating circumstances that need to be cleared with Professor Johnson). This paper is based on the readings from Niebuhr. Find passages in Niebuhr and one (1) outside source (book or article, nothing from the internet) to support or provide illustrations for your arguments.The papers should conform to the following specifications', 1, 'Suffolk University', 'Ethics and Civil Life', 'Assignment 1');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('A connected graph is graph that is connected in the sense of a topological space, i.e., there is a path from any point to any other point in the graph. A graph that is not connected is said to be disconnected. This definition means that the null graph and singleton graph are considered connected, while empty graphs on n>=2 nodes are disconnected. The number of n-node connected unlabeled graphs for n=1, 2, ... are 1, 1, 2, 6, 21, 112, 853, 11117, 261080, ... (OEIS A001349). The total number of (not necessarily connected) unlabeled n-node graphs is given by the Euler transform of the preceding sequence, 1, 2, 4, 11, 34, 156, 1044, 12346, ... (OEIS A000088; Sloane and Plouffe 1995, p. 20). Furthermore, in general, if a_n is the number of unlabeled connected graphs on n nodes satisfying some property, then the Euler transform b_n is the total number of unlabeled graphs (connected or not) with the same property. This application of the Euler transform is called Riddells formula.', 1, 'Suffolk University', 'Discrete Math', 'Connected Graphs');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('A proof by induction consists of two cases. The first, the base case (or basis), proves the statement for n = 0 without assuming any knowledge of other cases. The second case, the induction step, proves that if the statement holds for any given case n = k, then it must also hold for the next case n = k + 1. These two steps establish that the statement holds for every natural number n.[3] The base case does not necessarily begin with n = 0, but often with n = 1, and possibly with any fixed natural number n = N, establishing the truth of the statement for all natural numbers n ≥ N. The method can be extended to prove statements about more general well-founded structures, such as trees; this generalization, known as structural induction, is used in mathematical logic and computer science. Mathematical induction in this extended sense is closely related to recursion. Mathematical induction is an inference rule used in formal proofs, and in some form is the foundation of all correctness proofs for computer programs.[4] Although its name may suggest otherwise, mathematical induction should not be confused with inductive reasoning as used in philosophy (see Problem of induction). The mathematical method examines infinitely many cases to prove a general statement, but does so by a finite chain of deductive reasoning involving the variable n, which can take infinitely many values.[5] ', 8, 'Harvard College', 'Discrete Math 2', 'Mathematical Induction');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('In mathematics, real analysis is the branch of mathematical analysis that studies the behavior of real numbers, sequences and series of real numbers, and real functions.[1] Some particular properties of real-valued sequences and functions that real analysis studies include convergence, limits, continuity, smoothness, differentiability and integrability. Real analysis is distinguished from complex analysis, which deals with the study of complex numbers and their functions. ', 5, 'Boston University', 'Real Analysis', 'Intro Lecture');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('To create a file in Java, you can use the createNewFile() method. This method returns a boolean value: true if the file was successfully created, and false if the file already exists. Note that the method is enclosed in a try...catch block. This is necessary because it throws an IOException if an error occurs (if the file cannot be created for some reason). To create a file in a specific directory (requires permission), specify the path of the file and use double backslashes to escape the "\" character (for Windows). On Mac and Linux you can just write the path, like: /Users/name/filename.txt', 2, 'Tufts University', 'Java Programming', 'Input/Output Files');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]. A simple approach is to do linear search.The time complexity of above algorithm is O(n). Another approach to perform the same task is using Binary Search. Binary Search: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.', 10, 'Suffolk University', 'Data Structures and Algorithms', 'Binary Search');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('Linear and Logistic regressions are usually the first algorithms people learn in data science. Due to their popularity, a lot of analysts even end up thinking that they are the only form of regressions. The ones who are slightly more involved think that they are the most important among all forms of regression analysis. The truth is that there are innumerable forms of regressions, which can be performed. Each form has its own importance and a specific condition where they are best suited to apply. In this article, I have explained the most commonly used 7 types of regression in data science in a simple manner. Through this article, I also hope that people develop an idea of the breadth of regressions, instead of just applying linear/logistic regression to every machine learning problem they come across and hoping that they would just fit!', 7, 'MIT', 'Intro to Machine Learning', 'Regression Models');

INSERT INTO Notes (content, author, university, class,lectureName)
VALUES('NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices. NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely. NumPy stands for Numerical Python. In Python we have lists that serve the purpose of arrays, but they are slow to process. NumPy aims to provide an array object that is up to 50x faster than traditional Python lists. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy. Arrays are very frequently used in data science, where speed and resources are very important. NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently. This behavior is called locality of reference in computer science. This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.', 4, 'Suffolk University', 'Intro to Data Science', 'NumPy');

```

- Comments

```SQL
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
```

## ER Diagram

![ER Diagram](static/assets/ER Diagram.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)