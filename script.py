import yaml


def convert_text_to_yaml(input_file, output_file):
    """
    Convert a text file with user agents (one per line) to a YAML file.

    :param input_file: Path to the input text file
    :param output_file: Path to the output YAML file
    """
    # Read the input text file
    try:
        with open(input_file, "r") as f:
            user_agents = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return
    except IOError:
        print(f"Error: Could not read input file '{input_file}'.")
        return

    # Create a dictionary with user agents
    user_agents_dict = {"user_agents": user_agents}

    # Write to YAML file
    try:
        with open(output_file, "w") as f:
            yaml.dump(user_agents_dict, f, default_flow_style=False)
        print(f"Successfully converted {input_file} to {output_file}")
    except IOError:
        print(f"Error: Could not write to output file '{output_file}'.")


# Example usage
if __name__ == "__main__":
    input_file = "user-agents.txt"  # Replace with your input file name
    output_file = "user-agents.yaml"  # Replace with desired output file name

    convert_text_to_yaml(input_file, output_file)
