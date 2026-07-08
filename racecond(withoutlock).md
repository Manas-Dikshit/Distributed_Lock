```mermaid
sequenceDiagram

participant Worker A
participant Worker B
participant Database

Worker A->>Database: Read Stock = 1
Worker B->>Database: Read Stock = 1

Worker A->>Database: Buy Item
Worker B->>Database: Buy Item

Database-->>Worker A: Success
Database-->>Worker B: Success

Note over Database: Overselling occurs
```