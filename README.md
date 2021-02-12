# udacity-dend-capstone-project

This notebook gets output data from [metro-big-data-unir](https://github.com/juananthony/metro-big-data-unir) project and create a database to analysis.

[*Metro de Madrid*](https://www.metromadrid.es/) is the name of the tube/subway service that operates in Madrid, Spain. This service has 302 stations on 13 lines plus a light rail system called *Metro Ligero*. This service is used, on average in 2020, more than 30 million times each month.

## Conceptual Data Model
The data we want to store is all messages that inform about any issue or complaint in a line or a station even if one message inform about an issue that affect two different lines. That the reason why the fact table is the inform fact, that can be a complaint or an issue. One tweet can inform about an issue that affect two lines (i.e.: a closed station and all lines that stops there). In other words, one tweet generates one or many "inform fact" records.
![fact-dimension diagram](./img/class_diagram.png "Fact-Dimension Diagram")



## Data dictionary 

### Dimension Tables

* **Line**
    * ```line_id```
        * ```Long```
        * Line identifier.
    * ```line_name```
        * ```String```
        * Line name.
    * ```
* **Station**
* **Class**
* **User**
* **Date**
* **Tweet**

### Fact Table

* **Inform**