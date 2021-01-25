
# About
- Git Repository is used for a Heroku APP which helps with database and corresponding REST APIs.
- Made for Hack Cambridge 2021 - Agrio app [Github](https://github.com/VasundharaAgarwal/HackCam21) [Devpost](https://devpost.com/software/agriconnect-l36kei)

# Endpoints
- https://farmer-api-cam.herokuapp.com/api/v1/
- Uses PostgreSQL with POS.GIS backend on Heroku.

# REST ENDPOINT
- "crop_search": "https://farmer-api-cam.herokuapp.com/api/v1/crop_search/",
- "seller_search": "https://farmer-api-cam.herokuapp.com/api/v1/seller_search/",
- "user_search": "https://farmer-api-cam.herokuapp.com/api/v1/user_search/",
- "cart_search": "https://farmer-api-cam.herokuapp.com/api/v1/cart_search/",
- "history_search": "https://farmer-api-cam.herokuapp.com/api/v1/history_search/",
- "img_search": "https://farmer-api-cam.herokuapp.com/api/v1/img_search/"

# Usage
- Use normal query searches with GET and POST requests

# Supports
- Geographical Sorting of shops with distance
- Transactional Updates to Inventory when items are purchased.
- Holds User's Purchase History
- Hold Seller's Information
- Image Endpoint for data analysis updates.

# Further Improvements
- Authentication and Encryption of data transfer
- Move to NoSQL from Relational database.
