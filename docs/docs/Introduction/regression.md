## Regression Class:
### __init__ method:
##### Parameters:
* **self**: To be used in form of `Regression()`
##### Functionality:
* **Initializes Regression object** 
### regressor method:
##### Parameters:
* **self**: To be used in form of `obj.regressor(dataset)`
* **dataset**: Takes a pandas dataframe as input . 
* **resultantColumn**: the column on which the predictions will take place. It should be present in  `dataset`.

##### Returns:
* **results**: A pandas dataframe that contains the benchmarking of dataset over vaious algorithms using `Pipeline()` and `GridSearchCV()`. 