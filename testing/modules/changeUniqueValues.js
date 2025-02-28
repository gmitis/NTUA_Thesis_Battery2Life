const fs = require('fs').promises;  // Importing fs.promises for asynchronous file operations

const unique_values = ["chemical_name", "name", "serial_number", "battery_name", "cell_name"];

const generateRandomUniqueString = () => {
  return Math.random().toString(36).substring(2, 10);
};

const modifyObject = (obj) => {
  if (Array.isArray(obj)) {
    return obj.map(modifyObject);
  } else if (obj !== null && typeof obj === 'object') {
    Object.keys(obj).forEach(key => {
      // If the current key is in our unique_values list, replace its value
      if (unique_values.includes(key)) {
        obj[key] = generateRandomUniqueString();
      } else {
        // Otherwise, recursively process the value in case it contains nested objects/arrays
        obj[key] = modifyObject(obj[key]);
      }
    });
    return obj;
  }
  // Return the value if it's a primitive type
  return obj;
};

// Function to load the input data and apply modifyObject
async function loadData() {
  try {
    // Read the valid and invalid input files using fs.promises.readFile
    const vi = JSON.parse(await fs.readFile("./data/valid_input.json", "utf8"));

    // Sequentially change unique values for valid and invalid input
    const valid_input = modifyObject(vi);

    // Write the modified data back to the respective files
    await fs.writeFile("./data/valid_input.json", JSON.stringify(valid_input, null, 2), "utf8");
    return valid_input
  } catch (error) {
    console.error("Error loading data:", error);
    return { valid_input: [] }; // Return empty arrays in case of error
  }
}


// Use the loadData function and ensure everything happens sequentially
async function initialize() {
  await loadData();
  console.log("Unique fields in input data changed successfully");
}

initialize();
