# Named Entity Recognition (NER) with spaCy
![Project Banner](https://github.com/LearnCode801/Name-Entity-Recognition-NER-Project/blob/main/Screenshot%202025-09-21%20140344.png)

[![Demo Video](https://img.shields.io/badge/Demo-Video-red.svg)](https://drive.google.com/file/d/1GLqMEue5x8sYKaOfK0uJeKGXmh73IWF7/view?usp=sharing)

A comprehensive Natural Language Processing (NLP) project implementing Named Entity Recognition using spaCy to extract and classify named entities from unstructured text documents.

## Problem Statement

Information extraction from unstructured text is a fundamental challenge in Natural Language Processing. Raw text documents contain valuable information in the form of entities like person names, organizations, locations, dates, monetary values, and other important categories. However, this information is embedded within natural language text, making it difficult to extract programmatically.

The key challenges addressed by this project include:

- **Information Overload**: Large volumes of unstructured text make manual information extraction impractical
- **Entity Ambiguity**: The same text can refer to different entity types depending on context
- **Scalability**: Need for automated systems to process thousands of documents efficiently
- **Accuracy**: Requirement for high precision in identifying and classifying entities
- **Customization**: Ability to recognize domain-specific entities not covered by pre-trained models

## Project Approach

### 1. Technology Selection
- **spaCy Framework**: Chosen for its fast statistical entity recognition system and pre-trained models
- **English Language Model**: Utilizes `en_core_web_sm` for robust English text processing
- **Visualization Tools**: Implements spaCy's displaCy for interactive entity visualization

### 2. Core Methodology
The project implements a multi-layered approach to NER:

1. **Pre-trained Model Usage**: Leverages spaCy's statistical models for standard entity recognition
2. **Custom Entity Addition**: Extends the model with user-defined entities using Span objects
3. **Phrase Matching**: Implements pattern matching for multi-token entity recognition
4. **Visualization Integration**: Provides interactive displays for better understanding and validation

### 3. Entity Classification System
Uses spaCy's comprehensive entity labeling system covering:
- Personal information (PERSON, NORP)
- Geographic data (GPE, LOC)
- Organizations (ORG)
- Temporal information (DATE, TIME)
- Numerical data (MONEY, PERCENT, QUANTITY, CARDINAL, ORDINAL)
- Cultural references (WORK_OF_ART, LANGUAGE, EVENT)

## Features

- **Comprehensive Entity Recognition**: Identifies 18+ different entity types
- **Real-time Processing**: Fast token-level entity identification
- **Custom Entity Support**: Add domain-specific entities to existing models
- **Interactive Visualization**: Browser-based entity highlighting with displaCy
- **Batch Processing**: Handle multiple documents efficiently
- **Token-level Analysis**: Access detailed entity boundaries and classifications
- **Pattern Matching**: Recognize multi-word entities and custom phrases
- **IOB Tagging**: Inside-Outside-Beginning scheme for precise entity boundaries

## Technical Specifications

- **Framework**: spaCy 3.x
- **Language Model**: en_core_web_sm (English small)
- **Entity Types**: 18 standard categories + custom entities
- **Processing Speed**: Optimized for real-time text analysis
- **Visualization**: displaCy integration for Jupyter notebooks
- **Token Processing**: Character-level and token-level indexing

## Requirements

```txt
spacy>=3.4.0
```

## Installation

### 1. Install spaCy
```bash
pip install spacy
```

### 2. Download Language Model
```bash
python -m spacy download en_core_web_sm
```

### 3. For Jupyter Notebook Visualization
```bash
pip install jupyter
```

## Quick Start

### Basic Entity Recognition

```python
import spacy

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Process text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Extract entities
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}")
```

**Output:**
```
Apple - ORG - Companies, agencies, institutions, etc.
U.K. - GPE - Countries, cities, states
$1 billion - MONEY - Monetary values, including unit
```

## Core Components

### 1. Entity Display Function

```python
def show_ents(doc):
    """Display basic entity information with positions and labels"""
    if doc.ents:
        for ent in doc.ents:
            print(f"{ent.text} - {ent.start_char} - {ent.end_char} - "
                  f"{ent.label_} - {spacy.explain(ent.label_)}")
    else:
        print('No named entities found.')
```

### 2. Entity Annotations Access

```python
# Document-level access
for ent in doc.ents:
    print(ent.text, ent.label_, ent.start, ent.end)

# Token-level access
for token in doc:
    if token.ent_type_:
        print(f"{token.text} - {token.ent_iob_} - {token.ent_type_}")
```

### 3. Custom Entity Addition

```python
from spacy.tokens import Span

# Create custom entity
doc = nlp("Tesla to build a U.K. factory for $6 million")
ORG = doc.vocab.strings['ORG']
new_ent = Span(doc, 0, 1, label=ORG)  # Tesla as organization
doc.ents = list(doc.ents) + [new_ent]
```

## Entity Categories

| Type | Description | Example |
|------|-------------|---------|
| **PERSON** | People, including fictional | *Fred Flintstone* |
| **NORP** | Nationalities, religious or political groups | *The Republican Party* |
| **FAC** | Buildings, airports, highways, bridges | *Logan International Airport* |
| **ORG** | Companies, agencies, institutions | *Microsoft, FBI, MIT* |
| **GPE** | Countries, cities, states | *France, Chicago, Idaho* |
| **LOC** | Non-GPE locations, mountain ranges, bodies of water | *Europe, Nile River* |
| **PRODUCT** | Objects, vehicles, foods (not services) | *Formula 1* |
| **EVENT** | Named hurricanes, battles, wars, sports events | *Olympic Games* |
| **WORK_OF_ART** | Titles of books, songs | *The Mona Lisa* |
| **LAW** | Named documents made into laws | *Roe v. Wade* |
| **LANGUAGE** | Any named language | *English* |
| **DATE** | Absolute or relative dates or periods | *20 July 1969* |
| **TIME** | Times smaller than a day | *Four hours* |
| **PERCENT** | Percentage, including "%" | *Eighty percent* |
| **MONEY** | Monetary values, including unit | *Twenty Cents* |
| **QUANTITY** | Measurements, weight or distance | *Several kilometers, 55kg* |
| **ORDINAL** | "first", "second", etc. | *9th, Ninth* |
| **CARDINAL** | Numerals that don't fall under another type | *2, Two, Fifty-two* |

## Advanced Features

### IOB Tagging Scheme

The project implements the Inside-Outside-Beginning tagging scheme:

- **B (Beginning)**: Token starts a new entity
- **I (Inside)**: Token continues an entity
- **O (Outside)**: Token is not part of any entity

```python
doc = nlp("San Francisco considers banning sidewalk delivery robots")

for token in doc:
    print(f"{token.text} - {token.ent_iob_} - {token.ent_type_}")
```

**Output:**
```
San - B - GPE
Francisco - I - GPE
considers - O - 
banning - O - 
```

### Pattern Matching for Multi-token Entities

```python
from spacy.matcher import PhraseMatcher

# Create matcher for custom phrases
matcher = PhraseMatcher(nlp.vocab)
phrase_list = ['vacuum cleaner', 'vacuum-cleaner']
phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('newproduct', None, *phrase_patterns)

# Apply to document
doc = nlp("Our company plans to introduce a new vacuum cleaner.")
matches = matcher(doc)

# Convert matches to named entities
PROD = doc.vocab.strings['PRODUCT']
new_ents = [Span(doc, match[1], match[2], label=PROD) for match in matches]
doc.ents = list(doc.ents) + new_ents
```

## Visualization

### Basic Entity Visualization

```python
from spacy import displacy

text = "When S. Thrun started working on self driving cars at Google in 2007"
doc = nlp(text)
displacy.render(doc, style="ent", jupyter=True)
```

### Custom Styling

```python
# Custom colors and options
colors = {
    'ORG': 'linear-gradient(90deg, #f2c707, #dc9ce7)',
    'PRODUCT': 'radial-gradient(90deg, #aa9cde, #dc9ce7)'
}

options = {
    'ents': ['ORG', 'PRODUCT'],
    'colors': colors
}

displacy.render(doc, style='ent', jupyter=True, options=options)
```

### Sentence-by-Sentence Visualization

```python
# Process each sentence separately
for sent in doc.sents:
    displacy.render(nlp(sent.text), style='ent', jupyter=True)
```









## Contact

For questions, suggestions, or collaboration opportunities, please create an issue in the GitHub repository.
