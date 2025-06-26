# Token-normalization-tool

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python tool for normalizing and cleaning text with multiple configurable options.

## Features

- Case normalization (lowercasing)
- Accent/diacritic removal
- Contraction expansion ("can't" → "cannot")
- Abbreviation expansion ("Dr." → "Doctor")
- Punctuation handling (optional removal)
- Number handling (optional removal)
- Whitespace normalization
- Special pattern replacement:
  - URLs → `<URL>`
  - Email addresses → `<EMAIL>`
  - Phone numbers → `<PHONE>`
- Interactive command-line interface
- Option to save normalized text to file

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/text-normalizer.git
cd text-normalizer
```

2. Ensure you have Python 3.7+ installed

3. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

## Usage

### Command-line Interactive Mode
```bash
python text_normalizer.py
```

Follow the on-screen prompts to:
1. Enter your text
2. Select normalization options
3. View the normalized output
4. Optionally save to a file

### Programmatic Usage
```python
from text_normalizer import TextNormalizer

normalizer = TextNormalizer()
normalized_text = normalizer.normalize(
    "Your text here...",
    lowercase=True,
    remove_accents=True,
    expand_contractions=True,
    # ... other options
)
```

## Configuration Options

All available normalization parameters with their defaults:

| Parameter               | Type    | Default    | Description |
|-------------------------|---------|------------|-------------|
| `lowercase`             | bool    | `True`     | Convert text to lowercase |
| `remove_accents`        | bool    | `True`     | Remove diacritics/accents |
| `expand_contractions`   | bool    | `True`     | Expand contractions |
| `expand_abbreviations`  | bool    | `False`    | Expand abbreviations |
| `remove_punctuation`    | bool    | `False`    | Remove punctuation |
| `remove_numbers`        | bool    | `False`    | Remove numbers |
| `remove_extra_whitespace` | bool | `True` | Normalize whitespace |
| `replace_urls`          | str/None | `"<URL>"` | Replace URLs with specified string |
| `replace_emails`        | str/None | `"<EMAIL>"` | Replace emails |
| `replace_phone_numbers` | str/None | `"<PHONE>"` | Replace phone numbers |

## Examples

### Input
```
Hello! This is a test with:
- Contractions: can't, won't
- Abbreviations: Dr. Smith, St. Louis
- Mixed case and accents: CAFÉ, naïve
- Numbers: 123-456-7890
- URL: https://example.com
```

### Output (with most options enabled)
```
hello this is a test with contractions cannot will not abbreviations doctor smith saint louis mixed case and accents cafe naive numbers <PHONE> url <URL>
```

## Adding Custom Mappings

You can extend the tool by modifying the `abbreviations` and `contractions` dictionaries in the `TextNormalizer` class initialization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
