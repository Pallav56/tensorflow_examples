import tensorflow as tf

# Simple hello world using TensorFlow to check tensorflow is properly installed

hello = tf.constant('Hello, TensorFlow!')

sess = tf.Session()

print(sess.run(hello))

# Will cover all the above function in next scripts