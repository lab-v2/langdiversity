import re

class NumberExtractor:

    @staticmethod
    def extract_decimals_from_text(text: str) -> str:
        preprocessed_text = NumberExtractor.__preprocess(text)
        extracted_strings = re.findall(r'-?\d+\.?\d*\/-?\d+\.?\d*|-?\d+\.?\d*', preprocessed_text)
        postprocessed_text = NumberExtractor.__postprocess(extracted_strings)
        return postprocessed_text
    
    def __preprocess(text: str) -> str: 
        text = NumberExtractor.__remove_commas_between_numbers(text)
        return text
    
    def __postprocess(text: str) -> str:
        text = [NumberExtractor.__remove_leading_zeros(extracted_string) for extracted_string in text]
        return text

    def __remove_leading_zeros(text: str) -> str:
        while len(text) > 1 and text.startswith('0') and text[1].isdigit(): text = text[1:]
        return text

    def __remove_commas_between_numbers(text: str) -> str: 
        """
        Removes commas that are directly in between numbers.\n
        For example,\n
        0, 0 --> 0, 0 will stay the same.\n
        0,0 --> 00 will have its comma removed.\n
        """
        
        return re.sub(r'(?<=\d)\,(?=\d)', '', text)
