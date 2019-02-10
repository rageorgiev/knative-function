def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)

    print("I am knative demo");
    
    outputs = {
      "greeting": greeting
    }

    return outputs
