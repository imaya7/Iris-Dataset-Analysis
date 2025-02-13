import pandas as pd
import os

try:
    # Define the file paths
    base_dir = os.path.dirname(__file__)
    petal_file = os.path.join(base_dir, 'Petal_Data.csv')
    sepal_file = os.path.join(base_dir, 'Sepal_Data.csv')

    # Load the datasets
    petal_data = pd.read_csv(petal_file, index_col=0)
    sepal_data = pd.read_csv(sepal_file, index_col=0)

    # Merge the datasets on 'sample_id'
    merged_data = pd.merge(petal_data, sepal_data, on=['sample_id', 'species'])

    # Calculate the average of each variable for all species
    average_values = merged_data.groupby('species').mean(numeric_only=True)

    # Calculate the median of each variable for all species
    median_values = merged_data.groupby('species').median(numeric_only=True)

    # Calculate the standard deviation of each variable for all species
    std_dev_values = merged_data.groupby('species').std(numeric_only=True)

    # Calculate the correlation between each variable for all species
    correlation_matrix = merged_data.drop(columns=['sample_id', 'species']).corr()

    # Calculate pairwise differences in average values for similarity
    species_pairs = average_values.index
    similarity_scores = {}

    for i in range(len(species_pairs)):
        for j in range(i + 1, len(species_pairs)):
            species1 = species_pairs[i]
            species2 = species_pairs[j]
            difference = (average_values.loc[species1] - average_values.loc[species2]).abs().sum()
            similarity_scores[(species1, species2)] = difference

    # Sort species pairs by similarity (least to most similar)
    sorted_similarity = sorted(similarity_scores.items(), key=lambda x: x[1])

    # Write all information to a text file
    output_file = os.path.join(base_dir, 'iris_data_analysis.txt')
    with open(output_file, 'w') as file:
        file.write("Assignment 3: pandas\n\n")
        file.write("Average values for all species:\n")
        file.write(average_values.to_string())
        file.write("\n\nMedian values for all species:\n")
        file.write(median_values.to_string())
        file.write("\n\nStandard deviation values for all species:\n")
        file.write(std_dev_values.to_string())
        file.write("\n\nCorrelation matrix for all variables:\n")
        file.write(correlation_matrix.to_string())
        
        for species in merged_data['species'].unique():
            species_data = merged_data[merged_data['species'] == species]
            file.write(f"\n\nAll values for {species}:\n")
            file.write(species_data.to_string())
        
        file.write("\n\nSpecies similarity from least to most similar:\n")
        for pair, score in sorted_similarity:
            file.write(f"{pair[0]} and {pair[1]}: {score}\n")
        
        # Explanation of similarity calculation
        file.write("\n\nExplanation of similarity calculation:\n")
        file.write("The similarity between species was calculated by comparing the average values of each variable (petal length, petal width, sepal length, and sepal width).\n")
        file.write("For each pair of species, the absolute differences in the average values of these variables were summed to get a similarity score.\n")
        file.write("The species pairs were then sorted from least similar (highest score) to most similar (lowest score).\n")

    print("All information has been written to iris_data_analysis.txt")

except FileNotFoundError as e:
    print(f"Error: {e}. Please ensure the CSV files are in the correct location.")
except pd.errors.EmptyDataError as e:
    print(f"Error: {e}. The CSV files are empty.")
except pd.errors.ParserError as e:
    print(f"Error: {e}. There was an error parsing the CSV files.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
