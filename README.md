Empirical-CheckStyle
====================

Link to trello board:
[Empirical-CheckStyle Trello board](https://trello.com/b/QlvMd8iU/empirical-checkstyle)

Link to FinalReport.md
[FinalReport.md](https://github.ncsu.edu/CSC510-Fall2014/Empirical-CheckStyle/blob/master/reports/FinalReport.md)


### Project environment set-up

#### Installing dependencies

For ubuntu:

Install Mysql: 

`sudo apt-get install mysql-server`

Install python-3: 

`sudo apt-get install python3 python3-dev python3-pip`

Install development headers: 

`sudo apt-get install build-essential libmysqlclient-dev`

Install pylint:

`sudo apt-get install pylint`

Install mysql connector for python: 

`sudo pip3 install git+git://github.com/davispuh/MySQL-for-Python-3`

#### Installing dependencies for plotting

```
sudo apt-get install python3-pandas 
pip3 install ggplot  matplotlib --user
```


#### Database setup:

This project requires mysql to be installed on your machine. After successful installation of mysql, run the sql commands from the file `data_base_schema.sql` located in the project folder. This will create required database and tables. 

Default database credentials are 
user-name: root
password: root


### Data Collection

+ Clone some python repositories from gitHub.

+ Run the main python file `python3 checkstyle/empirical_checkStyle.py` with required parameters. This file takes 3 parameters.
    1. <repo_path> This is the path to the downloaded python repository. 
    2. <package_path> This is the path to main python package located in repository.
    3. <project_name> Name of the project. This is basically the name you wish to store in database.

### Report Generation

Once the data is successfully collected in the database, all the reports that are mentioned in FinalReport.md are generated by running `python3 dataExploration.py`. 

Please note that the name of the modules for which the report is generated are according to the repos that I have cloned. You may need to change these names in the mysql queries according to the data collected in your machine.



### References:

* [Prioritizing Warning Categories by Analyzing Software History](https://github.ncsu.edu/CSC510-Fall2014/Empirical-CheckStyle/blob/master/papers/Warnings.pdf?raw=true)

* [Pylint software for code analysis](http://www.pylint.org/)
