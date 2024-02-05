# test_list_operations.py
import pytest

# Test function for main() in list_operations.py
def test_main_operations(capsys):
    # Import the script which executes the main function
    import list_operations
    list_operations.main()
    
    # Capture the output of the print statements
    captured = capsys.readouterr()
    output = captured.out.strip().split('\n')
    
    # Test the output - note that this will need to be updated based on the exact instructions given to the students
    # Example checks:
    assert "Initial list: " in output[0]
    assert "After appending:" in output[1]
    assert "After inserting at index 1:" in output[2]
    assert "After removing element at index 3:" in output[3]
    assert "After popping the last element:" in output[4]
    
    # Example check for the correct number of items in the list after all operations
    # This assumes the final operation is to pop the last item.
    final_list_output = output[-1].replace("After popping the last element: ", "")
    final_list = eval(final_list_output)
    assert len(final_list) == 3  # replace with the expected number based on instructions

if __name__ == '__main__':
    pytest.main()
