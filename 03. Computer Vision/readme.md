
# 🧠 Lab 07 - Computer Vision with OpenCV and YOLOv8

Welcome to **Lab 07** of the SP25 Artificial Intelligence Course. This lab provides a deep dive into **computer vision**, combining traditional image processing techniques with deep learning-powered object detection using **YOLOv8**. You'll explore how to work with images and video using OpenCV and learn how to detect real-world objects using the state-of-the-art YOLOv8 model, leveraging Roboflow for dataset management and training.

---

## 🧭 Table of Contents

- [Objectives](#🎯-objectives)
- [Lab Overview](#📚-lab-overview)
  - [Part 1: OpenCV](#🔹-part-1-image-processing-with-opencv)
  - [Part 2: YOLOv8](#🔹-part-2-custom-object-detection-using-yolov8)
- [Requirements](#🛠️-requirements)
- [Getting Started](#🚀-getting-started)
- [Lab Tasks](#🧪-lab-tasks)
- [Evaluation Criteria](#📊-evaluation-criteria)
- [Use Case Ideas](#🧠-suggested-use-cases)
- [Resources](#📎-resources)
- [Instructor](#👨‍🏫-instructor)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- Understand fundamental concepts of image processing using OpenCV.
- Capture and manipulate images and videos in Python.
- Train custom object detection models using YOLOv8.
- Use Roboflow for dataset annotation, augmentation, and export.
- Perform inference using trained YOLOv8 models on real-world images or video.

---

## 📚 Lab Overview

### 🔹 Part 1: Image Processing with OpenCV

In this part, students will:

- Read and write images.
- Display images using OpenCV.
- Draw shapes (rectangle, circle, line) and annotate images with text.
- Capture live video from a webcam.
- Convert images to grayscale, RGB, or HSV formats.
- Detect edges using Canny Edge Detection.
- (Bonus) Use Haar Cascades for face detection.

📘 **Key Notebook**: `open_cv_lab.ipynb`

---

### 🔹 Part 2: Custom Object Detection using YOLOv8

In this part, students will:

- Understand the architecture and working of the YOLOv8 model.
- Use [Roboflow](https://roboflow.com/) to create, annotate, and manage datasets.
- Train the YOLOv8 model in Google Colab using Ultralytics.
- Evaluate model performance using metrics like mAP, Precision, and Recall.
- Perform inference on new images or live video.

📘 **Key Notebook**: `YOLOv8.ipynb`

---

## 🛠️ Requirements

Ensure the following libraries are installed:

```bash
pip install opencv-python
pip install ultralytics
pip install roboflow
```

You also need:
- A **Google Colab** account
- A **Roboflow** account (free version is sufficient)
- Labeled dataset (custom or from Roboflow's public dataset hub)

---

## 🚀 Getting Started

### Step 1: Clone the Repository

```bash
git clone https://github.com/Jamil226/SP25-AI.git
cd SP25-AI/Lab-07 - Computer Vision
```

### Step 2: Run the OpenCV Notebook
- Launch `open_cv_lab.ipynb` in **Jupyter Notebook** or **Colab**
- Complete all tasks (image manipulation, edge detection, video streaming)

### Step 3: Work with YOLOv8
- Launch `YOLOv8.ipynb` in **Google Colab**
- Follow steps to install YOLO, load dataset from Roboflow, train and test model

---

## 🧪 Lab Tasks

### 🔧 OpenCV Tasks
| Task No. | Task Description |
|----------|------------------|
| 1 | Read and display an image |
| 2 | Draw shapes and text on an image |
| 3 | Convert image to grayscale and detect edges |
| 4 | Capture live video from webcam |
| 5 | (Bonus) Detect faces using Haar Cascades |

### 🤖 YOLOv8 Tasks
| Task No. | Task Description |
|----------|------------------|
| 6 | Choose a real-world detection problem (e.g., Fire, Helmet, Mask) |
| 7 | Upload and annotate dataset on Roboflow |
| 8 | Export YOLOv8 dataset from Roboflow |
| 9 | Train YOLOv8 model using Colab |
| 10 | Test model with images or video and analyze results |

---

## 📊 Evaluation Criteria

| Criteria                          | Marks |
|-----------------------------------|-------|
| OpenCV Tasks                      | 10    |
| Dataset Annotation (Roboflow)     | 10    |
| Training Execution & Code Quality | 20    |
| Inference and Model Accuracy      | 10    |
| Report/Presentation                | 10    |
| **Total**                         | **60**|

---

## 🧠 Suggested Use Cases

Students can pick from 50+ use cases provided in the YOLOv8 Lab PDF. Some ideas:

- 🚧 Pothole Detection
- 🧑‍🏭 PPE/Helmet Detection
- 🚗 Number Plate Recognition
- 😷 Mask Detection
- 🐯 Wildlife Monitoring
- 🚒 Fire/Smoke Detection
- 🛒 Retail Theft Detection
- 🏫 Smart Classroom Monitoring

📄 **[View Full List (PDF)] (https://github.com/Jamil226/SP25-AI/blob/main/Lab-07%20-%20Computer%20Vision/YOLOv8/Yolo%20Algorithm%20-%20Lab.pdf)**

---

## 📎 Resources

- [Roboflow Website](https://roboflow.com/)
- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Train YOLOv8 in Colab - Roboflow Guide](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov12-object-detection-model.ipynb?ref=blog.roboflow.com)
- [Open Images Dataset](https://storage.googleapis.com/openimages/web/index.html)
- [COCO Dataset](https://cocodataset.org/#download)

---

## 👨‍🏫 Instructor

**Jamil**  
Instructor, SP25 Artificial Intelligence Course  
📧 Email: *[your email if desired]*  
🔗 [GitHub](https://github.com/Jamil226)

---

> 🧠 *“The future of AI is in visual understanding. With OpenCV and YOLOv8, we empower machines to see, understand, and make decisions just like humans.”*
