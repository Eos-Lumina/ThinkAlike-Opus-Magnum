---
title: Agent Memory Protocol
version: 1.0
status: Draft
summary: Defines the standardized interface for agent memory persistence, including conversation histories and agent-specific states.
tags:
  - agent
  - memory
  - protocol
  - data
---

## 1. Overview

This document defines the protocol for agent memory persistence within the ThinkAlike project. It establishes a standardized interface for storing and retrieving agent-related data, primarily focusing on conversation histories and agent-specific states. The goal is to ensure data integrity, scalability, and a clear separation of concerns between agent logic and data storage mechanisms.

The primary persistence mechanism will be a PostgreSQL database, ensuring transactional safety and relational query capabilities. Specialized stores (e.g., vector databases) may be integrated for specific functionalities like semantic search in the future.

## 2. Core Component: `BaseMemoryStore`

The `BaseMemoryStore` is an abstract base class that defines the contract for all memory store implementations. Agents will interact with a concrete implementation of this interface, which will be dependency-injected.

### 2.1. Intended Implementations

*   **`InMemoryMemoryStore`**: A transient, in-memory store suitable for testing, development, and single-session interactions.
*   **`DatabaseMemoryStore`**: The primary production implementation, interacting with the PostgreSQL database.

## 3. `BaseMemoryStore` Interface Definition

The following methods must be implemented by any concrete memory store.

```python
from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict

class BaseMemoryStore(ABC):

    @abstractmethod
    def store_conversation(self, session_id: str, user_id: str, conversation: dict) -> None:
        """Stores or updates an entire conversation history."""
        pass

    @abstractmethod
    def retrieve_conversation(self, session_id: str) -> Optional[dict]:
        """Retrieves a conversation history by its session_id."""
        pass

    @abstractmethod
    def delete_conversation(self, session_id: str) -> bool:
        """Deletes a conversation history by its session_id."""
        pass

    @abstractmethod
    def list_conversations_for_user(self, user_id: str, limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
        """Lists conversation metadata for a given user."""
        pass

    @abstractmethod
    def store_agent_state(self, agent_id: str, owner_id: str, key: str, state_data: Any) -> None:
        """Stores or updates a specific piece of state data for an agent."""
        pass

    @abstractmethod
    def retrieve_agent_state(self, agent_id: str, owner_id: str, key: str) -> Optional[Any]:
        """Retrieves a specific piece of state data for an agent."""
        pass

    @abstractmethod
    def delete_agent_state(self, agent_id: str, owner_id: str, key: str) -> bool:
        """Deletes a specific piece of state data for an agent."""
        pass

    @abstractmethod
    def get_all_agent_states(self, agent_id: str, owner_id: str) -> Dict[str, Any]:
        """Retrieves all state data for a given agent and owner."""
        pass
```

## 4. Data Schemas for Persistence

### 4.1. `conversation_history` Table

*   `session_id` (TEXT, PRIMARY KEY)
*   `user_id` (TEXT, INDEXED)
*   `created_at` (TIMESTAMP WITH TIME ZONE)
*   `updated_at` (TIMESTAMP WITH TIME ZONE)
*   `conversation_data` (JSONB)
*   `version` (TEXT)

### 4.2. `agent_state_store` Table

*   `agent_id` (TEXT, INDEXED)
*   `owner_id` (TEXT, INDEXED)
*   `state_key` (TEXT, INDEXED)
*   `state_value` (JSONB or BYTEA)
*   `created_at` (TIMESTAMP WITH TIME ZONE)
*   `updated_at` (TIMESTAMP WITH TIME ZONE)
*   PRIMARY KEY (`agent_id`, `owner_id`, `state_key`)

## 5. Relationship with Model Context Protocol

The `full_history_reference` field within the `InteractionHistory` object of the Model Context Protocol will directly correspond to the `session_id` used in this protocol.

## 6. Future Considerations

*   **Vector Storage:** For semantic search capabilities, message embeddings will be stored in a dedicated vector database.
*   **Data Migration:** Schema migrations will be managed using tools like Alembic.
*   **Security & Access Control:** Robust security measures will be implemented to protect user data.
*   **Archival:** Strategies for archiving old conversations will be developed.
