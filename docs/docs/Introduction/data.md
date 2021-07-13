## Data class : 
### __init__ method:
##### Parameters:
* **self**: To be used in form of `Data()`
##### Functionality:
* **Initializes Data object** 
### show_datasets: 
##### Parameters:
* **self**: To be used in form of `obj.show_datasets()` 
##### Returns:
* **dataset_names**: returns a list that contains the list of all available datasets that can be loaded through `load_dataset()`


### load_dataset : 
##### Parameters:
* **self**: To be used in form of `obj.show_dataset(name)`
* **name**: contains the  name of one of the datasets that were shown using `show_datasets()`
##### Returns:
* **dataset**: returns a dataset whose name of given as input
