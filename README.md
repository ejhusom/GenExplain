# GenExplain - Explanation Generation for the Intent-based Computing Continuum

The purpose of this tool is to use AI and XAI methods to describe and explain adaptions made in the edge-cloud continuum by the INTEND toolbox.

Project structure:

- `config`: Configuration files.
- `data`: Contains example files for running a simple demo.
- `src`: Source code.


## Usage

### Configuration

The configuration file is located in `config/config.ini`. The configuration file contains the following fields:

- `General`: General configuration.
    - `llm_service`: The language model service to use (ollama or openai).
    - `use_case_context`: The context of the use case.
    - `system_prompt`: The prompt for the system.
- `OpenAI`: OpenAI configuration.
    - `api_key`: Your OpenAI API key.
- `Ollama`: Ollama configuration.
    - `model`: The Ollama model to use.

Example:

```
[General]
llm_service = ollama
use_case_context = A company is using an edge-cloud computing infrastructure to process data from IoT devices spread across multiple locations. The primary intent is to optimize energy consumption across the infrastructure while ensuring data is processed efficiently and sustainably.
system_prompt =	You are a helpful assistant that describes and explains adaptations made in the edge-cloud computing infrastructure based on the available information.
	You will be provided with a list of intents, and a list of adaptations.
	List the intents, and list the adaptations under each of the intents.
	Under each adaptation, explain why the adaptation was made.

[OpenAI]
api_key = your_openai_api_key_here

[Ollama]
model = llama3
```

### Run

```
python3 src/GenExplain.py
```

## Concept overview: GenExplain Framework

Purpose: GenExplain is a Python framework designed to generate human-understandable explanations for a series of actions, events, or decisions. These actions could originate from AI agents, machine learning models, or even sequences in a complex system. The goal is to provide clear, context-aware explanations that help users understand why a specific sequence of events occurred.

Key Components:

- Event/Action Tracking:
    - The framework is built around monitoring and analyzing a sequence of actions or events. These can be:
        - AI Agent Actions: Decisions made by AI agents (e.g., in reinforcement learning environments).
        - Model Predictions: Outputs from a machine learning model (e.g., classification decisions, predictions).
        - System-Level Events: Events in a broader system (e.g., decision-making workflows, automated processes).
- Contextual Information Integration:
    - Explanations are more meaningful when they are contextualized. GenExplain incorporates additional data sources such as:
        - Knowledge Graphs: To provide relational context (e.g., how entities or concepts are related).
        - Textual Information: Supplementary descriptions, labels, or even structured documentation.
- Explanation Generation Modules:
    - The framework offers customizable explanation modules for different types of users or applications. Example modules include:
        - Sequential Event Reasoning: Tracing causality across actions.
        - Conceptual Explanations: Relating actions to high-level concepts using a knowledge graph.
        - Contrastive Explanations: Answering "why not" questions by comparing actual outcomes with alternative possibilities.
        - Model Explanation Techniques: Integrating techniques like SHAP, LIME, or counterfactual explanations to break down model decisions.
- User-Centric Explanation Templates:
    - Depending on the user’s needs, explanations can vary in depth and detail:
        - End-Users: High-level, non-technical explanations focusing on the "what" and "why".
        - Technical Users: More detailed, step-by-step reasoning with insights into model behavior or system logic.
        - Interactive Explanations: Allowing users to drill down or query specific steps in the explanation sequence.
- Pipeline Structure and Integration:
    - The framework follows a modular pipeline, where different components (event tracking, contextual information processing, explanation generation) can be swapped or extended. This makes it easy to integrate with existing AI/ML pipelines or enterprise systems.
- Extensibility and Customization:
    - API and Plugins: GenExplain provides a well-documented API for users to add custom event types, knowledge sources, and explanation templates.
    - Model-Agnostic Design: It can work across different types of models and systems, ensuring broad applicability.

Main goals and benefits:

- Trust and Transparency: By providing understandable and accurate explanations, GenExplain aims to improve trust in AI systems and enable better decision-making.
- User-Focused Explanations: Tailoring explanations based on the audience ensures that users get relevant insights at the right level of complexity.
- Contextual Understanding: By leveraging external knowledge sources, the framework can provide richer, more connected explanations that go beyond the event sequence itself.
- Scalable and Extensible Design: The modular pipeline and plugin system make GenExplain adaptable to different application domains and extendable for future improvements.

Example Use Cases

- AI Agents in Games: Explaining why an AI chose a specific strategy or move in a game.
- Decision Support Systems: Offering clear justifications for automated decisions in critical domains like healthcare or finance.
- Model Behavior Interpretation: Unpacking how and why a machine learning model arrived at a specific prediction or classification.

