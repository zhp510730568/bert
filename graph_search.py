#! /bin/python
import tensorflow as tf

# 1-d convolutional layer
def conv1d(X, num_filters=8, filter_width=3, stride=1, padding='SAME'):
    # helper function for a 1D convolutional filter
    # initalize filter
    window_size = int(X.get_shape()[1])
    num_sensors = int(X.get_shape()[2])
    stddev = 1
    f = tf.Variable(tf.truncated_normal((filter_width,num_sensors,num_filters),stddev=.2),trainable=True,name='conv1d_filter')
    # initialize bias
    b = tf.Variable(0.0,name='conv1d_bias')
    conv = tf.nn.conv1d(value=X,filters=f,stride=stride,padding=padding,name='conv1d_op')
    return tf.add(conv,b)

# print out graph structure
def print_graph():
    # prints the graph operations out
    with tf.Session() as sess:
        op = sess.graph.get_operations()
    for o in op:
        print(o.outputs)

if __name__=="__main__":
  tf.squeeze
  print_graph()