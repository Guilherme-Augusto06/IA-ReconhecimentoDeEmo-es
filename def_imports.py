from google.cloud import vision

def detect_faces(path):

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = (
        "UNKNOWN",
        "VERY_UNLIKELY",
        "UNLIKELY",
        "POSSIBLE",
        "LIKELY",
        "VERY_LIKELY",
    )

    print(f"Faces:{faces}")

    # for face in faces:
    #     print(f"anger: {likelihood_name[face.anger_likelihood]}")
    #     print(f"joy: {likelihood_name[face.joy_likelihood]}")
    #     print(f"surprise: {likelihood_name[face.surprise_likelihood]}")

    #     vertices = [
    #         f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
    #     ]

    #     print("face bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
