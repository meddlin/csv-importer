# csv-importer

Generate SQL to create tables and import data from CSV files

## Why?

Excel wasn't cutting it.

I needed to shove some CSV files into a database; standing up a database, ETL process, 
and architecture was too much.

This utility will take your CSV file as input, and create some opinionated (and rather 
naive) table structure for you, in Postgres. Why Postgres? Opinions.