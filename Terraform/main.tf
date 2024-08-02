provider "google" {
  project = ""
}

resource "google_bigquery_table" "products" {
  dataset_id                  = "steph_dataset"
  table_id                    = "products"

  schema = <<EOF
[
  {
    "name": "ProductKey",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The Product ID"
  },
  {
    "name": "Product",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The Product name"
  },
  {
    "name": "StandardCost",
    "type": "FLOAT",
    "mode": "REQUIRED",
    "description": "The Product cost"
  },
  {
    "name": "Colour",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The Product colour"
  },
  {
    "name": "Subcategory",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The Product subcategory"
  },
    {
    "name": "Category",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The Product category"
  },
    {
    "name": "Background Colour Format",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The background colour format"
  },
    {
    "name": "Font Colour Format",
    "type": "STRING",
    "mode": "REQUIRED",
    "description": "The font colour format"
  }
]
EOF

}
