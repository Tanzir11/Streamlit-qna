# from modules.Scrapper import EnbeddingGenerator
# from modules.ChatBot import QuestionAnswer
# from fastapi import FastAPI

# app = FastAPI()

# app.include_router(EnbeddingGenerator)
# app.include_router(QuestionAnswer)

# if __name__ == "__main__":
#     import uvicorn
#     # Replace '68.183.90.40' with your actual server IP address
#     uvicorn.run("app:app", host="68.183.90.40", port=8000, reload=True)
import streamlit as st
from modules.Scrapper import upload_resume
from modules.ChatBot import Chat_bot

def main():
    st.title("Embedding Generator and ChatBot")
    
    # Option selection for the user
    option = st.selectbox("Choose a service", ["Embedding Generator", "Question Answer"])

    if option == "Embedding Generator":
        st.subheader("Embedding Generator")

        # File uploader for the embedding generator
        uploaded_file = st.file_uploader("Upload a file for embedding generation", type=["txt", "pdf", "docx"])
        
        if uploaded_file is not None:
            st.write("File uploaded successfully!")
            if st.button("Generate Embedding"):
                # Pass the file to the Embedding Generator logic
                # Assume EnbeddingGenerator can take a file as input
                result = upload_resume(uploaded_file)
                st.write("Generated Embedding: ", result)

    elif option == "Question Answer":
        st.subheader("ChatBot - Question Answer")
        user_question = st.text_input("Ask a question:")
        session_id = st.text_input("Session Id( For Chat History)")
        if st.button("Get Answer"):
            # Call your Question Answer logic here
            answer = Chat_bot(user_question,session_id)
            st.write("Answer: ", answer)

if __name__ == "__main__":
    main()
