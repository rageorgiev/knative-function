def handler(context, inputs):
    greeting = "Hello, NEW NEW {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
