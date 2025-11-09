"""
LLM utility functions for DeepCode project.

This module provides common LLM-related utilities to avoid circular imports
and reduce code duplication across the project.
"""

import os
import yaml
from typing import Any, Type, Dict, Tuple

# Import LLM classes
from mcp_agent.workflows.llm.augmented_llm_anthropic import AnthropicAugmentedLLM
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM


def get_preferred_llm_class(config_path: str = "mcp_agent.secrets.yaml") -> Type[Any]:
    """
    Automatically select the LLM class based on API key availability in configuration.

    Reads from YAML config file and returns AnthropicAugmentedLLM if anthropic.api_key
    is available, otherwise returns OpenAIAugmentedLLM.

    Args:
        config_path: Path to the YAML configuration file

    Returns:
        class: The preferred LLM class
    """
    try:
        # Try to read the configuration file
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            # Check for anthropic API key in config
            anthropic_config = config.get("anthropic", {})
            anthropic_key = anthropic_config.get("api_key", "")

            if anthropic_key and anthropic_key.strip() and not anthropic_key == "":
                # print("🤖 Using AnthropicAugmentedLLM (Anthropic API key found in config)")
                return AnthropicAugmentedLLM
            else:
                # print("🤖 Using OpenAIAugmentedLLM (Anthropic API key not configured)")
                return OpenAIAugmentedLLM
        else:
            print(f"🤖 Config file {config_path} not found, using OpenAIAugmentedLLM")
            return OpenAIAugmentedLLM

    except Exception as e:
        print(f"🤖 Error reading config file {config_path}: {e}")
        print("🤖 Falling back to OpenAIAugmentedLLM")
        return OpenAIAugmentedLLM


def get_default_models(config_path: str = "mcp_agent.config.yaml"):
    """
    Get default models from configuration file.

    Args:
        config_path: Path to the configuration file

    Returns:
        dict: Dictionary with 'anthropic' and 'openai' default models
    """
    try:
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            # Handle null values in config sections
            anthropic_config = config.get("anthropic") or {}
            openai_config = config.get("openai") or {}

            anthropic_model = anthropic_config.get(
                "default_model", "claude-sonnet-4-20250514"
            )
            openai_model = openai_config.get("default_model", "o3-mini")

            return {"anthropic": anthropic_model, "openai": openai_model}
        else:
            print(f"Config file {config_path} not found, using default models")
            return {"anthropic": "claude-sonnet-4-20250514", "openai": "o3-mini"}

    except Exception as e:
        print(f"❌Error reading config file {config_path}: {e}")
        return {"anthropic": "claude-sonnet-4-20250514", "openai": "o3-mini"}


def get_document_segmentation_config(
    config_path: str = "mcp_agent.config.yaml",
) -> Dict[str, Any]:
    """
    Get document segmentation configuration from config file.

    Args:
        config_path: Path to the main configuration file

    Returns:
        Dict containing segmentation configuration with default values
    """
    try:
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            # Get document segmentation config with defaults
            seg_config = config.get("document_segmentation", {})
            return {
                "enabled": seg_config.get("enabled", True),
                "size_threshold_chars": seg_config.get("size_threshold_chars", 50000),
            }
        else:
            print(
                f"📄 Config file {config_path} not found, using default segmentation settings"
            )
            return {"enabled": True, "size_threshold_chars": 50000}

    except Exception as e:
        print(f"📄 Error reading segmentation config from {config_path}: {e}")
        print("📄 Using default segmentation settings")
        return {"enabled": True, "size_threshold_chars": 50000}


def should_use_document_segmentation(
    document_content: str, config_path: str = "mcp_agent.config.yaml"
) -> Tuple[bool, str]:
    """
    Determine whether to use document segmentation based on configuration and document size.

    Args:
        document_content: The content of the document to analyze
        config_path: Path to the configuration file

    Returns:
        Tuple of (should_segment, reason) where:
        - should_segment: Boolean indicating whether to use segmentation
        - reason: String explaining the decision
    """
    seg_config = get_document_segmentation_config(config_path)

    if not seg_config["enabled"]:
        return False, "Document segmentation disabled in configuration"

    doc_size = len(document_content)
    threshold = seg_config["size_threshold_chars"]

    if doc_size > threshold:
        return (
            True,
            f"Document size ({doc_size:,} chars) exceeds threshold ({threshold:,} chars)",
        )
    else:
        return (
            False,
            f"Document size ({doc_size:,} chars) below threshold ({threshold:,} chars)",
        )


def get_adaptive_agent_config(
    use_segmentation: bool, search_server_names: list = None
) -> Dict[str, list]:
    """
    Get adaptive agent configuration based on whether to use document segmentation.

    Args:
        use_segmentation: Whether to include document-segmentation server
        search_server_names: Base search server names (from get_search_server_names)

    Returns:
        Dict containing server configurations for different agents
    """
    if search_server_names is None:
        search_server_names = []

    # Base configuration
    config = {
        "concept_analysis": [],
        "algorithm_analysis": search_server_names.copy(),
        "code_planner": search_server_names.copy(),
    }

    # Add document-segmentation server if needed
    if use_segmentation:
        config["concept_analysis"] = ["document-segmentation"]
        if "document-segmentation" not in config["algorithm_analysis"]:
            config["algorithm_analysis"].append("document-segmentation")
        if "document-segmentation" not in config["code_planner"]:
            config["code_planner"].append("document-segmentation")
    else:
        config["concept_analysis"] = ["filesystem"]
        if "filesystem" not in config["algorithm_analysis"]:
            config["algorithm_analysis"].append("filesystem")
        if "filesystem" not in config["code_planner"]:
            config["code_planner"].append("filesystem")

    return config


def get_adaptive_prompts(use_segmentation: bool) -> Dict[str, str]:
    """
    Get appropriate prompt versions based on segmentation usage.

    Args:
        use_segmentation: Whether to use segmented reading prompts

    Returns:
        Dict containing prompt configurations
    """
    # Import here to avoid circular imports
    from prompts.code_prompts import (
        PAPER_CONCEPT_ANALYSIS_PROMPT,
        PAPER_ALGORITHM_ANALYSIS_PROMPT,
        CODE_PLANNING_PROMPT,
        PAPER_CONCEPT_ANALYSIS_PROMPT_TRADITIONAL,
        PAPER_ALGORITHM_ANALYSIS_PROMPT_TRADITIONAL,
        CODE_PLANNING_PROMPT_TRADITIONAL,
    )

    if use_segmentation:
        return {
            "concept_analysis": PAPER_CONCEPT_ANALYSIS_PROMPT,
            "algorithm_analysis": PAPER_ALGORITHM_ANALYSIS_PROMPT,
            "code_planning": CODE_PLANNING_PROMPT,
        }
    else:
        return {
            "concept_analysis": PAPER_CONCEPT_ANALYSIS_PROMPT_TRADITIONAL,
            "algorithm_analysis": PAPER_ALGORITHM_ANALYSIS_PROMPT_TRADITIONAL,
            "code_planning": CODE_PLANNING_PROMPT_TRADITIONAL,
        }
