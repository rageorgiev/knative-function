def handler(context, inputs):
    greeting = "Hello, AHHAHAH {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
