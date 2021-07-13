## Pipeline Class:
### __init__ method:
##### Parameters:
* **self**: To be used in form of `obj.Pipeline(dataset)`
* **dataset**: Takes a pandas dataframe as input .
##### Functionality:
* **Initializes Pipeline object** 
### show_graph method:
##### Parameters:
* **self**: To be used in form of `obj.show_graph(name)`
* **pipeline_show**: any sklearn `Pipeline()` 
##### Functionality:
* **Makes Dot Graph**: converts the pipeline to list and saves the dot graph of pipeline as `Filename.jpeg` in your current directory 