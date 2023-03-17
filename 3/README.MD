Blue/green - this is an rollout(upgrade) strategy whenever both, old and new set of software running in the cluster
simultaniously, but only one of them are active. 

Requires double resorces, but benefit is seemless upgrade for enduser.


On deployment level - two deployments running same time with two versions, service is using blue, and whenever green is ready - service got patches to use green.


On service level - ingress rules are configured to use one services, with blue software version, then ingress re-configured (patched) to use another services set with green software.


On ingress level - DNS is re-configured to use full set of software on ingress level from blue to green, in case of major re-work on applications structure required.
