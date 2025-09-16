import streamlit as st
import prediction
import info

PAGES = {
    "Home": info,
    "Predict": prediction
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.main()

if __name__ == "__main__":
    main()
