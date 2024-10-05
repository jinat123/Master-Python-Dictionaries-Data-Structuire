# Product 1
product_object1 = {
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 750,
    "stock": 50,
    "supplier email": "supplier1@gmail.com"
}

# Product 2
product_object2 = {
    "id": 2,
    "name": "Desk Chair",
    "category": "Furniture",
    "price": 100,
    "stock": 200,
    "supplier email": "supplier2@gmail.com"
}

# Product 3
product_object3 = {
    "id": 3,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 200,
    "stock": 150,
    "supplier email": "supplier3@gmail.com"
}

# Product 4
product_object4 = {
    "id": 4,
    "name": "Notebook",
    "category": "Stationery",
    "price": 5,
    "stock": 500,
    "supplier email": "supplier4@gmail.com"
}

# Product 5
product_object5 = {
    "id": 5,
    "name": "Running Shoes",
    "category": "Apparel",
    "price": 80,
    "stock": 100,
    "supplier email": "supplier5@gmail.com"
}

products = [product_object1, product_object2, product_object3, product_object4, product_object5]

for product in products:
    print(f"id: {product.get('id')}, category: {product.get('category')}, price: {product.get('price')}, stock: {product.get('stock')}, supplier email: {product.get('supplier email')}")

# Employee 1
employee_object1 = {
    "id": 1,
    "name": "John Doe",
    "department": "Sales",
    "age": 30,
    "email": "john.doe@company.com"
}

# Employee 2
employee_object2 = {
    "id": 2,
    "Name": "Jane Smith",
    "Department": "Human Resources",
    "Age": 25,
    "email": "jane.smith@company.com"
}

# Employee 3
employee_object3 = {
    "id": 3,
    "name": "Mark John",
    "department": "IT",
    "age": 40,
    "email": "mark.johnson@company.com"
}

# employee 4
employee_object4 = {
    "id": 4,
    "name": "Lisa Wong",
    "department": "Finance",
    "age": 28,
    "email": "lisa.wong@company.com"
}

# Employee 5
employee_object5 = {
    "id": 5,
    "name": "Paul Mcdonald",
    "department": "Finance",
    "age": 35,
    "email": "paul.mcdonald@company.com"
}

employees = [employee_object1, employee_object2, employee_object3, employee_object4, employee_object5]

for employee in employees:
    print(f"id: {employee.get('id')}, name: {employee.get('name')}, department: {employee.get('department')}, age: {employee.get('age')}, email: {employee.get('email')}")

# Books 1
books_object1 = {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction",
    "published year": 1925,
    "isbn": "978-0743273565",
    "stock": 20,
    "price": 15.99
}

# Books 2
books_object2 = {
    "id": 2,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "published year": 1960,
    "isbn": "978-0060935467",
    "stock": 35,
    "price": 10.99
}

# Books 3
books_object3 = {
    "id": 3,
    "title": "1894",
    "author": "	George Orwell",
    "genre": "Dystopian",
    "published year": 1949,
    "isbn": "978-0451524935",
    "stock": 40,
    "price": 9.99
}

# Books 4
books_object4 = {
    "id": 4,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "genre": "Fiction",
    "published year": 1951,
    "isbn": "978-0316769488",
    "stock": 25,
    "price": 8.99
}
# Books 5
books_object5 = {
    "id": 5,
    "title": "A Brief History of Time",
    "author": "Stephen Hawking",
    "genre": "Non-Fiction",
    "published year": 1988,
    "isbn": "978-0553380163",
    "stock": 10,
    "price": 18.99
}

books = [books_object1, books_object2, books_object3, books_object4, books_object5]

for book in books:
    print(f"id: {book.get('id')}, title: {book.get('title')}, author: {book.get('author')}, genre: {book.get('genre')}, published year: {book.get('published year')}, isbn: {book.get('isbn')}, stock: {book.get('stock')}, price: {book.get('price')}")

# University 1
university_object1 = {
    "id": 1,
    "name": "University of the Philippines",
    "location": "Quezon City",
    "established year": 1908,
    "type": "Public",
    "Website": "www.up.edu.ph"
}

# University 2
university_object2 = {
    "id": 2,
    "name": "Ateneo De Manila University",
    "location": "Quezon City",
    "established year": 1859,
    "type": "Private",
    "Website": "www.ateneo.edu"
}

# University 3
university_object3 = {
    "id": 3,
    "name": "De La Salle University",
    "location": "Manila",
    "established year": 1911,
    "type": "Private",
    "Website": "www.dlsu.edu.ph"
}

# University 4
university_object4 = {
    "id": 4,
    "name": "University of Santo Tomas",
    "location": "Manila",
    "established year": 1611,
    "type": "Public",
    "Website": "www.ust.edu.ph"
}

# University 5
university_object5 = {
    "id": 5,
    "name": "Polytechnic University of the Philippines",
    "location": "Manila",
    "established year": 1904,
    "type": "Public",
    "Website": "www.pup.edu.ph"
}

universities = [university_object1, university_object2, university_object3, university_object4, university_object5]

for university in universities:
    print(f"id: {university.get('id')}, name: {university.get('name')}, location: {university.get('location')}, established year: {university.get('established year')}, type: {university.get('type')}, Website: {university.get('Website')}")

# Restaurant 1
restaurant_object1 = {
    "id": 1,
    "name": "Vikings Luxury Buffet",
    "location": "Pasay City",
    "cuisine type": "Buffet",
    "established year": 2011,
    "website or contact": "www.vikings.ph"
}

# Restaurant 2
restaurant_object2 = {
    "id": 2,
    "name": "Antonio's Restaurant",
    "location": "Tagaytay",
    "cuisine type": "Fine Dining",
    "established year": 2002,
    "website or contact": "www.antoniosrestaurant.ph"
}

# Restaurant 3
restaurant_object3 = {
    "id": 3,
    "name": "Mesa Filipino Moderne",
    "location": "Makati City",
    "cuisine type": "Filipino",
    "established year": 2009,
    "website or contact": "	www.mesa.ph"
}

# Restaurant 4
restaurant_object4 = {
    "id": 4,
    "name": "Manam Comfort Filipino",
    "location": "Quezon City",
    "cuisine type": "Filipino",
    "established year": 2013,
    "website or contact": "www.manam.ph"
}

# Restaurant 5
restaurant_object5 = {
    "id": 5,
    "name": "Ramen Nagi",
    "location": "Various Locations",
    "cuisine type": "Japanese",
    "established year": 2013,
    "website or contact": "www.ramennagi.com.ph"
}

restaurants = [restaurant_object1, restaurant_object2, restaurant_object3, restaurant_object4, restaurant_object5]

for restaurant in restaurants:
    print(f"id: {restaurant.get('id')}, name: {restaurant.get('name')}, location: {restaurant.get('location')}, cuisine type: {restaurant.get('cuisine type')}, established year: {restaurant.get('established year')}, website or contact: {restaurant.get('website or contact')}")