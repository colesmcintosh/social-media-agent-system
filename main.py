from agents import Agent, Runner, WebSearchTool, function_tool
from openai import OpenAI
from pydantic import BaseModel, Field
import base64

class ImageFile(BaseModel):
    filename: str = Field(..., description="The name of the image file")

class Post(BaseModel):
    post: str = Field(..., description="The post to be used for the social media post")
    image_filename: str = Field(..., description="The name of the image file")

@function_tool
def generate_image(prompt: str) -> str:
    client = OpenAI()
    result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
    )

    image_base64 = result.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    response = client.responses.parse(
    model="gpt-4.1-nano",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "generate a filename for the image, do not include any special characters or the extension, just the name."},
            {
                "type": "input_image",
                "image_url": f"data:image/jpeg;base64,{image_base64}",
            },
        ],
    }],
    text_format=ImageFile
  )

    # Save the image to a file
    with open(f"{response.output_parsed.filename}.png", "wb") as f:
        f.write(image_bytes)

    return f"{response.output_parsed.filename}.png"

research_agent = Agent(
    name="Research Agent",
    instructions="""
    You are a social media researcher.
    """,
    model="gpt-4.1-mini",
    tools=[
        WebSearchTool(),
    ],
)

social_media_agent = Agent(
    name="Social Media Agent",
    instructions="""
    You are a social media content creation expert. You will be given a trend or topic to research, and you will need to generate a post and an image for the post.
    """,
    tools=[
        research_agent.as_tool(
            tool_name="research_agent",
            tool_description="Research current trends and topics for Social Media",
        ),
        generate_image,
    ],
    model="gpt-4.1-mini",
    output_type=Post,
)


if __name__ == "__main__":
    result = Runner.run_sync(social_media_agent, input="AI in the medical field")

    final_output = result.final_output


    with open("result.md", "w") as f:
        f.write(final_output.post)
        # Skip a line and add the image
        f.write("\n\n")
        f.write(f"![{final_output.image_filename}]({final_output.image_filename})")
