import streamlit as st


@st.dialog("Support Us")
def support_modal():
    st.write(
        """
        <div style="display: flex; align-items: center;">
            <span style="margin-right: 1rem;">❤️</span>
            <span>
                Support the developer: <a href="https://buymeacoffee.com/pooria7" target="_blank">Buy me a coffee</a>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        <div style="display: flex; align-items: center; margine-top: 1rem; margin-bottom: 3rem;">
            <span style="margin-right: 1rem;">❤️</span>
            <span>
                Follow the builder on X: <a href="https://x.com/PooriaTaghdiri" target="_blank">Pooria's X</a>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )
