
import requests
import json

def handler(context, inputs):
    greeting = "Hello, {0}!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }
    
    slackMsg = ':label: Tag VM action! tag: "' + greeting + '".'
    body = {
     "channel": "#rado-demo",
     "username": "ABX",
     "text": slackMsg,
     "icon_emoji": ":bell:"
    }
    # requests.post('https://hooks.slack.com/services/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', data=json.dumps(body), verify=False)

    return outputs

