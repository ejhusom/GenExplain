#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GenExplain - Explainability module.

This module provides the functionality to generate explanations for system
adaptations based on log entries. It is intended to be used as a part of the
inGen system, which is a conversational AI system that can adapt to user
feedback.

"""
import configparser
import re


class ExplanationGenerator:
    """Generates explanations for system adaptations based on log entries.

    This class provides the functionality to generate explanations for system
    adaptations based on log entries. It is intended to be used as a part of the
    inGen system, which is a conversational AI system that can adapt to user
    feedback.

    Attributes:
        config (configparser.ConfigParser): The configuration settings for the
            explanation generator.
        log_file_path (str): The path to the log file containing system
            adaptations.
        system_prompt (str): The prompt to use for the language model.
        llm (langchain.llms.LanguageModel): The language model to use for
            generating explanations.

    """

    def __init__(self, config_path=config.CONFIG_FILE_PATH, log_file_path=self.LOG_FILE_PATH):
        """Initializes the ExplanationGenerator.

        Args:
            config_path (str): The path to the configuration file for the
                explanation generator.
            log_file_path (str): The path to the log file containing system
                adaptations.

        """

        self.config = self._read_config(config_path)
        self.log_file_path = log_file_path
        self.llm = self._initialize_llm()


    def _read_config(self, config_path):
        """
        Reads the configuration settings from the specified file.

        Args:
            config_path (str): The path to the configuration file.

        """
        config = configparser.ConfigParser()
        config.read(config_path)
        return config

    def _initialize_llm(self):
        """Initializes the language model to use for generating explanations.

        Returns:
            langchain.llms.LanguageModel: The language model to use for
                generating explanations.

        """
        llm_name = self.config.get('General', 'llm', fallback='openai')
        if llm_name == 'openai':
            api_key = self.config.get('OpenAI', 'api_key', fallback=None)
            if not api_key:
                raise ValueError("API key for OpenAI is required in config.ini")
            return OpenAI(api_key=api_key)
        elif llm_name == 'ollama':
            model = self.config.get('Ollama', 'model', fallback='llama3')
            return Ollama(model=model)
        else:
            raise ValueError(f"Unsupported LLM: {llm_name}")

    def generate_explanation(self, intent_id):
        """Generates an explanation for system adaptations using an LLM.

        Args:
            intent_id (str): The intent ID for which to generate an explanation.

        Returns:
            str: The generated explanation.

        """

        print("Reading log entries...")
        log_entries = self._read_log_entries()
        print("Generating prompt...")
        prompt = self._generate_explanation_prompt(log_entries)
        print("Creating chain...")
        chain = prompt | self.llm
        breakpoint()
        print("Evoking chain...")
        result = chain.invoke({})
        return result

    def _read_log_entries(self):
        """Reads the log entries from the log file.

        Returns:
            list: The log entries.

        """
        with open(self.log_file_path, "r") as file:
            log_entries = file.readlines()
        return log_entries

    def _generate_explanation_prompt(self, log_entries):
        """Generates a prompt for the language model to generate an explanation.

        Returns:
            str: The generated prompt.

        """
        use_case_context = self.config.get('General', 'use_case_context', fallback='')
        system_prompt = self.config.get('General', 'system_prompt', fallback='')
        full_system_prompt = f"{use_case_context}\n\n{system_prompt}"

        messages = [("system", full_system_prompt)]
        breakpoint()
        # messages += [("user", entry) for entry in log_entries]
        messages += [("user", entry) for entry in log_entries]

        prompt = ChatPromptTemplate.from_messages(messages)

        return prompt

if __name__ == '__main__':
    pass
