from flask import Flask, request, render_template, redirect, url_for
from src.pipeline.test_pipeline import TestPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predictscore', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')

    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('race_ethnicity'),
            parental_level_of_education=request.form.get('parental_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            writing_score=request.form.get('writing_score'),
            reading_score=request.form.get('reading_score')
        )
        
        pred_df = data.get_data_as_dataframe()
        print("Before Prediction")
        print(pred_df)
        
        predict_pipeline = TestPipeline()
        res = predict_pipeline.main(pred_df)

        print("After Prediction")
        return redirect(url_for('results', result = str(res[0])))
    
@app.route('/results')
def results():
    final_result = request.args.get('result')
    return render_template('result.html', results=final_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)