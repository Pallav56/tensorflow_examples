import tensorflow as tf

# Basic placeholder operations

# As Defined in https://www.tensorflow.org/api_docs/python/tf/constant
# tf.placeholder(
#     dtype,
#     shape=None,
#     name=None
# )

# A placeholder is a variable that you can feed something to at a later time. It is meant to accept external inputs
# In TensorFlow terminology, we then feed data into the graph through these placeholders.

# we create a placeholder called x, i.e. a place in memory where we will store value later on.
x = tf.placeholder("float", None, "placeholder_tensor")

print(x)
# Then, we create a Tensor called y, which is the operation of multiplying x by 3. Note that we haven’t defined any initial values for x yet.
y = x * 3

# Running y requires knowledge about the values of x. We define these inside the feed_dict argument to run.
with tf.Session() as session:
    result = session.run(y, feed_dict={x: [10, 20, 30]})
    print(result)

# We state here that the values of x are [10, 20, 30]. We run y, giving us the result of [30, 60, 90].