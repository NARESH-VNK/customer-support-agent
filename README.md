
# AI Customer Support Agent

A production-grade customer support AI agent built with **LangChain**.

The goal of this project is to build a realistic customer support system that can answer general questions, retrieve information from company documentation, access customer-specific data through tools, and combine information from multiple sources when necessary.

> **Current scope:** LangChain only.
> **LangGraph is intentionally not used in this project.**

---

## 1. Project Goal

Build an AI customer support agent that can:

* Answer general product questions
* Search company documentation
* Retrieve customer-specific information
* Retrieve billing/payment information
* Retrieve support ticket information
* Combine information from multiple sources
* Provide grounded answers with supporting sources
* Maintain conversation context
* Handle tool/API failures gracefully

The final system should behave like a real customer support assistant rather than a simple chatbot or PDF question-answering application.

---

## 2. Example User Questions

The agent should eventually be able to handle questions such as:

### General Product Questions

> What features are included in the Pro plan?

### Billing Questions

> Why did my last payment fail?

### Refund Questions

> Can I get a refund for my latest payment?

### Subscription Questions

> Is my subscription currently active?

### Customer Account Questions

> What plan am I currently subscribed to?

### Technical Questions

> Why am I getting a 429 error when calling the API?

### Multi-source Questions

> My payment failed yesterday. Is my subscription still active, and can I get a refund?

For the last question, the agent may need to use multiple capabilities:

```text
Customer Information
        +
Billing Information
        +
Company Refund Policy
        ↓
    Final Answer
```

---

## 3. High-Level Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │ Support Agent   │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
            RAG       Customer Tool   Billing Tool
             │             │             │
             ▼             ▼             ▼
       Company Docs    Customer DB    Billing DB/API
                           │
                           ▼
                    Support Tool
                           │
                           ▼
                       Ticket DB
```

The agent should dynamically determine which capability or tool is required to answer the user's question.

---

## 4. Main Information Sources

### 4.1 Company Knowledge Base

The knowledge base will contain documents such as:

```text
Product Documentation
Billing Policy
Refund Policy
Subscription Policy
Account Security
API Documentation
API Rate Limits
Troubleshooting Guide
Cancellation Policy
```

These documents will be processed through a RAG pipeline.

```text
Documents
    ↓
Document Loader
    ↓
Text Splitting
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retriever
    ↓
Agent / RAG
```

---

### 4.2 Customer Information

Customer-specific information will be stored in a database.

Example information:

```text
customer_id
name
email
plan
subscription_status
created_at
```

The agent should access this information through a tool rather than directly accessing the database.

---

### 4.3 Billing Information

Billing data will contain information such as:

```text
transaction_id
customer_id
amount
status
date
failure_reason
```

The agent will use a billing tool to retrieve this information.

---

### 4.4 Support Tickets

Support tickets will contain:

```text
ticket_id
customer_id
subject
description
status
created_at
```

The agent should be able to retrieve relevant tickets through a tool.

---

## 5. Agent Capabilities

The final agent should be able to:

### Knowledge Retrieval

Search company documentation and answer questions using relevant information.

### Customer Lookup

Retrieve information about the authenticated customer.

### Billing Lookup

Retrieve recent transactions and payment status.

### Support Ticket Lookup

Retrieve existing support tickets and their status.

### Multi-tool Reasoning

Use multiple tools when a question requires information from different sources.

### Source Attribution

Clearly identify where important information came from.

For example:

```text
Your latest payment failed because the payment
provider reported insufficient funds.

Source:
Transaction TX1001
```

---

## 6. LangChain Concepts Used

This project is intended to exercise the major LangChain concepts already learned.

### Core

* Chat Models
* Messages
* Prompt Templates
* Runnables
* LCEL
* Chains
* Structured Output

### RAG

* Documents
* Document Loaders
* Text Splitters
* Embeddings
* Vector Stores
* Retrievers
* Retrieval Chains

### Agents

* Tools
* Tool Schemas
* Tool Calling
* Agents
* Agent Execution
* Multiple Tools

### Application Features

* Conversation History
* Streaming
* Callbacks
* Error Handling
* Retries
* Timeouts
* Logging

### Production

* Authentication
* Authorization
* Input Validation
* Prompt Injection Protection
* Customer Data Isolation
* Evaluation
* Observability
* Cost and Latency Tracking

---

## 7. Example Agent Flow

For a simple knowledge question:

```text
User
  │
  ▼
Agent
  │
  ▼
Knowledge Retrieval
  │
  ▼
Relevant Documents
  │
  ▼
LLM
  │
  ▼
Answer
```

For a customer-specific question:

```text
User
  │
  ▼
Agent
  │
  ▼
Customer Tool
  │
  ▼
Customer Database
  │
  ▼
Agent
  │
  ▼
Answer
```

For a complex question:

```text
User
  │
  ▼
Agent
  │
  ├──────────────► Customer Tool
  │
  ├──────────────► Billing Tool
  │
  └──────────────► Knowledge Retrieval
                         │
                         ▼
                    Company Policy
                         │
                         ▼
                    Final Answer
```

---

## 8. Production Requirements

The final application should not be treated as a simple demo.

It should include:

### Reliability

* Retry handling
* Timeout handling
* Tool failure handling
* LLM failure handling
* Invalid tool input handling
* Graceful error responses

### Security

* Authentication
* Authorization
* Customer data isolation
* Input validation
* Prompt injection defenses
* Secure secret management

### Observability

* Request logging
* Agent/tool execution logging
* Error logging
* Latency tracking
* Token/cost tracking

### Evaluation

* Test dataset
* RAG evaluation
* Retrieval evaluation
* Tool-selection evaluation
* Answer correctness evaluation
* Regression tests

---

## 9. Project Constraints

This project will intentionally use:

```text
LangChain
Python
LLM Provider
Vector Store
Database
REST/API layer
```

### Explicitly excluded for now

```text
LangGraph
Multi-agent orchestration
Complex graph workflows
Long-running autonomous workflows
```

LangGraph will be studied and used in a separate project after completing this one.

---

## 10. Success Criteria

The project will be considered complete when the agent can reliably:

* Answer company knowledge questions
* Retrieve relevant documentation
* Answer customer-specific questions
* Retrieve billing information
* Retrieve support ticket information
* Select appropriate tools
* Use multiple tools when necessary
* Maintain conversation context
* Stream responses
* Handle failures gracefully
* Protect customer-specific data
* Provide source/evidence information
* Pass an automated evaluation dataset
* Run as a real application rather than only a notebook

---

## 11. Development Approach

The project will be developed incrementally.

### Phase 1 — Requirements and Architecture

Define:

* Requirements
* Data models
* Tool contracts
* System architecture

### Phase 2 — Data Layer

Build:

* Customer data
* Billing data
* Ticket data
* Company knowledge documents

### Phase 3 — RAG

Build:

```text
Documents
    ↓
Loader
    ↓
Splitter
    ↓
Embeddings
    ↓
Vector Store
    ↓
Retriever
```

### Phase 4 — Tools

Build:

```text
Customer Tool
Billing Tool
Ticket Tool
Knowledge Tool
```

### Phase 5 — Agent

Connect the tools and RAG system to the LangChain agent.

### Phase 6 — Conversation & Streaming

Add:

* Conversation history
* Streaming
* Proper response handling

### Phase 7 — Production Hardening

Add:

* Security
* Error handling
* Retries
* Timeouts
* Logging
* Observability

### Phase 8 — Evaluation

Create a test dataset and measure:

* Retrieval quality
* Tool selection
* Answer correctness
* Groundedness
* Latency
* Cost

### Phase 9 — Deployment

Package and deploy the application as a real service.

---

## 12. Final Objective

The final objective is not simply to demonstrate that LangChain APIs can be used.

The objective is to demonstrate the ability to **design, build, evaluate, and productionize an AI application using LangChain**.

The project should answer the question:

> **"Can I use LangChain to build a reliable AI system that solves a realistic business problem?"**

---

## Status

**Current Step:** Project Definition

**Next Step:** Data Model and Tool Contract Design

**LangGraph:** Not used in this project
