# 🌊 DDoS-Layer4
 Layer 4 UDP DDoS Script written in python with the help of multi-threading & sockets.

 ```Don't use for malicious reasons. You can use it for testing, trolling your friends or learning from the code.```

  A distributed denial-of-service (DDoS) attack is a malicious attempt to disrupt the normal traffic of a targeted server, service or network by overwhelming the target or its surrounding infrastructure with a flood of Internet traffic. DDoS attacks achieve effectiveness by utilizing multiple compromised computer systems as sources of attack traffic. Exploited machines can include computers and other networked resources such as IoT devices. From a high level, a DDoS attack is like an unexpected traffic jam clogging up the highway, preventing regular traffic from arriving at its destination.

  ### Layer 4
  <img align="left" alt="PNG" src="https://raw.githubusercontent.com/xShamir/DDoS-Layer4/master/example.png" width="380" height="230" />
  Layer 4 DDoS attacks are often referred to as SYN flood. It works at the TCP (Transport Protocol) layer. A TCP connection is established in what is known as a 3-way handshake. The client sends a SYN packet, the server responds with a SYN-ACK, and the client responds to that with an ACK. after the "three-way-handshake" is complete, the TCP connection is considered established.<br />

  Usage: ```python DDoS.py {ip} {port} {method}``` <br />
  Example: ```python DDoS.py 127.0.0.1 8080 UDP-Mix```<br />

12
