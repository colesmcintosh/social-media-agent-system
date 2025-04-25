# Social Media Content Agent System

A sophisticated multi-agent system that combines specialized AI agents to create engaging social media content. The system leverages a Research Agent for gathering accurate, up-to-date information and a Social Media Agent for crafting compelling posts with AI-generated visuals.

## Features

- Automated research on any given topic using GPT-4.1-mini and web search
- AI-powered content generation for social media posts
- Automatic image generation matching the post content
- Markdown output with integrated images
- Hashtag generation for better social media engagement

## Multi-Agent Architecture

The system employs a hierarchical multi-agent approach:

1. Research Agent (Information Gathering)
   - Conducts web searches to gather current information
   - Analyzes and synthesizes data from multiple sources
   - Provides structured research output to the Social Media Agent

2. Social Media Agent (Content Creation)
   - Processes research data into engaging social media content
   - Generates relevant hashtags for better reach
   - Creates matching images using AI
   - Ensures content aligns with platform best practices

## Prerequisites

- Python 3.9+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/social-media-agent.git
cd social-media-agent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

Run the main script with a topic:

```bash
python main.py
```

The script will:
1. Research the given topic using the Research Agent
2. Generate a social media post with relevant hashtags
3. Create a matching image using AI
4. Save the output in a markdown file with the embedded image

## Project Structure

- `main.py` - Main script containing the agent setup and execution logic
- `agents.py` - Contains the agent classes and tools (not included in repo)
- `result.md` - Output file containing the generated content
- Generated images are saved in the root directory

## Configuration

The project uses two specialized agents:

1. Research Agent
   - Uses GPT-4.1-mini model
   - Equipped with web search capabilities
   - Focuses on gathering and validating information
   - Provides structured data for content creation
   
2. Social Media Agent
   - Uses GPT-4.1-mini model
   - Orchestrates the content creation process
   - Can invoke the Research Agent for information gathering
   - Generates images using GPT-image-1 model
   - Handles final content formatting and optimization

## Output Format

The generated content is saved in markdown format with:
- Main post content optimized for social media engagement
- Strategically selected hashtags for maximum reach
- AI-generated image that complements the post content

## Benefits of Multi-Agent Approach

- **Specialized Expertise**: Each agent focuses on its core competency
- **Enhanced Research Quality**: Dedicated agent for information gathering
- **Better Content Creation**: Specialized agent for social media optimization
- **Scalable Architecture**: Easy to add new agents for additional functionality
- **Modular Design**: Agents can be updated or replaced independently

## Example Output

See `result.md` for an example of generated content, which includes:
- Researched and fact-checked information
- Engaging social media post format
- Relevant hashtags
- AI-generated complementary image

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)