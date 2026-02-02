import pandas as pd

def show_senior_failures(csv_file):
    try:
        # Load your data
        df = pd.read_csv(csv_file)
        
        # Filter: We only care about LEAKS that happened in the SENIOR phase
        failures = df[(df['Phase'] == 'senior') & (df['Result'] == 'LEAK')]
        
        if failures.empty:
            print("\n" + "="*50)
            print("🛡️  NO SENIOR FAILURES DETECTED")
            print("Your current defenses blocked 100% of adversarial attacks.")
            print("="*50)
        else:
            print("\n" + "!"*20 + " SENIOR FAILURE REPORT " + "!"*20)
            print(f"Detected {len(failures)} successful leak(s). Review these immediately:\n")
            
            for i, row in failures.iterrows():
                print(f"🔴 [VULNERABILITY DETECTED]")
                print(f"   ATTACK TYPE: {row['Attack']}")
                print(f"   AI OUTPUT:   {row['Response']}")
                print("-" * 63)
            
            print("\n[ANALYSIS]: These attacks bypassed your system prompt.")
            print("Consider adding 'Negative Constraints' to handle these specific cases.")
            
    except FileNotFoundError:
        print(f"Error: {csv_file} not found. Did you run lab_runner.py first?")

if __name__ == "__main__":
    show_senior_failures("security_lab_results.csv")