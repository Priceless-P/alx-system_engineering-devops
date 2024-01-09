# 0x11-python-network_1

## Tasks

1. [What's my status?](0-hbtn_status.py)
    - Fetches https://alx-intranet.hbtn.io/status
    - Uses the package urllib
    - Displays the body of the response in a specific format

2. [Response header value](1-hbtn_header.py)
    - Takes a URL, sends a request, and displays the value of the X-Request-Id header
    - Uses urllib and sys packages

3. [POST an email](2-post_email.py)
    - Sends a POST request with an email parameter to a URL and displays the response body
    - Uses urllib and sys packages

4. [Error code](3-error_code.py)
    - Takes a URL, sends a request, and displays the body of the response
    - Handles urllib.error.HTTPError exceptions

5. [What's my status?](4-hbtn_status.py)
    - Fetches https://alx-intranet.hbtn.io/status
    - Uses the package requests

6. [Response header value](5-hbtn_header.py)
    - Takes a URL, sends a request, and displays the value of the X-Request-Id header
    - Uses the packages requests and sys

7. [POST an email](6-post_email.py)
    - Sends a POST request with an email parameter to a URL and displays the response body
    - Uses the packages requests and sys

8. [Error code](7-error_code.py)
    - Takes a URL, sends a request, and displays the body of the response
    - Displays an error code for HTTP status codes >= 400
    - Uses the packages requests and sys

9. [Search API](8-json_api.py)
    - Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter
    - Displays JSON-formatted response data

10. [My GitHub!](10-my_github.py)
    - Uses GitHub API with Basic Authentication to display your GitHub user ID
    - Uses requests and sys packages

11. [Time for an interview!](100-github_commits.py)
    - Lists 10 commits from the most recent to oldest of a specified repository by a given owner using the GitHub API
    - Takes repository name and owner name as arguments
    - Uses requests and sys packages
