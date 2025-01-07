INSERT INTO "Member" ("F_name", "L_name", "Password", "Gender", "Email", "Phone", "Birth", "Address", "Reg_date", "A_flag", "S_flag", "C_flag") 
VALUES 
  ('Harrison', 'Mckinney', 'Password123', 'Male', 'harrison4356@gmail.com', '0912345678', '1990-01-15', '123 Main St, Springfield', '2024-10-13', TRUE, FALSE, FALSE),
  ('Hudson', 'Smith', 'Passw0rd!', 'Male', 'hudson247@gmail.com', '0923456789', '1992-05-20', '456 Elm St, Springfield', '2024-10-14', FALSE, TRUE, FALSE),
  ('Chris', 'Lee', 'Qwerty123', 'Other', 'chris_lee@gmail.com', '0993174028', '1995-03-10', '789 Maple St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('Cecilia', NULL, '1234Pass', 'Female', 'cecilia643@gmail.com', '0934567890', '1988-07-08', '321 Oak St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('Landon', 'Burke', 'Bur2023!', 'Male', 'landon232@gmail.com', '0945678901', '1990-10-25', '654 Pine St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('妍婷', '許', 'MyP@ssw0rd', 'Female', 'emily331565@gmail.com', '0921390592', '1999-02-14', '987 Birch St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('家文', '何', 'T0mP@ss', 'Male', 'tom1121@gmail.com', '0956789012', NULL, '159 Cedar St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('家綺', '溫', 'Sophia!@#', 'Female', 'sophiamiller@gmail.com', '0967890123', '2000-09-12', '753 Cherry St, Springfield', '2024-10-14', FALSE, TRUE, FALSE),
  ('Asher', 'Clark', 'AsherClark1', 'Other', 'alex_taylor@gmail.com', '0978901234', '1994-06-30', '852 Walnut St, Springfield', '2024-10-17', FALSE, TRUE, FALSE),
  ('瑞池', '宋', 'Liam2024', 'Male', 'liam_anderson@gmail.com', '0989012345', '1985-11-05', '951 Willow St, Springfield', '2024-10-28', FALSE, FALSE, TRUE),
  ('John', 'Doe', 'password123', 'Male', 'john.doe@example.com', '5551234567', '1990-01-15', '123 Main St, Springfield', '2025-01-01', FALSE, FALSE, TRUE),
  ('Jane', 'Smith', 'securepass456', 'Female', 'jane.smith@example.com', '5559876543', '1992-06-25', '456 Elm St, Springfield', '2025-01-02', FALSE, FALSE, TRUE),
  ('Michael', 'Johnson', 'mypassword789', 'Male', 'michael.johnson@example.com', '5552345678', '1988-09-12', '789 Pine St, Springfield', '2025-01-03', FALSE, FALSE, TRUE),
  ('Emily', 'Davis', 'emilypass123', 'Female', 'emily.davis@example.com', '5558765432', '1995-03-08', '321 Oak St, Springfield', '2025-01-04', FALSE, FALSE, TRUE),
  ('Daniel', 'Brown', 'dansecure456', 'Male', 'daniel.brown@example.com', '5553456789', '1993-12-20', '654 Cedar St, Springfield', '2025-01-05', FALSE, FALSE, TRUE),
  ('Sophia', 'Wilson', 'sophiapass789', 'Female', 'sophia.wilson@example.com', '5556543210', '1991-05-17', '987 Birch St, Springfield', '2025-01-06', FALSE, FALSE, TRUE),
  ('William', 'Moore', 'willpass123', 'Male', 'william.moore@example.com', '5557654321', '1987-08-30', '432 Maple St, Springfield', '2025-01-07', FALSE, FALSE, TRUE),
  ('Olivia', 'Taylor', 'oliviasecure456', 'Female', 'olivia.taylor@example.com', '5555432109', '1994-11-22', '123 Willow St, Springfield', '2025-01-08', FALSE, FALSE, TRUE),
  ('家豪', '王', 'jiahao@123', 'Male', 'jiahao.wang@example.com', '0912345677', '1989-07-14', '456 萬松路, Taipei', '2025-01-09', FALSE, FALSE, TRUE),
  ('雅婷', '林', 'Yating!456', 'Female', 'yating.lin@example.com', '0913455789', '1996-10-10', '123 文昌街, Kaohsiung', '2025-01-10', FALSE, FALSE, TRUE);

INSERT INTO "Credit_card" ("Number", "CMID", "Expiry_date", "CVV") 
VALUES 
  ('4532147890123456', 3, '2025-12-31', '123'),
  ('5312345678901233', 4, '2026-06-30', '456'),
  ('3530111333300505', 5, '2027-09-15', '789'),
  ('5412345678901232', 6, '2026-03-20', '321'),
  ('5212345678901234', 10, '2028-11-10', '654'),
  ('4111111111111111', 10, '2026-01-01', '123'),
  ('4111111111112222', 10, '2027-02-01', '234'),
  ('4111111111113333', 10, '2025-12-01', '345'),
  ('4705111111114444', 10, '2026-07-01', '456'),
  ('4705380311112222', 10, '2025-10-01', '567'),
  ('5110111111116666', 4, '2030-10-01', '657'),
  ('5110980011116666', 4, '2030-03-01', '125'),
  ('4705380314576893', 4, '2029-01-01', '158'),
  ('5110980025789634', 3, '2028-03-01', '147'),
  ('4705380355412356', 3, '2028-08-01', '159'),
  ('511038035478962 ', 3, '2031-07-01', '127'),
  ('5110980054789627', 3, '2029-07-01', '127');

INSERT INTO "Discount" ("Disc_code", "Disc_value", "Disc_type", "Disc_name", "Policy_desc", "Max_usage")
VALUES
  ('SHIP500FREE', 0.00, 'Shipping', 'Free Shipping Over $500', 'Applies to orders with a total purchase amount greater than or equal to $500. Valid from 2024-11-01 to 2024-12-31.', 1000),
  ('SHIP10OFF', 0.90, 'Shipping', 'Flat 10% Off Shipping Fee', 'Valid for orders placed from 2024-11-15 to 2024-12-31. Shipping fee will be reduced by 10% for all eligible orders.', 500),
  ('FIRSTSHIP', 0.00, 'Shipping', 'Free Shipping for First Order', 'Applies to first-time customers on their first order, regardless of purchase amount. Valid from 2024-10-01 to 2024-12-31.', 2000),
  ('SEASON5OFF', 0.95, 'Seasoning', '5% Off Seasonings', 'A 5% discount applied to all seasoning products. Valid from 2024-11-01 to 2024-11-30.', 300),
  ('SPICEHOLIDAY', 0.90, 'Seasoning', 'Holiday Spice Discount', 'A 10% discount applied to purchases of seasoning products above $100. Valid from 2024-12-01 to 2024-12-25.', 150),
  ('HERBS2024', 0.92, 'Seasoning', 'Herbs Special Discount', 'A discount of 8% on World Literature during the promotional period. Valid from 2024-11-15 to 2024-12-15.', 100),
  ('EVENTBOGO', 0.00, 'Special Event', 'Buy 1 Get 1 Free', 'Buy 1 get 1 free on selected products. Valid from 2024-11-01 to 2024-11-30. Discount code applies to product IDs 101, 102, and 103.', 500),
  ('HOLIDAY50', 0.50, 'Special Event', '50% Off Holiday Special', '50% discount on selected holiday products. Valid from 2024-12-01 to 2024-12-31. Applies to product IDs 201, 202, and 203.', 300),
  ('FLASHSALE10', 0.90, 'Special Event', '10% Off Flash Sale', '10% off on flash sale items during the promotional period. Valid from 2024-11-20 to 2024-11-22. Discount code applies to product IDs 301, 302, and 303.', 200);

INSERT INTO "Shipping" ("DID", "Min_purchase")
VALUES
  (1, 500),  
  (2, 100),  
  (3, NULL);

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

INSERT INTO "Order" ("CMID", "SMID", "DID", "Credit_num", "Time", "Ship_address", "Ship_fee", "Status", "Pay_method", "Tot_price") 
VALUES
  (10, 9, 3, '5212345678901234', '2024-11-24 09:30:00', '987 Elm Dr, Brockway', 35, 'Shipping', 'Credit card', 2100),
  (3, 2, 3, '4532147890123456', '2024-11-29 10:30:00', '123 Maple St, Springfield', 50, 'Processing', 'Credit card', 3450),
  (6, 2, 3, '5412345678901232', '2024-11-26 13:10:00', '321 Birch Rd, Ogdenville', 40, 'Closed', 'Credit card', 1210),
  (5, 9, NULL, NULL, '2024-11-27 18:20:00', '789 Pine Ln, Capital City', 20, 'Received', 'COD', 5520),
  (4, 8, 1, '5312345678901233', '2024-11-28 15:45:00', '456 Oak Ave, Shelbyville', 30, 'Shipping', 'Credit card', 800),
  (7, 8, 2, NULL, '2024-11-25 11:00:00', '654 Cedar Ct, North Haverbrook', 25, 'Processing', 'COD', 3700),
  (4, 8, NULL, NULL, '2024-11-22 16:40:00', '852 Cypress Way, Shelbyville', 20, 'Closed', 'COD', 4190),
  (3, 2, 1, '4532147890123456',' 2024-11-23 14:50:00', '741 Willow Blvd, Springfield', 50, 'Received', 'Credit card', 1600),
  (5, 9, NULL, '3530111333300505', '2024-11-21 12:15:00', '963 Aspen Pkwy, Capital City', 45, 'Processing', 'Credit card', 5750),
  (6, 2, 2, NULL, '2024-11-20 08:30:00', '357 Redwood Ln, Ogdenville', 30, 'Shipping', 'COD', 7161);

INSERT INTO "Product" ("SMID", "SpEvent_ID", "Name", "Desc", "Author", "Price", "Stock_quantity", "Category", "Product_pict", "Sale_count") 
VALUES
  (2, 9, 'Harry Potter and the Sorcerer''s Stone', 'The beginning of the magical journey of Harry Potter, a young wizard discovering his powers and fighting the dark forces at Hogwarts.', 'J.K. Rowling', 1500, 10, 'Fantasy', 'https://lh3.googleusercontent.com/d/1TCCNKgDTdkbYGIkjeGSyLyRPAgqVc0Ro', 2),
  (2, NULL, 'The Lord of the Rings: The Fellowship of the Ring', 'A fantasy epic about a young hobbit, Frodo, tasked with destroying a powerful ring to save Middle-earth.', 'J.R.R. Tolkien', 1200, 20, 'Fantasy', 'https://lh3.googleusercontent.com/d/1XZrgK6bN9xFzAHqBpWrTN_QMPCedr_0E', 1),
  (8, NULL, 'The Great Gatsby', 'A classic exploration of the American Dream, wealth, and unrequited love during the Roaring Twenties.', 'F. Scott Fitzgerald', 900, 5, 'Classic', 'https://lh3.googleusercontent.com/d/1Mp0b8Q5V-BhtuQEckZMJpIAT1y60Rwl-', 4),
  (8, NULL, 'Pride and Prejudice', 'A beloved romance set in 19th-century England, highlighting societal expectations and enduring love.', 'Jane Austen', 450, 30, 'Romance', 'https://lh3.googleusercontent.com/d/1w_voCRLtQiEhsWRxr_ukYOOzkErXevLQ', 1),
  (2, NULL, 'To Kill a Mockingbird', 'A timeless tale of racial injustice and moral growth in the American South.', 'Harper Lee', 1320, 2, 'Classic', 'https://lh3.googleusercontent.com/d/1khcqiJES68XpZ3tKGTLudrTeQXILDwiX', 1),
  (9, NULL, '1984', 'A dystopian masterpiece portraying a world dominated by surveillance, oppression, and propaganda.', 'George Orwell', 1100, 1, 'Science Fiction', 'https://lh3.googleusercontent.com/d/19J3EBDiZnKt3BZv1oXpqwWbvT1_ISwjT', 0),
  (8, 9, 'The Catcher in the Rye', 'A story of teenage angst and rebellion through the perspective of the iconic Holden Caulfield.', 'J.D. Salinger', 1000, 0, 'Classic', 'https://lh3.googleusercontent.com/d/17m8SpzPB87pIDZ-B4rpEIhKj7N5fMdid', 1),
  (9, NULL, 'Moby-Dick', 'An adventurous tale of obsession, revenge, and the pursuit of the great white whale.', 'Herman Melville', 870, 6, 'Adventure', 'https://lh3.googleusercontent.com/d/1TVsXJNn3b0ei8ywggkkXh8R8ZakrHSBn', 0),
  (9, NULL, 'The Hobbit', 'A prequel to ''The Lord of the Rings,'' following Bilbo Baggins on his unexpected journey through Middle-earth.', 'J.R.R. Tolkien', 1400, 99, 'Fantasy', 'https://lh3.googleusercontent.com/d/1CqTK_93FhYN6Ikj0neuaB6W9lyj4oQUx', 5),
  (2, NULL, 'Animal Farm', 'A satirical novella that uses a farm animal uprising to explore themes of power and corruption.', 'George Orwell', 890, 101, 'Political Fiction', 'https://lh3.googleusercontent.com/d/1wb4_TnhD7DUPLC7U7B5tgG3dOvs8LINh', 1),
  (9, 7, 'The Alchemist', 'A journey of self-discovery and following one''s dreams, told through the story of Santiago, a shepherd.', 'Paulo Coelho', 1300, 80, 'Adventure', 'https://lh3.googleusercontent.com/d/1vsccriUVd-e_0I0lwaugvhtCR7gL6zHW', 1),
  (8, NULL, 'Jane Eyre', 'A Gothic romance exploring love, independence, and resilience through the life of Jane Eyre.', 'Charlotte Brontë', 990, 4, 'Romance', 'https://lh3.googleusercontent.com/d/1PrlRKWvyUsjR3kVqx1aQ7JQUnGFuXLkt', 0),
  (2, NULL, 'The Little Prince', 'A poetic tale about love, loss, and imagination, narrated by a young prince from another planet.', 'Antoine de Saint-Exupéry', 1000, 70, 'Classic', 'https://lh3.googleusercontent.com/d/1GLp6S50D8rJN_XZQly2LKIh1jZw1mhNk', 7),
  (8, NULL, 'War and Peace', 'A grand novel interweaving Russian society, history, and personal relationships during the Napoleonic Wars.', 'Leo Tolstoy', 1111, 3, 'Historical Fiction', 'https://lh3.googleusercontent.com/d/15OVfiFJs7I_Fgg67O2QpbbF_amw1L-fh', 1),
  (8, NULL, 'The Kite Runner', 'A moving story of friendship, betrayal, and redemption set against the backdrop of Afghanistan.', 'Khaled Hosseini', 1600, 0, 'Drama', 'https://lh3.googleusercontent.com/d/1181ckwZg6BxOSXg1jZ4dULb8-NfJ-pAM', 1),
  (9, NULL, 'The Fault in Our Stars', NULL, 'John Green', 700, 9, 'Romance', 'https://lh3.googleusercontent.com/d/1HXqhzcaTWUcqVhrLJBNTSI965VIG0ucd', 0),
  (2, NULL, 'Sapiens: A Brief History of Humankind', 'A compelling exploration of human evolution, culture, and the forces that shaped modern society.', 'Yuval Noah Harari', 650, 11, 'Non-fiction', 'https://lh3.googleusercontent.com/d/1QSfnM_0qXatulU5bKnoBhTIrwjXvO68m', 5),
  (2, NULL, 'The Hunger Games', 'A dystopian novel about a teenage girl who becomes a symbol of rebellion in a world ruled by authoritarian control.', 'Suzanne Collins', 750, 0, 'Science Fiction', 'https://lh3.googleusercontent.com/d/1bUE0N2s-b1X4gLJTgUnyj2xzJ76Omrei', 1),
  (9, NULL, 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe', 'A magical adventure in the land of Narnia, where children discover their destiny to save a world in turmoil.', 'C.S. Lewis', 1210, 100, 'Fantasy', 'https://lh3.googleusercontent.com/d/1Jd6gPnKkOa1hdIr0ibRMoQrJrwusTwMN', 1),
  (9, NULL, 'The Da Vinci Code', 'A thrilling mystery that blends art, religion, and history in a race to uncover hidden secrets of the Church.', NULL, 800, 4, 'Mystery', 'https://lh3.googleusercontent.com/d/1IS8pqBCkkseuLix7YOg9i17tS7wsPqds', 1),
  (2, NULL, 'A Sea of Unspoken Things', 'Ever since James lost her twin brother in a freak accident, life hasn''t been the same. Both tragic and tender, this is a breathtaking journey of grief, love and history from the bestselling author of Fable.', 'Adrienne Young', 900, 33, 'Mystery', 'https://lh3.googleusercontent.com/d/1UBF_STRf0hL2qh8mCCvzjEoOGzbirOup', 0),
  (2, NULL, 'How To Sleep At Night', 'Politics and romance collide in this heartfelt and hilarious read. With the wry voice of Emma Straub and the banter of Taffy Brodesser-Akner, How to Sleep at Night is a tender and timely read.', 'Elizabeth Harris', 850, 10, 'Romance', 'https://lh3.googleusercontent.com/d/1T2dUJn5lblMLZ9EDwmJZBC-XexZM1-dp', 0),
  (9, NULL, 'Your Brain On Art', 'Practical, comprehensive and essential, Your Brain on Art is ripe with insight. If you ever wanted to truly understand what art can do for the world, let this book be your guide.', 'Susan Magsamen, Ivy Ross', 700, 16, 'Non Fiction', 'https://lh3.googleusercontent.com/d/1BJNi958l2EYChdVrC2zheZcZrV5RV1s3', 0),
  (2, NULL, 'Homeseeking', 'An epic and intimate tale of one couple across sixty years as world events pull them together and apart, illuminating the Chinese diaspora and exploring what it means to find home far from your homeland.', 'Karissa Chen', 1000, 20, 'Romance', 'https://lh3.googleusercontent.com/d/1R_2XSbjoycYlckJ2aAJ4YbMWW5X2kX38', 0),
  (2, NULL, 'All The Water In The World', 'Haunting and unforgettable, All the Water in the World tells the story of a flooded world, and one family''s determination to keep their community alive. This all-too-prescient story introduces us to a fictional account of a possible dystopian future.', 'Eiren Caffall', 1000, 20, 'Mystery', 'https://lh3.googleusercontent.com/d/1f-URxRz_VDmGC7MGZ0ykyxlT_ZyoApk9', 0),
  (2, NULL, 'Mom, I Want to Hear Your Story', 'Moms contain multitudes, but have you ever wondered who she was before she was your mother? Now you can find out with this touching gift journal.', 'Jeffrey Mason', 500, 22, 'Non Fiction', 'https://lh3.googleusercontent.com/d/1CWdpE5BXs5cTImdo1txwOrgyv-weev7M', 0),
  (8, NULL, 'The Tenant', 'A new, jaw-dropping thriller from the instant #1 New York Times bestseller of The Boyfriend and The Housemaid!  There''s no place like home...', 'Freida McFadden', 800, 30, 'Mystery', 'https://lh3.googleusercontent.com/d/1EOWySx3FpN8MABq-4Mq6ebgVGO-rXEPu', 0),
  (9, NULL, 'Cher: The Memoir, Part One', 'The truly one-of-a-kind life story of Cher, told by the superstar herself, tracing from her humble origins to the remarkable heights she’s reached and everything in between. It’s honest, authentic and incredible.', 'Cher', 1000, 35, 'Classic', 'https://lh3.googleusercontent.com/d/1OTe1KkeTs74th5_ovusE0S1BG6XIM0W8', 0),
  (8, NULL, 'Where the Creek Bends', 'From acclaimed #1 New York Times bestselling author Linda Lael Miller comes a beautifully rendered timeslip novel about the family we create for ourselves…', 'Linda Lael Miller', 500, 9, 'Drama', 'https://lh3.googleusercontent.com/d/1DJplK6oF1wjD-J2MVhv9ER4LLfSBfigp', 0),
  (8, NULL, 'James', 'A powerful story of family, home and freedom. Percival Everett has flipped the script on an American classic as Huck Finn steps to the side and Jim — James — takes center stage.', 'Percival Everett', 700, 15, 'Fantasy', 'https://lh3.googleusercontent.com/d/1y3td-bS02dbqIwtiRPaG-dbKiG_vN-95', 0),
  (8, NULL, ' Add to Wishlist Nightbitch: A Novel', '"A must-read for anyone who can’t get enough of the ever-blurring line between the psychological and supernatural that Yellowjackets exemplifies." —Vulture', 'Rachel Yoder', 600, 21, 'Classic', 'https://lh3.googleusercontent.com/d/1Qv0xaOgaAtiENjoo2GteTNBUfcFRQUve', 0),
  (8, NULL, 'The Women', 'The Women is both singular and expansive in focus. Centered on one woman who goes to war in Vietnam, it is a stark reminder of the sacrifices women make for their country.', 'Kristin Hannah', 700, 12, 'Classic', 'https://lh3.googleusercontent.com/d/1lx897GA5MHMP2RBkhbUf7R1BhxP-NT8h', 0),
  (8, NULL, 'You''ll Never Believe Me: A Life of Lies, Second Tries, and Things I Should Only Tell My Therapist', 'A larger-than-life true story bursting with deeply personal and honest insights. This coming-of-age tale takes readers through Ferrell''s misadventures to prison and back, delivering a satisfying redemptive arc for the ages.', 'Kari Ferrell', 1000, 5, 'Fantasy', 'https://lh3.googleusercontent.com/d/17TFIXdy3Xg1fxDSg36BndinDFa8pSG2t', 0),
  (2, NULL, 'The Let Them Theory: A Life-Changing Tool That Millions of People Can''t Stop Talking About', 'Bestselling author, podcaster and motivational speaker Mel Robbins returns with her most insightful and life-changing book yet. From helping you build friendships to break free from insecurities to finding joy and success in everyday life, The Let Them Theory is a liberating read, perfect for fans of Brené Brown and Glennon Doyle.', 'Mel Robbins', 1000, 100, 'Non Fiction', 'https://lh3.googleusercontent.com/d/1lAJJ9AarcBfVLrQ-_T_S7WUEdP5E9fgK', 0),
  (2, NULL, 'Backwater Justice', 'The Sisterhood: a group of women from all walks of life bound by friendship and years of adventure. Armed with vast resources, top-notch expertise, and a loyal network of allies around the globe, the Sisterhood will not rest until every wrong is made right.', 'Fern Michaels', 300, 30, 'Classic', 'https://lh3.googleusercontent.com/d/1uF4fnvORn9i3oDaQisOI0IGzNxUGIeva', 0),
  (9, NULL, 'To Die For', 'A brand-new action-packed thriller from David Baldacci where Travis Devine learns to keep his friends close, and his enemies closer.', 'David Baldacci', 500, 15, 'Mystery', 'https://lh3.googleusercontent.com/d/1O4X0jlyf6SLPrdL4CntDwDO9xDfUN1Tg', 0),
  (9, NULL, 'Quicksilver', 'The global phenomenon by Callie Hart—a highly addicting enemies-to-lovers Romantasy with razor-sharp banter, heart-stopping action, and blistering hot romance—now has an embossed cover, silver foiling, and an updated interior design.', 'Callie Hart', 700, 55, 'Adventure', 'https://lh3.googleusercontent.com/d/1qoahudHpwyuP5Xg2fHJmwn-lX2WxysrZ', 0),
  (2, NULL, 'Stranger Skies', 'The sequel to Curious Tides takes us into the world of Wychwood, a storybook realm flipped on its head. With Emory and Romie trapped in Wychwood and Baz and Kai stuck in another world, they all must work together to uncover Aldryn’s sinister secrets.', 'Pascale Lacelle', 500, 11, 'Mystery', 'https://lh3.googleusercontent.com/d/1NLP_JNfduBInMBF9dZRzU5JcpwQj6QpG', 0),
  (9, NULL, 'The Three Lives of Cate Kay: A Novel', 'A tale about identity, coming-of-age, friendship and love, The Three Lives of Cate Kay is a dazzling, big-hearted journey.', 'Kate Fagan', 900, 27, 'Romance', 'https://lh3.googleusercontent.com/d/1vGfaNe83hPTWl1vL0ZVZ52ChJJwKFBnQ', 0),
  (9, NULL, 'The Life Cycle of the Common Octopus', 'A sharp coming-of-age journey set in a glamorous world of high academia, old money and one eccentric upper-class family. This heartfelt tale is sure to please fans of Sally Rooney and Emma Donoghue.', 'Emma Knight', 990, 87, 'Classic', 'https://lh3.googleusercontent.com/d/1xMsn6ADzAr8sSP7Vl9KuB72hkPZwAfru', 0);

INSERT INTO "ShoppingCart_item" ("CMID", "Tot_price")
VALUES
  (3, 2400),
  (4, 1320),
  (5, 4370),
  (7, 4741),
  (6, 3900);

INSERT INTO "Item_line" ("PID", "OID", "SCID", "Line_type", "Quantity")
VALUES
  (2, 1, NULL, 'Order', 1),
  (4, 1, NULL, 'Order', 1),
  (1, 2, NULL, 'Order', 2),
  (5, 2, NULL, 'Order', 1),
  (20, 3, NULL, 'Order', 1),
  (10, 4, NULL, 'Order', 3),
  (6, 4, NULL, 'Order', 1),
  (3, 5, NULL, 'Order', 1),
  (4, 6, NULL, 'Order', 3),
  (8, 6, NULL, 'Order', 1),
  (11, 7, NULL, 'Order', 1),
  (12, 7, NULL, 'Order', 1),
  (14, 7, NULL, 'Order', 2),
  (16, 8, NULL, 'Order', 1),
  (14, 9, NULL, 'Order', 5),
  (19, 9, NULL, 'Order', 1),
  (15, 10, NULL, 'Order', 1),
  (10, 10, NULL, 'Order', 2),
  (18, 10, NULL, 'Order', 5),
  (4, NULL, 1, 'ShoppingCart', 1),
  (1, NULL, 1, 'ShoppingCart', 1),
  (6, NULL, 2, 'ShoppingCart', 1),
  (9, NULL, 3, 'ShoppingCart', 4),
  (11, NULL, 3, 'ShoppingCart', 1),
  (15, NULL, 5, 'ShoppingCart', 1),
  (20, NULL, 5, 'ShoppingCart', 3),
  (12, NULL, 4, 'ShoppingCart', 3);

INSERT INTO "Review" ("PID", "MID", "Time", "Rate", "Rev_text")
VALUES
  (1, 3, '2024-10-13 14:23:00', 4, 'An enthralling read with rich characters and a gripping plot. The author masterfully weaves themes of love, loss, and resilience into a story that lingers long after the final page.'),
  (2, 4, '2024-11-14 09:15:00', 5, 'A captivating journey through a richly imagined world. Highly recommended for fantasy lovers.'),
  (3, 5, '2024-10-02 16:45:00', 3, 'An engaging plot, but the pacing felt uneven at times.'),
  (4, 6, '2024-10-28 11:20:00', 4, 'Insightful and beautifully written. The author''s storytelling is superb.'),
  (5, 7, '2024-09-17 18:30:00', 2, 'The story had potential, but the characters lacked depth.'),
  (6, 10, '2024-11-26 14:00:00', 5, 'An absolute masterpiece! This book will stay with me for a long time.');