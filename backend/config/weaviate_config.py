from weaviate import Client

# creating a client object to interact with the Weaviate server. It specifies the scheme (http) and the host
# (localhost:8080) where the Weaviate server is running. This client object can be used to perform
# various operations such as creating classes, adding data, querying data, etc. */


weaviate_client = Client("http://localhost:8080")

# The `schemaConfig` object is defining the schema for a class called "Meme" in the Weaviate server.
# It specifies the properties and data types of the class. 
schema_config = {
        class: "Hush",
        vectorizer: "img2vec-neural",
        vectorIndexType: "hnsw",
        moduleConfig: {
            "img2vec-neural": {
            imageFields: ["image"],
            },
        },
        properties: [
            {
            name: "image",
            dataType: ["blob"],
            },
            {
            name: "text",
            dataType: ["string"],
            },
        ],
        }

# create a class with specified config

def create_weaviate(schema_config):
  weaviate_client.schema.create_class(schema_config)


# def storePhoto(image_url):

#   with open(image_url, "rb") as image_file:
#     image_data = image_file.read()

#   image_base64 = image_data.encode("base64").decode()

#   weaviate_client.data.create(
#     class_name="Hush",
#     properties={
#       "image": image_base64,
#       "text": image_url.split("/")[-1].split(".")[0]
#     }
#   )

# def search_similar(sample_image_path):
#   with open(sample_image_path, "rb") as sample_image_file:
#     sample_image_data = sample_image_file.read()

#     sample_image_base64 = sample_image_data.encode("base64").decode()

#     result = weaviate.client.query.get(
#       class_name="Hush",
#       fields=["image"],
#       near_image={"image": sample_image_base64},
#       limit=1
#     )
#     result_image_base64 = result["data"]["Get"]["Hush"][0]["image"]

#     with open("result.jpg", "wb") as result_image_file: 
#       result_image_file.write(result_image_base64.encode("base64"))


# "http://res.cloudinary.com/dlw7wjlp3/image/upload/v1705452114/obgnyi7emkpac0lktdhx.jpg"

