DROP TABLE IF EXISTS pet_adoption_data;
CREATE TABLE IF NOT EXISTS pet_adoption_data (
    PetID INT,
    PetType VARCHAR(255),
    Breed VARCHAR(255),
    AgeMonths INT,
    Color VARCHAR(255),
    Size VARCHAR(255),
    WeightKg DOUBLE,
    Vaccinated INT,
    HealthCondition INT,
    TimeInShelterDays INT,
    AdoptionFee INT,
    PreviousOwner INT,
    AdoptionLikelihood INT
);