# extract_numbers
Extract citation numbers within parenthesis such as [10, 26, 30]. This partially helps automation of daily routines.

# Test example of "test.txt"
```
Deep neural networks have demonstrated remarkable performance
in various fields such as object detection, semantic segmentation,
and image classification [10, 26, 30]. The performance of deep neural
networks varies depending on the architecture. State-of-the-art
results have been obtained by designing large neural networks
with increased depth [11], width [46], and cardinality [45].
```

# Result from "python main.py"
```
[10, 11, 26, 30, 45, 46]
10
11
26
30
45
46
```
