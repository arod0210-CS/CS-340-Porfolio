from pymongo import MongoClient


class AnimalShelter:
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        """Initialize the MongoDB connection."""

        host = "localhost"
        port = 27017
        database_name = "aac"
        collection_name = "animals"

        # Connect to MongoDB using the supplied username and password.
        self.client = MongoClient(
            f"mongodb://{username}:{password}@{host}:{port}"
        )

        # Access the AAC database and animals collection.
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None:
            try:
                result = self.collection.insert_one(data)
                return result.acknowledged
            except Exception as error:
                print(f"Create error: {error}")
                return False

        return False

    def read(self, query):
        """Find documents that match the supplied query."""

        if query is not None:
            try:
                cursor = self.collection.find(query)
                return list(cursor)
            except Exception as error:
                print(f"Read error: {error}")
                return []

        return []

    def update(self, query, new_values):
        """Update documents that match the supplied query."""

        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": new_values}
                )
                return result.modified_count
            except Exception as error:
                print(f"Update error: {error}")
                return 0

        return 0

    def delete(self, query):
        """Delete documents that match the supplied query."""

        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as error:
                print(f"Delete error: {error}")
                return 0

        return 0