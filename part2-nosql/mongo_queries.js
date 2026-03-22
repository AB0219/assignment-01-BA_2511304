// OP1: insertMany() — insert all 3 documents
db.products.insertMany([
  {
    product_id: "ELEC001",
    name: "Samsung Smart TV 55 inch",
    category: "Electronics",
    price: 55000,
    brand: "Samsung",
    warranty_years: 2,
    specifications: {
      resolution: "4K",
      display_type: "LED",
      voltage: "220V"
    },
    features: ["Smart TV", "WiFi", "Bluetooth"],
    ratings: { average: 4.5, reviews_count: 1200 }
  },
  {
    product_id: "CLOT001",
    name: "Men's Cotton T-Shirt",
    category: "Clothing",
    price: 799,
    brand: "Levis",
    size: ["S", "M", "L", "XL"],
    material: "Cotton",
    color: ["Black", "White", "Blue"],
    care_instructions: {
      wash: "Machine wash",
      dry: "Do not tumble dry"
    },
    ratings: { average: 4.2, reviews_count: 300 }
  },
  {
    product_id: "GROC001",
    name: "Organic Milk 1L",
    category: "Groceries",
    price: 60,
    brand: "Amul",
    expiry_date: new Date("2024-12-30"),
    weight: "1L",
    nutritional_info: {
      calories: 150,
      protein: "8g",
      fat: "8g"
    },
    storage_instructions: "Keep refrigerated",
    ratings: { average: 4.6, reviews_count: 800 }
  }
]);

// OP2: find Electronics with price > 20000
db.products.find({
  category: "Electronics",
  price: { $gt: 20000 }
});

// OP3: find Groceries expiring before 2025-01-01
db.products.find({
  category: "Groceries",
  expiry_date: { $lt: new Date("2025-01-01") }
});

// OP4: updateOne() — add discount_percent
db.products.updateOne(
  { product_id: "ELEC001" },
  { $set: { discount_percent: 10 } }
);

// OP5: createIndex() — index on category
db.products.createIndex({ category: 1 });

// Explanation:
// This index improves query performance when filtering products by category,
// such as Electronics or Groceries, by avoiding full collection scans.
