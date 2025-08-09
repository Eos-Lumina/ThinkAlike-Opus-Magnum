---
title: Agent Memory Protocol v1.0
version: 1.0.0
status: Draft
last_updated: 2025-06-21
maintained_by: Eos Lumina ∴ (Collective Intelligence Meta-Agent)
tags:
- agent_framework
---


# Agent Memory Protocol v1.0

**Version:** 1.0
**Date:** 2025-06-13
**Status:** Draft

## 1. Overview

This document defines the protocol for agent memory persistence within the ThinkAlike project. It establishes a standardized interface for storing and retrieving agent-related data, primarily focusing on conversation histories and agent-specific states. The goal is to ensure data integrity, scalability, and a clear separation of concerns between agent logic and data storage mechanisms.

The primary persistence mechanism will be a PostgreSQL database, ensuring transactional safety and relational query capabilities. Specialized stores (e.g., vector databases) may be integrated for specific functionalities like semantic search in the future.

## 2. Core Component: `BaseMemoryStore`

The `BaseMemoryStore` is an abstract base class that defines the contract for all memory store implementations. Agents will interact with a concrete implementation of this interface, which will be dependency-injected.

### 2.1. Intended Implementations

*   **`InMemoryMemoryStore`**: A transient, in-memory store suitable for testing, development, and single-session interactions. This will be a refactoring of the existing `memory_store.py`.
*   **`DatabaseMemoryStore`**: The primary production implementation, interacting with the PostgreSQL database via SQLAlchemy (or a similar ORM). This store will handle serialization of complex objects (like `ConversationContext`) to appropriate database schemas.

## 3. `BaseMemoryStore` Interface Definition

The following methods must be implemented by any concrete memory store.

```python
from abc import ABC, abstractmethod
from typing import Any, Optional, List, Dict
from src.agents.framework.utils.conversation_context import ConversationContext # Assuming path

class BaseMemoryStore(ABC):

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
        Does not return the full ConversationContext objects to avoid large data transfers.

        Args:
            user_id: The identifier for the user.
            limit: Maximum number of conversation metadata entries to return.
            offset: Offset for pagination.

        Returns:
            A list of dictionaries, where each dictionary contains metadata for a conversation.
        """
        pass

    @abstractmethod
    def store_agent_state(self, agent_id: str, owner_id: str, # e.g., user_id or system
                          key: str, state_data: Any) -> None:
        """
        Stores or updates a specific piece of state data for an agent, associated with an owner.
        The state_data will be serialized (e.g., to JSON or Pickle) for storage.

        Args:
            agent_id: The unique identifier for the agent (or agent_type if state is shared).
            owner_id: The identifier for the owner of this state (e.g., user_id, session_id, or a global system ID).
            key: The key for the specific piece of state data.
            state_data: The Python object to store.
        """
        pass

    @abstractmethod
    def retrieve_agent_state(self, agent_id: str, owner_id: str, key: str) -> Optional[Any]:
        """
        Retrieves a specific piece of state data for an agent, associated with an owner.
        The stored data will be deserialized back into a Python object.

        Args:
            agent_id: The unique identifier for the agent.
            owner_id: The identifier for the owner of this state.
            key: The key for the specific piece of state data.

        Returns:
            The Python object if found, otherwise None.
        """
        pass

    @abstractmethod
    def delete_agent_state(self, agent_id: str, owner_id: str, key: str) -> bool:
        """
        Deletes a specific piece of state data for an agent, associated with an owner.

        Args:
            agent_id: The unique identifier for the agent.
            owner_id: The identifier for the owner of this state.
            key: The key for the specific piece of state data.

        Returns:
            True if deletion was successful or item did not exist, False on error.
        """
        pass

    @abstractmethod
    def get_all_agent_states(self, agent_id: str, owner_id: str) -> Dict[str, Any]:
        """
        Retrieves all state data for a given agent and owner.

        Args:
            agent_id: The unique identifier for the agent.
            owner_id: The identifier for the owner of this state.

        Returns:
            A dictionary of all state key-value pairs for the agent and owner.
        """
        pass

```

## 4. Data Schemas for Persistence (PostgreSQL Focus)

This section outlines the conceptual schema for storing conversation histories in the PostgreSQL database. The `DatabaseMemoryStore` will manage the serialization and deserialization.

### 4.1. `conversation_history` Table

*   `session_id` (TEXT, PRIMARY KEY): Unique ID for the conversation session. This corresponds to `ConversationContext.session_id` and the `full_history_reference` in `AgentContextProtocol`.
*   `user_id` (TEXT, INDEXED): ID of the user involved in the conversation.
*   `created_at` (TIMESTAMP WITH TIME ZONE, DEFAULT CURRENT_TIMESTAMP): Timestamp of conversation creation.
*   `updated_at` (TIMESTAMP WITH TIME ZONE, DEFAULT CURRENT_TIMESTAMP): Timestamp of last update to the conversation.
*   `conversation_data` (JSONB): The serialized `ConversationContext` object. This will include:
    *   `session_id` (already key)
    *   `messages` (Array of Message objects, serialized)
        *   Each `Message` object: `role`, `content`, `timestamp`, `metadata`
    *   `metadata` (JSON object for overall conversation metadata)
    *   `agent_participants` (Array of agent identifiers involved)
*   `version` (TEXT): Version of the `ConversationContext` schema used for this record.

### 4.2. `agent_state_store` Table

*   `agent_id` (TEXT, INDEXED): Identifier of the agent.
*   `owner_id` (TEXT, INDEXED): Identifier of the entity that owns this state (e.g., `user_id`, `session_id`, or a global/system identifier).
*   `state_key` (TEXT, INDEXED): The specific key for the state data.
*   `state_value` (JSONB or BYTEA): The serialized state data. JSONB is preferred for structured data; BYTEA might be used for pickled objects if necessary, though JSONB is generally safer and more interoperable.
*   `created_at` (TIMESTAMP WITH TIME ZONE, DEFAULT CURRENT_TIMESTAMP)
*   `updated_at` (TIMESTAMP WITH TIME ZONE, DEFAULT CURRENT_TIMESTAMP)
*   PRIMARY KEY (`agent_id`, `owner_id`, `state_key`)

## 5. Relationship with `AgentContextProtocol`

The `full_history_reference` field within the `AgentContextProtocol`'s `InteractionHistory` object will directly correspond to the `session_id` used in the `BaseMemoryStore` methods and as the primary key in the `conversation_history` table.

When an agent requires access to the full conversation history, it will use this `session_id` to call `memory_store.retrieve_conversation(session_id)` on its injected memory store instance.

## 6. Future Considerations

*   **Vector Storage:** For semantic search capabilities on conversation histories or other agent memories, message embeddings will be generated and stored in a dedicated vector database or an indexed structure within/alongside PostgreSQL. This will be a separate concern, potentially managed by a specialized service that consumes data from the `conversation_history` table.
*   **Data Migration:** Tools like Alembic will be used to manage schema migrations for the `DatabaseMemoryStore` as the data structures evolve.
*   **Security & Access Control:** Implementation of the `DatabaseMemoryStore` must ensure appropriate security measures, including encryption at rest (if deemed necessary beyond database-level encryption) and robust access control to prevent unauthorized data access or modification.
*   **Configuration:** Database connection details and other store-specific configurations will be managed via environment variables or a centralized configuration service.
*   **Archival and Tiered Storage:** Strategies for archiving old conversations or moving them to cheaper storage tiers may be developed as the volume of data grows.

## 7. Evolution

This protocol will evolve as the needs of the ThinkAlike agent framework mature. Future versions may include additional methods, refined data schemas, or support for new types of memory stores.
