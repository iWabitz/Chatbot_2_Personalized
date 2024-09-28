import datetime
import streamlit as st
def generate_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    minute = current_time.minute

    day = current_time.weekday()

    current_time = datetime.datetime.now()

    return current_time
