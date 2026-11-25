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

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    sh '''
                        set +x
                        echo "$DOCKER_TOKEN" | docker login -u "$DOCKER_USER" --password-stdin
                        trap 'docker logout' EXIT
                        docker tag devops-flask-app muffashal/devops-flask-app:latest
                        docker push muffashal/devops-flask-app:latest
                    '''
                }
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
