# Email Webcam Detection

This project captures video from a webcam, detects movement, and sends an email with an image attachment when movement is detected. The project uses OpenCV for video processing and the `smtplib` library for sending emails.

## Requirements

- Python 3.x
- OpenCV
- smtplib
- imghdr
- email

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Nibir2405/email_webcam_detection.git
    cd email_webcam_detection
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Update the email credentials in `sending_email.py`:
    ```python
    EMAIL_ADDRESS = "your_email@example.com"
    PASSWORD = "your_password"
    Receiver = "recipient_email@example.com"
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Press `q` to quit the video feed.

## Project Structure

- `main.py`: The main script that captures video, detects movement, and triggers the email sending.
- `sending_email.py`: The script that handles sending emails with the captured image as an attachment.
- `images/`: Directory where captured images are stored temporarily.

## How It Works

1. The script captures video from the webcam.
2. It converts each frame to grayscale and applies Gaussian blur.
3. It calculates the difference between the current frame and the first frame to detect movement.
4. If movement is detected, it saves an image and sends an email with the image attached.
5. The script cleans up the `images/` directory after sending the email.

## Troubleshooting

- Ensure that you have enabled access for less secure apps in your email account settings.
- Check your SMTP server details and credentials.
- If you encounter issues with sending emails, try using a different email provider.

