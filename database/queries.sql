-- View all records
SELECT * FROM cleaned_patients LIMIT 10;

-- Count by test result
SELECT test_results, COUNT(*) AS count
FROM cleaned_patients
GROUP BY test_results;

-- Check for duplicates
SELECT age, gender, billing_amount, COUNT(*)
FROM cleaned_patients
GROUP BY age, gender, billing_amount
HAVING COUNT(*) > 1;