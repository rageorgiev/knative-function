def handler(context, inputs):
    greeting = "Hello,dsadsadas {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
