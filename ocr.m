% Step 1: Read the image
img = imread('/MATLAB Drive/flip2.png');  % Use the correct path to your image

% Step 2: Display the image to verify it's loaded correctly
imshow(img);  % Optional: Displays the image to ensure it's properly loaded

% Step 3: Check the class/type of the image to make sure it's supported
img_class = class(img);
disp(['Image class: ', img_class]);

% Step 4: If the image is not in uint8 format, convert it
if ~isa(img, 'uint8')
    img = uint8(img);
    disp('Image converted to uint8 format.');
end

% Step 5: If the image is in RGB format (i.e., 3 color channels), convert it to grayscale
if size(img, 3) == 3  % Check if the image has 3 channels (RGB)
    img = rgb2gray(img);  % Convert the image to grayscale
    disp('Image converted to grayscale.');
end

% Step 6: Apply OCR to the image
txt = ocr(img);  % Pass the processed image to the OCR function

% Step 7: Display the recognized text
disp('Extracted Text:');
disp(txt.Text);
