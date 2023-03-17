There is mechanism in kubernetes (network policies)to restict access in between pods. Disabled by default.
In secured projects it make sense to restrict traffic on between pods in case of breach on one of the pods, no access given on other resources.
For example we have 2 deployments cofigured which can't send traffic to each other (see files)
