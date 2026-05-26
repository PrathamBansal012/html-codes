CREATE TABLE IF NOT EXISTS DEPARTMENT(
EMPLOYEE_ID TEXT,
NAME TEXT,
DEPARTMENT_ID TEXT,
MANGER_ID TEXT,
SALARY REAL
);
INSERT INTO DEPARTMENT (EMPLOYEE_ID, NAME, DEPARTMENT_ID, MANAGER_ID, SALARY)
VALUES
('100', 'STEVEN KING', '90', '100', 24000),
('101', 'NEENA KOCHHAR', '90', '100', 17000),
('102', 'LEX DEHAAN', '90', '102', 9000),
('103', 'BRUCE LEE', '60', '103', 4800),
('104', 'DIANA WILLS', '60', '103', 25000),
('105', 'VALLI PATOR', '50', '100', 4200),
('1973', 'LUV HAMI', '60', '102', 5000),
('106', 'DAVID AUSTIN', '90', '100', 6000);
SELECT department_id AS "Depatment_Code",
    COUNT(*) AS "NO.OF EMPLOYEES"
FROM DEPARTMENT
GROUP BY DEPARTMENT_ID
SELECT department_id AS "Department Code",
     COUNT(*) AS "No of Employees",
     SUM(SALARY)AS "TOTAL SALARY"
FROM DEPARTMENT
GROUP BY department_id;
SELECT department_id, SUM(salary)
FROM DEPARTMENT
GROUP BY department_id;
SELECT department_id AS "Department Code",
    COUNT(*) AS "No of Employees",
    SUM(salary) AS "Total Salary"
FROM DEPARTMENT
GROUP BY department_id;
SELECT department_id AS "Department Code",
    SUM(salary) AS "Total Salary"
FROM DEPARTMENT
WHERE MANAGER_ID = '103'
GROUP BY department_id;