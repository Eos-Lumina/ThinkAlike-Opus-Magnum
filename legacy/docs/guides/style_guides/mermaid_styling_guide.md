---
title: Mermaid Diagram Styling Guide
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Project Team
tags: []
---

# Mermaid Diagram Styling Guide

To ensure visual consistency, all Mermaid diagrams used in ThinkAlike documentation should be styled to match the official color palette.

## Mermaid Theme Definition

You can define a theme at the top of your Markdown file or directly within the Mermaid code block using `%%{init: ...}%%`. Here is the recommended theme for ThinkAlike:

```mermaid
%%{
  init: {
    "theme": "base",
    "themeVariables": {
      "background": "#0a0a0a",
      "primaryColor": "#1a1a2e",
      "primaryTextColor": "#e8e8e8",
      "primaryBorderColor": "#ffb347",
      "lineColor": "#e8e8e8",
      "secondaryColor": "#1a1a2e",
      "tertiaryColor": "#1a1a2e",
      "nodeTextColor": "#e8e8e8",
      "mainBkg": "#1a1a2e",
      "actorBorder": "#ffb347",
      "actorTextColor": "#e8e8e8",
      "actorBkg": "#1a1a2e",
      "labelBoxBkgColor": "#1a1a2e",
      "labelTextColor": "#e8e8e8",
      "loopTextColor": "#e8e8e8",
      "noteBkgColor": "#1a1a2e",
      "noteTextColor": "#e8e8e8",
      "noteBorderColor": "#6a89cc",
      "activationBkgColor": "#f67280",
      "activationBorderColor": "#e8e8e8",
      "sequenceNumberColor": "#e8e8e8",
      "altBackground": "#1a1a2e"
    }
  }
}%%

graph TD
    A[Start] --> B{Is it styled?};
    B -->|Yes| C[Looks Great!];
    B -->|No| D[Apply Theme];
    C --> E[End];
    D --> C;

    style A fill:#1a1a2e,stroke:#ffb347,stroke-width:2px,color:#e8e8e8
    style B fill:#1a1a2e,stroke:#ffb347,stroke-width:2px,color:#e8e8e8
    style C fill:#1a1a2e,stroke:#6a89cc,stroke-width:2px,color:#e8e8e8
    style D fill:#1a1a2e,stroke:#f67280,stroke-width:2px,color:#e8e8e8
    style E fill:#1a1a2e,stroke:#ffb347,stroke-width:2px,color:#e8e8e8
```

## Usage

Copy the `%%{init: ...}%%` block into any Mermaid diagram to apply the theme. You can also define custom styles for specific nodes as shown in the example above to use accent colors.

Refer to the [Visual Identity Guide](../visual_identity_guide.md) for the full color palette.
