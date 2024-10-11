# Streamlit PDF Embeddings & Question Answering App

This Streamlit app provides two endpoints:
1. **PDF Embedding Creation**: Upload a PDF file, and the app will create embeddings using Azure GPT-4 and store them for future use.
2. **Question Answering**: Users can ask questions based on the PDF's content, and the app will answer using conversation memory for context.

## Features
- **PDF Embedding Creation**: Generates embeddings for each page of the PDF to prepare for question-answering tasks.
- **Question Answering with Conversation Memory**: Keeps track of the conversation context to provide better, more coherent responses.
- **Powered by Azure GPT-4**: Leverages Azure's GPT-4 for generating accurate answers based on the provided PDF.
- **MongoDB for Storage**: Embeddings and conversation history are stored in MongoDB for fast retrieval and persistent conversations.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Tanzir11/Streamlit-qna.git>
   cd <Streamlit-qna>
   ```

2. **Install dependencies:**
   Use the provided `requirements.txt` file to install the necessary Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables:**
   Create a `.env` file in the root directory with the following information:
   ```bash
   AZURE_OPENAI_API_KEY=<your_azure_openai_api_key>
   AZURE_OPENAI_API_ENDPOINT=<your_azure_openai_endpoint>
   MONGODB_URI=<your_mongodb_uri>
   openai_api_version=<"openai-api-version">
   NAMESPACE=<"NameSpace">
   INDEX_NAME=<"Index_name">
   ```

## Running the App

Once the dependencies are installed and the environment variables are configured, run the Streamlit app:

```bash
streamlit run app.py
```

This will start a local server where you can interact with the app.

## Usage

### 1. **Upload PDF for Embedding**
- In the "Upload PDF" section, upload a PDF file. The app will process the file and generate embeddings for the text.

### 2. **Ask Questions**
- After uploading the PDF and generating embeddings, navigate to the "Ask Questions" section.
- Enter your question related to the PDF content, and the app will use Azure GPT-4 to generate a response, considering the previous conversation context.

### Key Libraries Used
- **[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)**: For PDF processing and extracting text.
- **[pymongo](https://pypi.org/project/pymongo/)**: For storing embeddings and conversation memory in MongoDB.
- **[langchain-community](https://pypi.org/project/langchain-community/)** & **[langchain-openai](https://pypi.org/project/langchain-openai/)**: For managing conversation memory and handling the interaction with Azure GPT-4.
- **[Streamlit](https://streamlit.io/)**: For building the app's UI.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: For managing environment variables securely.

## Future Improvements
- **Multi-language support** for PDFs.
- **Advanced conversation context management** with longer conversation history retention.

## License
This project is licensed under the MIT License.

---

### Contributions

Feel free to fork this project and submit pull requests to contribute to its improvement!
