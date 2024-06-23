{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cbedd5c8-fa53-4ace-9890-683adce922f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib\n",
    "\n",
    "# Load the trained model\n",
    "model = joblib.load('model_file.pkl')\n",
    "\n",
    "# Define the expected feature names used during training\n",
    "expected_features = ['movement_reactions', 'mentality_composure', 'passing', 'dribbling', 'physic',\n",
    "                     'attacking_short_passing', 'mentality_vision', 'skill_long_passing', 'shooting',\n",
    "                     'power_shot_power', 'age']\n",
    "\n",
    "def main():\n",
    "    st.title(\"FIFA Player Rating Predictor\")\n",
    "    html_temp = \"\"\"\n",
    "    <div style=\"background:#025246 ;padding:10px\">\n",
    "    <h2 style=\"color:white;text-align:center;\">Player Rating Predictor App </h2>\n",
    "    </div>\n",
    "    \"\"\"\n",
    "    st.markdown(html_temp, unsafe_allow_html=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b121a4c-60b8-44c4-aa47-6ed82f5a870d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
