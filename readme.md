## About

Repository contains maper and reducer used by Hadoop Streaming which are processing data about accidents which has happened in NYC after 2012 year.

After that Hive script is checking which incidets has happened on Manhattan and showing 3 most dangerous streets in term of incidents with casualties for both killed and injured victims.

## Prerequisites

- GCP stogare bucket with stored CSV files with initial data (change [THIS](https://github.com/Kacperek0/wsb-big-data-project/blob/02ecb6bce5aefb3d90ebf0a9a30b60cdb6c411de/run.sh#L23) line to make run script work)

## Running the project

1. Create *Storage bucket* and feed it with initial CSV files.
2. Deploy *Dataproc cluster*.
3. Connect via SSH with master node.
4. Clone this repository
```bash
git clone https://github.com/Kacperek0/wsb-big-data-project.git
```
5. Enter the repo directory
```bash
cd wsb-big-data-project
```
6. Add execution rights to run script
```bash
chmod +x run.sh
```
7. Run a script and wait few seconds for the results (around 2 min tbh. hadoop streaming ain't super fast)
```bash
./run.sh
```
8. Profit :)

### Alternative way of running the project

1. Create *Storage bucket* and feed it with initial CSV files.
2. Deploy *Dataproc cluster*.
3. Connect via SSH with master node.
4. Run init wrapper
```bash
curl https://raw.githubusercontent.com/Kacperek0/wsb-big-data-project/master/init.sh | bash
```

## Author
Scripts has been developed by [Kacperek0](https://github.com/Kacperek0)

### License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
