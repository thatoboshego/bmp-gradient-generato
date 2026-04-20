# Gradient BMP Image Generator 🎨

## 📌 Description

This project generates a 100x100 BMP image from scratch using Python. It draws a smooth color gradient between two user-defined points by calculating directional interpolation and writing raw pixel data into a BMP file format.

This project demonstrates low-level file handling, binary data manipulation, and basic computer graphics concepts.

---

## ⚙️ How It Works

The program:

1. Takes two points with RGB colors from command-line arguments
2. Computes a directional vector between the points
3. Uses projection to interpolate colors across the image
4. Generates pixel data row by row
5. Writes a valid BMP file manually using binary formatting

---

## 🧮 Key Concepts Used

* Vector direction and projection
* Color interpolation (RGB blending)
* Binary file writing
* BMP file format structure
* Command-line arguments (`sys.argv`)
* Data packing using `struct`

---

## ▶️ How to Run

### Requirements

* Python 3.x

### Run command:

```bash id="k3b9xa"
python image_generator.py "10,10=255,0,0" "90,90=0,0,255" output.bmp
```

---

## 🖼️ Example Output

A 100x100 BMP image with a smooth gradient between two colors based on the input points.

---

## 📁 Project Structure

```id="m7nqz1"
image_generator.py
README.md
output.bmp (generated file)
```

---

## 🚀 Future Improvements

* Support different image sizes
* Add diagonal and radial gradients
* Allow multiple color points
* Add GUI for input selection

---

## 👤 Author

Thato Boshego

---

## 📄 License

This project is open-source under the MIT License.
