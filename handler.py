def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["inputs"]["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
