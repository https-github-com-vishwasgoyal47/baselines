## Pipeline Class
### Import Pipeline
```python
from baseline.pipeline import Pipeline
```
### Instantiate Pipeline
```python
graph = Pipeline(dataset)
```
### Use show_graph
```python
#pipeline should only have sklearn components
graph.show_graph(pipelineToBeShown)
```