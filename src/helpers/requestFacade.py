#
# File containing code to send HTTP requests
#
#

# Dependencies
import requests, bs4, json

# Function to send requests to given url
def send(url, headers={}):
    """Send requests to url. Retry upto 3 times upon failure.

    Keyword Arguments:
    url -- string
    """
    # Initialise response object
    response = {
        "status": 404,
        "payload": ""
    }
    # Check if url is not empty
    if len(url) > 0:
        # Initialise variable for number of retries
        maxRetries = 3
        # Initialise counter for retries
        retryCount = 0
        # Iterate till success or till max retires is reached
        while retryCount < maxRetries:
            # Update counter
            retryCount = retryCount + 1
            # Send request
            res = requests.get(url, headers=headers)
            # Check status code
            if res.status_code >= 400 and res.status_code <= 499:
                response["status"] = res.status_code
                response["payload"] = res.text
                break
            elif res.status_code >= 500 and res.status_code <= 599:
                response["status"] = res.status_code
                response["payload"] = res.text
            else:
                response["status"] = res.status_code
                response["payload"] = res.text
                break
    # Return response
    return response

# Function to parse JSON response
def parse_JSON(url, headers={}):
    """Calls send_request function with given url.
    Parse returned payload into JSON

    Keyword Arguments:
    url -- string
    """
    # Call send_request function
    res = send(url, headers)
    # Parse payload
    res["payload"] = json.loads(res["payload"])
    # Return response object
    return res

# Function to parse HTML response
def parse_HTML(url, headers={}):
    """Calls send_request function with given url.
    Parse returned payload into HTML

    Keyword Arguments:
    url -- string
    """
    # Call send_request function
    res = send(url, headers)
    # Parse payload
    res["payload"] = bs4.BeautifulSoup(res["payload"], features="html.parser")
    # Return response object
    return res

# Function to return dict of above functions
def requestFacade():
    return {
        "RAW": send,
        "JSON": parse_JSON,
        "HTML": parse_HTML
    }
