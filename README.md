<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:06b6d4&height=170&section=header&text=JSON%20CSV%20Bridge&fontColor=ffffff&fontSize=38&animation=fadeIn" width="100%" alt="JSON CSV Bridge banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&duration=2800&pause=900&color=06B6D4&center=true&vCenter=true&width=650&lines=Convert+JSON+to+CSV+and+back;Flatten+nested+objects+into+columns;Small+tools.+Clear+workflows." alt="Typing introduction"/>
<p>Move tabular data between JSON and CSV without surprises.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/json-csv-bridge?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/json-csv-bridge?style=for-the-badge" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/json-csv-bridge?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/json-csv-bridge?style=for-the-badge" alt="Last commit"/></p>
<img src="assets/icon.svg" width="112" alt="Project icon"/>
</div>

## ✨ Overview
A local command-line converter for arrays of JSON objects and CSV tables. Nested objects become dotted column names, arrays remain compact JSON cells, and the source file is never modified.

## 🚀 Features
- ✨ Convert JSON object arrays to CSV and CSV rows to JSON
- ✨ Flatten nested objects into stable dotted column names
- ✨ Preserve UTF-8 text and read spreadsheet-style UTF-8 BOM files
- ✨ Keep arrays and nested values as valid JSON inside cells
- ✨ Write to a separate output path

## 🎬 Demo
Convert with `python main.py sample.json sample.csv`, or reverse the direction with `python main.py sample.csv restored.json`.

## ⚡ Quick Start
```bash
python main.py sample.json sample.csv
python main.py sample.csv restored.json
```

## 🧰 Tech Stack
Python 3.10+ and the standard-library `json`, `csv`, and `argparse` modules. No third-party dependencies.

## 🗂️ Folder Structure
```text
.
├── main.py
├── requirements.txt
├── tests/test_main.py
├── assets/icon.svg
├── .gitignore
└── LICENSE
```

## 🧭 Roadmap
- [ ] Add optional column selection
- [ ] Add a dry-run schema summary
- [ ] Add configurable nested-field separators

## 🤝 Contributing
Issues and focused pull requests are welcome. Keep changes small and include tests when behavior changes.

## 📄 License
Released under the [MIT License](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:06b6d4&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
