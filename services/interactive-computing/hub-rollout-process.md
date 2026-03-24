# Hub Rollout Process

The hub rollout process is a collaboration between **Business Development (BD)** and **Product & Services (PS)**. BD bookends the process — identifying communities and tracking long-term value — while PS leads the technical engagement from sales engineering through validation.

```{mermaid}
flowchart
    subgraph BD["Business Development (BD)"]
        BD1["<b>1. Identify Communities</b><br/>BD identifies communities<br/>with hub needs"]
        BD2["<b>3. Close the Deal</b><br/>BD closes financial and<br/>contractual aspects"]
        BD3["<b>9. Track Value</b><br/>BD tracks value received<br/>by community"]
    end
    subgraph PS["Product & Services (PS)"]
        A["<b>2. Sales Engineering</b><br/>PS joins sales call as<br/>technical advisor"]
        C["<b>4. Needs Assessment</b><br/>PS confirms requirements<br/>with community"]
        D["<b>5. Solution Design</b><br/>PS writes GitHub issue with<br/>technical plan and subtasks"]
        E["<b>6. Execution</b><br/>PS executes on<br/>GitHub issues"]
        F{"<b>7. Validation</b><br/>Are the community's<br/>needs met?"}
        G["<b>8. Value Delivered</b><br/>Community is receiving<br/>value from 2i2c"]
    end
    BD1 --> A
    A --> BD2
    BD2 --> C
    C --> D
    D --> E
    E --> F
    F -- "No" --> C
    F -- "Yes" --> G
    G --> BD3
    style BD fill:#e8f0fe,stroke:#4a90d9,color:#2c5f8a
    style PS fill:#e8fee8,stroke:#50c878,color:#308050
    style BD1 fill:#3a7bc8,color:#fff,stroke:#2c5f8a
    style A fill:#4a90d9,color:#fff,stroke:#2c5f8a
    style BD2 fill:#5ba0e0,color:#fff,stroke:#3670a7
    style C fill:#6db3e8,color:#fff,stroke:#4080b5
    style D fill:#7fc4f0,color:#000,stroke:#4a90c3
    style E fill:#91d5f8,color:#000,stroke:#5aa0d1
    style F fill:#f0c040,color:#000,stroke:#c09830
    style G fill:#50c878,color:#fff,stroke:#308050
    style BD3 fill:#3a7bc8,color:#fff,stroke:#2c5f8a
```
