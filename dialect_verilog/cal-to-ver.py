import os
import subprocess

def convert_futil_to_verilog(futil_file_path, output_file_name):
    # Get user's home directory
    home_dir = os.path.expanduser("~")

    # Define the directories and file paths
    turbo_dialect_path = os.path.join(home_dir, 'turbo-dialect')
    calyx_path = os.path.join(home_dir, 'calyx')
    verilog_directory = os.path.join(turbo_dialect_path, 'verilog')
    output_file_path = os.path.join(verilog_directory, output_file_name)

    # Check if the necessary directories exist
    if not os.path.isdir(turbo_dialect_path):
        print(f"Error: The directory '{turbo_dialect_path}' does not exist.")
        return
    if not os.path.isdir(calyx_path):
        print(f"Error: The directory '{calyx_path}' does not exist.")
        return
    if not os.path.isfile(futil_file_path):
        print(f"Error: The file '{futil_file_path}' does not exist.")
        return

    # Create the verilog directory if it doesn't exist
    os.makedirs(verilog_directory, exist_ok=True)

    # Debug statements
    print("Current working directory:", os.getcwd())
    print("Is 'verilog' folder already present?", os.path.exists(verilog_directory))
    print("Is 'calyx' folder already present?", os.path.exists(calyx_path))

    # Define the command to convert futil to verilog and run optimizations
    command = f"fud e {futil_file_path} --to verilog --from calyx > {output_file_path}"
    
    # Run the command from the calyx directory
    result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=calyx_path)

    # Debug statement for subprocess result
    print("Command executed:", command)
    print("Return code:", result.returncode)
    if result.returncode != 0:
        print("Error output:", result.stderr)
    else:
        print("Conversion and optimization successful.")

def read_verilog(verilog_file_name):
    home_dir = os.path.expanduser("~")
    verilog_file_path = os.path.join(home_dir, 'turbo-dialect', 'verilog', verilog_file_name)
    with open(verilog_file_path, 'r') as file:
        verilog_code = file.read()
    return verilog_code

# Example usage
if __name__ == "__main__":
    futil_file_path = input("Enter the path to your .futil file: ")
    output_file_name = input("Enter the desired output file name (e.g., output.v): ")
    
    convert_futil_to_verilog(futil_file_path, output_file_name)
    verilog_code = read_verilog(output_file_name)
    print(verilog_code)





# import os
# import subprocess
# import tempfile
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def convert_futil_to_verilog(futil_file, output_file_name, session_id):
#     # Create a temporary directory for the session
#     session_temp_dir = os.path.join(tempfile.gettempdir(), f"session_{session_id}")
#     os.makedirs(session_temp_dir, exist_ok=True)
#     print("Session temporary directory created:", session_temp_dir)

#     # Define the directories and file paths
#     calyx_path = os.path.expanduser("~/calyx")
#     verilog_directory = os.path.join(session_temp_dir, 'verilog')
#     output_file_path = os.path.join(verilog_directory, output_file_name)

#     # Check if the necessary directories exist
#     if not os.path.isdir(calyx_path):
#         print(f"Error: The directory '{calyx_path}' does not exist.")
#         return
#     if not futil_file:
#         print("Error: No .futil file uploaded.")
#         return

#     # Create the verilog directory within the temporary directory
#     os.makedirs(verilog_directory, exist_ok=True)

#     # Define the path to save the uploaded .futil file
#     futil_temp_path = os.path.join(session_temp_dir, 'input.futil')
#     with open(futil_temp_path, 'wb') as f:
#         for chunk in futil_file.chunks():
#             f.write(chunk)

#     # Define the command to convert futil to verilog
#     convert_command = f"fud e {futil_temp_path} --to verilog --from calyx > {output_file_path}"

#     # Run the conversion command from the calyx directory
#     convert_result = subprocess.run(convert_command, shell=True, capture_output=True, text=True, cwd=calyx_path)

#     # Debug statement for subprocess result
#     print("Conversion command executed:", convert_command)
#     print("Conversion return code:", convert_result.returncode)
#     if convert_result.returncode != 0:
#         print("Conversion error output:", convert_result.stderr)
#         return
#     else:
#         print("Conversion successful.")

#     return session_temp_dir

# @csrf_exempt
# def home(request):
#     if request.method == 'POST':
#         futil_file = request.FILES.get('futil_file')
#         session_id = request.POST.get('session_id')
#         output_file_name = futil_file.name + ".v"

#         session_temp_dir = convert_futil_to_verilog(futil_file, output_file_name, session_id)
#         if session_temp_dir:
#             # Read the Verilog file from the session temporary directory
#             verilog_file_path = os.path.join(session_temp_dir, 'verilog', output_file_name)
#             with open(verilog_file_path, 'r') as file:
#                 verilog_code = file.read()
#             return render(request, 'result.html', {'verilog_code': verilog_code})
#     return render(request, 'index.html')
