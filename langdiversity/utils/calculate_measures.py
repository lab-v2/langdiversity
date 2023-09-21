from langdiversity.extras.spinner import loading_spinner

class DiversityCalculator:
    def __init__(self, measures=[]):
        self.measures = measures

    def calculate(self, values):
        results = {}
        for measure in self.measures:
            display_name = measure.__class__.__name__
            with loading_spinner(f"Calculating '{display_name}' for {len(values)} values..."):
                results[display_name] = measure.generate(values)
                
        return results
