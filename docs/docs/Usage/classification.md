## Classification Class
### Import Classification
```python
from baseline.classification import Classification
```
### Instantiate Classification
```python
classifier = Classification()
```
### Use classification method
```python
# dataset's last column should be the column to be classified
results = classifier.classification(dataset)
print(results)
```