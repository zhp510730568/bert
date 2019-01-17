from __future__ import print_function

import json

import nltk
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn
import csv
import tensorflow as tf


if __name__=='__main__':
  tf.nn.rnn_cell.BasicRNNCell