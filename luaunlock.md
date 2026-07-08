```mermaid
flowchart TD

A[Read Current Owner]

B{Owner == UUID?}

C[Delete Key]

D[Return Success]

E[Return Failure]

A --> B

B -- Yes --> C

C --> D

B -- No --> E
```