# CS 340 Client Server Development Portfolio

**Alberto Rodriguez**

## Project overview

For Project Two, I developed a dashboard for Grazioso Salvare to help staff identify shelter dogs that meet search-and-rescue training criteria. The application connects Python to MongoDB through a reusable CRUD module. Users can choose water rescue, mountain or wilderness rescue, or disaster or individual tracking filters, review a searchable and sortable table, inspect breed distributions, and view an animal's location on a map.

## Portfolio artifacts

- [Final dashboard notebook](ProjectTwoDashboard.ipynb)
- [Project Two README in Word format](Project_Two_README.docx)
- [Reusable CRUD Python module](CRUD_Python_Module.py)
- [Dashboard logo](<Grazioso Salvare Logo.png>)

The Word document contains the Project Two documentation and dashboard screenshots. This repository README provides my course reflection.

## How do you write programs that are maintainable readable and adaptable

I write maintainable programs by using descriptive names, separating responsibilities, and documenting the purpose of functions and important decisions. In this project, the AnimalShelter class handles database operations while the dashboard callbacks handle user interactions and presentation. The CRUD module from Project One exposes create, read, update, and delete methods, so the dashboard can retrieve records through the read method without repeating MongoDB connection code in each widget.

This separation made the dashboard easier to extend and helped keep database logic consistent. I could change a rescue filter by changing its query dictionary while keeping the same database interface. It also gives me a smaller component to troubleshoot independently. In the future, I could reuse the module in a command-line shelter management tool, another dashboard, or a web service that needs access to the same animal records. For a different database schema, I would adapt the connection configuration and validate the expected fields.

## How do you approach a problem as a computer scientist

I start by translating the client's goals into specific data requirements and observable behaviors. For Grazioso Salvare, that meant identifying the required breeds, sex, and age ranges for each rescue category, converting those rules into MongoDB queries, and connecting the query results to the table, chart, and map. I also considered what the interface should display when a filter returns no animals or a record has invalid location information.

This project required me to think about the complete path from stored records to an interactive user interface. Compared with an isolated programming exercise, a change in one part could affect several others: filtering changes the table, and the table's current data influences the visualizations. For future client databases, I would clarify requirements with sample records and expected results, define field types, check data quality, and test boundary cases. I would also examine common queries before choosing indexes and confirm that access permissions fit the client's needs.

## What do computer scientists do and why does it matter

Computer scientists turn real problems into systems that organize information, apply rules consistently, and help people make decisions. The work involves understanding users, choosing appropriate data structures, building software, and checking that the results match the intended requirements.

For a company like Grazioso Salvare, this dashboard could reduce the time spent manually reviewing shelter records. Staff can narrow the records to dogs that match a rescue category, compare the results, and inspect location information in one interface. The dashboard supports the initial screening process; staff still need to evaluate each dog's health, behavior, and training suitability. Making relevant information easier to find helps the organization focus its effort on evaluating potential rescue dogs.

## Running the portfolio copy

Use the course MongoDB environment with the `aac.animals` collection populated. Keep the notebook, CRUD module, and logo together. The application uses Python, PyMongo, pandas, NumPy, Matplotlib, Dash, JupyterDash, Plotly, and Dash Leaflet. See the Word README for the course setup and dashboard details.

The portfolio notebook reads the connection credentials from the `AAC_MONGO_USERNAME` and `AAC_MONGO_PASSWORD` environment variables. Set these in your local environment before running the notebook. Notebook execution outputs have been cleared for publication. The credential configuration is the only application source change made for this portfolio copy.
