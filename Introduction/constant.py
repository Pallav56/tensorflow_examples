import tensorflow as tf

# Basic constant operations

# As Defined in https://www.tensorflow.org/api_docs/python/tf/constant
# tf.constant(
#     value,
#     dtype=None,
#     shape=None,
#     name='Const',
#     verify_shape=False
# )

# For this example, we'll create a TensorFlow constant tensor with dimensions 2, 3, 4, which is populated with a scalar value 5.0, and a data type of float32.

# if we don't specify the shape, then tf.constant will use the dimensions of the value that we pass in to create the constant.

x = tf.constant(10.0, shape=[2, 3, 4], dtype="float32",name="constant_float_tensor")

print(x)

# Because we haven't run and evaluated the tensor in a TensorFlow session, we don't see any values.

# Now that we have created our TensorFlow tensors, it's time to run the computational graph.

# We launch the graph in a session.

sess = tf.Session()

# Then we initialize all the global variables and tensors in the graph.

sess.run(tf.global_variables_initializer())

print(sess.run(x))

