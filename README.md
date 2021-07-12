# baselines
a python package used for benchmarking algorithms over various datasets<br>

Data class : <br>
    show_datasets to show available datasets<br>
    load_dataset to load specific dataset (pass name as argument)<br>

Classification class :<br>
    classification method:<br>
        parameters:<br>
            dataset in csv format or pandas dataframe with classification column at last<br>
        result:<br>
            returns benchmark for dataset with various algorithms and its f1_score<br>
