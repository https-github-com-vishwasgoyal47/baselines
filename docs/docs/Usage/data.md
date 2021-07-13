## Data Class
### import class from baseline.data
```python
from baseline.Data import Data
 
```
### Instatiate Data Class
```python

data = Data()

```
### Use show_dataset method
```python
dataset_names = data.show_dataset()
print(dataset_names)

```
### Use load_dataset
```python
#name should be only from dataset_names 
dataset = data.load_dataset('name')
print(dataset) 
```