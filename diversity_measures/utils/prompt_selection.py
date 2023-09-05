class PromptSelection:
    def __init__(self):
        pass

    def find_extreme_scores(self, all_scores, measures, selection_method='max'):
        extreme_values = {}
        
        for measure in measures:
            scores_for_measure = [score[measure] for score in all_scores]
            
            if selection_method == 'max':
                extreme_values[measure] = max(scores_for_measure)
            elif selection_method == 'min':
                extreme_values[measure] = min(scores_for_measure)
        
        return extreme_values
