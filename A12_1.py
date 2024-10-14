import requests
r1 = requests.get("https://gsom.spbu.ru/en/")

# Save the content to a new variable
r1_content = r1.content

# Convert the content to a string
string_content = r1_content.decode("utf-8") # Assuming UTF-8 encoding

#1. Count how many links to png images
count = string_content.count(".png")
print(f"1) The webpage contains {count} '.png'")

index = string_content.find(".png")
#print(index)
#print(string_content[342])

start_index = index - 27
end_index = index + 4
element = string_content[start_index:end_index]
print(f"2) The first link to '.png' image is: '{element}'")

full_element = "https://gsom.spbu.ru" + element
print(f"The full link to the image is: {full_element}")

#steal the image
r2 = requests.get(full_element)
file = open("/home/jovyan/Assig12/favicon.png", "wb")
file.write(r2.content)

print("The image was successfully stolen")