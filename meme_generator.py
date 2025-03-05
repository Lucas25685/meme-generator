import json
import base64
import boto3
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4569",
    aws_access_key_id="S3RVER",
    aws_secret_access_key="S3RVER",
    region_name="us-east-1",
)

BUCKET_NAME = os.getenv("S3_BUCKET", "s3memestorage-dev")

def handler(event, context):
    try:
        body = json.loads(event["body"])
        image_data = base64.b64decode(body["image"])
        text_top = body["text-top"]
        text_bottom = body["text-bottom"]

        image = Image.open(BytesIO(image_data))
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype("impact.ttf", 50)
        except IOError:
            font = ImageFont.load_default()

        image_width, image_height = image.size

        for text, y_position in [(text_top, 5), (text_bottom, image_height - 70)]:
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]

            x_position = (image_width - text_width) // 2

            # Draw border
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    draw.text((x_position + dx, y_position + dy), text, font=font, fill="white")

            # Draw text
            draw.text((x_position, y_position), text, font=font, fill="black")

        output_buffer = BytesIO()
        image.save(output_buffer, format="PNG")
        output_buffer.seek(0)

        file_name = f"meme_{text_top}_{text_bottom}.png"
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=output_buffer,
            ContentType="image/png",
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Image uploaded", "url": f"http://localhost:4569/{BUCKET_NAME}/{file_name}"}),
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}