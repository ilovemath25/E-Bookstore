const translateDataSets = {
   // Header
   "Home": "首頁",
   "Book": "書籍",
   "Language": "語言",
   "Cart": "購物車",
   "Profile": "個人資料",
   "Search": "搜尋",
   // Category
   "Fantasy": "奇幻",
   "Mystery": "懸疑",
   "Classic": "經典",
   "Romance": "愛情",
   "Science Fiction": "科幻",
   "Adventure": "冒險",
   "Political Fiction": "政治小說",
   "Historical Fiction": "歷史小說",
   "Drama": "戲劇",
   "Non-fiction": "非小說",
   // Home page
   "Price:": "價格:",
   "Rate: ": "評分: ",
   "Best Seller": "暢銷書籍",
   "New Release": "新書上市",
   "Top 5 Category": "前五名類別",
   "Most Rated": "最高評分",
   // Book list page
   "Result of : ": "搜尋結果: ",
   // Book detail page
   "Category:": "類別:",
   "Stock Quantity:": "庫存數量:",
   "Sales Count:": "銷售數量:",
   "by": "作者",
   "Customer Reviews": "顧客評論",
   "No reviews yet ! Be the first to share your thoughts": "還沒有評論！成為第一個分享想法的人",
   "Add to Cart": "加入購物車",
   "Buy Now": "立即購買",
   // Book names and descriptions
   "Harry Potter and the Sorcerer's Stone": "哈利波特與神秘的魔法石",
   "The beginning of the magical journey of Harry Potter, a young wizard discovering his powers and fighting the dark forces at Hogwarts.": "哈利波特的魔法之旅開始，他在霍格華茲發現自己的力量並對抗黑暗勢力。",
   "The Lord of the Rings: The Fellowship of the Ring": "魔戒：護戒使者",
   "A fantasy epic about a young hobbit, Frodo, tasked with destroying a powerful ring to save Middle-earth.": "一個關於年輕哈比人弗羅多的奇幻史詩，他的使命是摧毀強大的戒指以拯救中土。",
   "The Da Vinci Code": "達文西密碼",
   "A thrilling mystery that blends art, religion, and history in a race to uncover hidden secrets of the Church.": "一部融合藝術、宗教和歷史的驚悚懸疑小說，展現了揭露教會隱藏祕密的競速過程。",
   "The Great Gatsby": "大亨小傳",
   "A classic exploration of the American Dream, wealth, and unrequited love during the Roaring Twenties.": "探索美國夢、財富和無望的愛情，背景設定於咆哮的二十年代。",
   "Pride and Prejudice": "傲慢與偏見",
   "A beloved romance set in 19th-century England, highlighting societal expectations and enduring love.": "經典愛情故事，背景是19世紀的英國，展現社會期望和堅定的愛情。",
   "To Kill a Mockingbird": "梅岡城故事",
   "A timeless tale of racial injustice and moral growth in the American South.": "一部關於美國南部種族不公和道德成長的永恆故事。",
   "1984": "一九八四",
   "A dystopian masterpiece portraying a world dominated by surveillance, oppression, and propaganda.": "一部描繪由監視、壓迫和宣傳支配的世界的反烏托邦傑作。",
   "The Catcher in the Rye": "麥田捕手",
   "A story of teenage angst and rebellion through the perspective of the iconic Holden Caulfield.": "透過標誌性人物霍頓·考菲爾德的視角，描寫青春期的焦慮和反叛。",
   "Moby-Dick": "白鯨記",
   "An adventurous tale of obsession, revenge, and the pursuit of the great white whale.": "一部探討執念、復仇以及追捕巨大白鯨的冒險故事。",
   "The Hobbit": "哈比人歷險記",
   "A prequel to 'The Lord of the Rings,' following Bilbo Baggins on his unexpected journey through Middle-earth.": "《魔戒》的前傳，講述比爾博·巴金斯在中土的意外旅程。",
   "Animal Farm": "動物農莊",
   "A satirical novella that uses a farm animal uprising to explore themes of power and corruption.": "一部寓言式小說，利用農場動物的起義來探討權力和腐敗的主題。",
   "The Alchemist": "牧羊少年奇幻之旅",
   "A journey of self-discovery and following one's dreams, told through the story of Santiago, a shepherd.": "一部關於自我發現和追隨夢想的旅程故事，講述牧羊人聖地亞哥的冒險。",
   "Jane Eyre": "簡愛",
   "A Gothic romance exploring love, independence, and resilience through the life of Jane Eyre.": "一部哥特式愛情小說，通過簡愛的生活探索愛情、獨立和堅韌。",
   "The Little Prince": "小王子",
   "A poetic tale about love, loss, and imagination, narrated by a young prince from another planet.": "一個關於愛、失落和想像力的詩意故事，由一位來自另一顆星球的小王子講述。",
   "War and Peace": "戰爭與和平",
   "A grand novel interweaving Russian society, history, and personal relationships during the Napoleonic Wars.": "一部結合俄羅斯社會、歷史和個人關係的宏大小說，背景為拿破崙戰爭時期。",
   "The Kite Runner": "追風箏的孩子",
   "A moving story of friendship, betrayal, and redemption set against the backdrop of Afghanistan.": "一部感人的故事，描述友誼、背叛與救贖，背景為阿富汗。",
   "The Fault in Our Stars": "星運里的錯",
   "A poignant love story between two teenagers with terminal illnesses, exploring life's greatest questions.": "一個關於兩位罹患絕症的青少年的感人愛情故事，探索生命中的重大問題。",
   "Sapiens: A Brief History of Humankind": "人類大歷史",
   "A compelling exploration of human evolution, culture, and the forces that shaped modern society.": "一部引人入勝的探索人類演化、文化及塑造現代社會力量的書籍。",
   "The Hunger Games": "飢餓遊戲",
   "A dystopian novel about a teenage girl who becomes a symbol of rebellion in a world ruled by authoritarian control.": "一部反烏托邦小說，描述一位少女成為由威權統治的世界中的反抗象徵。",
   "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe": "納尼亞傳奇：獅子、女巫和魔衣櫥",
   "A magical adventure in the land of Narnia, where children discover their destiny to save a world in turmoil.": "在納尼亞國度的奇幻冒險，孩子們發現了拯救混亂世界的命運。",
   // profile menu
   "My Profile": "我的個人資料",
   "Credit Card": "信用卡",
   "Change Password": "更改密碼",
   "Order History": "訂單歷史",
   "Discount": "折扣",
   "Logout": "登出",
   "Yes": "是",
   "No": "否",
   "Are you sure you want to log out?": "您確定要登出嗎？",
   // profile page
   "Name": "姓名",
   "First Name": "名字",
   "Last Name": "姓氏",
   "Birth": "生日",
   "Gender": "性別",
   "Male": "男性",
   "Female": "女性",
   "Other": "其他",
   "Email": "電子郵件",
   "Phone": "電話",
   "Address": "地址",
   "Register Date": "註冊日期",
   "Not Provided": "未提供",
   "Edit": "編輯",
   "Edit Profile": "編輯個人資料",
   "Cancel": "取消",
   "Save": "儲存",
   // credit card page
   "Add new card": "新增信用卡",
   "New Card": "新卡",
   "Card Number": "卡號",
   "Expiry Date (MM/YY)": "到期日 (MM/YY)",
   "Are you sure you want to delete this card?": "您確定要刪除這張卡嗎？",
   // change password page
   "Change Password": "更改密碼",
   "Current Password": "目前密碼",
   "New Password": "新密碼",
   "Confirm Password": "確認密碼",
   // order history page
   "Total Order": "總訂單數",
   "Processing": "處理中",
   "Shipping": "運送中",
   "Received": "已收到",
   "Closed": "已關閉",
   "Order History": "訂單歷史",
   "Order ID :": "訂單編號 :",
   "No Result !": "沒有結果 !",
   // discount page
   "Discount": "折扣",
   "Available": "可用",
   "Used": "已使用",
   "Expired": "已過期",
   "Max usage:": "最大使用次數 :",
   "Valid from:": "有效期限 :",
   "Valid to:": "有效至 :",
   "Free Shipping Over $500": "購物滿500美元免運費",
   "Applies to orders with a total purchase amount greater than or equal to $500. Valid from 2024-11-01 to 2024-12-31.": "適用於總購物金額大於或等於500美元的訂單。有效期從2024年11月1日到2024年12月31日。",
   "Flat 10% Off Shipping Fee": "運費一律減免10%",
   "Valid for orders placed from 2024-11-15 to 2024-12-31. Shipping fee will be reduced by 10% for all eligible orders.": "適用於2024年11月15日至2024年12月31日期間下的訂單，運費將減免10%。",
   "Free Shipping for First Order": "首次訂單免運費",
   "Applies to first-time customers on their first order, regardless of purchase amount. Valid from 2024-10-01 to 2024-12-31.": "適用於首次下訂的顧客，不限購物金額。有效期從2024年10月1日到2024年12月31日。",
   "5% Off Seasonings": "調味品享95折優惠",
   "A 5% discount applied to all seasoning products. Valid from 2024-11-01 to 2024-11-30.": "適用於所有調味品，享有95折優惠。有效期從2024年11月1日到2024年11月30日。",
   "Holiday Spice Discount": "假日香料優惠",
   "A 10% discount applied to purchases of seasoning products above $100. Valid from 2024-12-01 to 2024-12-25.": "適用於購買超過100美元的調味品，享有9折優惠。有效期從2024年12月1日到2024年12月25日。",
   "Herbs Special Discount": "香草特別優惠",
   "A discount of 8% on World Literature during the promotional period. Valid from 2024-11-15 to 2024-12-15.": "促銷期間，購買世界文學享有92折優惠。有效期從2024年11月15日到2024年12月15日。",
   "Buy 1 Get 1 Free": "買一送一優惠",
   "Buy 1 get 1 free on selected products. Valid from 2024-11-01 to 2024-11-30. Discount code applies to product IDs 101, 102, and 103.": "指定商品買一送一優惠。有效期從2024年11月1日到2024年11月30日。折扣碼適用於產品ID 101、102和103。",
   "50% Off Holiday Special": "假日特惠享5折優惠",
   "50% discount on selected holiday products. Valid from 2024-12-01 to 2024-12-31. Applies to product IDs 201, 202, and 203.": "指定假日商品享有5折優惠。有效期從2024年12月1日到2024年12月31日。適用於產品ID 201、202和203。",
   "10% Off Flash Sale": "限時促銷商品享9折優惠",
   "10% off on flash sale items during the promotional period. Valid from 2024-11-20 to 2024-11-22. Discount code applies to product IDs 301, 302, and 303.": "促銷期間限時促銷商品享有9折優惠。有效期從2024年11月20日到2024年11月22日。折扣碼適用於產品ID 301、302和303。",
   // cart page
   "Select All": "全選",
   "Unit price": "單價",
   "Quantity": "數量",
   "Total": "總計",
   "Subtotal": "小計",
   "items": "件",
   "Discount": "折扣",
   "Enter discount code": "輸入折扣碼",
   "Apply": "應用",
   "Payment Method": "付款方式",
   "COD": "貨到付款",
   "Select Payment Account:": "選擇付款賬戶：",
   "Receiver Information": "收件人信息",
   "Phone number": "電話號碼",
   "+ Pay with another card": "+ 使用另一張卡付款",
   "Another Card": "另一張卡",
   "Item Subtotal:": "商品小計：",
   "Discount:": "折扣：",
   "Shipping Subtotal:": "運費小計：",
   "Total:": "總計：",
   "Checkout": "結帳",
};