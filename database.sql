PGDMP  3    /            
    |         
   ebookstore    16.1    16.0 V    o           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            p           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            q           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            r           1262    16398 
   ebookstore    DATABASE     �   CREATE DATABASE ebookstore WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE ebookstore;
                postgres    false            w           1247    16659    Item_amount_type    TYPE     S   CREATE TYPE public."Item_amount_type" AS ENUM (
    'Order',
    'ShoppingCart'
);
 %   DROP TYPE public."Item_amount_type";
       public          postgres    false            _           1247    16490 	   disc_type    TYPE     a   CREATE TYPE public.disc_type AS ENUM (
    'Shipping',
    'Seasonings',
    'Special Events'
);
    DROP TYPE public.disc_type;
       public          postgres    false            Y           1247    16422    gender    TYPE     M   CREATE TYPE public.gender AS ENUM (
    'male',
    'female',
    'other'
);
    DROP TYPE public.gender;
       public          postgres    false            \           1247    16449    order_status    TYPE     l   CREATE TYPE public.order_status AS ENUM (
    'Received',
    'Processing',
    'Shipping',
    'Closed'
);
    DROP TYPE public.order_status;
       public          postgres    false            �            1259    16714    Applies    TABLE     Z   CREATE TABLE public."Applies" (
    "OID" integer NOT NULL,
    "DID" integer NOT NULL
);
    DROP TABLE public."Applies";
       public         heap    postgres    false            �            1259    16438    Credit_card    TABLE     �   CREATE TABLE public."Credit_card" (
    "Number" character(16) NOT NULL,
    "CMID" integer NOT NULL,
    "Expiry_date" date NOT NULL,
    "CVV" character(3) NOT NULL
);
 !   DROP TABLE public."Credit_card";
       public         heap    postgres    false            �            1259    16498    Discount    TABLE     c  CREATE TABLE public."Discount" (
    "DID" integer NOT NULL,
    "Disc_code" character varying(20) NOT NULL,
    "Disc_value" numeric NOT NULL,
    "Disc_type" public.disc_type NOT NULL,
    "Disc_name" character varying(50) NOT NULL,
    "Policy_desc" character varying(1000) NOT NULL,
    "Disc_desc" character varying(1000),
    "Max_usage" integer
);
    DROP TABLE public."Discount";
       public         heap    postgres    false    863            �            1259    16663    Item_Amount    TABLE     �   CREATE TABLE public."Item_Amount" (
    "AID" integer NOT NULL,
    "PID" integer NOT NULL,
    "Amount_type" public."Item_amount_type" NOT NULL,
    "Quantity" integer NOT NULL
);
 !   DROP TABLE public."Item_Amount";
       public         heap    postgres    false    887            �            1259    16430    Members    TABLE     �  CREATE TABLE public."Members" (
    "MID" integer NOT NULL,
    "F_name" character varying(15) NOT NULL,
    "L_name" character varying(15),
    "Password" character varying(15) NOT NULL,
    "Gender" public.gender NOT NULL,
    "Email" character varying(100) NOT NULL,
    "Phone" integer,
    "Birth" date,
    "Address" character varying(200),
    "Reg_date" date NOT NULL,
    "A_flag" boolean NOT NULL,
    "S_flag" boolean NOT NULL,
    "C_flag" boolean NOT NULL
);
    DROP TABLE public."Members";
       public         heap    postgres    false    857            �            1259    16698    Order_Item_Amount    TABLE     d   CREATE TABLE public."Order_Item_Amount" (
    "AID" integer NOT NULL,
    "OID" integer NOT NULL
);
 '   DROP TABLE public."Order_Item_Amount";
       public         heap    postgres    false            �            1259    16458    Orders    TABLE     
  CREATE TABLE public."Orders" (
    "OID" integer NOT NULL,
    "MID" integer NOT NULL,
    "Credit_num" character(1),
    "Time" timestamp without time zone NOT NULL,
    "Ship_address" character varying(200) NOT NULL,
    "Ship_fee" integer NOT NULL,
    "Status" public.order_status NOT NULL,
    "Pay_method" character varying NOT NULL,
    "Tot_price" integer,
    CONSTRAINT orders_pay_method_check CHECK ((("Pay_method")::text = ANY ((ARRAY['Credit card'::character varying, 'COD'::character varying])::text[])))
);
    DROP TABLE public."Orders";
       public         heap    postgres    false    860            �            1259    16603    Product    TABLE     �  CREATE TABLE public."Product" (
    "PID" integer NOT NULL,
    "SMID" integer NOT NULL,
    "SpEvent_ID" integer,
    "Name" character varying(50) NOT NULL,
    "Desc" character varying(1000),
    "Author" character varying(30),
    "Price" integer NOT NULL,
    "Stock_quantity" integer NOT NULL,
    "Category" character varying(20),
    "Product_pict" character varying(100),
    "Sale_count" integer
);
    DROP TABLE public."Product";
       public         heap    postgres    false            �            1259    16739    Review    TABLE     L  CREATE TABLE public."Review" (
    "RID" integer NOT NULL,
    "PID" integer NOT NULL,
    "CMID" integer NOT NULL,
    "Time" timestamp without time zone NOT NULL,
    "Rate" integer NOT NULL,
    "Rev_text" character varying(500),
    "Rev_picture" character varying,
    "Rev_video" character varying,
    "Reply_RID" integer
);
    DROP TABLE public."Review";
       public         heap    postgres    false            �            1259    16637 	   Seasoning    TABLE     �   CREATE TABLE public."Seasoning" (
    "DID" integer NOT NULL,
    "Valid_to" date NOT NULL,
    "Valid_from" date NOT NULL,
    CONSTRAINT "Valid_date_range" CHECK (("Valid_to" >= "Valid_from"))
);
    DROP TABLE public."Seasoning";
       public         heap    postgres    false            �            1259    16648    Shipping    TABLE     [   CREATE TABLE public."Shipping" (
    "DID" integer NOT NULL,
    "Min_purchase" integer
);
    DROP TABLE public."Shipping";
       public         heap    postgres    false            �            1259    16673    ShoppingCart_Item    TABLE        CREATE TABLE public."ShoppingCart_Item" (
    "SCID" integer NOT NULL,
    "CMID" integer,
    "Tot_price" integer NOT NULL
);
 '   DROP TABLE public."ShoppingCart_Item";
       public         heap    postgres    false            �            1259    16683    ShoppingCart_Item_Amount    TABLE     �   CREATE TABLE public."ShoppingCart_Item_Amount" (
    "AID" integer NOT NULL,
    "SCID" integer NOT NULL,
    "Selected" boolean
);
 .   DROP TABLE public."ShoppingCart_Item_Amount";
       public         heap    postgres    false            �            1259    16626    Special_event    TABLE     �   CREATE TABLE public."Special_event" (
    "DID" integer NOT NULL,
    "Valid_to" date NOT NULL,
    "Valid_from" date NOT NULL,
    CONSTRAINT "Valid_date_range" CHECK (("Valid_to" >= "Valid_from"))
);
 #   DROP TABLE public."Special_event";
       public         heap    postgres    false            �            1259    16497    discount_did_seq    SEQUENCE     �   CREATE SEQUENCE public.discount_did_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.discount_did_seq;
       public          postgres    false    221            s           0    0    discount_did_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.discount_did_seq OWNED BY public."Discount"."DID";
          public          postgres    false    220            �            1259    16429    members_mid_seq    SEQUENCE     �   CREATE SEQUENCE public.members_mid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.members_mid_seq;
       public          postgres    false    216            t           0    0    members_mid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.members_mid_seq OWNED BY public."Members"."MID";
          public          postgres    false    215            �            1259    16457    orders_oid_seq    SEQUENCE     �   CREATE SEQUENCE public.orders_oid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.orders_oid_seq;
       public          postgres    false    219            u           0    0    orders_oid_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.orders_oid_seq OWNED BY public."Orders"."OID";
          public          postgres    false    218            �            1259    16738    review_RID_seq    SEQUENCE     �   CREATE SEQUENCE public."review_RID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public."review_RID_seq";
       public          postgres    false    232            v           0    0    review_RID_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public."review_RID_seq" OWNED BY public."Review"."RID";
          public          postgres    false    231            �           2604    16501    Discount DID    DEFAULT     p   ALTER TABLE ONLY public."Discount" ALTER COLUMN "DID" SET DEFAULT nextval('public.discount_did_seq'::regclass);
 ?   ALTER TABLE public."Discount" ALTER COLUMN "DID" DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    16433    Members MID    DEFAULT     n   ALTER TABLE ONLY public."Members" ALTER COLUMN "MID" SET DEFAULT nextval('public.members_mid_seq'::regclass);
 >   ALTER TABLE public."Members" ALTER COLUMN "MID" DROP DEFAULT;
       public          postgres    false    216    215    216            �           2604    16461 
   Orders OID    DEFAULT     l   ALTER TABLE ONLY public."Orders" ALTER COLUMN "OID" SET DEFAULT nextval('public.orders_oid_seq'::regclass);
 =   ALTER TABLE public."Orders" ALTER COLUMN "OID" DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    16742 
   Review RID    DEFAULT     n   ALTER TABLE ONLY public."Review" ALTER COLUMN "RID" SET DEFAULT nextval('public."review_RID_seq"'::regclass);
 =   ALTER TABLE public."Review" ALTER COLUMN "RID" DROP DEFAULT;
       public          postgres    false    231    232    232            j          0    16714    Applies 
   TABLE DATA           1   COPY public."Applies" ("OID", "DID") FROM stdin;
    public          postgres    false    230   �o       ]          0    16438    Credit_card 
   TABLE DATA           O   COPY public."Credit_card" ("Number", "CMID", "Expiry_date", "CVV") FROM stdin;
    public          postgres    false    217   �o       a          0    16498    Discount 
   TABLE DATA           �   COPY public."Discount" ("DID", "Disc_code", "Disc_value", "Disc_type", "Disc_name", "Policy_desc", "Disc_desc", "Max_usage") FROM stdin;
    public          postgres    false    221   �o       f          0    16663    Item_Amount 
   TABLE DATA           P   COPY public."Item_Amount" ("AID", "PID", "Amount_type", "Quantity") FROM stdin;
    public          postgres    false    226   p       \          0    16430    Members 
   TABLE DATA           �   COPY public."Members" ("MID", "F_name", "L_name", "Password", "Gender", "Email", "Phone", "Birth", "Address", "Reg_date", "A_flag", "S_flag", "C_flag") FROM stdin;
    public          postgres    false    216   ,p       i          0    16698    Order_Item_Amount 
   TABLE DATA           ;   COPY public."Order_Item_Amount" ("AID", "OID") FROM stdin;
    public          postgres    false    229   Ip       _          0    16458    Orders 
   TABLE DATA           �   COPY public."Orders" ("OID", "MID", "Credit_num", "Time", "Ship_address", "Ship_fee", "Status", "Pay_method", "Tot_price") FROM stdin;
    public          postgres    false    219   fp       b          0    16603    Product 
   TABLE DATA           �   COPY public."Product" ("PID", "SMID", "SpEvent_ID", "Name", "Desc", "Author", "Price", "Stock_quantity", "Category", "Product_pict", "Sale_count") FROM stdin;
    public          postgres    false    222   �p       l          0    16739    Review 
   TABLE DATA           }   COPY public."Review" ("RID", "PID", "CMID", "Time", "Rate", "Rev_text", "Rev_picture", "Rev_video", "Reply_RID") FROM stdin;
    public          postgres    false    232   �p       d          0    16637 	   Seasoning 
   TABLE DATA           F   COPY public."Seasoning" ("DID", "Valid_to", "Valid_from") FROM stdin;
    public          postgres    false    224   �p       e          0    16648    Shipping 
   TABLE DATA           ;   COPY public."Shipping" ("DID", "Min_purchase") FROM stdin;
    public          postgres    false    225   �p       g          0    16673    ShoppingCart_Item 
   TABLE DATA           J   COPY public."ShoppingCart_Item" ("SCID", "CMID", "Tot_price") FROM stdin;
    public          postgres    false    227   �p       h          0    16683    ShoppingCart_Item_Amount 
   TABLE DATA           O   COPY public."ShoppingCart_Item_Amount" ("AID", "SCID", "Selected") FROM stdin;
    public          postgres    false    228   q       c          0    16626    Special_event 
   TABLE DATA           J   COPY public."Special_event" ("DID", "Valid_to", "Valid_from") FROM stdin;
    public          postgres    false    223   1q       w           0    0    discount_did_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.discount_did_seq', 1, false);
          public          postgres    false    220            x           0    0    members_mid_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.members_mid_seq', 1, false);
          public          postgres    false    215            y           0    0    orders_oid_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.orders_oid_seq', 1, false);
          public          postgres    false    218            z           0    0    review_RID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."review_RID_seq"', 1, false);
          public          postgres    false    231            �           2606    16718    Applies Applies_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public."Applies"
    ADD CONSTRAINT "Applies_pkey" PRIMARY KEY ("OID", "DID");
 B   ALTER TABLE ONLY public."Applies" DROP CONSTRAINT "Applies_pkey";
       public            postgres    false    230    230            �           2606    16667    Item_Amount Item_Amount_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Item_Amount"
    ADD CONSTRAINT "Item_Amount_pkey" PRIMARY KEY ("AID");
 J   ALTER TABLE ONLY public."Item_Amount" DROP CONSTRAINT "Item_Amount_pkey";
       public            postgres    false    226            �           2606    16702 (   Order_Item_Amount Order_Item_Amount_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public."Order_Item_Amount"
    ADD CONSTRAINT "Order_Item_Amount_pkey" PRIMARY KEY ("AID");
 V   ALTER TABLE ONLY public."Order_Item_Amount" DROP CONSTRAINT "Order_Item_Amount_pkey";
       public            postgres    false    229            �           2606    16609    Product Product_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY ("PID");
 B   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_pkey";
       public            postgres    false    222            �           2606    16642    Seasoning Seasoning_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Seasoning"
    ADD CONSTRAINT "Seasoning_pkey" PRIMARY KEY ("DID");
 F   ALTER TABLE ONLY public."Seasoning" DROP CONSTRAINT "Seasoning_pkey";
       public            postgres    false    224            �           2606    16652    Shipping Shipping_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Shipping"
    ADD CONSTRAINT "Shipping_pkey" PRIMARY KEY ("DID");
 D   ALTER TABLE ONLY public."Shipping" DROP CONSTRAINT "Shipping_pkey";
       public            postgres    false    225            �           2606    16687 6   ShoppingCart_Item_Amount ShoppingCart_Item_Amount_pkey 
   CONSTRAINT     {   ALTER TABLE ONLY public."ShoppingCart_Item_Amount"
    ADD CONSTRAINT "ShoppingCart_Item_Amount_pkey" PRIMARY KEY ("AID");
 d   ALTER TABLE ONLY public."ShoppingCart_Item_Amount" DROP CONSTRAINT "ShoppingCart_Item_Amount_pkey";
       public            postgres    false    228            �           2606    16677 (   ShoppingCart_Item ShoppingCart_Item_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."ShoppingCart_Item"
    ADD CONSTRAINT "ShoppingCart_Item_pkey" PRIMARY KEY ("SCID");
 V   ALTER TABLE ONLY public."ShoppingCart_Item" DROP CONSTRAINT "ShoppingCart_Item_pkey";
       public            postgres    false    227            �           2606    16631     Special_event Special_event_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."Special_event"
    ADD CONSTRAINT "Special_event_pkey" PRIMARY KEY ("DID");
 N   ALTER TABLE ONLY public."Special_event" DROP CONSTRAINT "Special_event_pkey";
       public            postgres    false    223            �           2606    16442    Credit_card creditcard_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public."Credit_card"
    ADD CONSTRAINT creditcard_pkey PRIMARY KEY ("Number");
 G   ALTER TABLE ONLY public."Credit_card" DROP CONSTRAINT creditcard_pkey;
       public            postgres    false    217            �           2606    16507    Discount discount_disc_code_key 
   CONSTRAINT     c   ALTER TABLE ONLY public."Discount"
    ADD CONSTRAINT discount_disc_code_key UNIQUE ("Disc_code");
 K   ALTER TABLE ONLY public."Discount" DROP CONSTRAINT discount_disc_code_key;
       public            postgres    false    221            �           2606    16505    Discount discount_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Discount"
    ADD CONSTRAINT discount_pkey PRIMARY KEY ("DID");
 B   ALTER TABLE ONLY public."Discount" DROP CONSTRAINT discount_pkey;
       public            postgres    false    221            �           2606    16437    Members members_email_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT members_email_key UNIQUE ("Email");
 E   ALTER TABLE ONLY public."Members" DROP CONSTRAINT members_email_key;
       public            postgres    false    216            �           2606    16435    Members members_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Members"
    ADD CONSTRAINT members_pkey PRIMARY KEY ("MID");
 @   ALTER TABLE ONLY public."Members" DROP CONSTRAINT members_pkey;
       public            postgres    false    216            �           2606    16466    Orders orders_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT orders_pkey PRIMARY KEY ("OID");
 >   ALTER TABLE ONLY public."Orders" DROP CONSTRAINT orders_pkey;
       public            postgres    false    219            �           2606    16746    Review review_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT review_pkey PRIMARY KEY ("RID");
 >   ALTER TABLE ONLY public."Review" DROP CONSTRAINT review_pkey;
       public            postgres    false    232            �           2606    16724    Applies Applies_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Applies"
    ADD CONSTRAINT "Applies_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public."Applies" DROP CONSTRAINT "Applies_DID_fkey";
       public          postgres    false    4773    230    221            �           2606    16719    Applies Applies_OID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Applies"
    ADD CONSTRAINT "Applies_OID_fkey" FOREIGN KEY ("OID") REFERENCES public."Orders"("OID") ON UPDATE CASCADE ON DELETE CASCADE;
 F   ALTER TABLE ONLY public."Applies" DROP CONSTRAINT "Applies_OID_fkey";
       public          postgres    false    4769    219    230            �           2606    16668     Item_Amount Item_Amount_PID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Item_Amount"
    ADD CONSTRAINT "Item_Amount_PID_fkey" FOREIGN KEY ("PID") REFERENCES public."Product"("PID") ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public."Item_Amount" DROP CONSTRAINT "Item_Amount_PID_fkey";
       public          postgres    false    222    4775    226            �           2606    16703 ,   Order_Item_Amount Order_Item_Amount_AID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Order_Item_Amount"
    ADD CONSTRAINT "Order_Item_Amount_AID_fkey" FOREIGN KEY ("AID") REFERENCES public."Item_Amount"("AID") ON UPDATE CASCADE ON DELETE CASCADE;
 Z   ALTER TABLE ONLY public."Order_Item_Amount" DROP CONSTRAINT "Order_Item_Amount_AID_fkey";
       public          postgres    false    226    4783    229            �           2606    16708 ,   Order_Item_Amount Order_Item_Amount_OID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Order_Item_Amount"
    ADD CONSTRAINT "Order_Item_Amount_OID_fkey" FOREIGN KEY ("OID") REFERENCES public."Orders"("OID") ON UPDATE CASCADE ON DELETE CASCADE;
 Z   ALTER TABLE ONLY public."Order_Item_Amount" DROP CONSTRAINT "Order_Item_Amount_OID_fkey";
       public          postgres    false    229    4769    219            �           2606    16610    Product Product_SMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_SMID_fkey" FOREIGN KEY ("SMID") REFERENCES public."Members"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 G   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_SMID_fkey";
       public          postgres    false    222    4765    216            �           2606    16615    Product Product_SpEvent_ID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_SpEvent_ID_fkey" FOREIGN KEY ("SpEvent_ID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 M   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_SpEvent_ID_fkey";
       public          postgres    false    221    222    4773            �           2606    16643    Seasoning Seasoning_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Seasoning"
    ADD CONSTRAINT "Seasoning_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Seasoning" DROP CONSTRAINT "Seasoning_DID_fkey";
       public          postgres    false    224    4773    221            �           2606    16653    Shipping Shipping_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Shipping"
    ADD CONSTRAINT "Shipping_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public."Shipping" DROP CONSTRAINT "Shipping_DID_fkey";
       public          postgres    false    225    4773    221            �           2606    16688 :   ShoppingCart_Item_Amount ShoppingCart_Item_Amount_AID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."ShoppingCart_Item_Amount"
    ADD CONSTRAINT "ShoppingCart_Item_Amount_AID_fkey" FOREIGN KEY ("AID") REFERENCES public."Item_Amount"("AID") ON UPDATE CASCADE ON DELETE CASCADE;
 h   ALTER TABLE ONLY public."ShoppingCart_Item_Amount" DROP CONSTRAINT "ShoppingCart_Item_Amount_AID_fkey";
       public          postgres    false    228    4783    226            �           2606    16693 ;   ShoppingCart_Item_Amount ShoppingCart_Item_Amount_SCID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."ShoppingCart_Item_Amount"
    ADD CONSTRAINT "ShoppingCart_Item_Amount_SCID_fkey" FOREIGN KEY ("SCID") REFERENCES public."ShoppingCart_Item"("SCID") ON UPDATE CASCADE ON DELETE CASCADE;
 i   ALTER TABLE ONLY public."ShoppingCart_Item_Amount" DROP CONSTRAINT "ShoppingCart_Item_Amount_SCID_fkey";
       public          postgres    false    228    227    4785            �           2606    16678 -   ShoppingCart_Item ShoppingCart_Item_CMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."ShoppingCart_Item"
    ADD CONSTRAINT "ShoppingCart_Item_CMID_fkey" FOREIGN KEY ("CMID") REFERENCES public."Members"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 [   ALTER TABLE ONLY public."ShoppingCart_Item" DROP CONSTRAINT "ShoppingCart_Item_CMID_fkey";
       public          postgres    false    216    4765    227            �           2606    16632 $   Special_event Special_event_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Special_event"
    ADD CONSTRAINT "Special_event_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 R   ALTER TABLE ONLY public."Special_event" DROP CONSTRAINT "Special_event_DID_fkey";
       public          postgres    false    221    4773    223            �           2606    16443     Credit_card creditcard_cmid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Credit_card"
    ADD CONSTRAINT creditcard_cmid_fkey FOREIGN KEY ("CMID") REFERENCES public."Members"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 L   ALTER TABLE ONLY public."Credit_card" DROP CONSTRAINT creditcard_cmid_fkey;
       public          postgres    false    4765    217    216            �           2606    16472    Orders orders_credit_num_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT orders_credit_num_fkey FOREIGN KEY ("Credit_num") REFERENCES public."Credit_card"("Number") ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public."Orders" DROP CONSTRAINT orders_credit_num_fkey;
       public          postgres    false    4767    217    219            �           2606    16467    Orders orders_mid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Orders"
    ADD CONSTRAINT orders_mid_fkey FOREIGN KEY ("MID") REFERENCES public."Members"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 B   ALTER TABLE ONLY public."Orders" DROP CONSTRAINT orders_mid_fkey;
       public          postgres    false    219    216    4765            �           2606    16752    Review review_CMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "review_CMID_fkey" FOREIGN KEY ("CMID") REFERENCES public."Members"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 E   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "review_CMID_fkey";
       public          postgres    false    4765    216    232            �           2606    16747    Review review_PID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "review_PID_fkey" FOREIGN KEY ("PID") REFERENCES public."Product"("PID") ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "review_PID_fkey";
       public          postgres    false    4775    232    222            j      x������ � �      ]      x������ � �      a      x������ � �      f      x������ � �      \      x������ � �      i      x������ � �      _      x������ � �      b      x������ � �      l      x������ � �      d      x������ � �      e      x������ � �      g      x������ � �      h      x������ � �      c      x������ � �     