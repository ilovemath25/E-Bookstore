from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def combined_features(product):
   try: return f"{product.Name} {product.Category or ''} {product.Desc or ''} {product.Author or ''}"
   except: pass
   try: return f"{product.get('Name', '')} {product.get('Category', '')} {product.get('Desc', '')} {product.get('Author', '')}"
   except: pass

def search_books(query, products):
   product_features = [combined_features(product) for product in products]
   product_features.append(query)
   cv = CountVectorizer()
   count_matrix = cv.fit_transform(product_features)
   cosine_sim = cosine_similarity(count_matrix)
   query_sim = cosine_sim[-1, :-1]
   scored_products = [
      (score, product) for score, product in zip(query_sim, products) 
      if score >= 0.1
   ]
   scored_products.sort(key=lambda x: x[0], reverse=True)
   return [product for _, product in scored_products]