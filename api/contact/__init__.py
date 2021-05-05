import json

import azure.functions as func


def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:
    message_text = "{name}\n{email}\{message}"
    message.set(json.dumps({
        "content": [{
            "type": "text/plain",
            "value": message_text.format(**req.form)
        }]
    }))

    return func.HttpResponse(status_code=302, headers={
        "location": "/"
    })
