# AI-Powered Web Search Agent

An intelligent web search agent that uses GPT-4 and browser automation to find detailed information online. This project specifically helps users find information about products, prices, and market research.

## 🚀 Features

- Automated web searching and data extraction
- Natural language task processing
- Detailed result summaries
- Browser automation for real-time data gathering
- Support for complex search queries
- GIF generation of search history

## 🛠️ Installation

1. Clone the repository:

```bash
git clone
cd ai-web-search-agent
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_api_key_here
```

## 📝 Usage

Run the main script with your search query:

```python
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    try:
        agent = Agent(
            task="Your search query here",
            llm=ChatOpenAI(
                model="gpt-4-1106-preview",
                openai_api_key=os.getenv("OPENAI_API_KEY")
            ),
        )
        result = await agent.run()
        print(result)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

asyncio.run(main())
```

## 🔑 Environment Variables

The following environment variables are required:

- `OPENAI_API_KEY`: Your OpenAI API key

## 📋 Example Queries

The agent can handle various types of queries, such as:

- Market research for products
- Price comparisons
- Product availability
- Detailed product information
- Market trends and analysis

Example:

```python
task="""find the best cars in dubai which
        i can buy which is under 1 million and have a
        good market to sell it as well"""
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool uses browser automation and AI. Please ensure you comply with the terms of service of any websites you interact with and use responsibly.

## 🙏 Acknowledgments

- OpenAI for GPT-4
- Langchain for the ChatOpenAI implementation
- Browser-use library for web automation

## 📞 Support

For support, please open an issue in the GitHub repository.
