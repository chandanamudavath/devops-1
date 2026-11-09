pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                bat 'docker build -t myapp:latest ./exam'
            }
        }

        stage('Run') {
            steps {
                echo 'running the docker'
                bat 'docker rm -f mycontainer || exit 0'
                bat 'docker run -d --name mycontainer -p 5000:5000 myapp:latest'

            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}
