pipeline {
agent any

stages {
    stage('Preparar') {
        steps {
         //  bat 'where python'
           bat '"C:\\Python312\\python.exe" -m pip install pandas'  
           bat '"C:\\Python312\\python.exe" -m pip install openpyxl'
         
        }
    }
    
    stage('READ') {
        steps {

          bat '"C:\\Python312\\python.exe" C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\DataPipeline_Store_LT\\data_read.py'
    
        }
    }
        
         stage('TRANSFORM') {
        steps {

          bat '"C:\\Python312\\python.exe" C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\DataPipeline_Store_LT\\data_transform.py'
    
        }
    }
         stage('EXPORT') {
        steps {

          bat '"C:\\Python312\\python.exe" C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\DataPipeline_Store_LT\\data_export.py'
    
        }
    }
    
}
}