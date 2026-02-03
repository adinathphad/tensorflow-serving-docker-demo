import tensorflow as tf
import numpy as np

# Sample training data (y = 0.5x + 2)
x = np.array([-1, 0, 1, 2, 3, 4], dtype=float)
y = 0.5 * x + 2

# Simple linear model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mse')

# Train
model.fit(x, y, epochs=200, verbose=1)

# Export for TensorFlow Serving (IMPORTANT: export, not save)
model.export("half_plus_two/1")

print("✅ Model exported to half_plus_two/1")
