# Lab Overview

This lab show the difference between procedural-style code and OOP-style code, While also
show the use of lambda function in python, including the pros and cons.

Furthermore, this lab let us implement a database and joining table ourself

## Project Structure

### oop_lab_1

- `READEME.md`: This readme file
- `Cities.csv`: The Cities data
- `Countries.csv`: The Countries data
- `data_processing.py`: The analysis code for this program

## Design Overview

### Dataloader Class

Located in `data_processing.py`, the `Dataloader` class includes:

**Attributes**
- `base_path` (str): The path of csv file. (Default = file in the same directory)

**Methods**
- `load_csv(self, filename)`: Retrieve the `csv data` from path and return as a `list`.

### DB Class

Located in `data_processing.py`, this class is used to store all the table, the `DB` class include:

**Attributes**

- `datas` (list): The list of tables.

**Methods**

- `insert(self, table)`: Insert `table` inside the `Database`.
- `search(self, target)`: Find and return the given `table` name

### Table Class

Located in `data_processing.py`, the `Table` class includes:

**Attributes**

- `table_name` (str): The name of the table.
- `table` (list): The Data

**Methods**

- `filter(self, condition)`: Filter the `data` with given `condition`, Then return as a `Table` class.
- `aggregate(self, aggregation_function, aggregation_key)`: Aggregate the `data` with given `condition` and `column name(key)`, Then return as a value.
- `join(self, other_table, key)`: Join two `table` with the given `key` and return as a new `table`.

##  Running the Code

To run the data processing, execute `data_processing.py`:

```bash
python data_processing.py
