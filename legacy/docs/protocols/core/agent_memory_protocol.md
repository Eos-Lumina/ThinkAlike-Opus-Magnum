---
title: "Agent Memory Protocol"
version: 3.0.0
status: Canonical
last_updated: 2025-07-08
authors:
  - "Eos Lumina ∴ (Collective Intelligence Meta-Agent)"
tags: [protocol, core, agent, memory, persistence, data_storage]
spec_for: [Backend Developers, Agent Developers]
harmonization_note: |
  Canonicalized from the v1.0 draft. This protocol establishes the standardized interface for agent memory persistence, ensuring data integrity, scalability, and a clear separation of concerns between agent logic and data storage. It formalizes the `BaseMemoryStore` abstract base class as the core contract for all memory implementations.
---

# Agent Memory Protocol

## 1. Vision & Purpose

This protocol defines the standardized interface for agent memory persistence within the ThinkAlike ecosystem. It establishes a formal contract for storing and retrieving agent-related data, focusing on conversation histories, agent states, and learned knowledge. The goal is to ensure data integrity, scalability, and a clear separation of concerns between agent logic and the underlying data storage mechanisms.

Adherence to this protocol allows for a pluggable memory architecture, where different storage backends (e.g., in-memory for testing, PostgreSQL for production, vector databases for semantic search) can be used without altering the agent's core logic.

## 2. Core Component: `BaseMemoryStore`

The `BaseMemoryStore` is an abstract base class (ABC) in Python that defines the contract for all memory store implementations. Agents will interact with a concrete implementation of this interface, which will be provided via dependency injection.

### 2.1. Intended Implementations

*   **`InMemoryMemoryStore`**: A transient, in-memory store suitable for testing, development, and single-session interactions where persistence is not required.
*   **`DatabaseMemoryStore`**: The primary production implementation, interacting with a relational database (e.g., PostgreSQL) via an ORM like SQLAlchemy. This store handles the serialization of complex objects (like `ConversationContext`) to appropriate database schemas.
*   **`VectorMemoryStore`**: A specialized implementation for storing and retrieving information based on semantic similarity, crucial for Retrieval Augmented Generation (RAG) and long-term associative memory.

## 3. `BaseMemoryStore` Interface Definition

The following methods MUST be implemented by any concrete memory store class that inherits from `BaseMemoryStore`.

```python
from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict

# Assuming the location of the ConversationContext object
from src.backend.app.utils.conversation_context import ConversationContext

class BaseMemoryStore(ABC):
    """
    Abstract base class defining the contract for agent memory stores.
    """

    @abstractmethod
    def store_conversation(self, session_id: str, user_id: str, conversation: ConversationContext) -> None:
        """
        Stores or updates an entire conversation history.
        The ConversationContext object will be serialized (e.g., to JSON) for storage.

        Args:
            session_id: The unique identifier for the conversation session.
            user_id: The identifier for the user associated with this conversation.
            conversation: The ConversationContext object to store.
        """
        pass

    @abstractmethod
    def retrieve_conversation(self, session_id: str) -> Optional[ConversationContext]:
        """
        Retrieves a conversation history by its session_id.
        The stored data will be deserialized back into a ConversationContext object.

        Args:
            session_id: The unique identifier for the conversation session.

        Returns:
            The ConversationContext object if found, otherwise None.
        """
        pass

    @abstractmethod
    def delete_conversation(self, session_id: str) -> bool:
        """
        Deletes a conversation history by its session_id.

        Args:
            session_id: The unique identifier for the conversation session.

        Returns:
            True if deletion was successful or item did not exist, False on error.
        """
        pass

    @abstractmethod
    def list_conversations_for_user(self, user_id: str, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """
        Lists conversation metadata (e.g., session_id, last_updated, summary) for a given user.
        This method should not return the full ConversationContext objects to avoid large data transfers.

        Args:
            user_id: The identifier for the user.
            limit: Maximum number of conversation metadata entries to return.
            offset: Offset for pagination.

        Returns:
            A list of dictionaries, where each dictionary contains metadata for a conversation.
        """
        pass

    @abstractmethod
    def store_agent_state(self, agent_id: str, key: str, value: Any) -> None:
        """
        Stores a specific key-value pair representing a piece of the agent's state.

        Args:
            agent_id: The identifier for the agent.
            key: The key for the state value.
            value: The state value to store (must be serializable).
        """
        pass

    @abstractmethod
    def retrieve_agent_state(self, agent_id: str, key: str) -> Optional[Any]:
        """
        Retrieves a specific piece of agent state by its key.

        Args:
            agent_id: The identifier for the agent.
            key: The key for the state value.

        Returns:
            The deserialized state value if found, otherwise None.
        """
        pass

```

## 4. Data Models & Serialization

-   **Conversation Context:** The `ConversationContext` object, which contains the full history of messages, metadata, and state for a session, will be serialized to a JSONB or equivalent format in the database.
-   **Agent State:** Generic agent state will be stored in a key-value format, likely in a table with columns for `agent_id`, `key`, and a `value` field (e.g., JSONB) to accommodate various data types.

## 5. Dependencies

-   **Protocol:** [`/protocols/data/data_traceability_protocol.md`](/protocols/data/data_traceability_protocol.md) - for ensuring memory operations are traceable.
-   **Architecture:** [`/architecture/data_architecture.md`](/architecture/data_architecture.md) - for the underlying database schema design.
