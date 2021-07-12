# baselines
a python package used for benchmarking algorithms over various datasets<br>

Data class : <br>
&nbsp;   show_datasets : show available datasets<br>
&nbsp;    load_dataset : load specific dataset (pass name as argument)<br>

Classification class :<br>
&nbsp;    classification method:<br>
&nbsp;&nbsp;  parameters:<br>
&nbsp;&nbsp;&nbsp;       dataset in csv format or pandas dataframe with classification column at last<br>
&nbsp;&nbsp;       result:<br>
&nbsp;         returns benchmark for dataset with various algorithms and its f1_score<br>

Regression Class:<br>
&nbsp;regressor method:<br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;dataset (pandas dataframe)
&nbsp;&nbsp;&nbsp;resultantColumn (name of column which has the value to be predicted)

Pipeline Class:<br>
&nbsp; __init__ method:<br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;dataset (pandas dataframe)
&nbsp;show_graph method:<br>
&nbsp;&nbsp;parameters:<br>
&nbsp;&nbsp;&nbsp;pipeline_show (sklearn Pipeline object which will be inturn turned to graph)