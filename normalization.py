import re
import unicodedata
from typing import Optional

class TextNormalizer:
    def __init__(self):
        # Common abbreviations mapping
        self.abbreviations = {
            "mr.": "mister",
            "mrs.": "missus",
            "dr.": "doctor",
            "st.": "saint",
            "co.": "company",
            "jr.": "junior",
            "sr.": "senior",
            "etc.": "et cetera",
            "e.g.": "for example",
            "i.e.": "that is",
        }
        
        # Common contractions mapping
        self.contractions = {
            "won't": "will not",
            "can't": "cannot",
            "n't": " not",
            "'re": " are",
            "'s": " is",
            "'d": " would",
            "'ll": " will",
            "'ve": " have",
            "'m": " am",
        }

    def normalize(self, text: str, 
                 lowercase: bool = True,
                 remove_accents: bool = True,
                 expand_contractions: bool = True,
                 expand_abbreviations: bool = False,
                 remove_punctuation: bool = False,
                 remove_numbers: bool = False,
                 remove_extra_whitespace: bool = True,
                 replace_urls: Optional[str] = "<URL>",
                 replace_emails: Optional[str] = "<EMAIL>",
                 replace_phone_numbers: Optional[str] = "<PHONE>") -> str:
        """
        Normalize text with various options.
        """
        if not text:
            return text
            
        normalized = text
        
        # Replace URLs
        if replace_urls is not None:
            normalized = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 
                              replace_urls, normalized)
        
        # Replace email addresses
        if replace_emails is not None:
            normalized = re.sub(r'[\w\.-]+@[\w\.-]+', replace_emails, normalized)
            
        # Replace phone numbers
        if replace_phone_numbers is not None:
            normalized = re.sub(r'(\+?\d{1,3}[-\.\s]?)?\(?\d{3}\)?[-\.\s]?\d{3}[-\.\s]?\d{4}', 
                              replace_phone_numbers, normalized)
        
        # Remove accents
        if remove_accents:
            normalized = self._remove_accents(normalized)
            
        # Expand abbreviations
        if expand_abbreviations:
            normalized = self._expand_abbreviations(normalized)
            
        # Expand contractions
        if expand_contractions:
            normalized = self._expand_contractions(normalized)
            
        # Remove numbers
        if remove_numbers:
            normalized = re.sub(r'\d+', '', normalized)
            
        # Remove punctuation
        if remove_punctuation:
            normalized = re.sub(r'[^\w\s]', '', normalized)
            
        # Convert to lowercase
        if lowercase:
            normalized = normalized.lower()
            
        # Remove extra whitespace
        if remove_extra_whitespace:
            normalized = ' '.join(normalized.split())
            
        return normalized
    
    def _remove_accents(self, text: str) -> str:
        """Remove accent marks from characters."""
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text)
            if not unicodedata.combining(c)
        )
    
    def _expand_contractions(self, text: str) -> str:
        """Expand common contractions in English."""
        for contraction, expansion in self.contractions.items():
            text = text.replace(contraction, expansion)
        return text
    
    def _expand_abbreviations(self, text: str) -> str:
        """Expand common abbreviations."""
        words = text.split()
        for i, word in enumerate(words):
            lower_word = word.lower()
            if lower_word in self.abbreviations:
                words[i] = self.abbreviations[lower_word]
        return ' '.join(words)


def get_user_choice(prompt: str, default: bool) -> bool:
    """Get yes/no choice from user with a default value."""
    while True:
        choice = input(f"{prompt} [{'Y/n' if default else 'y/N'}] ").strip().lower()
        if not choice:
            return default
        if choice in ['y', 'yes']:
            return True
        if choice in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'")

def main():
    print("=== Text Normalization Tool ===")
    print("Enter your text to normalize (press Enter twice when done):")
    
    # Get multiline input from user
    lines = []
    while True:
        line = input()
        if line == "":
            if len(lines) > 0:  # Allow empty input if user wants
                break
        lines.append(line)
    user_text = "\n".join(lines)
    
    if not user_text.strip():
        print("No text entered. Exiting.")
        return
    
    print("\nChoose normalization options:")
    
    # Get user preferences
    lowercase = get_user_choice("Convert to lowercase?", True)
    remove_accents = get_user_choice("Remove accents?", True)
    expand_contractions = get_user_choice("Expand contractions?", True)
    expand_abbreviations = get_user_choice("Expand abbreviations?", False)
    remove_punctuation = get_user_choice("Remove punctuation?", False)
    remove_numbers = get_user_choice("Remove numbers?", False)
    remove_extra_whitespace = get_user_choice("Remove extra whitespace?", True)
    
    # Create normalizer and process text
    normalizer = TextNormalizer()
    normalized_text = normalizer.normalize(
        user_text,
        lowercase=lowercase,
        remove_accents=remove_accents,
        expand_contractions=expand_contractions,
        expand_abbreviations=expand_abbreviations,
        remove_punctuation=remove_punctuation,
        remove_numbers=remove_numbers,
        remove_extra_whitespace=remove_extra_whitespace
    )
    
    # Display results
    print("\n=== Original Text ===")
    print(user_text)
    print("\n=== Normalized Text ===")
    print(normalized_text)
    
    # Option to save to file
    if get_user_choice("\nSave normalized text to file?", False):
        filename = input("Enter filename (default: normalized.txt): ").strip()
        if not filename:
            filename = "normalized.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(normalized_text)
            print(f"Text saved to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()