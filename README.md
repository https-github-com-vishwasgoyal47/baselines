# baselines
a python package used for benchmarking algorithms over various datasets<br>

<h2>Data class :</h2> <br>
&nbsp;   <h3>show_datasets :</h3> show available datasets<br>
&nbsp;    <h3>load_dataset :</h3> load specific dataset (pass name as argument)<br>

<h2>Classification class :</h2><br>
&nbsp;    <h3>classification method:</h3><br>
&nbsp;&nbsp;  parameters:<br>
&nbsp;&nbsp;&nbsp;       dataset in csv format or pandas dataframe with classification column at last<br>
&nbsp;&nbsp;       result:<br>
&nbsp;         returns benchmark for dataset with various algorithms and its f1_score<br>

<h2>Regression Class:</h2><br>
&nbsp;<h3>regressor method:</h3><br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;dataset (pandas dataframe)<br>
&nbsp;&nbsp;&nbsp;resultantColumn (name of column which has the value to be predicted)

<h2>Pipeline Class:</h2><br>
&nbsp; __init__ method:<br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;dataset (pandas dataframe)<br>
&nbsp;show_graph method:<br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;pipeline_show (sklearn Pipeline object which will be inturn turned to graph)<br>

<h1>How to use</h1><br>
&nbsp;&nbsp;<h2>Data Class</h2><br>
```
from baseline.Data import Data
data = Data()
dataset_names = data.show_dataset()
#name should be only from dataset_names 
dataset = data.load_dataset('name') 
```
