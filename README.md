# F1 Italian Grand Prix 2025 Prediction Script 🏎️
- This Python script, f1_italian_grand.py, predicts the winner of the Italian Grand Prix based on a weighted analysis of recent race results and various performance factors.

## How It Works ⚙️
- The script calculates a total "weighted points" score for several drivers by taking into account:
- Recent Race Results: Points from the British, Belgian, Hungarian, and Dutch Grand Prix are used, with more recent races carrying a higher weight.
- External Factors: Adjustments are made for specific events, such as a penalty for Oscar Piastri at the British GP, a Monza track factor that boosts certain teams, and penalties for drivers with retirements (DNF).
- Qualifying Performance: A boost is applied to drivers who have shown strong qualifying performance.
- The script then identifies the driver with the highest weighted score and declares them the predicted winner.

## Requirements 🛠️
- To run this script, you need to have the matplotlib library installed for local visualization of the results. You can install it using pip:
- `pip install matplotlib`

## How to Run ▶️
- Save the code: Ensure the f1_italian_grand.py file is saved on your computer.
- Open a terminal or command prompt: Navigate to the directory where you saved the file.
- Run the script: Execute the file using Python.
- `python f1_italian_grand.py`
- The script will print the weighted points for each driver and the predicted winner to the console. It will also generate a bar chart visualizing the points.

## Predicted Winner 🏆
- Based on the current data and factors considered, the script predicts the winner of the Italian Grand Prix.
## Disclaimer ⚠️
- This is a prediction model and not an official forecast. The results are based on the data and factors defined within the script and do not guarantee the actual outcome of the race.
