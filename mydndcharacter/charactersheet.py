class CharacterSheet:
    sheet_values = {
        'charsheet-save': '',
        'charsheet-load': '',

        'cname-val': '',

        'race-val': '',
        'class-val': '',
        'background-val': '',
        'alignment-val': '',

        'level-val': '',
        'exp-points-val': '',

        'hit-points-val': '',
        'max-hit-points-val': '',
        'temp-hit-points-val': '',
        'hit-dice-num-val': '',
        'hit-dice-die-val': '',

        'death-save-success-1-val': '',
        'death-save-success-2-val': '',
        'death-save-success-3-val': '',
        'death-save-failure-1-val': '',
        'death-save-failure-2-val': '',
        'death-save-failure-3-val': '',

        'speed-val': '',
        'initiative-val': '',
        'inspiration-val': '',
        'proficiency-bonus-val': '',
        'passive-perception-val': '',

        'strength-val': '',
        'strength-modifier-sign': '',
        'strength-modifier-val': '',
        'dexterity-val': '',
        'dexterity-modifier-sign': '',
        'dexterity-modifier-val': '',
        'constitution-val': '',
        'constitution-modifier-sign': '',
        'constitution-modifier-val': '',
        'intelligence-val': '',
        'intelligence-modifier-sign': '',
        'intelligence-modifier-val': '',
        'wisdom-val': '',
        'wisdom-modifier-sign': '',
        'wisdom-modifier-val': '',
        'charisma-val': '',
        'charisma-modifier-sign': '',
        'charisma-modifier-val': '',

        'strength-sav-throw-prof-val': '',
        'strength-sav-throw-num-val': '',
        'dexterity-sav-throw-prof-val': '',
        'dexterity-sav-throw-num-val': '',
        'constitution-sav-throw-prof-val': '',
        'constitution-sav-throw-num-val': '',
        'intelligence-sav-throw-prof-val': '',
        'intelligence-sav-throw-num-val': '',
        'wisdom-sav-throw-prof-val': '',
        'wisdom-sav-throw-num-val': '',
        'charisma-sav-throw-prof-val': '',
        'charisma-sav-throw-num-val': '',

        'acrobatics-prof-val': '',
        'acrobatics-num-val': '',
        'animal-handling-prof-val': '',
        'animal-handling-num-val': '',
        'arcana-prof-val': '',
        'arcana-num-val': '',
        'athletics-prof-val': '',
        'athletics-num-val': '',
        'deception-prof-val': '',
        'deception-num-val': '',
        'history-prof-val': '',
        'history-num-val': '',
        'insight-prof-val': '',
        'insight-num-val': '',
        'intimidation-prof-val': '',
        'intimidation-num-val': '',
        'investigation-prof-val': '',
        'investigation-num-val': '',
        'medicine-prof-val': '',
        'medicine-num-val': '',
        'nature-prof-val': '',
        'nature-num-val': '',
        'perception-prof-val': '',
        'perception-num-val': '',
        'performance-prof-val': '',
        'performance-num-val': '',
        'persuasion-prof-val': '',
        'persuasion-num-val': '',
        'religion-prof-val': '',
        'religion-num-val': '',
        'sleight-of-hand-prof-val': '',
        'sleight-of-hand-num-val': '',
        'stealth-prof-val': '',
        'stealth-num-val': '',
        'survival-prof-val': '',
        'survival-num-val': '',

        'notes-val': '',
    }
    def __init__(self, sheet_values):
        if not type(sheet_values == dict):
            raise ValueError('sheet_values must be a dict')
        if any([k not in self.sheet_values for k in sheet_values]):
            raise AssertionError('invalid keys in sheet_values')
        for k, v in sheet_values.items():
            self.sheet_values[k] = v

    def get(self, sheet_key):
        return self.sheet_values.get(sheet_key, '')

    def put(self, sheet_key, sheet_value):
        if sheet_key not in self.sheet_values:
            raise ValueError(f'{sheet_key} is not a valid sheet_key')
        self.sheet_values[sheet_key] = sheet_value
