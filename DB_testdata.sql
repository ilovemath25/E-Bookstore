INSERT INTO "Member" ("F_name", "L_name", "Password", "Gender", "Email", "Phone", "Birth", "Address", "Reg_date", "A_flag", "S_flag", "C_flag") 
VALUES 
('Harrison', 'Mckinney', 'Password123', 'Male',   'harrison4356@gmail.com',  '0912345678',  '1990-01-15', '123 Main St, Springfield',   '2024-10-13', TRUE,  FALSE, FALSE),
('Hudson',   'Smith',    'Passw0rd!',   'Male',   'hudson247@gmail.com',     '0923456789',  '1992-05-20', '456 Elm St, Springfield',    '2024-10-14', FALSE, TRUE,  FALSE),
('Chris',    'Lee',      'Qwerty123',   'Other',  'chris_lee@gmail.com',     '0993174028',  '1995-03-10', '789 Maple St, Springfield',  '2024-10-28', FALSE, FALSE, TRUE),
('Cecilia',   NULL,      '1234Pass',    'Female', 'cecilia643@gmail.com',    '0934567890',  '1988-07-08', '321 Oak St, Springfield',    '2024-10-28', FALSE, FALSE, TRUE),
('Landon',   'Burke',    'Bur2023!',    'Male',   'landon232@gmail.com',     '0945678901',  '1990-10-25', '654 Pine St, Springfield',   '2024-10-28', FALSE, FALSE, TRUE),
('妍婷',      '許',       'MyP@ssw0rd',  'Female', 'emily331565@gmail.com',   '0921390592',  '1999-02-14', '987 Birch St, Springfield',  '2024-10-28', FALSE, FALSE, TRUE),
('家文',      '何',       'T0mP@ss',     'Male',   'tom1121@gmail.com',       '0956789012',   NULL,        '159 Cedar St, Springfield',  '2024-10-28', FALSE, FALSE, TRUE),
('家綺',      '溫',       'Sophia!@#',   'Female', 'sophiamiller@gmail.com',  '0967890123',  '2000-09-12', '753 Cherry St, Springfield', '2024-10-14', FALSE, TRUE,  FALSE),
('Asher',    'Clark',    'AsherClark1', 'Other',  'alex_taylor@gmail.com',   '0978901234',  '1994-06-30', '852 Walnut St, Springfield', '2024-10-17', FALSE, TRUE,  FALSE),
('瑞池',      '宋',       'Liam2024',    'Male',   'liam_anderson@gmail.com', '0989012345',  '1985-11-05', '951 Willow St, Springfield', '2024-10-28', FALSE, FALSE, TRUE);


INSERT INTO "Credit_card" ("Number", "CMID", "Expiry_date", "CVV") 
VALUES 
('4532147890123456', 3,  '2025-12-31', '123'),
('5312345678901233', 4,  '2026-06-30', '456'), 
('3530111333300505', 5,  '2027-09-15', '789'),
('5412345678901232', 6,  '2026-03-20', '321'),
('5212345678901234', 10, '2028-11-10', '654');


INSERT INTO "Order" ("CMID", "SMID", "DID", "Credit_num", "Time", "Ship_address", "Ship_fee", "Status", "Pay_method", "Tot_price") 
VALUES
(10, 9, 3,   '5212345678901234', '2024-11-24 09:30:00', '987 Elm Dr, Brockway',           35, 'Shipping',   'Credit card', 1300),
(3, 2, 3,    '4532147890123456', '2024-11-29 10:30:00', '123 Maple St, Springfield',      50, 'Processing', 'Credit card', 1200),
(6, 2, 3,    '5412345678901232', '2024-11-26 13:10:00', '321 Birch Rd, Ogdenville',       40, 'Closed',     'Credit card', 1500),
(5, 9, NULL,  NULL,              '2024-11-27 18:20:00', '789 Pine Ln, Capital City',      20, 'Received',   'COD',         600),
(4, 8, 1,    '5312345678901233', '2024-11-28 15:45:00', '456 Oak Ave, Shelbyville',       30, 'Shipping',   'Credit card', 850),
(7, 8, 2,     NULL,              '2024-11-25 11:00:00', '654 Cedar Ct, North Haverbrook', 25, 'Processing', 'COD',         950),
(4, 8, NULL,  NULL,              '2024-11-22 16:40:00', '852 Cypress Way, Shelbyville',   20, 'Closed',     'COD',         700),
(3, 2, 1,    '4532147890123456', '2024-11-23 14:50:00', '741 Willow Blvd, Springfield',   50, 'Received',   'Credit card', 1700),
(5, 9, NULL, '3530111333300505', '2024-11-21 12:15:00', '963 Aspen Pkwy, Capital City',   45, 'Processing', 'Credit card', 1400),
(6, 2, 2,     NULL,              '2024-11-20 08:30:00', '357 Redwood Ln, Ogdenville',     30, 'Shipping',   'COD',         1100);


INSERT INTO "Discount" ("Disc_code", "Disc_value", "Disc_type", "Disc_name", "Policy_desc", "Max_usage")
VALUES
('SHIP500FREE', 0.00, 'Shipping', 'Free Shipping Over $500', 
 'Applies to orders with a total purchase amount greater than or equal to $500. Valid from 2024-11-01 to 2024-12-31.', 
 1000),
('SHIP10OFF', 0.90, 'Shipping', 'Flat 10% Off Shipping Fee', 
 'Valid for orders placed from 2024-11-15 to 2024-12-31. Shipping fee will be reduced by 10% for all eligible orders.', 
 500),
('FIRSTSHIP', 0.00, 'Shipping', 'Free Shipping for First Order', 
 'Applies to first-time customers on their first order, regardless of purchase amount. Valid from 2024-10-01 to 2024-12-31.', 
 2000),

('SEASON5OFF', 0.95, 'Seasonings', '5% Off Seasonings', 
 'A 5% discount applied to all seasoning products. Valid from 2024-11-01 to 2024-11-30.', 
 300),
('SPICEHOLIDAY', 0.90, 'Seasonings', 'Holiday Spice Discount', 
 'A 10% discount applied to purchases of seasoning products above $100. Valid from 2024-12-01 to 2024-12-25.', 
 150),
('HERBS2024', 0.92, 'Seasonings', 'Herbs Special Discount', 
 'A discount of 8% on World Literature during the promotional period. Valid from 2024-11-15 to 2024-12-15.', 
 100),

('EVENTBOGO', 0.00, 'Special Events', 'Buy 1 Get 1 Free', 
 'Buy 1 get 1 free on selected products. Valid from 2024-11-01 to 2024-11-30. Discount code applies to product IDs 101, 102, and 103.', 
 500),
('HOLIDAY50', 0.50, 'Special Events', '50% Off Holiday Special', 
 '50% discount on selected holiday products. Valid from 2024-12-01 to 2024-12-31. Applies to product IDs 201, 202, and 203.', 
 300),
('FLASHSALE10', 0.90, 'Special Events', '10% Off Flash Sale', 
 '10% off on flash sale items during the promotional period. Valid from 2024-11-20 to 2024-11-22. Discount code applies to product IDs 301, 302, and 303.', 
 200);


INSERT INTO "Shipping" ("DID", "Valid_from", "Valid_to")
VALUES
  (1, '2024-11-01', '2024-12-31'),  
  (2, '2024-11-15', '2024-12-31'),  
  (3, '2024-10-01', '2024-12-31');  


INSERT INTO "Seasoning" ("DID", "Valid_from", "Valid_to")
VALUES
  (4, '2024-11-01', '2024-11-30'),
  (5, '2024-12-01', '2024-12-25'),  
  (6, '2024-11-15', '2024-12-15');  


INSERT INTO "Special_event" ("DID", "Valid_from", "Valid_to")
VALUES
  (7, '2024-11-01', '2024-11-30'), 
  (8, '2024-12-01', '2024-12-31'),  
  (9, '2024-11-20', '2024-11-22');



