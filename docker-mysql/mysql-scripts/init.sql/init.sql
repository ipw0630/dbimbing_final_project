CREATE DATABASE IF NOT EXISTS pet_adoption_db;

USE pet_adoption_db;

CREATE TABLE IF NOT EXISTS pet_adoption (
    PetID INT,
    PetType VARCHAR(50),
    Breed VARCHAR(100),
    AgeMonths INT,
    Color VARCHAR(50),
    Size VARCHAR(50),
    WeightKg DOUBLE,
    Vaccinated INT,
    HealthCondition INT,
    TimeInShelterDays INT,
    AdoptionFee INT,
    PreviousOwner INT,
    AdoptionLikelihood INT,
    AgeCategory VARCHAR(20)
);
