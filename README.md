---
dataset_info:
  features:
  - name: name
    dtype: string
  - name: relation
    dtype: string
  - name: description
    dtype: string
  - name: email
    dtype: string
  splits:
  - name: train
    num_bytes: 820
    num_examples: 3
  download_size: 3321
  dataset_size: 820
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
