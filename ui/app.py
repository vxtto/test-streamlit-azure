import streamlit as st
import time
import io

def process_file(file):
    # Example file processing with a progress update
    total_steps = 10
    for step in range(total_steps):
        time.sleep(0.1)  # Simulating long processing
        progress = (step + 1) / total_steps
        yield progress
    processed_file = io.BytesIO()  # Simulating processed file
    processed_file.write(file.getbuffer())
    processed_file.seek(0)
    return processed_file

def main():
    st.title("Minimal Streamlit App")
    
    uploaded_file = st.file_uploader("Choose a file")
    
    if uploaded_file is not None:
        # Display progress bar
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        # Process file and update progress
        processed_file = None
        for progress in process_file(uploaded_file):
            progress_bar.progress(progress)
            progress_text.text(f'Processing... {progress*100:.2f}%')
        
        progress_bar.progress(100)
        progress_text.text('Processing complete.')
        
        # Enable download button once processing is complete
        if processed_file:
            st.download_button(
                label="Download Processed File",
                data=processed_file,
                file_name="processed_file",
                mime="application/octet-stream",
                key='download-file'
            )

if __name__ == "__main__":
    main()
