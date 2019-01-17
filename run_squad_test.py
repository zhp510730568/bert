#! /usr/bin/python

import os, json

import tensorflow as tf

root_path = "./data"
filename="train-v2.0.json"

all_documents = [[]]
input_files = ["./sample_text.txt"]
for input_file in input_files:
    with tf.gfile.GFile(input_file, "r") as reader:
      while True:
        line = reader.readline()
        if not line:
          break
        line = line.strip()

        # Empty lines are used as document delimiters
        if not line:
          all_documents.append([])
        tokens = line.split()
        if tokens:
          all_documents[-1].append(tokens)
document = all_documents[0]
instances = []
current_chunk = []
current_length = 0
i = 0
while i < len(document):
    segment = document[i]
    current_chunk.append(segment)
    current_length += len(segment)
    i += 1

print([i for i in range(1)])