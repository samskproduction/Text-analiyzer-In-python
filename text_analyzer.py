import streamlit as st

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def text_analyzer():
    st.title("📊 Text Analyzer")
    
    text = st.text_area("Enter a paragraph:", "")
    
    if "search_word" not in st.session_state:
        st.session_state.search_word = ""
    if "replace_word" not in st.session_state:
        st.session_state.replace_word = ""

    search_word = st.text_input("Enter a word to search for:", st.session_state.search_word, key="search")
    replace_word = st.text_input("Enter a word to replace it with:", st.session_state.replace_word, key="replace")
    
    if st.button("Submit"):
        if not text.strip():
            st.warning("Please enter a valid paragraph.")
            return
        
        st.session_state.search_word = search_word
        st.session_state.replace_word = replace_word

        words = text.split()
        total_words = len(words)
        total_chars = len(text)
        vowels_count = count_vowels(text)

        st.write(f"**Total Words:** {total_words}")
        st.write(f"**Total Characters:** {total_chars}")
        st.write(f"**Number of Vowels:** {vowels_count}")

        modified_text = text.replace(st.session_state.search_word, st.session_state.replace_word) if st.session_state.search_word else text
        st.subheader("Modified Paragraph:")
        st.write(modified_text)

        st.subheader("Paragraph in Uppercase:")
        st.write(text.upper())

        st.subheader("Paragraph in Lowercase:")
        st.write(text.lower())

        contains_python = "Python" in text
        st.write(f"**Does the paragraph contain 'Python'?** {'Yes' if contains_python else 'No'}")

        avg_word_length = total_chars / total_words if total_words > 0 else 0
        st.write(f"**Average Word Length:** {round(avg_word_length, 2)}")

if __name__ == "__main__":
    text_analyzer()