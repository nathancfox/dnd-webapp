DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS character;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE character (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INTEGER NOT NULL,
    name TEXT,
    race TEXT,
    class TEXT,
    background TEXT,
    alignment TEXT,
    experience INTEGER,
    level INTEGER,
    current_hp INTEGER,
    max_hp INTEGER,
    temp_hp INTEGER,
    armor_class INTEGER,
    speed INTEGER,
    initiative INTEGER,
    hit_die_type TEXT,
    hit_die_number INTEGER,
    notes TEXT,
    death_save_successes INTEGER,
    death_save_failures INTEGER,
    inspiration INTEGER,
    proficiency_bonus INTEGER,
    passive_perception INTEGER,
    proficiency TEXT,
    strength INTEGER,
    dexterity INTEGER,
    constitution INTEGER,
    intelligence INTEGER,
    wisdom INTEGER,
    charisma INTEGER,
    strength_saving_throw INTEGER,
    dexterity_saving_throw INTEGER,
    constitution_saving_throw INTEGER,
    intelligence_saving_throw INTEGER,
    wisdom_saving_throw INTEGER,
    charisma_saving_throw INTEGER,
    strength_saving_throw_prof INTEGER,
    dexterity_saving_throw_prof INTEGER,
    constitution_saving_throw_prof INTEGER,
    intelligence_saving_throw_prof INTEGER,
    wisdom_saving_throw_prof INTEGER,
    charisma_saving_throw_prof INTEGER,
    acrobatics INTEGER,
    animal_handling INTEGER,
    arcana INTEGER,
    athletics INTEGER,
    deception INTEGER,
    history INTEGER,
    insight INTEGER,
    intimidation INTEGER,
    investigation INTEGER,
    medicine INTEGER,
    nature INTEGER,
    perception INTEGER,
    performance INTEGER,
    persuasion INTEGER,
    religion INTEGER,
    sleight_of_hand INTEGER,
    stealth INTEGER,
    survival INTEGER,
    acrobatics_prof INTEGER,
    animal_handling_prof INTEGER,
    arcana_prof INTEGER,
    athletics_prof INTEGER,
    deception_prof INTEGER,
    history_prof INTEGER,
    insight_prof INTEGER,
    intimidation_prof INTEGER,
    investigation_prof INTEGER,
    medicine_prof INTEGER,
    nature_prof INTEGER,
    perception_prof INTEGER,
    performance_prof INTEGER,
    persuasion_prof INTEGER,
    religion_prof INTEGER,
    sleight_of_hand_prof INTEGER,
    stealth_prof INTEGER,
    survival_prof INTEGER,
    FOREIGN KEY (owner_id) REFERENCES user (id)
);