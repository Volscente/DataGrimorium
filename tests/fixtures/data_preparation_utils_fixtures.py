"""
The module includes Fixtures related to the module "data_preparation_utils".
"""

# Import Standard Libraries
import os
import pathlib
from typing import List
from dynaconf import Dynaconf
import pytest

# Import Package Modules
from data_grimorium.data_preparation.data_preparation_types import (
    SentenceTransformersConfig,
    EmbeddingsConfig,
    PCAConfig,
    CompressEmbeddingsConfig,
    EncodingTextConfig,
    DateExtractionConfig,
    NumericalFeaturesConfig,
)

# Retrieve the root path
root_path = pathlib.Path(os.getenv("DATA_GRIMORIUM_ROOT_PATH"))

# Read the configuration file
config = Dynaconf(
    settings_files=[root_path / "configuration" / "datagrimorium_settings.toml"],
    environments=True,
    env="pytest",
)


@pytest.fixture
def fixture_sentence_transformers_config(
    sentence_transformers_config: dict = config["data_preparation"]["sentence_transformers_config"],
) -> SentenceTransformersConfig:
    """
    Fixture for a SentenceTransformersConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.SentenceTransformersConfig class definition.

    Args:
        sentence_transformers_config (Dictionary): Configurations for a SentenceTransformersConfig object

    Returns:
        (SentenceTransformersConfig): SentenceTransformersConfig object with configurations for embedding generation
    """
    return SentenceTransformersConfig(**sentence_transformers_config)


@pytest.fixture
def fixture_embeddings_config(
    fixture_sentence_transformers_config: SentenceTransformersConfig,
    embeddings_config: dict = config["data_preparation"]["embeddings_config"],
) -> EmbeddingsConfig:
    """
    Fixture for an EmbeddingsConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.EmbeddingsConfig class definition.

    Args:
        fixture_sentence_transformers_config (SentenceTransformersConfig): Configurations for a SentenceTransformersConfig object
        embeddings_config (Dictionary): Configurations for an EmbeddingsConfig object

    Returns:
        (EmbeddingsConfig): EmbeddingsConfig object with configurations for embedding generation
    """
    return EmbeddingsConfig(
        method=embeddings_config["method"],
        embedding_model_config=fixture_sentence_transformers_config,
    )


@pytest.fixture
def fixture_pca_config(pca_config: dict = config["data_preparation"]["pca_config"]) -> PCAConfig:
    """
    Fixture for a PCAConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.PCAConfig class definition.

    Args:
        pca_config (Dictionary): PCA configurations

    Returns:
        (PCAConfig): PCAConfig object with configurations for PCA
    """
    return PCAConfig(**pca_config)


@pytest.fixture
def fixture_compress_embeddings_config(
    fixture_pca_config: PCAConfig,
    compress_embeddings_config: dict = config["data_preparation"]["compress_embeddings_config"],
) -> CompressEmbeddingsConfig:
    """
    Fixture for a CompressEmbeddingsConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.CompressEmbeddingsConfig class definition.

    Args:
        fixture_pca_config (PCAConfig): Configurations for a PCAConfig object
        compress_embeddings_config (Dictionary): Configurations for a CompressEmbeddingsConfig object

    Returns:
        (CompressEmbeddingsConfig): CompressEmbeddingsConfig object with configurations for compressing embeddings
    """
    return CompressEmbeddingsConfig(
        method=compress_embeddings_config["method"], compress_model_config=fixture_pca_config
    )


@pytest.fixture
def fixture_encode_text_config(
    fixture_embeddings_config: EmbeddingsConfig,
    fixture_compress_embeddings_config: CompressEmbeddingsConfig,
) -> EncodingTextConfig:
    """
    Fixture for an EncodeTextConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.EncodingTextConfig class definition.

    Args:
        fixture_embeddings_config (EmbeddingsConfig): Configuration for embedding generation
        fixture_compress_embeddings_config (CompressEmbeddingsConfig): Configuration for embedding compression

    Returns:
        (EncodingTextConfig): EncodeTextConfig object with configurations for encoding text
    """
    return EncodingTextConfig(
        embeddings_config=fixture_embeddings_config,
        compress_embeddings_config=fixture_compress_embeddings_config,
    )


@pytest.fixture
def fixture_sentences(file_path: str = "data/test/sentences.txt") -> List[str]:
    """
    Fixture for a list of sentences to encode.

    Args:
        file_path (str): Path to the file containing the sentences.

    Returns:
        (List[str]): List of sentences to encode
    """
    # Initialise sentences
    sentences = []

    # Update the file_path with the project root directory
    file_path = root_path / pathlib.Path(file_path)

    # Read the file
    with open(file_path, "r", encoding="utf-8") as file:
        sentences = [line.strip() for line in file.readlines()]

    return sentences


@pytest.fixture
def fixture_date_extraction_config(
    date_extraction_config: dict = config["data_preparation"]["date_extraction_config"],
) -> DateExtractionConfig:
    """
    Fixture for a DateExtractionConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.DateExtractionConfig class definition.

    Args:
        date_extraction_config (Dictionary): Configurations for a DateExtractionConfig object

    Returns:
        (DateExtractionConfig): Object with all configs for a DateExtractionConfig set to True
    """
    return DateExtractionConfig(**date_extraction_config)


@pytest.fixture
def fixture_numerical_features_config(
    numerical_features_config: dict = config["data_preparation"]["numerical_features_config"],
) -> NumericalFeaturesConfig:
    """
    Fixture for a NumericalFeaturesConfig object
    from src/data_grimorium/data_preparation/data_preparation_types.NumericalFeaturesConfig class definition.

    Args:
        numerical_features_config (Dictionary): Numerical feature transformation configurations

    Returns:
        (NumericalFeaturesConfig): Object including numerical feature transformation configurations
    """
    return NumericalFeaturesConfig(**numerical_features_config)
