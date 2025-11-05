AlyWork Law Pro — v26_Smart_Integrated
Structure:
- app.py                      : Main launcher (Streamlit)
- pages/1_workers.py          : Workers page
- pages/2_employers.py        : Employers page
- pages/3_inspectors.py       : Inspectors page
- pages/4_researchers.py      : Researchers & trainees page
- mini_ai_smart.py            : Lightweight AI stub (replace with full engine)
- helpers/settings_manager.py : Configuration manager
- helpers/ui_components.py    : Reusable UI components
- config/config.json         : Template configuration (update ngrok token & workbook path)

How to run (Colab):
1. Upload the folder to Colab or copy to /content/.
2. Ensure dependencies installed: streamlit, pyngrok, pandas, openpyxl
3. Run: !streamlit run /path/to/app.py
4. For ngrok access, provide token in config/config.json or set env NGROK_AUTHTOKEN

Notes:
This package is a starting integrated skeleton. Replace mini_ai_smart.py with the full MiniLegalAI engine and set correct workbook path.