import streamlit as st 
import numpy as np
import tensorflow as tf
import os,urllib
import librosa


def main():
  selected_box = st.sidebar.selectbox('Choose an option...',('Emotion Recognition','view source code'))
