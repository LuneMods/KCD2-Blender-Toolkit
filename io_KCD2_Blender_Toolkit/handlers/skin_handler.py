import os
import subprocess

def skin_to_dae(input_file):
    if not os.path.isabs(input_file):
        print(f"Error: The input file path '{input_file}' must be an absolute path.")
        return None

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return None
    
    if not input_file.lower().endswith(".skin"):
        print(f"Error: Input file '{input_file}' is not a .skin file.")
        return None

    output_file = os.path.splitext(input_file)[0] + ".dae"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    convertor_path = os.path.join(parent_dir, "External", "KCD2-Convertor", "KCD2-Convertor.exe")

    if not os.path.isfile(convertor_path):
        print(f"Error: KCD2-Convertor.exe not found at '{convertor_path}'.")
        return None

    command = [
        convertor_path,
        input_file,
        "-outputfile", output_file
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("KCD2-Convertor.exe executed successfully!")
        print("STDOUT:")
        print(result.stdout)
        if os.path.isfile(output_file):
            print(f"DAE file created: {output_file}")
            return output_file
        else:
            print("DAE file was not created.")
            return None
    except subprocess.CalledProcessError as e:
        print("An error occurred while running KCD2-Convertor.exe")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        return None
    


def skin_to_glb(input_file):
    if not os.path.isabs(input_file):
        print(f"Error: The input file path '{input_file}' must be an absolute path.")
        return None

    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        return None
    
    if not input_file.lower().endswith(".skin"):
        print(f"Error: Input file '{input_file}' is not a .skin file.")
        return None

    output_file = os.path.splitext(input_file)[0] + ".glb"

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    convertor_path = os.path.join(parent_dir, "External", "KCD2-Convertor", "KCD2-Convertor.exe")

    if not os.path.isfile(convertor_path):
        print(f"Error: KCD2-Convertor.exe not found at '{convertor_path}'.")
        return None

    command = [
        convertor_path,
        input_file, "-glb",
        "-outputfile", output_file, 
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("KCD2-Convertor.exe executed successfully!")
        print("STDOUT:")
        print(result.stdout)
        if os.path.isfile(output_file):
            print(f"GLB file created: {output_file}")
            return output_file
        else:
            print("GLB file was not created.")
            return None
    except subprocess.CalledProcessError as e:
        print("An error occurred while running KCD2-Convertor.exe")
        print("STDOUT:")
        print(e.stdout)
        print("STDERR:")
        print(e.stderr)
        return None
    