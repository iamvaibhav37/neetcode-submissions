-- Write your query below
SELECT name
FROm customers 
WHERE id NOT IN(SELECT customer_id FROm orders);