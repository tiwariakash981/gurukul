from django.shortcuts import render
import pandas as pd
import pickle

# Load preprocessor and model
with open('courses/views/model_linear.pkl', 'rb') as file:
    model = pickle.load(file)

with open('courses/views/preprocessor.pkl', 'rb') as file:
    preprocessor = pickle.load(file)

def predict(request):
    prediction = None
    if request.method == 'POST':
        # Extract form data
        gender = request.POST.get('gender')
        race_ethnicity = request.POST.get('race_ethnicity')
        parental_level_of_education = request.POST.get('parental_level_of_education')
        lunch = request.POST.get('lunch')
        test_preparation_course = request.POST.get('test_preparation_course')
        reading_score = request.POST.get('reading_score')
        writing_score = request.POST.get('writing_score')

        # Validate and convert inputs
        try:
            reading_score = float(reading_score) if reading_score else 0.0
            writing_score = float(writing_score) if writing_score else 0.0
        except ValueError:
            reading_score, writing_score = 0.0, 0.0

        # Prepare input data
        input_data = pd.DataFrame(
            [[gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score]],
            columns=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course', 'reading_score', 'writing_score']
        )

        # Transform and predict
        transformed_data = preprocessor.transform(input_data)
        prediction = model.predict(transformed_data)[0]

    # Render template with prediction
    return render(request, 'courses/predict.html', context={'predict': prediction})