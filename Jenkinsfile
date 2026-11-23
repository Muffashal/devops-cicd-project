
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

        stage('Deploy Application') {
            steps {
                sh '''
                    docker rm -f flask-container || true

                    docker run -d \
                      --name flask-container \
                      -p 5000:5000 \
                      --restart unless-stopped \
                      devops-flask-app
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 3
                    curl --fail http://localhost:5000/health
                '''
            }
        }
    }
}
