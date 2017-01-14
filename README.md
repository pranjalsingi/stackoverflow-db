# stackoverflow-db
Designed database for implementation of stackoverflow. The designing includes ER Model and Relational Schema. Also the schema was translated to create tables.
Some queries were answered and there run time were improved with optimizing the queries.

<b>Data</b>
There were some text files which contains the data for implementation of stackoverflow database. 
The txt's were users, posts, comments, tags, posttags, votes and favs.

To implement the data according to the ER model built, the data was preprocessed.

The posts tables had all the questions and answers. It was split into questions and answers and altered favs too get rid of a redundant column using preprocess.py file. 

<b>Optimization</b>
Refactoring the data helped in processing the query faster as the desired index were created when the tables were formed.
There was no need to create additional indexes on the table. There were three additional tables created that is question, answers and hasaccepted that helped in optimizing.

<b>Run project</b>
Download data  - http://ir.cis.udel.edu/~carteret/data.zip

Preprocess data - paste the python file in the data folder and execute it.

Create a database in mysql and then load the schemadump.sql to make all the tables.

Load data - 
Example: LOAD DATA LOCAL INFILE ’/full/path/to/ques.txt’ INTO TABLE questions FIELDS TERMINATED BY ’\t’;

When importing data for questions and answers turn of the foreign key constraint by SET foreign key checks=0;

<b>Queries</b>
Find the queries and their answers in queries.txt

<b>more</b>
Please read report.txt for detailed information about the project.

PS: This is not all the data from the stackoverflow. It has been preprocessed before to stash the size of data.
