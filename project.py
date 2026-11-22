# import streamlit as st
# import pandas as pd
# from pathlib import Path


# import joblib
# st.title('Engine Health Prediction by Aniket🤠')
# st.write('running the app')

# BASE_DIR = Path(__file__).resolve().parent
# print('looking for files in:', BASE_DIR)
# print('files in directory:', [f.name for f in BASE_DIR.iterdir()])


# model = joblib.load(BASE_DIR / 'SVC_tractor.pkl')


# if isinstance(model, list):
#     st.write("Items stored in model file:", len(model))
#     st.write("Item types:", [type(item).__name__ for item in model])
# scaler = joblib.load(BASE_DIR / 'scalers_tractor.pkl')
# expected_columns = joblib.load(BASE_DIR / 'columns_tractor.pkl')
# print("MODEL TYPE:", type(model))
# print("SCALER TYPE:", type(scaler))
# print("EXPECTED COLUMNS:", expected_columns)

# if isinstance(model, list):
#     print("ITEMS INSIDE MODEL:", [type(item).__name__ for item in model])


# brand = st.selectbox('brand', ['Mahindra', 'Swaraj', 'John Deere'])
# model_name = st.selectbox('engine_model', [
#                           '585 DI', '855 FE', 'Arjun 605', '744 FE', '5039 D', '735 FE', '5050 D', '5310'])
# rpm = st.slider('rpm', 500, 2400, 1800)
# load = st.slider('load_pct', 0, 500, 50)
# ambient_temp = st.slider('ambient_temp_c', 0, 500, 25)
# operating_hours = st.slider('operating_hours', 0, 20000, 100)
# maintenance_days_ago = st.slider('maintenance_days_ago', 0, 600, 30)
# coolant_temp = st.slider('coolant_temp_c', 0, 600, 90)
# exhaust_temp = st.slider('exhaust_temp_c', 0, 600, 400)
# oil_temp = st.slider('oil_temp_c', 0, 700, 100)
# oil_pressure_bar = st.slider('oil_pressure_bar', 0, 10, 1)
# vibration_rms_mm_s = st.slider('vibration_rms_mm_s', 0, 10, 1)
# fuel_rate_lph = st.slider('fuel_rate_lph', 0, 50, 5)

# if st.button('Predict'):
#     # Create a raw input dictionary
#     raw_input = {
#         'brand' + brand: 1,
#         'engine_model_' + model_name: 1,
#         'rpm': rpm,
#         'load_pct': load,
#         'ambient_temp_c': ambient_temp,
#         'operating_hours': operating_hours,
#         'maintenance_days_ago': maintenance_days_ago,
#         'coolant_temp_c': coolant_temp,
#         'exhaust_temp_c': exhaust_temp,
#         'oil_temp_c': oil_temp,
#         'vibration_rms_mm_s': vibration_rms_mm_s,
#         'fuel_rate_lph': fuel_rate_lph,
#         'oil_pressure_bar': oil_pressure_bar
#     }

#     # input_df = pd.DataFrame([raw_input])
#     # for col in expected_columns:
#     #     if col not in input_df.columns:
#     #         input_df[col] = 0
#     # input_df = input_df[expected_columns]
#     # expected_features=scaler.feature_names_in_
#     # input_df=
#     # input_df.reindex(columns=expected_features, fill_value=0)

#     # input_df_scaled = scaler.transform(input_df)
#     input_df = pd.DataFrame([raw_input])

# # Match the exact columns used during model training
#     # input_df = input_df.reindex(
#     #     columns=expected_columns,
#     #     fill_value=0
#     # )
#     # st.write("Scaler expects:", list(scaler.feature_names_in_))
#     # st.write("Current input:", list(input_df.columns))
#     # st.write("Saved model expects:", list(model.feature_names_in_))
#     # numeric_features=list(scaler.feature_names_in_)
# # Scale the input
#     # Prepare numerical input for the scaler
#     numeric_features = list(scaler.feature_names_in_)

#     numeric_input = pd.DataFrame([raw_input])
#     numeric_input = numeric_input.reindex(
#         columns=numeric_features,
#         fill_value=0
#     )

#     input_df_scaled = scaler.transform(numeric_input)
#     # input_df_scaled = scaler.transform(input_df)
#     prediction = model.predict(input_df_scaled)[0]
#     if prediction == 1:
#         st.error('The engine is unlikely to have problem.🦠')
#     else:
#         st.success('The engine is likely to have problem.💚')
# import streamlit as st
# import pandas as pd

# import joblib

# model = joblib.load('SVC_tractor3.pkl')
# # print("actual model type:", repr(model))
# scaler = joblib.load('scalers_tractor3.pkl')
# expected_columns = joblib.load('columns_tractor3.pkl')


# st.title('Engine Health Prediction by Aniket🤠')
# st.markdown('This app predicts the health of a tractor engine based on various parameters. Please input the required values and click "Predict" to see the result.')
# brand = st.selectbox('brand', ['Mahindra', 'Swaraj', 'John Deere'])
# model_name = st.selectbox('engine_model', [
#                           '585 DI', '855 FE', 'Arjun 605', '744 FE', '5039 D', '735 FE', '5050 D', '5310'])
# rpm = st.slider('rpm', 500, 2400, 1800)
# load = st.slider('load_pct', 0, 500, 50)
# ambient_temp = st.slider('ambient_temp_c', 0, 500, 25)
# operating_hours = st.slider('operating_hours', 0, 20000, 100)
# maintenance_days_ago = st.slider('maintenance_days_ago', 0, 600, 30)
# coolant_temp = st.slider('coolant_temp_c', 0, 600, 90)
# exhaust_temp = st.slider('exhaust_temp_c', 0, 600, 400)
# oil_temp = st.slider('oil_temp_c', 0, 700, 100)
# vibration_rms_mm_s = st.slider('vibration_rms_mm_s', 0, 10, 1)
# fuel_rate_lph = st.slider('fuel_rate_lph', 0, 50, 5)

# if st.button('Predict'):
#     # Create a raw input dictionary
#     raw_input = {
#         'brand_' + brand: 1,
#         'engine_model_' + model_name: 1,
#         'rpm': rpm,
#         'load_pct': load,
#         'ambient_temp_c': ambient_temp,
#         'operating_hours': operating_hours,
#         'maintenance_days_ago': maintenance_days_ago,
#         'coolant_temp_c': coolant_temp,
#         'exhaust_temp_c': exhaust_temp,
#         'oil_temp_c': oil_temp,
#         'vibration_rms_mm_s': vibration_rms_mm_s,
#         'fuel_rate_lph': fuel_rate_lph
#     }

#     input_df = pd.DataFrame([raw_input])
#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0
#     input_df = input_df[expected_columns]
#     input_df_scaled = scaler.transform(input_df)
#     prediction = model.predict(input_df_scaled)[0]
#     if prediction == 1:
#         st.error('The engine is unlikely to have problem.🦠')
#     else:
#         st.success('The engine is likely to have problem.💚')

# import streamlit as st
# import pandas as pd
# import joblib

# # --------------------------------------------------
# # 1. LOAD TRAINED MODEL AND PREPROCESSING FILES
# # --------------------------------------------------

# model = joblib.load("SVC_tractor3.pkl")
# scaler = joblib.load("scalers_tractor3.pkl")
# expected_columns = joblib.load("columns_tractor3.pkl")


# # --------------------------------------------------
# # 2. DEFINE FEATURES USED DURING TRAINING
# # --------------------------------------------------

# numerical_cols = [
#     "rpm",
#     "load_pct",
#     "ambient_temp_c",
#     "operating_hours",
#     "maintenance_days_ago",
#     "coolant_temp_c",
#     "exhaust_temp_c",
#     "oil_pressure_bar",
#     "oil_temp_c",
#     "vibration_rms_mm_s",
#     "fuel_rate_lph"
# ]


# # Brand encoding
# brand_mapping = {
#     "John Deere": 0,
#     "Mahindra": 1,
#     "Swaraj": 2
# }


# # All 9 engine models from your original dataset
# engine_models = [
#     "5039 D",
#     "5050 D",
#     "5310",
#     "575 DI",
#     "585 DI",
#     "735 FE",
#     "744 FE",
#     "855 FE",
#     "Arjun 605"
# ]


# # --------------------------------------------------
# # 3. STREAMLIT INTERFACE
# # --------------------------------------------------

# st.title("Engine Health Prediction by Aniket 🤠")

# st.markdown(
#     "This app predicts the health of a tractor engine "
#     "based on various operating parameters. "
#     "Enter the required values and click Predict."
# )


# # Tractor brand
# brand = st.selectbox(
#     "Tractor Brand",
#     options=list(brand_mapping.keys())
# )


# # Engine model
# model_name = st.selectbox(
#     "Engine Model",
#     options=engine_models
# )


# # Engine parameters

# rpm = st.slider(
#     "Engine RPM",
#     500, 2400, 1800
# )

# load = st.slider(
#     "Load (%)",
#     0, 100, 50
# )

# ambient_temp = st.slider(
#     "Ambient Temperature (°C)",
#     0, 60, 25
# )

# operating_hours = st.slider(
#     "Operating Hours",
#     0, 20000, 100
# )

# maintenance_days_ago = st.slider(
#     "Days Since Last Maintenance",
#     0, 600, 30
# )

# coolant_temp = st.slider(
#     "Coolant Temperature (°C)",
#     0, 150, 90
# )

# exhaust_temp = st.slider(
#     "Exhaust Temperature (°C)",
#     0, 600, 400
# )

# oil_pressure_bar = st.slider(
#     "Oil Pressure (bar)",
#     0.0, 10.0, 3.5
# )

# oil_temp = st.slider(
#     "Oil Temperature (°C)",
#     0, 200, 100
# )

# vibration_rms_mm_s = st.slider(
#     "Vibration RMS (mm/s)",
#     0.0, 10.0, 1.0
# )

# fuel_rate = st.slider(
#     "Fuel Rate (L/h)",
#     0.0, 50.0, 5.0
# )


# # --------------------------------------------------
# # 4. PREDICTION
# # --------------------------------------------------

# if st.button("Predict Engine Health"):

#     # Create raw input dictionary

#     raw_input = {
#         "brand": brand_mapping[brand],
#         "rpm": rpm,
#         "load_pct": load,
#         "ambient_temp_c": ambient_temp,
#         "operating_hours": operating_hours,
#         "maintenance_days_ago": maintenance_days_ago,
#         "coolant_temp_c": coolant_temp,
#         "exhaust_temp_c": exhaust_temp,
#         "oil_pressure_bar": oil_pressure_bar,
#         "oil_temp_c": oil_temp,
#         "vibration_rms_mm_s": vibration_rms_mm_s,
#         "fuel_rate_lph": fuel_rate
#     }

#     input_df = pd.DataFrame([raw_input])

#     # Create engine model dummy columns

#     for col in expected_columns:

#         if col.startswith("engine_model_"):

#             input_df[col] = 0

#     # Select the chosen engine model

#     selected_dummy = "engine_model_" + model_name

#     if selected_dummy not in expected_columns:

#         st.error(
#             f"Engine model column not found: {selected_dummy}"
#         )

#         st.stop()

#     input_df[selected_dummy] = 1

#     # Match exact training columns and their order

#     input_df = input_df.reindex(
#         columns=expected_columns,
#         fill_value=0
#     )

#     # Scale only numerical features

#     input_df[numerical_cols] = scaler.transform(
#         input_df[numerical_cols]
#     )

#     # Make prediction

#     prediction = model.predict(input_df)[0]

#     # --------------------------------------------------
#     # 5. DISPLAY RESULT
#     # --------------------------------------------------

#     st.subheader("Prediction Result")

#     if prediction == 1:

#         st.success(
#             "Engine is unlikely to have a problem. 💚"
#         )

#     else:

#         st.error(
#             "Engine is likely to have a problem. "
#             "Maintenance may be required. 🦠"
#         )

# import streamlit as st
# import pandas as pd
# import joblib

# # --------------------------------------------------
# # 1. LOAD TRAINED MODEL AND PREPROCESSING FILES
# # --------------------------------------------------

# model = joblib.load("SVC_tractor3.pkl")
# scaler = joblib.load("scalers_tractor3.pkl")
# expected_columns = joblib.load("columns_tractor3.pkl")


# # --------------------------------------------------
# # 2. DEFINE TRAINING FEATURES
# # --------------------------------------------------

# numerical_cols = [
#     "rpm",
#     "load_pct",
#     "ambient_temp_c",
#     "operating_hours",
#     "maintenance_days_ago",
#     "coolant_temp_c",
#     "exhaust_temp_c",
#     "oil_pressure_bar",
#     "oil_temp_c",
#     "vibration_rms_mm_s",
#     "fuel_rate_lph"
# ]

# # Brand label encoding
# brand_mapping = {
#     "John Deere": 0,
#     "Mahindra": 1,
#     "Swaraj": 2
# }

# # All engine models from the dataset
# engine_models = [
#     "5039 D",
#     "5050 D",
#     "5310",
#     "575 DI",
#     "585 DI",
#     "735 FE",
#     "744 FE",
#     "855 FE",
#     "Arjun 605"
# ]


# # --------------------------------------------------
# # 3. STREAMLIT INTERFACE
# # --------------------------------------------------

# st.title("Engine Health Prediction by Aniket 🤠")

# st.markdown(
#     "This app predicts the health of a tractor engine "
#     "based on various operating parameters. "
#     "Enter the required values and click Predict."
# )

# brand = st.selectbox(
#     "Tractor Brand",
#     list(brand_mapping.keys())
# )

# model_name = st.selectbox(
#     "Engine Model",
#     engine_models
# )

# rpm = st.slider("RPM", 500, 2400, 1800)

# load = st.slider("Load (%)", 0, 100, 50)

# ambient_temp = st.slider(
#     "Ambient Temperature (°C)", 0, 60, 25
# )

# operating_hours = st.slider(
#     "Operating Hours", 0, 20000, 100
# )

# maintenance_days_ago = st.slider(
#     "Days Since Last Maintenance", 0, 600, 30
# )

# coolant_temp = st.slider(
#     "Coolant Temperature (°C)", 0, 150, 90
# )

# exhaust_temp = st.slider(
#     "Exhaust Temperature (°C)", 0, 600, 400
# )

# oil_pressure_bar = st.slider(
#     "Oil Pressure (bar)", 0.0, 10.0, 3.5
# )

# oil_temp = st.slider(
#     "Oil Temperature (°C)", 0, 200, 100
# )

# vibration_rms_mm_s = st.slider(
#     "Vibration RMS (mm/s)", 0.0, 10.0, 1.0
# )

# fuel_rate = st.slider(
#     "Fuel Rate (L/h)", 0.0, 50.0, 5.0
# )


# # --------------------------------------------------
# # 4. PREDICTION
# # --------------------------------------------------

# if st.button("Predict Engine Health"):

#     # Create raw input
#     raw_input = {
#         "brand": brand_mapping[brand],
#         "rpm": rpm,
#         "load_pct": load,
#         "ambient_temp_c": ambient_temp,
#         "operating_hours": operating_hours,
#         "maintenance_days_ago": maintenance_days_ago,
#         "coolant_temp_c": coolant_temp,
#         "exhaust_temp_c": exhaust_temp,
#         "oil_pressure_bar": oil_pressure_bar,
#         "oil_temp_c": oil_temp,
#         "vibration_rms_mm_s": vibration_rms_mm_s,
#         "fuel_rate_lph": fuel_rate
#     }

#     input_df = pd.DataFrame([raw_input])

#     # Create all engine model dummy columns
#     for col in expected_columns:
#         if col.startswith("engine_model_"):
#             input_df[col] = 0

#     # Select engine model
#     # 5039 D is the reference category.
#     if model_name != "5039 D":

#         selected_dummy = "engine_model_" + model_name

#         if selected_dummy not in expected_columns:
#             st.error(
#                 f"Feature not found: {selected_dummy}"
#             )
#             st.stop()

#         input_df[selected_dummy] = 1

#     # Arrange features in EXACT training order
#     input_df = input_df.reindex(
#         columns=expected_columns,
#         fill_value=0
#     )

#     # Scale only the 11 numerical features
#     input_df[numerical_cols] = scaler.transform(
#         input_df[numerical_cols]
#     )

#     # Predict
#     prediction = model.predict(input_df)[0]

#     # Display result
#     st.subheader("Prediction Result")

#     if prediction == 1:

#         st.success(
#             "The engine is unlikely to have a problem. 💚"
#         )

#     elif prediction == 0:

#         st.error(
#             "The engine is likely to have a problem. "
#             "Maintenance may be required. 🦠"
#         )

#     st.caption(
#         f"Selected tractor: {brand} - {model_name}"
#     )
# if st.button("Predict Engine Health"):

#     raw_input = {
#         "brand": brand_mapping[brand],
#         "rpm": rpm,
#         "load_pct": load,
#         "ambient_temp_c": ambient_temp,
#         "operating_hours": operating_hours,
#         "maintenance_days_ago": maintenance_days_ago,
#         "coolant_temp_c": coolant_temp,
#         "exhaust_temp_c": exhaust_temp,
#         "oil_pressure_bar": oil_pressure_bar,
#         "oil_temp_c": oil_temp,
#         "vibration_rms_mm_s": vibration_rms_mm_s,
#         "fuel_rate_lph": fuel_rate
#     }

#     input_df = pd.DataFrame([raw_input])

#     # Add engine model dummy variables
#     for col in expected_columns:
#         if col.startswith("engine_model_"):
#             input_df[col] = 0

#     # 5039 D is the reference category
#     if model_name != "5039 D":
#         selected_dummy = "engine_model_" + model_name

#         if selected_dummy not in expected_columns:
#             st.error(f"Feature not found: {selected_dummy}")
#             st.stop()

#         input_df[selected_dummy] = 1

#     # Arrange all 20 features in the exact training order
#     input_df = input_df.reindex(columns=expected_columns)

#     # Scale numerical features in the exact order used during scaler fitting
#     input_df.loc[:, numerical_cols] = scaler.transform(
#         input_df.loc[:, numerical_cols]
#     )

#     # Enforce the model's exact feature order
#     input_df = input_df.reindex(columns=model.feature_names_in_)

#     # Prediction
#     prediction = model.predict(input_df)[0]

#     st.subheader("Prediction Result")

#     if prediction == 1:
#         st.success("The engine is unlikely to have a problem. 💚")
#     elif prediction == 0:
#         st.error(
#             "The engine is likely to have a problem. Maintenance may be required. ⚠️")

#     st.caption(f"Selected tractor: {brand} - {model_name}")

# import streamlit as st
# import pandas as pd
# import joblib

# # --------------------------------------------------
# # 1. LOAD TRAINED MODEL AND PREPROCESSING FILES
# # --------------------------------------------------

# model = joblib.load("SVC_tractor3.pkl")
# scaler = joblib.load("scalers_tractor3.pkl")
# expected_columns = joblib.load("columns_tractor3.pkl")

# # Exact numerical feature order used when fitting the scaler
# numerical_cols = list(scaler.feature_names_in_)

# # Exact feature order used when fitting the SVC
# model_columns = list(model.feature_names_in_)

# # Check that the saved feature columns match the model
# if expected_columns != model_columns:
#     st.error("The saved feature columns do not match the trained SVC model.")
#     st.stop()

# # Brand encoding from LabelEncoder in your notebook
# brand_mapping = {
#     "John Deere": 0,
#     "Mahindra": 1,
#     "Swaraj": 2
# }

# # Engine models from your dataset
# engine_models = [
#     "5039 D",
#     "5050 D",
#     "5310",
#     "575 DI",
#     "585 DI",
#     "735 FE",
#     "744 FE",
#     "855 FE",
#     "Arjun 605"
# ]


# # --------------------------------------------------
# # 2. STREAMLIT PAGE
# # --------------------------------------------------

# st.set_page_config(
#     page_title="Tractor Engine Health Prediction",
#     page_icon="🚜",
#     layout="centered"
# )

# st.title("Tractor Engine Health Prediction 🚜")

# st.write(
#     "Enter the tractor details and engine operating parameters "
#     "to predict the engine condition."
# )


# # --------------------------------------------------
# # 3. USER INPUTS
# # --------------------------------------------------

# st.subheader("Tractor Details")

# brand = st.selectbox(
#     "Tractor Brand",
#     list(brand_mapping.keys())
# )

# model_name = st.selectbox(
#     "Engine Model",
#     engine_models
# )


# st.subheader("Engine Operating Parameters")

# rpm = st.slider("RPM", 500, 2400, 1800)

# load = st.slider("Load (%)", 0, 100, 50)

# ambient_temp = st.slider(
#     "Ambient Temperature (°C)", 0, 60, 25
# )

# operating_hours = st.slider(
#     "Operating Hours", 0, 20000, 100
# )

# maintenance_days_ago = st.slider(
#     "Days Since Last Maintenance", 0, 600, 30
# )

# coolant_temp = st.slider(
#     "Coolant Temperature (°C)", 0, 150, 90
# )

# exhaust_temp = st.slider(
#     "Exhaust Temperature (°C)", 0, 600, 400
# )

# oil_pressure = st.slider(
#     "Oil Pressure (bar)", 0.0, 10.0, 3.5
# )

# oil_temp = st.slider(
#     "Oil Temperature (°C)", 0, 200, 100
# )

# vibration = st.slider(
#     "Vibration RMS (mm/s)", 0.0, 10.0, 1.0
# )

# fuel_rate = st.slider(
#     "Fuel Rate (L/h)", 0.0, 50.0, 5.0
# )


# # --------------------------------------------------
# # 4. PREDICTION
# # --------------------------------------------------

# if st.button("Predict Engine Health"):

#     # Create input using the original dataset feature names
#     raw_input = {
#         "brand": brand_mapping[brand],
#         "rpm": rpm,
#         "load_pct": load,
#         "ambient_temp_c": ambient_temp,
#         "operating_hours": operating_hours,
#         "maintenance_days_ago": maintenance_days_ago,
#         "coolant_temp_c": coolant_temp,
#         "exhaust_temp_c": exhaust_temp,
#         "oil_pressure_bar": oil_pressure,
#         "oil_temp_c": oil_temp,
#         "vibration_rms_mm_s": vibration,
#         "fuel_rate_lph": fuel_rate
#     }

#     input_df = pd.DataFrame([raw_input])

#     # Add all engine-model dummy columns
#     for col in expected_columns:
#         if col.startswith("engine_model_"):
#             input_df[col] = 0

#     # 5039 D is the reference category.
#     # All engine-model dummy columns remain zero for this model.
#     if model_name != "5039 D":

#         selected_dummy = "engine_model_" + model_name

#         if selected_dummy not in expected_columns:
#             st.error(
#                 f"Engine model feature not found: {selected_dummy}"
#             )
#             st.stop()

#         input_df[selected_dummy] = 1

#     # Arrange all features in the exact SVC training order
#     input_df = input_df.reindex(
#         columns=model_columns,
#         fill_value=0
#     )

#     # IMPORTANT:
#     # Your notebook converted the entire encoded dataset to integers
#     # before fitting the scaler. We reproduce that preprocessing here.
#     input_df[numerical_cols] = input_df[numerical_cols].astype("float")

#     # Scale numerical features in the scaler's exact training order
#     scaled_values = scaler.transform(
#         input_df.loc[:, numerical_cols]
#     )

#     input_df.loc[:, numerical_cols] = scaled_values

#     # Final check: exact feature order expected by the SVC
#     input_df = input_df.loc[:, model_columns]

#     # Predict
#     prediction = model.predict(input_df)[0]

#     # --------------------------------------------------
#     # 5. DISPLAY RESULT
#     # --------------------------------------------------

#     st.subheader("Prediction Result")

#     # LabelEncoder in your notebook:
#     # abnormal = 0
#     # healthy = 1

#     if prediction == 1:
#         st.success("Engine Condition: HEALTHY NO Need for maintainence🚜 ")

#     elif prediction == 0:
#         st.error("Engine Condition: ABNORMAL Need for  maintenance ⚠️")

#     st.write("### Selected Tractor")
#     st.write(f"**Brand:** {brand}")
#     st.write(f"**Engine Model:** {model_name}")

#     st.caption(
#         "This prediction is based on the trained SVC model "
#         "and your supplied operating parameters."
#     )

#     st.warning(
#         "This model was trained on a synthetic dataset. "
#         "Its predictions are illustrative and should not be "
#         "used as the sole basis for actual maintenance decisions."


# import streamlit as st
# import pandas as pd
# import joblib

# # =====================================================
# # 1. PAGE CONFIGURATION
# # =====================================================

# st.set_page_config(
#     page_title="Tractor Engine Health Prediction",
#     page_icon="🚜",
#     layout="centered"
# )

# # =====================================================
# # 2. LOAD ALL FOUR PICKLE FILES
# # =====================================================

# try:
#     health_model = joblib.load("SVC_tractor3.pkl")
#     fault_model = joblib.load("fault_type_model.pkl")
#     scaler = joblib.load("scalers_tractor3.pkl")
#     expected_columns = joblib.load("columns_tractor3.pkl")

# except Exception as e:
#     st.error(f"Error loading model files: {e}")
#     st.stop()


# # =====================================================
# # 3. FEATURE CONFIGURATION
# # =====================================================

# numerical_cols = list(scaler.feature_names_in_)

# model_columns = list(health_model.feature_names_in_)
# fault_columns = list(fault_model.feature_names_in_)

# # Verify feature order for both models
# if expected_columns != model_columns:
#     st.error("Health model feature mismatch.")
#     st.stop()

# if expected_columns != fault_columns:
#     st.error("Fault model feature mismatch.")
#     st.stop()

# if len(numerical_cols) != 11:
#     st.error("Unexpected number of scaler features.")
#     st.stop()


# # Brand encoding from your notebook
# brand_mapping = {
#     "John Deere": 0,
#     "Mahindra": 1,
#     "Swaraj": 2
# }


# # Engine models from your dataset
# engine_models = [
#     "5039 D",
#     "5050 D",
#     "5310",
#     "575 DI",
#     "585 DI",
#     "735 FE",
#     "744 FE",
#     "855 FE",
#     "Arjun 605"
# ]


# # Fault labels from your trained fault model
# fault_descriptions = {
#     "excessive_vibration":
#         "Excessive Vibration",

#     "general_anomaly":
#         "General Engine Anomaly",

#     "high_exhaust_temperature":
#         "High Exhaust Temperature",

#     "overheating":
#         "Engine Overheating"
# }


# # =====================================================
# # 4. APPLICATION TITLE
# # =====================================================

# st.title("🚜 Tractor Engine Health Prediction")

# st.markdown(
#     """
#     This application uses machine learning to predict
#     tractor engine health and identify the possible
#     reason for an abnormal engine condition.
#     """
# )

# st.divider()


# # =====================================================
# # 5. TRACTOR DETAILS
# # =====================================================

# st.header("Tractor Details")

# brand = st.selectbox(
#     "Select Tractor Brand",
#     list(brand_mapping.keys())
# )

# model_name = st.selectbox(
#     "Select Engine Model",
#     engine_models
# )


# # =====================================================
# # 6. ENGINE PARAMETERS
# # =====================================================

# st.header("Engine Operating Parameters")

# rpm = st.slider(
#     "Engine RPM",
#     500, 2400, 1800
# )

# load = st.slider(
#     "Load (%)",
#     0, 100, 50
# )

# ambient_temp = st.slider(
#     "Ambient Temperature (°C)",
#     0, 60, 25
# )

# operating_hours = st.slider(
#     "Operating Hours",
#     0, 20000, 100
# )

# maintenance_days_ago = st.slider(
#     "Days Since Last Maintenance",
#     0, 600, 30
# )

# coolant_temp = st.slider(
#     "Coolant Temperature (°C)",
#     0, 150, 90
# )

# exhaust_temp = st.slider(
#     "Exhaust Temperature (°C)",
#     0, 600, 400
# )

# oil_pressure = st.slider(
#     "Oil Pressure (bar)",
#     0.0, 10.0, 3.5
# )

# oil_temp = st.slider(
#     "Oil Temperature (°C)",
#     0, 200, 100
# )

# vibration = st.slider(
#     "Vibration RMS (mm/s)",
#     0.0, 10.0, 1.0
# )

# fuel_rate = st.slider(
#     "Fuel Rate (L/h)",
#     0.0, 50.0, 5.0
# )


# st.divider()


# # =====================================================
# # 7. PREDICTION BUTTON
# # =====================================================

# if st.button("Predict Engine Health", type="primary"):

#     # -------------------------------------------------
#     # A. CREATE RAW INPUT
#     # -------------------------------------------------

#     raw_input = {
#         "brand": brand_mapping[brand],
#         "rpm": rpm,
#         "load_pct": load,
#         "ambient_temp_c": ambient_temp,
#         "operating_hours": operating_hours,
#         "maintenance_days_ago": maintenance_days_ago,
#         "coolant_temp_c": coolant_temp,
#         "exhaust_temp_c": exhaust_temp,
#         "oil_pressure_bar": oil_pressure,
#         "oil_temp_c": oil_temp,
#         "vibration_rms_mm_s": vibration,
#         "fuel_rate_lph": fuel_rate
#     }

#     input_df = pd.DataFrame([raw_input])


#     # -------------------------------------------------
#     # B. CREATE ENGINE MODEL DUMMY VARIABLES
#     # -------------------------------------------------

#     for col in expected_columns:

#         if col.startswith("engine_model_"):
#             input_df[col] = 0


#     # 5039 D is the reference category
#     if model_name != "5039 D":

#         selected_dummy = "engine_model_" + model_name

#         if selected_dummy not in expected_columns:
#             st.error(f"Missing feature: {selected_dummy}")
#             st.stop()

#         input_df[selected_dummy] = 1


#     # -------------------------------------------------
#     # C. ARRANGE FEATURES IN EXACT TRAINING ORDER
#     # -------------------------------------------------

#     input_df = input_df.reindex(
#         columns=model_columns,
#         fill_value=0
#     )


#     # -------------------------------------------------
#     # D. APPLY SAME PREPROCESSING AS NOTEBOOK
#     # -------------------------------------------------

#     # Your notebook converted encoded data to integers
#     # before applying StandardScaler.

#     input_df.loc[:, numerical_cols] = (
#         input_df.loc[:, numerical_cols]
#         .astype(int)
#         .astype(float)
#     )

#     # Scale numerical features
#     scaled_values = scaler.transform(
#         input_df.loc[:, numerical_cols]
#     )

#     input_df.loc[:, numerical_cols] = scaled_values


#     # Final feature order check
#     input_df = input_df.loc[:, model_columns]


#     # -------------------------------------------------
#     # E. MODEL 1: ENGINE HEALTH PREDICTION
#     # -------------------------------------------------

#     health_prediction = health_model.predict(input_df)[0]


#     # =================================================
#     # 8. DISPLAY ENGINE HEALTH
#     # =================================================

#     st.divider()
#     st.header("Prediction Results")

#     st.write(f"**Tractor:** {brand}")
#     st.write(f"**Engine Model:** {model_name}")

#     if health_prediction == 1:

#         st.success("💚 ENGINE CONDITION: HEALTHY")

#         st.write(
#             "The model predicts that the engine is healthy."
#         )

#         st.info(
#             "Fault classification is not required because "
#             "the health model predicted a healthy engine."
#         )


#     elif health_prediction == 0:

#         st.error("⚠️ ENGINE CONDITION: ABNORMAL")

#         st.write(
#             "The model predicts an abnormal engine condition."
#         )


#         # =============================================
#         # 9. MODEL 2: FAULT CLASSIFICATION
#         # =============================================

#         st.subheader("Possible Reason for Engine Fault")

#         fault_prediction = fault_model.predict(input_df)[0]

#         fault_name = fault_descriptions.get(
#             fault_prediction,
#             str(fault_prediction)
#         )

#         st.warning(f"Predicted Fault: {fault_name}")

#         # Display a simple explanation
#         fault_explanations = {

#             "excessive_vibration":
#                 "The model has classified the input as "
#                 "excessive vibration. Inspect vibration sources, "
#                 "mountings and rotating components.",

#             "general_anomaly":
#                 "The model has classified the input as a "
#                 "general engine anomaly. Further inspection "
#                 "is needed to identify the underlying issue.",

#             "high_exhaust_temperature":
#                 "The model has classified the input as high "
#                 "exhaust temperature. Inspect the cooling, "
#                 "air intake and combustion systems.",

#             "overheating":
#                 "The model has classified the input as "
#                 "overheating. Inspect the cooling system "
#                 "and coolant circulation."
#         }

#         st.write(
#             fault_explanations.get(
#                 fault_prediction,
#                 "Further engine inspection is recommended."
#             )
#         )


#     # =============================================
#     # 10. FINAL NOTE
#     # =============================================

#     st.divider()

#     st.caption(
#         "This application uses two trained SVC models: "
#         "one for engine health prediction and another "
#         "for fault classification."
#     )

#     st.warning(
#         "The models were trained using synthetic data. "
#         "Predictions are educational and illustrative, "
#         "not validated diagnoses for actual tractor engines."
#     )

import streamlit as st
import pandas as pd
import joblib

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Tractor Engine Health Prediction",
    page_icon="🚜",
    layout="centered"
)


# =====================================================
# 2. LOAD TRAINED MODELS AND FILES
# =====================================================

try:
    health_model = joblib.load("SVC_tractor3.pkl")
    fault_model = joblib.load("fault_type_model.pkl")
    scaler = joblib.load("scalers_tractor3.pkl")
    expected_columns = joblib.load("columns_tractor3.pkl")

except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()


# =====================================================
# 3. FEATURE CONFIGURATION
# =====================================================

numerical_cols = list(scaler.feature_names_in_)

model_columns = list(health_model.feature_names_in_)
fault_columns = list(fault_model.feature_names_in_)

# Check feature names and order
if expected_columns != model_columns:
    st.error("Health model feature names do not match.")
    st.stop()

if model_columns != fault_columns:
    st.error("Health and fault model feature orders do not match.")
    st.stop()


# Brand encoding from your notebook
brand_mapping = {
    "John Deere": 0,
    "Mahindra": 1,
    "Swaraj": 2
}


# Engine models
engine_models = [
    "5039 D",
    "5050 D",
    "5310",
    "575 DI",
    "585 DI",
    "735 FE",
    "744 FE",
    "855 FE",
    "Arjun 605"
]


# Fault descriptions
fault_descriptions = {
    "excessive_vibration": "Excessive Vibration",
    "general_anomaly": "General Engine Anomaly",
    "high_exhaust_temperature": "High Exhaust Temperature",
    "overheating": "Engine Overheating"
}


# =====================================================
# 4. APPLICATION TITLE
# =====================================================

st.title("Tractor Engine Health Prediction 🚜")

st.markdown(
    """
    This application predicts the health condition of a
    tractor engine and identifies the possible reason
    for an abnormal engine condition.
    """
)

st.divider()


# =====================================================
# 5. TRACTOR DETAILS
# =====================================================

st.header("Tractor Details")

brand = st.selectbox(
    "Select Tractor Brand",
    list(brand_mapping.keys())
)

model_name = st.selectbox(
    "Select Engine Model",
    engine_models
)


# =====================================================
# 6. ENGINE OPERATING PARAMETERS
# =====================================================

st.header("Engine Operating Parameters")

rpm = st.slider(
    "Engine RPM",
    500, 2400, 1800
)

load = st.slider(
    "Load (%)",
    0, 100, 50
)

ambient_temp = st.slider(
    "Ambient Temperature (°C)",
    0, 60, 25
)

operating_hours = st.slider(
    "Operating Hours",
    0, 20000, 100
)

maintenance_days_ago = st.slider(
    "Days Since Last Maintenance",
    0, 600, 30
)

coolant_temp = st.slider(
    "Coolant Temperature (°C)",
    0, 150, 90
)

exhaust_temp = st.slider(
    "Exhaust Temperature (°C)",
    0, 600, 400
)

oil_pressure = st.slider(
    "Oil Pressure (bar)",
    0.0, 10.0, 3.5
)

oil_temp = st.slider(
    "Oil Temperature (°C)",
    0, 200, 100
)

vibration = st.slider(
    "Vibration RMS (mm/s)",
    0.0, 10.0, 1.0
)

fuel_rate = st.slider(
    "Fuel Rate (L/h)",
    0.0, 50.0, 5.0
)


st.divider()


# =====================================================
# 7. PREDICTION BUTTON
# =====================================================

if st.button("Predict Engine Health", type="primary"):

    # -------------------------------------------------
    # A. CREATE RAW INPUT
    # -------------------------------------------------

    raw_input = {
        "brand": brand_mapping[brand],
        "rpm": rpm,
        "load_pct": load,
        "ambient_temp_c": ambient_temp,
        "operating_hours": operating_hours,
        "maintenance_days_ago": maintenance_days_ago,
        "coolant_temp_c": coolant_temp,
        "exhaust_temp_c": exhaust_temp,
        "oil_pressure_bar": oil_pressure,
        "oil_temp_c": oil_temp,
        "vibration_rms_mm_s": vibration,
        "fuel_rate_lph": fuel_rate
    }

    input_df = pd.DataFrame([raw_input])

    # -------------------------------------------------
    # B. CREATE ENGINE MODEL DUMMY VARIABLES
    # -------------------------------------------------

    for col in expected_columns:

        if col.startswith("engine_model_"):
            input_df[col] = 0

    # 5039 D is the reference category
    if model_name != "5039 D":

        selected_dummy = "engine_model_" + model_name

        if selected_dummy not in expected_columns:
            st.error(f"Feature not found: {selected_dummy}")
            st.stop()

        input_df[selected_dummy] = 1

    # -------------------------------------------------
    # C. ARRANGE FEATURES IN TRAINING ORDER
    # -------------------------------------------------

    input_df = input_df.reindex(
        columns=model_columns,
        fill_value=0
    )

    # -------------------------------------------------
    # D. APPLY ORIGINAL NOTEBOOK PREPROCESSING
    # -------------------------------------------------

    # Convert numerical values to integers first,
    # matching the preprocessing used in your notebook.

    numerical_input = (
        input_df.loc[:, numerical_cols]
        .astype(int)
        .astype(float)
    )

    # Apply the trained scaler
    scaled_values = scaler.transform(numerical_input)

    # Create a separate floating-point DataFrame
    scaled_df = pd.DataFrame(
        scaled_values,
        columns=numerical_cols,
        index=input_df.index
    )

    # Replace numerical columns individually
    for col in numerical_cols:
        input_df[col] = scaled_df[col].astype(float)

    # Ensure exact feature order for both models
    input_df = input_df.loc[:, model_columns]

    # -------------------------------------------------
    # E. MODEL 1: ENGINE HEALTH PREDICTION
    # -------------------------------------------------

    health_prediction = health_model.predict(input_df)[0]

    # =================================================
    # 8. DISPLAY ENGINE HEALTH
    # =================================================

    st.divider()

    st.header("Engine Diagnosis Report 🚜")

    st.write(f"**Tractor Brand:** {brand}")
    st.write(f"**Engine Model:** {model_name}")

    # -------------------------------------------------
    # HEALTHY ENGINE
    # -------------------------------------------------

    if health_prediction == 1:

        st.success("💚 ENGINE CONDITION: HEALTHY")

        st.write(
            "The model predicts that the tractor engine "
            "is healthy."
        )

        st.subheader("Fault Diagnosis")

        st.success("Fault Type: No Fault Detected")

    # -------------------------------------------------
    # ABNORMAL ENGINE
    # -------------------------------------------------

    elif health_prediction == 0:

        st.error("⚠️ ENGINE CONDITION: ABNORMAL")

        st.write(
            "The model predicts an abnormal engine condition."
        )

        # =============================================
        # MODEL 2: FAULT TYPE PREDICTION
        # =============================================

        st.subheader("Fault Diagnosis")

        fault_prediction = fault_model.predict(input_df)[0]

        fault_name = fault_descriptions.get(
            fault_prediction,
            str(fault_prediction)
        )

        st.warning(
            f"Predicted Fault Type: {fault_name}"
        )

        # =============================================
        # FAULT EXPLANATIONS
        # =============================================

        fault_explanations = {

            "excessive_vibration":
                "The model predicts excessive engine vibration.",

            "general_anomaly":
                "The model predicts a general engine anomaly.",

            "high_exhaust_temperature":
                "The model predicts high exhaust temperature.",

            "overheating":
                "The model predicts possible engine overheating."
        }

        st.write(
            fault_explanations.get(
                fault_prediction,
                "Further engine inspection is recommended."
            )
        )

    # =================================================
    # 9. FINAL INFORMATION
    # =================================================

    st.divider()

    st.caption(
        "Engine health and fault classification are "
        "predictions from two separate trained SVC models."
    )

    st.warning(
        "This application uses a synthetic dataset. "
        "Its predictions are educational and illustrative "
        "and are not validated mechanical diagnoses."
    )
