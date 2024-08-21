# GenExplain - Explanation Generation for the Intent-based Computing Continuum

The purpose of this tool is to use AI and XAI methods to describe and explain adaptions made in the edge-cloud continuum by the INTEND toolbox.

Project structure:

- `config`: Configuration files.
- `data`: Contains example files for running a simple demo.
- `src`: Source code.


## How to use


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


### Run

```
python3 src/ExplanationGenerator.py
```

