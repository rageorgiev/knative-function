def handler(context, inputs):
    greeting = "Hello, dasdsadad {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
