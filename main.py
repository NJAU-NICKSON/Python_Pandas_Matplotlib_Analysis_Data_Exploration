from task1_load_explore import load_and_explore
from task2_analysis import analyze_data
from task3_visualization import visualize_data

def main():
    print("="*50)
    print("TASK 1: LOAD AND EXPLORE DATASET")
    print("="*50)
    df = load_and_explore()   
    
    print("\n" + "="*50)
    print("TASK 2: BASIC DATA ANALYSIS")
    print("="*50)
    analyze_data()
    
    print("\n" + "="*50)
    print("TASK 3: DATA VISUALIZATION")
    print("="*50)
    visualize_data()

if __name__ == "__main__":
    main()
