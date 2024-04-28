# Required Python Packages

Numpy is a python package used to define the Laplacian error function.

Prefixspan is a python package used to mine the most frequent patterns from a given Trajectory Database.

## Installation

Use the package manager `pip` to install Numpy and Prefixspan.

```bash
pip3 install -U numpy
pip3 install -U prefixspan
```

or you can just do
```
pip install -r requirements.txt
```

## Achieving Differential Privacy

We start with the `Trajectory_Dataset.txt` file that contains a record of Trajectories with Timestamps.

We process this data using `data.py` and create a new file `Trajectory_Dataset_Final.txt` that contains a record of trajectories of the type `2,3,4,5` which means a trajectory `2->3->4->5`.
```
python3 data.py
```
Now the database in `Trajectory_Dataset_Final.txt` will be used to create a sanitized dataset using the `Prefixtree.py` file.

This file contains the program to create a noisy prefix tree based on our curent database by inducing Laplacian Noise.

The `Privacy_Budget`, `Noisy_Tree_Height` and `Theta_threshold` can be changed in `Prefixtree.py` on the lines 80,81 and 82.
```
python3 Prefixtree.py
```
A new file `Sanitized_data.txt` is created which contains a new database created according to the `Privacy_Budget`,`Theta_threshold` which has achieved Differential Privacy.


## Evaluation

Evaluation is carried out using `CountQueries` and `FrequentPattern` tasks.

For Evaluating the Average Count Query Error run the `count_queries.py` file.

```
python3 count_queries.py
``` 
The output is of the form
```
Average Count Query Error : 0.231493904011065
```

For evaluating the Frequent Patterns task run the `frequent_pattern.py` file.

Set the `max_height` variable on line 26 to the same value as the height in `Prefixtree.py`.

Set the `top_k` variable on line 27 to change the number of most frequent patterns to be mined. 

```
python3 frequent_pattern.py
```
The output is of the form
```
Number of matches in top 200 frequent patterns : 48
```
