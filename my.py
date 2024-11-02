from toolkit.job import get_job

import runpod
from runpod.serverless.utils import rp_upload, rp_cleanup
from runpod.serverless.utils.rp_validator import validate

INPUT_SCHEMA = {
    'test': {
        'type': str,
        'required': False,
    }
}

def start_training(job):
    '''
    Generate an image from text using your Model
    '''
    job_input = job["input"]

    # Input validation
    validated_input = validate(job_input, INPUT_SCHEMA)

    if 'errors' in validated_input:
        return {"error": validated_input['errors']}
    job_input = validated_input['validated_input']

    job = get_job('tmp/1da5c2fa-47db-48b0-82eb-7e599df3ff34-marie-3.yaml')
    job.run()
    job.cleanup()

    print(f"Training completed successfully.")

    # image_urls = _save_and_upload_images(output, job['id'])

    results = {
        "thisisa": "test"
    }

    return results

runpod.serverless.start({"handler": start_training})

# def _save_and_upload_images(images, job_id):
#     os.makedirs(f"/{job_id}", exist_ok=True)
#     image_urls = []
#     for index, image in enumerate(images):
#         image_path = os.path.join(f"/{job_id}", f"{index}.png")
#         image.save(image_path)

#         if os.environ.get('BUCKET_ENDPOINT_URL', False):
#             image_url = rp_upload.upload_image(job_id, image_path)
#             image_urls.append(image_url)
#         else:
#             with open(image_path, "rb") as image_file:
#                 image_data = base64.b64encode(
#                     image_file.read()).decode("utf-8")
#                 image_urls.append(f"data:image/png;base64,{image_data}")

#     rp_cleanup.clean([f"/{job_id}"])
#     return image_urls