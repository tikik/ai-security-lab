import pandas as pd
import matplotlib.pyplot as plt

def generate_report_chart(csv_file):
    try:
        # Load the results
        df = pd.read_csv(csv_file)
        
        # Calculate Security Score: (SECURE count / Total count) * 100
        # We group by 'Phase' to see the difference between Junior and Senior
        stats = df.groupby('Phase')['Result'].value_counts(normalize=True).unstack(fill_value=0)
        
        # Ensure 'SECURE' column exists even if everything leaked
        if 'SECURE' not in stats.columns:
            stats['SECURE'] = 0
            
        scores = stats['SECURE'] * 100

        # Plotting
        plt.style.use('ggplot')
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Use Red for Junior (Vulnerable) and Blue/Green for Senior (Hardened)
        colors = ['#e74c3c' if phase == 'junior' else '#2ecc71' for phase in scores.index]
        
        bars = ax.bar(scores.index, scores.values, color=colors, edgecolor='black', alpha=0.8)

        # Formatting
        ax.set_title('AI Security Lab: Model Hardening Results', fontsize=15, pad=20)
        ax.set_ylabel('Security Score (% Blocked Attacks)', fontsize=12)
        ax.set_ylim(0, 105)
        ax.set_xlabel('Prompt Configuration Phase', fontsize=12)

        # Add data labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 5), 
                        textcoords="offset points",
                        ha='center', va='bottom', fontweight='bold')

        plt.tight_layout()
        plt.savefig('lab_security_comparison.png')
        print("✅ Chart generated: lab_security_comparison.png")
        
    except FileNotFoundError:
        print("Error: security_lab_results.csv not found. Run the lab_runner.py first!")

if __name__ == "__main__":
    generate_report_chart("security_lab_results.csv")