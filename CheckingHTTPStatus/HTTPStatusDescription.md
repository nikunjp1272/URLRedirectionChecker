# HTTP Status Codes with Descriptions and Resolutions

This file provides a comprehensive list of HTTP status codes, their descriptions, and general advice on how to resolve issues related to each code.

## 1xx Informational

### 100 Continue
**Description:** The server has received the request headers, and the client should proceed to send the request body.<br/>
**Resolution:** This is an intermediate response. The client should continue sending the request. If the server doesn't send a final response, there might be a network issue or a problem with the server's handling of the request body.

### 101 Switching Protocols
**Description:** The server is switching protocols as requested by the client's Upgrade header.<br/>
**Resolution:** This is usually handled automatically by the client and server. If issues arise, ensure both client and server are configured correctly for the agreed-upon protocol.

### 102 Processing (WebDAV)
**Description:** The server has received and is processing the request, but no response is yet available.<br/>
**Resolution:** This indicates the server is taking longer than usual. The client should wait for the final response. If it takes excessively long, there might be a server-side performance issue.

### 103 Early Hints
**Description:** The server is likely to send a final response with the headers included in this response.
**Resolution:** This is used for performance optimization. Client-side implementation handles this. Issues might arise if the final response doesn't align with the early hints.

## 2xx Success

### 200 OK
**Description:** The request has succeeded. The meaning of the success depends on the HTTP method.
**Resolution:** The request was successful. If you expected data in the response body, verify its integrity and content.

### 201 Created
**Description:** The request has been fulfilled and resulted in a new resource being created.
**Resolution:** The resource was created successfully. The response usually contains details about the new resource's location.

### 202 Accepted
**Description:** The request has been accepted for processing, but the processing has not been completed.
**Resolution:** The server has accepted the request and will process it later. The client might need to check the status of the processing through another mechanism provided by the server.

### 203 Non-Authoritative Information
**Description:** The server successfully processed the request but is returning information that may be from another source.
**Resolution:** The response is valid but might not be the most up-to-date or complete information. Consider if the freshness of the data is critical.

### 204 No Content
**Description:** The server successfully processed the request and is not returning any content.
**Resolution:** The action was successful, but there's no data to display. This is common for successful delete operations.

### 205 Reset Content
**Description:** The server successfully processed the request, asks the user agent to reset the document view, and is not returning any content.
**Resolution:** Similar to 204, but also instructs the client to reset the view. This is often used after a successful form submission.

### 206 Partial Content
**Description:** The server is delivering only a portion of the resource due to a range header sent by the client.
**Resolution:** The client requested a specific part of the resource, and the server fulfilled that request. Ensure your client-side logic correctly handles partial content.

### 207 Multi-Status (WebDAV)
**Description:** The response body contains XML that can contain a number of separate response codes, depending on how many sub-requests were made.
**Resolution:** Examine the XML body to understand the status of each sub-request.

### 208 Already Reported (WebDAV)
**Description:** The members of a binding have already been enumerated in a preceding part of the (multistatus) response, and are not being included again.
**Resolution:** This is an informational code within a WebDAV multi-status response. Client-side WebDAV implementations should handle this.

### 226 IM Used (HTTP Delta encoding)
**Description:** The server has fulfilled a GET request for the resource, and the response is a result of applying one or more instance-manipulations applied to the current instance.
**Resolution:** This relates to delta encoding for efficient updates. Ensure your client correctly handles delta responses.

## 3xx Redirection

### 300 Multiple Choices
**Description:** The user agent can choose one of the set of representations.
**Resolution:** The server is offering multiple options for the resource. The client should present these options to the user or choose one based on its capabilities.

### 301 Moved Permanently
**Description:** This and all future requests should be directed to the given URL.
**Resolution:** The requested resource has permanently moved. Update any bookmarks or links to the new URL provided in the `Location` header.

### 302 Found (Previously "Moved Temporarily")
**Description:** The requested resource resides temporarily under a different URI.
**Resolution:** The resource is temporarily located elsewhere. The client should use the URL in the `Location` header for this request, but future requests should still use the original URL.

### 303 See Other
**Description:** The response to the request can be found under another URI using a GET method.
**Resolution:** The requested action was processed, but the result is available at a different URL, which should be retrieved using a GET request.

### 304 Not Modified
**Description:** There is no need to retransmit the requested resource. The client can use its cached version.
**Resolution:** The client's cached version of the resource is still valid. The client should use its local cache.

### 305 Use Proxy (Deprecated)
**Description:** The requested resource is available only through a proxy, the address for which is provided in the response.
**Resolution:** This status code is deprecated due to security concerns regarding in-band configuration of a proxy. Clients should not rely on it.

### 307 Temporary Redirect
**Description:** The requested resource resides temporarily under a different URI, and the user agent MUST NOT change the request method if it performs an automatic redirection to that URI.
**Resolution:** Similar to 302, but explicitly forbids changing the request method (e.g., from POST to GET). The client should use the URL in the `Location` header for this request, and future requests should use the original URL.

### 308 Permanent Redirect
**Description:** The requested resource has been permanently moved to the URI given by the Location headers, and all future requests should be directed to this URI. This is similar to 301 but forbids changing the HTTP method.
**Resolution:** The resource has permanently moved. Update bookmarks and links to the new URL in the `Location` header.

## 4xx Client Errors

### 400 Bad Request
**Description:** The server cannot or will not process the request due to an apparent client error.
**Resolution:** There's an issue with the client's request. Check the request syntax, parameters, and headers for errors.

### 401 Unauthorized
**Description:** Authentication is required and has failed or has not yet been provided.
**Resolution:** The client needs to authenticate itself to access the resource. Provide the necessary credentials (e.g., using the `Authorization` header).

### 402 Payment Required
**Description:** This code is reserved for future use. The original intention was that this code might be used in digital payment systems.
**Resolution:** This status code is not commonly used. If encountered, it usually indicates that payment is required to access the resource.

### 403 Forbidden
**Description:** The request was valid, but the server is refusing action.
**Resolution:** The client does not have permission to access the resource, even with authentication. Ensure the client has the necessary privileges.

### 404 Not Found
**Description:** The requested resource could not be found on the server.
**Resolution:** The URL is incorrect or the resource no longer exists. Double-check the URL for typos. If the resource should exist, there might be a server-side issue or the resource has been moved or deleted.

### 405 Method Not Allowed
**Description:** The method specified in the request is not allowed for the resource identified by the Request-URI.
**Resolution:** The HTTP method (GET, POST, PUT, DELETE, etc.) used in the request is not supported for the requested URL. Check the server's documentation for allowed methods.

### 406 Not Acceptable
**Description:** The server cannot produce a response matching the list of acceptable values defined in the client's request headers.
**Resolution:** The server cannot provide content in a format acceptable to the client (based on headers like `Accept`). Check the server's supported formats or modify the client's `Accept` headers.

### 407 Proxy Authentication Required
**Description:** The client must first authenticate itself with the proxy.
**Resolution:** The client needs to authenticate with the proxy server before accessing the requested resource. Provide the necessary proxy credentials.

### 408 Request Timeout
**Description:** The server timed out waiting for the request.
**Resolution:** The client did not send a complete request within the server's timeout period. Try sending the request again, possibly with a shorter payload or from a network with better latency.

### 409 Conflict
**Description:** The request could not be completed due to a conflict with the current state of the resource.
**Resolution:** The request conflicts with the current state of the resource on the server. The response should include information about the conflict to help the client resolve it.

### 410 Gone
**Description:** The requested resource is no longer available at the server and no forwarding address is known.
**Resolution:** The resource has been permanently removed. The client should not expect it to be available again. Remove any links to this URL.

### 411 Length Required
**Description:** The server refuses to accept the request without a defined `Content-Length`.
**Resolution:** The server requires a `Content-Length` header in the request. Add this header specifying the size of the request body.

### 412 Precondition Failed
**Description:** One or more of the preconditions given in the request header fields evaluated to false when tested by the server.
**Resolution:** The server did not meet one or more conditions specified in the client's request headers (e.g., `If-Match`, `If-None-Match`). Modify the request headers to meet the server's requirements.

### 413 Payload Too Large (Previously Request Entity Too Large)
**Description:** The server is refusing to process a request because the request payload is larger than the server is willing or able to process.
**Resolution:** The request body is too large. Reduce the size of the data being sent.

### 414 URI Too Long (Previously Request-URI Too Long)
**Description:** The URI provided was too long for the server to process.
**Resolution:** The requested URL is too long. This can happen with excessive query parameters. Try shortening the URL.

### 415 Unsupported Media Type
**Description:** The server refuses to accept the request because the payload format is in an unsupported format.
**Resolution:** The `Content-Type` of the request body is not supported by the server. Check the server's documentation for supported media types and adjust the `Content-Type` header accordingly.

### 416 Range Not Satisfiable
**Description:** The client has asked for a portion of the file, but the server cannot supply that portion.
**Resolution:** The requested range in the `Range` header is invalid or outside the bounds of the resource. Request a valid range or the entire resource.

### 417 Expectation Failed
**Description:** The server cannot meet the requirements of the `Expect` request-header field.
**Resolution:** The server does not support the expectation specified in the `Expect` header. Remove or modify the `Expect` header.

### 418 I'm a teapot
**Description:** This server refuses to brew coffee because it is, permanently, a teapot. (Hyper Text Coffee Pot Control Protocol - HTCPCP/1.0)
**Resolution:** This is a humorous, rarely encountered code. The server is literally stating it's a teapot and cannot brew coffee.

### 421 Misdirected Request
**Description:** The request was directed at a server that is not able to produce a response.
**Resolution:** The client connected to the wrong server for the requested resource. Ensure the DNS resolution and server configuration are correct.

### 422 Unprocessable Entity (WebDAV)
**Description:** The server understands the content type of the request entity, and the syntax of the request entity is correct, but it was unable to process the contained instructions.
**Resolution:** The request body is semantically incorrect, even though the syntax is valid. Check the data being sent for logical errors.

### 423 Locked (WebDAV)
**Description:** The requested resource is currently locked.
**Resolution:** The resource is locked, preventing access. The client may need to wait for the lock to be released or provide appropriate lock tokens.

### 424 Failed Dependency (WebDAV)
**Description:** The request failed because it depended on another request and that request failed.
**Resolution:** This code is used in WebDAV when a command depends on the success of a previous command that failed. Examine the response body for details of the failed dependency.

### 426 Upgrade Required
**Description:** The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol.
**Resolution:** The server requires the client to use a different protocol (specified in the `Upgrade` header). Upgrade the client's protocol.

### 428 Precondition Required
**Description:** The origin server requires the request to be conditional.
**Resolution:** The server requires the request to include a precondition header (e.g., `If-Match`) to prevent lost updates.

### 429 Too Many Requests
**Description:** The user has sent too many requests in a given amount of time ("rate limiting").
**Resolution:** The client has been rate-limited. Wait for a specified period before sending more requests. Check the `Retry-After` header if provided.

### 431 Request Header Fields Too Large
**Description:** The server is unwilling to process the request because its header fields are too large.
**Resolution:** The size of the request headers exceeds the server's limit. Reduce the size of the headers.

### 451 Unavailable For Legal Reasons
**Description:** The server is denying access to the resource as a consequence of a legal demand.
**Resolution:** Access to the resource has been blocked due to legal reasons. There is likely nothing the client can do to resolve this.

## 5xx Server Errors

### 500 Internal Server Error
**Description:** The server has encountered a situation it doesn't know how to handle.
**Resolution:** This is a generic server error. The problem lies with the server. Report the issue to the website administrator. Retrying the request later might succeed.

### 501 Not Implemented
**Description:** The server does not support the functionality required to fulfill the request.
**Resolution:** The server does not support the requested feature or HTTP method. Check the server's documentation or try a different approach.

### 502 Bad Gateway
**Description:** The server, while acting as a gateway or proxy, received an invalid response from the upstream server it accessed in attempting to fulfill the request.
**Resolution:** The server acting as a gateway received an error from another server. The issue might be with the upstream server. Try again later. If the problem persists, contact the website administrator.

### 503 Service Unavailable
**Description:** The server is currently unable to handle the request due to a temporary overloading or maintenance of the server.
**Resolution:** The server is temporarily unavailable. Try again later. The server might provide a `Retry-After` header indicating how long to wait.

### 504 Gateway Timeout
**Description:** The server, while acting as a gateway or proxy, did not receive a timely response from the upstream server specified by the URI.
**Resolution:** The server acting as a gateway did not receive a response from another server within the timeout period. The issue might be with the upstream server or network connectivity. Try again later.

### 505 HTTP Version Not Supported
**Description:** The server does not support the HTTP protocol version used in the request.
**Resolution:** The HTTP version used by the client is not supported by the server. Try using a different HTTP version (e.g., HTTP/1.1 or HTTP/2).

### 506 Variant Also Negotiates
**Description:** The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper endpoint in the negotiation process.
**Resolution:** This is a server configuration issue that needs to be resolved by the server administrator.

### 507 Insufficient Storage (WebDAV)
**Description:** The server is unable to store the representation needed to complete the request.
**Resolution:** The server does not have enough storage space to fulfill the request. The server administrator needs to free up space.

### 508 Loop Detected (WebDAV)
**Description:** The server detected an infinite loop while processing the request with Depth: infinity.
**Resolution:** This indicates a problem with the server's WebDAV configuration, likely a circular reference. The server administrator needs to investigate.

### 510 Not Extended
**Description:** The server needs further extensions to the request to fulfill it.
**Resolution:** The client needs to send additional information or use extensions supported by the server.

### 511 Network Authentication Required
**Description:** The client needs to authenticate to gain network access.
**Resolution:** The client needs to authenticate with the network infrastructure (e.g., a captive portal) before accessing the requested resource.
