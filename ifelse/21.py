working_days = int(input("Enter the total number of working days: "))
absent_days = int(input("Enter the number of days absent: "))

# Calculate the attendance percentage
attendance_percentage = ((working_days - absent_days) / working_days) * 100

# Determine eligibility based on the attendance percentage
if attendance_percentage >= 75:
    
    print("You are eligible.")
    
else:
    print("You are not eligible.")

# Print the attendance percentage for reference
print(f"Your attendance percentage is: {attendance_percentage:.2f}%")