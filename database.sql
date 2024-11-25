PGDMP                    
    |         
   ebookstore    16.1    16.0 T    h           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            i           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            j           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            k           1262    16398 
   ebookstore    DATABASE     �   CREATE DATABASE ebookstore WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE ebookstore;
                postgres    false            r           1247    16819 	   Disc_type    TYPE     c   CREATE TYPE public."Disc_type" AS ENUM (
    'Shipping',
    'Seasonings',
    'Special Events'
);
    DROP TYPE public."Disc_type";
       public          postgres    false            c           1247    16758    Gender    TYPE     O   CREATE TYPE public."Gender" AS ENUM (
    'Male',
    'Female',
    'Other'
);
    DROP TYPE public."Gender";
       public          postgres    false            `           1247    16659    Item_amount_type    TYPE     S   CREATE TYPE public."Item_amount_type" AS ENUM (
    'Order',
    'ShoppingCart'
);
 %   DROP TYPE public."Item_amount_type";
       public          postgres    false            �           1247    16904 	   Line_type    TYPE     L   CREATE TYPE public."Line_type" AS ENUM (
    'Order',
    'ShoppingCart'
);
    DROP TYPE public."Line_type";
       public          postgres    false            l           1247    16785    Order_status    TYPE     n   CREATE TYPE public."Order_status" AS ENUM (
    'Processing',
    'Shipping',
    'Received',
    'Closed'
);
 !   DROP TYPE public."Order_status";
       public          postgres    false            ]           1247    16490 	   disc_type    TYPE     a   CREATE TYPE public.disc_type AS ENUM (
    'Shipping',
    'Seasonings',
    'Special Events'
);
    DROP TYPE public.disc_type;
       public          postgres    false            W           1247    16422    gender    TYPE     M   CREATE TYPE public.gender AS ENUM (
    'male',
    'female',
    'other'
);
    DROP TYPE public.gender;
       public          postgres    false            Z           1247    16449    order_status    TYPE     l   CREATE TYPE public.order_status AS ENUM (
    'Received',
    'Processing',
    'Shipping',
    'Closed'
);
    DROP TYPE public.order_status;
       public          postgres    false            �            1259    16774    Credit_card    TABLE     �   CREATE TABLE public."Credit_card" (
    "Number" character(16) NOT NULL,
    "CMID" integer NOT NULL,
    "Expiry_date" date NOT NULL,
    "CVV" character(3) NOT NULL
);
 !   DROP TABLE public."Credit_card";
       public         heap    postgres    false            �            1259    16826    Discount    TABLE     O  CREATE TABLE public."Discount" (
    "DID" integer NOT NULL,
    "OID" integer,
    "Disc_code" character varying(20) NOT NULL,
    "Disc_value" numeric NOT NULL,
    "Disc_type" public."Disc_type" NOT NULL,
    "Disc_name" character varying(50) NOT NULL,
    "Policy_desc" character varying(1000) NOT NULL,
    "Max_usage" integer
);
    DROP TABLE public."Discount";
       public         heap    postgres    false    882            �            1259    16825    Discount_DID_seq    SEQUENCE     �   CREATE SEQUENCE public."Discount_DID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."Discount_DID_seq";
       public          postgres    false    221            l           0    0    Discount_DID_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public."Discount_DID_seq" OWNED BY public."Discount"."DID";
          public          postgres    false    220            �            1259    16909 	   Item_line    TABLE     �   CREATE TABLE public."Item_line" (
    "LID" integer NOT NULL,
    "PID" integer NOT NULL,
    "OID" integer,
    "SCID" integer,
    "Line_type" public."Line_type" NOT NULL,
    "Quantity" integer NOT NULL
);
    DROP TABLE public."Item_line";
       public         heap    postgres    false    903            �            1259    16766    Member    TABLE     �  CREATE TABLE public."Member" (
    "MID" integer NOT NULL,
    "F_name" character varying(15) NOT NULL,
    "L_name" character varying(15),
    "Password" character varying(15) NOT NULL,
    "Gender" public."Gender" NOT NULL,
    "Email" character varying(100) NOT NULL,
    "Phone" character(10),
    "Birth" date,
    "Address" character varying(200),
    "Reg_date" date NOT NULL,
    "A_flag" boolean NOT NULL,
    "S_flag" boolean NOT NULL,
    "C_flag" boolean NOT NULL
);
    DROP TABLE public."Member";
       public         heap    postgres    false    867            �            1259    16765    Member_MID_seq    SEQUENCE     �   CREATE SEQUENCE public."Member_MID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public."Member_MID_seq";
       public          postgres    false    216            m           0    0    Member_MID_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public."Member_MID_seq" OWNED BY public."Member"."MID";
          public          postgres    false    215            �            1259    16794    Order    TABLE     *  CREATE TABLE public."Order" (
    "OID" integer NOT NULL,
    "CMID" integer NOT NULL,
    "SMID" integer NOT NULL,
    "Credit_num" character(1),
    "Time" timestamp without time zone NOT NULL,
    "Ship_address" character varying(200) NOT NULL,
    "Ship_fee" integer NOT NULL,
    "Status" public."Order_status" NOT NULL,
    "Pay_method" character varying NOT NULL,
    "Tot_price" integer,
    CONSTRAINT "Order_Pay_method_check" CHECK ((("Pay_method")::text = ANY ((ARRAY['Credit card'::character varying, 'COD'::character varying])::text[])))
);
    DROP TABLE public."Order";
       public         heap    postgres    false    876            �            1259    16793    Order_OID_seq    SEQUENCE     �   CREATE SEQUENCE public."Order_OID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public."Order_OID_seq";
       public          postgres    false    219            n           0    0    Order_OID_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public."Order_OID_seq" OWNED BY public."Order"."OID";
          public          postgres    false    218            �            1259    16875    Product    TABLE     �  CREATE TABLE public."Product" (
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
       public         heap    postgres    false            �            1259    16874    Product_PID_seq    SEQUENCE     �   CREATE SEQUENCE public."Product_PID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."Product_PID_seq";
       public          postgres    false    226            o           0    0    Product_PID_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."Product_PID_seq" OWNED BY public."Product"."PID";
          public          postgres    false    225            �            1259    16930    Review    TABLE     K  CREATE TABLE public."Review" (
    "RID" integer NOT NULL,
    "PID" integer NOT NULL,
    "MID" integer NOT NULL,
    "Time" timestamp without time zone NOT NULL,
    "Rate" integer NOT NULL,
    "Rev_text" character varying(500),
    "Rev_picture" character varying,
    "Rev_video" character varying,
    "Reply_RID" integer
);
    DROP TABLE public."Review";
       public         heap    postgres    false            �            1259    16929    Review_RID_seq    SEQUENCE     �   CREATE SEQUENCE public."Review_RID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public."Review_RID_seq";
       public          postgres    false    230            p           0    0    Review_RID_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public."Review_RID_seq" OWNED BY public."Review"."RID";
          public          postgres    false    229            �            1259    16853 	   Seasoning    TABLE     �   CREATE TABLE public."Seasoning" (
    "DID" integer NOT NULL,
    "Valid_to" date NOT NULL,
    "Valid_from" date NOT NULL,
    CONSTRAINT valid_date_range CHECK (("Valid_to" >= "Valid_from"))
);
    DROP TABLE public."Seasoning";
       public         heap    postgres    false            �            1259    16864    Shipping    TABLE     [   CREATE TABLE public."Shipping" (
    "DID" integer NOT NULL,
    "Min_Purchase" integer
);
    DROP TABLE public."Shipping";
       public         heap    postgres    false            �            1259    16893    ShoppingCart_item    TABLE        CREATE TABLE public."ShoppingCart_item" (
    "SCID" integer NOT NULL,
    "CMID" integer,
    "Tot_price" integer NOT NULL
);
 '   DROP TABLE public."ShoppingCart_item";
       public         heap    postgres    false            �            1259    16841    Special_event    TABLE     �   CREATE TABLE public."Special_event" (
    "DID" integer NOT NULL,
    "Valid_to" date NOT NULL,
    "Valid_from" date NOT NULL,
    CONSTRAINT valid_date_range CHECK (("Valid_to" >= "Valid_from"))
);
 #   DROP TABLE public."Special_event";
       public         heap    postgres    false            �           2604    16829    Discount DID    DEFAULT     r   ALTER TABLE ONLY public."Discount" ALTER COLUMN "DID" SET DEFAULT nextval('public."Discount_DID_seq"'::regclass);
 ?   ALTER TABLE public."Discount" ALTER COLUMN "DID" DROP DEFAULT;
       public          postgres    false    221    220    221            �           2604    16769 
   Member MID    DEFAULT     n   ALTER TABLE ONLY public."Member" ALTER COLUMN "MID" SET DEFAULT nextval('public."Member_MID_seq"'::regclass);
 =   ALTER TABLE public."Member" ALTER COLUMN "MID" DROP DEFAULT;
       public          postgres    false    215    216    216            �           2604    16797 	   Order OID    DEFAULT     l   ALTER TABLE ONLY public."Order" ALTER COLUMN "OID" SET DEFAULT nextval('public."Order_OID_seq"'::regclass);
 <   ALTER TABLE public."Order" ALTER COLUMN "OID" DROP DEFAULT;
       public          postgres    false    218    219    219            �           2604    16878    Product PID    DEFAULT     p   ALTER TABLE ONLY public."Product" ALTER COLUMN "PID" SET DEFAULT nextval('public."Product_PID_seq"'::regclass);
 >   ALTER TABLE public."Product" ALTER COLUMN "PID" DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    16933 
   Review RID    DEFAULT     n   ALTER TABLE ONLY public."Review" ALTER COLUMN "RID" SET DEFAULT nextval('public."Review_RID_seq"'::regclass);
 =   ALTER TABLE public."Review" ALTER COLUMN "RID" DROP DEFAULT;
       public          postgres    false    229    230    230            X          0    16774    Credit_card 
   TABLE DATA           O   COPY public."Credit_card" ("Number", "CMID", "Expiry_date", "CVV") FROM stdin;
    public          postgres    false    217   k       \          0    16826    Discount 
   TABLE DATA           �   COPY public."Discount" ("DID", "OID", "Disc_code", "Disc_value", "Disc_type", "Disc_name", "Policy_desc", "Max_usage") FROM stdin;
    public          postgres    false    221   <k       c          0    16909 	   Item_line 
   TABLE DATA           [   COPY public."Item_line" ("LID", "PID", "OID", "SCID", "Line_type", "Quantity") FROM stdin;
    public          postgres    false    228   Yk       W          0    16766    Member 
   TABLE DATA           �   COPY public."Member" ("MID", "F_name", "L_name", "Password", "Gender", "Email", "Phone", "Birth", "Address", "Reg_date", "A_flag", "S_flag", "C_flag") FROM stdin;
    public          postgres    false    216   vk       Z          0    16794    Order 
   TABLE DATA           �   COPY public."Order" ("OID", "CMID", "SMID", "Credit_num", "Time", "Ship_address", "Ship_fee", "Status", "Pay_method", "Tot_price") FROM stdin;
    public          postgres    false    219   �k       a          0    16875    Product 
   TABLE DATA           �   COPY public."Product" ("PID", "SMID", "SpEvent_ID", "Name", "Desc", "Author", "Price", "Stock_quantity", "Category", "Product_pict", "Sale_count") FROM stdin;
    public          postgres    false    226   �k       e          0    16930    Review 
   TABLE DATA           |   COPY public."Review" ("RID", "PID", "MID", "Time", "Rate", "Rev_text", "Rev_picture", "Rev_video", "Reply_RID") FROM stdin;
    public          postgres    false    230   �k       ^          0    16853 	   Seasoning 
   TABLE DATA           F   COPY public."Seasoning" ("DID", "Valid_to", "Valid_from") FROM stdin;
    public          postgres    false    223   �k       _          0    16864    Shipping 
   TABLE DATA           ;   COPY public."Shipping" ("DID", "Min_Purchase") FROM stdin;
    public          postgres    false    224   l       b          0    16893    ShoppingCart_item 
   TABLE DATA           J   COPY public."ShoppingCart_item" ("SCID", "CMID", "Tot_price") FROM stdin;
    public          postgres    false    227   $l       ]          0    16841    Special_event 
   TABLE DATA           J   COPY public."Special_event" ("DID", "Valid_to", "Valid_from") FROM stdin;
    public          postgres    false    222   Al       q           0    0    Discount_DID_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Discount_DID_seq"', 1, false);
          public          postgres    false    220            r           0    0    Member_MID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Member_MID_seq"', 1, false);
          public          postgres    false    215            s           0    0    Order_OID_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public."Order_OID_seq"', 1, false);
          public          postgres    false    218            t           0    0    Product_PID_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."Product_PID_seq"', 1, false);
          public          postgres    false    225            u           0    0    Review_RID_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public."Review_RID_seq"', 1, false);
          public          postgres    false    229            �           2606    16778    Credit_card Credit_card_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public."Credit_card"
    ADD CONSTRAINT "Credit_card_pkey" PRIMARY KEY ("Number");
 J   ALTER TABLE ONLY public."Credit_card" DROP CONSTRAINT "Credit_card_pkey";
       public            postgres    false    217            �           2606    16835    Discount Discount_Disc_code_key 
   CONSTRAINT     e   ALTER TABLE ONLY public."Discount"
    ADD CONSTRAINT "Discount_Disc_code_key" UNIQUE ("Disc_code");
 M   ALTER TABLE ONLY public."Discount" DROP CONSTRAINT "Discount_Disc_code_key";
       public            postgres    false    221            �           2606    16833    Discount Discount_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Discount"
    ADD CONSTRAINT "Discount_pkey" PRIMARY KEY ("DID");
 D   ALTER TABLE ONLY public."Discount" DROP CONSTRAINT "Discount_pkey";
       public            postgres    false    221            �           2606    16913    Item_line Item_line_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Item_line"
    ADD CONSTRAINT "Item_line_pkey" PRIMARY KEY ("LID");
 F   ALTER TABLE ONLY public."Item_line" DROP CONSTRAINT "Item_line_pkey";
       public            postgres    false    228            �           2606    16773    Member Member_Email_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_Email_key" UNIQUE ("Email");
 E   ALTER TABLE ONLY public."Member" DROP CONSTRAINT "Member_Email_key";
       public            postgres    false    216            �           2606    16771    Member Member_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Member"
    ADD CONSTRAINT "Member_pkey" PRIMARY KEY ("MID");
 @   ALTER TABLE ONLY public."Member" DROP CONSTRAINT "Member_pkey";
       public            postgres    false    216            �           2606    16802    Order Order_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_pkey" PRIMARY KEY ("OID");
 >   ALTER TABLE ONLY public."Order" DROP CONSTRAINT "Order_pkey";
       public            postgres    false    219            �           2606    16882    Product Product_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_pkey" PRIMARY KEY ("PID");
 B   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_pkey";
       public            postgres    false    226            �           2606    16937    Review Review_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "Review_pkey" PRIMARY KEY ("RID");
 @   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "Review_pkey";
       public            postgres    false    230            �           2606    16858    Seasoning Seasoning_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public."Seasoning"
    ADD CONSTRAINT "Seasoning_pkey" PRIMARY KEY ("DID");
 F   ALTER TABLE ONLY public."Seasoning" DROP CONSTRAINT "Seasoning_pkey";
       public            postgres    false    223            �           2606    16868    Shipping Shipping_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public."Shipping"
    ADD CONSTRAINT "Shipping_pkey" PRIMARY KEY ("DID");
 D   ALTER TABLE ONLY public."Shipping" DROP CONSTRAINT "Shipping_pkey";
       public            postgres    false    224            �           2606    16897 (   ShoppingCart_item ShoppingCart_item_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public."ShoppingCart_item"
    ADD CONSTRAINT "ShoppingCart_item_pkey" PRIMARY KEY ("SCID");
 V   ALTER TABLE ONLY public."ShoppingCart_item" DROP CONSTRAINT "ShoppingCart_item_pkey";
       public            postgres    false    227            �           2606    16846     Special_event Special_event_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public."Special_event"
    ADD CONSTRAINT "Special_event_pkey" PRIMARY KEY ("DID");
 N   ALTER TABLE ONLY public."Special_event" DROP CONSTRAINT "Special_event_pkey";
       public            postgres    false    222            �           2606    16779 !   Credit_card Credit_card_CMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Credit_card"
    ADD CONSTRAINT "Credit_card_CMID_fkey" FOREIGN KEY ("CMID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 O   ALTER TABLE ONLY public."Credit_card" DROP CONSTRAINT "Credit_card_CMID_fkey";
       public          postgres    false    217    216    4767            �           2606    16836    Discount Discount_OID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Discount"
    ADD CONSTRAINT "Discount_OID_fkey" FOREIGN KEY ("OID") REFERENCES public."Order"("OID") ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public."Discount" DROP CONSTRAINT "Discount_OID_fkey";
       public          postgres    false    4771    221    219            �           2606    16919    Item_line Item_line_OID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Item_line"
    ADD CONSTRAINT "Item_line_OID_fkey" FOREIGN KEY ("OID") REFERENCES public."Order"("OID") ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Item_line" DROP CONSTRAINT "Item_line_OID_fkey";
       public          postgres    false    4771    228    219            �           2606    16914    Item_line Item_line_PID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Item_line"
    ADD CONSTRAINT "Item_line_PID_fkey" FOREIGN KEY ("PID") REFERENCES public."Product"("PID") ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Item_line" DROP CONSTRAINT "Item_line_PID_fkey";
       public          postgres    false    228    226    4783            �           2606    16924    Item_line Item_line_SCID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Item_line"
    ADD CONSTRAINT "Item_line_SCID_fkey" FOREIGN KEY ("SCID") REFERENCES public."ShoppingCart_item"("SCID") ON UPDATE CASCADE ON DELETE CASCADE;
 K   ALTER TABLE ONLY public."Item_line" DROP CONSTRAINT "Item_line_SCID_fkey";
       public          postgres    false    4785    227    228            �           2606    16803    Order Order_CMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_CMID_fkey" FOREIGN KEY ("CMID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public."Order" DROP CONSTRAINT "Order_CMID_fkey";
       public          postgres    false    4767    216    219            �           2606    16813    Order Order_Credit_num_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_Credit_num_fkey" FOREIGN KEY ("Credit_num") REFERENCES public."Credit_card"("Number") ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public."Order" DROP CONSTRAINT "Order_Credit_num_fkey";
       public          postgres    false    219    4769    217            �           2606    16808    Order Order_SMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Order"
    ADD CONSTRAINT "Order_SMID_fkey" FOREIGN KEY ("SMID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 C   ALTER TABLE ONLY public."Order" DROP CONSTRAINT "Order_SMID_fkey";
       public          postgres    false    4767    216    219            �           2606    16883    Product Product_SMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_SMID_fkey" FOREIGN KEY ("SMID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 G   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_SMID_fkey";
       public          postgres    false    4767    226    216            �           2606    16888    Product Product_SpEvent_ID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Product"
    ADD CONSTRAINT "Product_SpEvent_ID_fkey" FOREIGN KEY ("SpEvent_ID") REFERENCES public."Special_event"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 M   ALTER TABLE ONLY public."Product" DROP CONSTRAINT "Product_SpEvent_ID_fkey";
       public          postgres    false    222    4777    226            �           2606    16943    Review Review_MID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "Review_MID_fkey" FOREIGN KEY ("MID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "Review_MID_fkey";
       public          postgres    false    4767    216    230            �           2606    16938    Review Review_PID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "Review_PID_fkey" FOREIGN KEY ("PID") REFERENCES public."Product"("PID") ON UPDATE CASCADE ON DELETE CASCADE;
 D   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "Review_PID_fkey";
       public          postgres    false    230    226    4783            �           2606    16948    Review Review_Reply_RID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Review"
    ADD CONSTRAINT "Review_Reply_RID_fkey" FOREIGN KEY ("Reply_RID") REFERENCES public."Review"("RID") ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Review" DROP CONSTRAINT "Review_Reply_RID_fkey";
       public          postgres    false    4789    230    230            �           2606    16859    Seasoning Seasoning_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Seasoning"
    ADD CONSTRAINT "Seasoning_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public."Seasoning" DROP CONSTRAINT "Seasoning_DID_fkey";
       public          postgres    false    4775    223    221            �           2606    16869    Shipping Shipping_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Shipping"
    ADD CONSTRAINT "Shipping_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public."Shipping" DROP CONSTRAINT "Shipping_DID_fkey";
       public          postgres    false    221    4775    224            �           2606    16898 -   ShoppingCart_item ShoppingCart_item_CMID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."ShoppingCart_item"
    ADD CONSTRAINT "ShoppingCart_item_CMID_fkey" FOREIGN KEY ("CMID") REFERENCES public."Member"("MID") ON UPDATE CASCADE ON DELETE CASCADE;
 [   ALTER TABLE ONLY public."ShoppingCart_item" DROP CONSTRAINT "ShoppingCart_item_CMID_fkey";
       public          postgres    false    216    4767    227            �           2606    16847 $   Special_event Special_event_DID_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Special_event"
    ADD CONSTRAINT "Special_event_DID_fkey" FOREIGN KEY ("DID") REFERENCES public."Discount"("DID") ON UPDATE CASCADE ON DELETE CASCADE;
 R   ALTER TABLE ONLY public."Special_event" DROP CONSTRAINT "Special_event_DID_fkey";
       public          postgres    false    4775    222    221            X      x������ � �      \      x������ � �      c      x������ � �      W      x������ � �      Z      x������ � �      a      x������ � �      e      x������ � �      ^      x������ � �      _      x������ � �      b      x������ � �      ]      x������ � �     