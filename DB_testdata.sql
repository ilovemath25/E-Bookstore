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
(10, 9, 3,   '5212345678901234', '2024-11-24 09:30:00', '987 Elm Dr, Brockway',           35, 'Shipping',   'Credit card', 2100),
(3, 2, 3,    '4532147890123456', '2024-11-29 10:30:00', '123 Maple St, Springfield',      50, 'Processing', 'Credit card', 3450),
(6, 2, 3,    '5412345678901232', '2024-11-26 13:10:00', '321 Birch Rd, Ogdenville',       40, 'Closed',     'Credit card', 1210),
(5, 9, NULL,  NULL,              '2024-11-27 18:20:00', '789 Pine Ln, Capital City',      20, 'Received',   'COD',         5520),
(4, 8, 1,    '5312345678901233', '2024-11-28 15:45:00', '456 Oak Ave, Shelbyville',       30, 'Shipping',   'Credit card', 800),
(7, 8, 2,     NULL,              '2024-11-25 11:00:00', '654 Cedar Ct, North Haverbrook', 25, 'Processing', 'COD',         3700),
(4, 8, NULL,  NULL,              '2024-11-22 16:40:00', '852 Cypress Way, Shelbyville',   20, 'Closed',     'COD',         4190),
(3, 2, 1,    '4532147890123456', '2024-11-23 14:50:00', '741 Willow Blvd, Springfield',   50, 'Received',   'Credit card', 1600),
(5, 9, NULL, '3530111333300505', '2024-11-21 12:15:00', '963 Aspen Pkwy, Capital City',   45, 'Processing', 'Credit card', 5750),
(6, 2, 2,     NULL,              '2024-11-20 08:30:00', '357 Redwood Ln, Ogdenville',     30, 'Shipping',   'COD',         7161);


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


INSERT INTO "product" ("SMID", "SpEvent_ID", "Name", "Desc", "Author", "Price", "Stock_quantity", "Category", "Product_pict", "Sale_count") 
VALUES
  (2, 9,    "Harry Potter and the Sorcerer's Stone", "The beginning of the magical journey of Harry Potter, a young wizard discovering his powers and fighting the dark forces at Hogwarts.","J.K. Rowling",1500,10,NULL,"ebookstore_flask/static/image/books/PID_book1.png", 2),
  (2, NULL, "The Lord of the Rings: The Fellowship of the Ring", "A fantasy epic about a young hobbit, Frodo, tasked with destroying a powerful ring to save Middle-earth.", "J.R.R. Tolkien",1200, 20,NULL,"ebookstore_flask/static/image/books/PID_book2.png", 1),
  (9, NULL, "The Da Vinci Code" ,"A thrilling mystery that blends art, religion, and history in a race to uncover hidden secrets of the Church.", NULL , 800, 4,NULL,"bookstore_flask/static/image/books/PID_book3.png", 1),
  (8, NULL, "The Great Gatsby", "A classic exploration of the American Dream, wealth, and unrequited love during the Roaring Twenties.", "F. Scott Fitzgerald", 900, 5,NULL,"ebookstore_flask/static/image/books/PID_book4.png", 4),
  (8, NULL, "Pride and Prejudice","A beloved romance set in 19th-century England, highlighting societal expectations and enduring love.", "Jane Austen", 450, 30,NULL,"ebookstore_flask/static/image/books/PID_book5.png", 1),
  (2, NULL, "To Kill a Mockingbird", "A timeless tale of racial injustice and moral growth in the American South.", "Harper Lee", 1320, 2,NULL,"ebookstore_flask/static/image/books/PID_book6.png", 1),
  (9, NULL, "1984", "A dystopian masterpiece portraying a world dominated by surveillance, oppression, and propaganda.", "George Orwell", 1100, 1,NULL,"ebookstore_flask/static/image/books/PID_book7.png", 0),
  (8, 9,    "The Catcher in the Rye", "A story of teenage angst and rebellion through the perspective of the iconic Holden Caulfield.", "J.D. Salinger", 1000, 0,NULL,"ebookstore_flask/static/image/books/PID_book8.png", 1),
  (9, NULL, "Moby-Dick", "An adventurous tale of obsession, revenge, and the pursuit of the great white whale.", "Herman Melville", 870, 6,NULL,"ebookstore_flask/static/image/books/PID_book9.png", 0),
  (9, NULL, "The Hobbit", "A prequel to 'The Lord of the Rings,' following Bilbo Baggins on his unexpected journey through Middle-earth.", "J.R.R. Tolkien",1400, 99, NULL,"ebookstore_flask/static/image/books/PID_book10.png", 5),
  (2, NULL, "Animal Farm", "A satirical novella that uses a farm animal uprising to explore themes of power and corruption.", "George Orwell",890, 101 ,NULL,"ebookstore_flask/static/image/books/PID_book11.png", 1),
  (9, 7,    "The Alchemist", "A journey of self-discovery and following one's dreams, told through the story of Santiago, a shepherd.", "Paulo Coelho", 1300, 80, NULL,"ebookstore_flask/static/image/books/PID_book12.png", 1),
  (8, NULL, "Jane Eyre","A Gothic romance exploring love, independence, and resilience through the life of Jane Eyre.", "Charlotte Brontë", 990, 4,NULL,"ebookstore_flask/static/image/books/PID_book13.png", 0),
  (2, NULL, "The Little Prince", "A poetic tale about love, loss, and imagination, narrated by a young prince from another planet.", "Antoine de Saint-Exupéry", 1000, 70, NULL,"ebookstore_flask/static/image/books/PID_book14.png", 7),
  (8, NULL, "War and Peace", "A grand novel interweaving Russian society, history, and personal relationships during the Napoleonic Wars.", "Leo Tolstoy", 1111, 3, NULL,"ebookstore_flask/static/image/books/PID_book15.png", 1),
  (8, NULL, "The Kite Runner", "A moving story of friendship, betrayal, and redemption set against the backdrop of Afghanistan.", "Khaled Hosseini", 1600, 0, NULL,"ebookstore_flask/static/image/books/PID_book16.png", 1),
  (9, NULL, "The Fault in Our Stars", NULL, "John Green", 700,9 ,NULL,"ebookstore_flask/static/image/books/PID_book17.png", 0),
  (2, NULL, "Sapiens: A Brief History of Humankind", "A compelling exploration of human evolution, culture, and the forces that shaped modern society.", "Yuval Noah Harari",650,11, NULL,"ebookstore_flask/static/image/books/PID_book18.png", 5),
  (2, NULL, "The Hunger Games", "A dystopian novel about a teenage girl who becomes a symbol of rebellion in a world ruled by authoritarian control.", "Suzanne Collins", 750, 0,NULL,"ebookstore_flask/static/image/books/PID_book19.png", 1),
  (9, NULL, "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "A magical adventure in the land of Narnia, where children discover their destiny to save a world in turmoil.", "C.S. Lewis", 1210, 100, NULL,"ebookstore_flask/static/image/books/PID_book20.png", 1);

INSERT INTO "ShoppingCart_item" ("CMID", "Tot_price")
VALUES
  (3, 2400),
  (4, 1320),
  (5, 4370), 
  (6, 2600), 
  (7, 4741);


INSERT INTO "item_line" ("PID","OID","SCID","Line_type","Quantity")
VALUES
  (2,  1,     NULL, 'Order', 1),
  (4,  1,     NULL, 'Order', 1),
  (1,  2,     NULL, 'Order', 2),
  (5,  2,     NULL, 'Order', 1),
  (20, 3,     NULL, 'Order', 1),
  (10, 4,     NULL, 'Order', 3),
  (6,  4,     NULL, 'Order', 1),
  (3,  5,     NULL, 'Order', 1),
  (4,  6,     NULL, 'Order', 3),
  (8,  6,     NULL, 'Order', 1),
  (11, 7,     NULL, 'Order', 1),
  (12, 7,     NULL, 'Order', 1),
  (14, 7,     NULL,' Order', 2),
  (16, 8,     NULL, 'Order', 1),
  (14, 9,     NULL, 'Order', 5),
  (19, 9,     NULL, 'Order', 1),
  (15, 10,    NULL, 'Order', 1),
  (10, 10,    NULL, 'Order', 2),
  (18, 10,    NULL, 'Order', 5),
  (4,  NULL,  1,    'ShoppingCart', 1),
  (1,  NULL,  1,    'ShoppingCart', 1),
  (6,  NULL,  2,    'ShoppingCart', 1),
  (9,  NULL,  3,    'ShoppingCart', 4),
  (11, NULL,  3,    'ShoppingCart', 1),
  (12, NULL,  4,    'ShoppingCart', 2),
  (15, NULL,  5,    'ShoppingCart', 1),
  (20, NULL,  5,    'ShoppingCart', 3),


INSERT INTO "Review" ("PID","MID","Time","Rate","Rev_text","Rev_picture","Rev_video","Reply_RID")
VALUES
  (1, 3, '2024-10-13 14:23:00', 4, "An enthralling read with rich characters and a gripping plot. The author masterfully weaves themes of love, loss, and resilience into a story that lingers long after the final page.","ebookstore_flask/static/image/books/PID_book1.png", "ebookstore_flask/static/video/video1.mp4", NULL)
  (2, 4, '2024-11-14 09:15:00', 5, "A captivating journey through a richly imagined world. Highly recommended for fantasy lovers.","ebookstore_flask/static/image/books/PID_book2.png", NULL, NULL),
  (3, 5, '2024-10-02 16:45:00', 3, "An engaging plot, but the pacing felt uneven at times.","ebookstore_flask/static/image/books/PID_book3.png", NULL, NULL),
  (4, 6, '2024-10-28 11:20:00', 4, "Insightful and beautifully written. The author's storytelling is superb.","ebookstore_flask/static/image/books/PID_book4.png", "ebookstore_flask/static/video/video2.mp4", NULL),
  (5, 7, '2024-09-17 18:30:00', 2, "The story had potential, but the characters lacked depth.","ebookstore_flask/static/image/books/PID_book5.png", NULL, NULL),
  (6, 10, '2024-11-26 14:00:00', 5, "An absolute masterpiece! This book will stay with me for a long time.","ebookstore_flask/static/image/books/PID_book6.png", "ebookstore_flask/static/video/video3.mp4", NULL),
  (6, 2, '2024-11-26 18:19:00', NULL, "Thank you for the reply!", NULL, NULL),
  (1, 8, '2024-10-15 20:59:00', NULL, "Thank you for the reply!", NULL, NULL),
  (2, 9, '2024-11-15 18:45:00', NULL, "Thank you for the reply!", NULL, NULL);