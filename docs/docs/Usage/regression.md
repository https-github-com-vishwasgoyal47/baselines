## Regression Class
### Import Regression Class
```python
from baseline.regression import Regression
```
### Instantiate Regression
```python
regressors = Regression()
```
### use regressor method
```python
# also pass the resultant column
results = regressors.regressor(dataset , resultantColumn)
print(results)
```