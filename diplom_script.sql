-- Задание 1

SELECT 
  "Couriers"."login", 
  count("inDelivery") 
FROM "Couriers" 
  INNER JOIN "Orders" on "Couriers"."id" = "Orders"."courierId" 
WHERE "inDelivery" = true 
GROUP BY "Couriers"."login";

-- Задание 2

SELECT 
  "track",
  CASE 
    WHEN "finished" = true then 2
    WHEN "cancelled" = true then -1
    WHEN "inDelivery" = true then 1 
  ELSE 0
  END AS Status
FROM "Orders";