from rich.console import Console
from pipeline.profile_extractor import ProfileExtractor
from pipeline.billing_generator import BillingGenerator
from pipeline.cost_analyzer import CostAnalyzer
from utils.file_io import load_json


console = Console()


extractor = ProfileExtractor()
biller = BillingGenerator()
analyzer = CostAnalyzer()




def show_menu():
    while True:
        console.print("\n[bold cyan]Cloud Cost Optimizer[/bold cyan]")
        console.print("1. Enter new project description")
        console.print("2. Run Complete Cost Analysis")
        console.print("3. View Recommendations")
        console.print("4. Exit")


        choice = input("Select option: ")


        if choice == "1":
            desc = input("Enter project description: ")
            extractor.run(desc)
            console.print("Profile generated.")


        elif choice == "2":
            profile = load_json("data/project_profile.json")
            billing = biller.run(profile)
            analyzer.run(profile, billing)
            console.print("Cost analysis complete.")


        elif choice == "3":
            report = load_json("data/cost_optimization_report.json")
            for r in report.get("recommendations", []):
                console.print(f"- {r['title']} → Save ₹{r['potential_savings']}")


        elif choice == "4":
            break