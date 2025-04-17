# 🎯 Predictor Suite

Predictor Suite is a dual-function predictive analytics application focused on:
- **UK Horse Racing** (Top 10 combo predictors for major races)
- **EuroMillions Lottery** (Optimized number lines targeting jackpot-tier wins)

It combines historical data analysis, probability techniques, and a GUI interface to help you make high-risk, high-reward predictions in a calculated way.

## Reporting Issues and Requesting Features

### Reporting a Vulnerability
If you discover a security vulnerability, please report it by opening an issue in the **[GitHub Issues tab](../../issues/new?template=bug_report.md)**. 

### Requesting Features
If you have an idea for a new feature or improvement, please submit it via the **[Feature Request template](../../issues/new?template=feature_request.md)**.


## 💡 Features

### 🔹 EuroMillions Predictor
- Generates two optimized lines based on historical draw trends
- Identifies hot/cold numbers, repeated patterns, and distribution balance
- Probabilistic scoring for each combination
- Lucky Star prediction logic

### 🔹 Horse Racing Predictor
- Focused on 4 key races: Grand National, Ascot Gold Cup, King George VI Chase, and Chester Cup
- Generates 5 high-risk, top-10 finish combinations per final race
- Strategy based: £4 per bet, 5 bets per race
- Yearly betting budget: £80 (4 races)

### 🖥 GUI Features
- Tabbed interface for switching between lottery and racing modes
- Clean design, easy input and export of prediction results
- Future plans for export to PDF or CSV

## 🧰 Requirements

- Python 3.10+
- pip / poetry (for dependency management)
- OS: Windows, macOS, or Linux

Python dependencies (see `requirements.txt`):
- pandas, numpy
- matplotlib / seaborn
- tkinter or PyQt5
- flake8 / pre-commit (optional for linting)

## ⚙️ Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/predictor-suite.git
cd predictor-suite

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python src/main.py

```

## 🚀 Usage

- Run the app to launch the GUI
- Choose between Horse Racing and EuroMillions tabs
- Load your data (or use included sample data)
- Generate predictions and export/save them
- Each session refreshes recommendations based on updated history

## 📈 Roadmap

- [ ]  Prediction logic for EuroMillions and Horse Racing
- [ ]  Tabbed GUI using Tkinter
- [ ]  Real-time data scraping (race entries, lottery draws)
- [ ]  Export results to PDF/CSV
- [ ]  Betting return calculator
- [ ]  Machine learning model integration (Phase 2)

## 🔒 License

This project is not open source. Unauthorized use, modification, or distribution is prohibited.

See **[LICENSE](LICENSE)** for more details.