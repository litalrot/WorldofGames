pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git clone
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'docker build -t game-app .'
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker-compose up -d web'
                    sh 'sleep 10'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python e2e.py'
                }
            }
            post {
                failure {
                    echo "E2E tests failed!"
                    error "Tests failed"
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Push to Docker Hub or deploy to production
                    sh 'docker tag game-app lit7/game-app'
                    sh 'docker push lit7/game-app'
                }
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
            sh 'docker system prune -f'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}