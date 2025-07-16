import math

def main():
  # e1_perceptron_simulation()
  # e2_sigmoid_neuron_simulation()
  e3_sigmoid_backward()

def e3_sigmoid_backward():
  """
  Forward propagation
  """
  # Inputs
  x1 = 1 # ¿Está lloviendo?
  x2 = 1 # ¿Dormí bien el día anterior?
  x3 = 0 # ¿Hay examen?

  # Weights
  w1 = -3
  w2 = 7
  w3 = 9

  # Bias
  b = 0

  # Linear function
  z = x1 * w1 + x2 * w2 + x3 * w3 + b

  # Activation function
  a = sigmoid(z)

  """
  Backpropagation
  """
  # Loss 
  prediction = a
  expected_result = 0

  L = (prediction - expected_result)**2


  print(f"z: {z}")
  print(f"predicción: {a}")
  print("Ve a la universidad" if a > 0.5 else "Quédate en casa")
  print("L: ", L)

def e2_sigmoid_neuron_simulation():
  """
  Forward propagation
  """

  # Inputs
  x1 = 1 # ¿Está lloviendo?
  x2 = 1 # ¿Dormí bien el día anterior?
  x3 = 0 # ¿Hay examen?

  # Weights
  w1 = -3
  w2 = 7
  w3 = 9

  # Bias
  b = 0

  # Linear function
  z = x1 * w1 + x2 * w2 + x3 * w3 + b

  # Activation function
  a = sigmoid(z)

  print(f"z: {z}")
  print(f"predicción: {a}")
  print("Ve a la universidad" if a > 0.5 else "Quédate en casa")

def sigmoid(z: int | float):
  return 1 / (1 + math.exp(-z))


def e1_perceptron_simulation():
  # Inputs
  x1 = 1 # ¿Está lloviendo?
  x2 = 1 # ¿Dormí bien el día anterior?
  x3 = 0 # ¿Hay examen?

  # Weights
  w1 = -3
  w2 = 7
  w3 = 9

  # 1 * -3 + 1 * 7 + 0 * 9 = -3 + 7 + 0 = 4
  z = x1 * w1 + x2 * w2 + x3 * w3

  # 0
  a = 1 if z > 5 else 0 # 1: University 0: Home

  # 0
  # "Quédate en casa"
  print(f"predicción: {a}")
  print("Ve a la universidad" if a == 1 else "Quédate en casa")

if __name__ == "__main__":
  main()
