
########################################################################################
# === IMPORTS [beg] === #

# import os
# import uuid

import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px

import matplotlib.pyplot as plt
import numpy as np

from src.utils import (
    initiate_session_state,
    show_progression,
    display_gauge_chart,
    display_radar_chart,
    display_score_sheet,
    display_score_sheet_for_section,
    display_model_score_evolution,
    compute_score,
    include_footer,
    clicked,
    is_input_invalid
)

from app_pages import (
    home_page,
    ml_analysis_page
)


# === IMPORTS [end] === #
########################################################################################




#######################################################################################
# === INIT [beg] === #

st.set_page_config(
    page_title="ML Workflow Analysis",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:blhyver@eulidia.com',
        'Report a bug': "mailto:blhyver@eulidia.com",
        'About': "# TBD"
    }
)

with open('content/style.css', 'r') as f:
    css = f.read()

# with open('wave.css', 'r') as f:
#     css = f.read()

st.markdown(
    f'<style>{css}</style>',
    unsafe_allow_html=True
)

initiate_session_state()

# home_page.view()

# === INIT [end] === #
#######################################################################################


#######################################################################################
# === CORE [beg] === #


with st.sidebar:
    # st.title("Méthode d'évaluation de workflow ML / IA")

    # st.sidebar.image(
    #     "./content/eulidia_logo.png",
    #     use_container_width=True
    # )

    # st.subheader("by Eulidia")
    # st.title("ML/AI Workflow Analyst")
    st.markdown("<h1 style='text-align: center'>Score Cards</h1>", unsafe_allow_html=True)
    
    _, _col_m, _ = st.columns([1, 1, 1])
    with _col_m:
        st.markdown("<h4 style='text-align: center'>by</h4>", unsafe_allow_html=True)
        st.image(
            "./content/eulidia_blue.png",
            use_container_width=True
        )

    st.divider()

    st.markdown("<h3 style='text-align: center'>Score Cards</h3>", unsafe_allow_html=True)

    sc_ml_button = st.button(
        "ML / AI",
        type="primary",
        use_container_width=True,
        on_click=clicked,
        args=[0]
    )

    sc_genai_button = st.button(
        "GenAI",
        type="primary",
        use_container_width=True,
        on_click=clicked,
        args=[4]
    )

    score_cards_button = st.button(
        "BI / DA",
        type="primary",
        use_container_width=True,
        on_click=clicked,
        args=[5]
    )

    # model_sheet = st.button(
    #     "Update specific sheet",
    #     type="primary",
    #     use_container_width=True,
    #     disabled=is_input_invalid(),
    #     on_click=clicked,
    #     args=[1]
    # )

    # score_cards_button = st.button(
    #     "Home page",
    #     type="primary",
    #     use_container_width=True,
    #     on_click=clicked,
    #     args=[0]
    # )


    # st.write("Follow completion")
    # show_progression()



# if st.session_state.clicked[0] or :

# if st.session_state.clicked[1]:
# if st.session_state["validate_workflow"] and not st.session_state.clicked[0]:
#     ml_analysis_page.view()

if not st.session_state.clicked[2]:
    # st.session_state["validate_workflow"] = True
    # st.session_state["model_evaluation_df"]["filled"] = False
    # st.session_state["model_evaluation_df"]["Score"] = 0
    # st.write(len(st.session_state["model_evaluation_df"]["filled"].sum()))
    # if st.session_state["model_evaluation_df"]["filled"].sum() != len(st.session_state["model_evaluation_df"]):
    #     st.warning("test")
    # else:
    # st.session_state["radio_button_create_or_retrieve"] = None
    st.session_state["project_name"] = ""
    st.session_state["workflow_name"] = ""
    st.session_state["workflow_version"] = ""
    home_page.view()

elif st.session_state.clicked[2]:
    ml_analysis_page.view()

# ---

# _col_l, _ = st.columns([0.5, 9])
# with _col_l:
#     # st.write()
#     st.image(
#         "./content/eulidia_logo.png",
#         use_container_width=False
#     )

# st.title("Evaluation de workflow ML / IA")

# add_vertical_space(2)


# === CORE [end] === #
########################################################################################

include_footer()

# ##################################################################################### #

#                                # === END OF FILE === #                                #

# ##################################################################################### #