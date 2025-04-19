def calculate_area_of_rectangle(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns:
    float: The area of the rectangle.
    """
    return length * width

function fetchUserData(userId) {
    // Simulate fetching user data from an API
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const userData = {
                id: userId,
                name: "John Doe",
                age: 30
            };
            resolve(userData);
        }, 1000);
    });
}
function displayUserData(userId) {
    fetchUserData(userId)
        .then(userData => {
            console.log(`User ID: ${userData.id}`);
            console.log(`Name: ${userData.name}`);
            console.log(`Age: ${userData.age}`);
        })
        .catch(error => {
            console.error("Error fetching user data:", error);
        });
}
# Example usage
length = 5
width = 10
area = calculate_area_of_rectangle(length, width)
print(f"The area of the rectangle is: {area}")
# Example usage of the JavaScript function
userId = 1
displayUserData(userId)
# Example usage of the Python function
