def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)
    
    
    print("I am demo knative function")

    outputs = {
      "greeting": greeting
    }

    return outputs
