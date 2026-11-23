
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-flask-app .'
            }
        }

        stage('Test Application') {
            steps {
                sh 'docker image inspect devops-flask-app'
            }
        }
    }
}
