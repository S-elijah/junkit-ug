```markdown
🗑️ JunkIt UG  
Spot It. Snap It. JunkIt.
Report Waste. Restore Clean.

[Streamlit App] (https://junkit-ug-mjg53ajpdkskvqfngi3qrm.strea)

A community-driven platform that empowers Ugandans to report illegal waste dumping and track cleanup progress. Built for the **RELX Environmental Challenge 2026**.


✨ Current MVP Features

- 📝 Report Illegal Dumping– Submit location and description of waste dumped in your community.  
- 📊 Public Dashboard – View all active reports and filter by status.  
- 🔄 Status Tracking – Reports move from **Pending → Acknowledged → Resolved**.  
- 📈 Statistics– Real‑time metrics and bar charts showing community impact.  
- 📱 Mobile‑Responsive – Works on any smartphone browser without app installation.  

Planned features: photo upload, GPS auto‑location, USSD access for basic phones, SMS alerts, and an interactive hotspot map.*

🛠️ Tech Stack

| Layer           | Technology                        |
|-----------------|-----------------------------------|
| Frontend       | [Streamlit](https://streamlit.io) |
| Backend        | Python                            |
| Data Storage   | CSV (prototype) → SQLite (planned)|
| Hosting        | [Streamlit Community Cloud](https://streamlit.io/cloud) |
| Future APIs    | Africa’s Talking (USSD/SMS)       |



Run Locally

Requirements:Python 3.8+, pip, Git

```bash
# Clone the repo
git clone https://github.com/S-elijah/junkit-ug.git
cd junkit-ug

# Create & activate virtual environment
python3 -m venv junkit-env
source junkit-env/bin/activate   # Linux/Mac
# On Windows: junkit-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run junkit.py
```

Open http://localhost:8501 in your browser.


🌐 Live App https://junkit-ug-mjg53ajpdkskvqfngi3qrm.streamlit.app/ 

🔗 JunkIt UG on Streamlit Cloud


📁 Project Structure

junkit-ug/
——>junkit.py           # Main Streamlit application
——>requirements.txt    # Python dependencies
——>README.md           # This file


👤 About the Developer

Elijah Senabulya
First‑year Software Engineering student at Victoria University, Kampala.
📧 senabulyaelijahk@gmail.com
🔗 GitHub

Passionate about using technology to solve real community problems. This prototype was built with four months of Python programming fundamentals.



🤝 Contributing

This is an open‑source student project. Feedback, bug reports, and pull requests are welcome!
Fork the repo, create a branch, commit your changes, and open a PR.


JunkIt UG – Turning community vigilance into cleaner neighbourhoods, one report at a time.


🗑️ Spot It. 📸 Snap It. 🚮 JunkIt.
