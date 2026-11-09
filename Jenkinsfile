Pipeline{
    agent any
    stages('Build'){
        steps{
            echo 'Building the application...'
            bat 'docker build -t myapp:latest .'
        }
        stages('Run'){
            steps{
                echo 'running the docker'
                bat 'docker rm -f mycontainer || exit 0'
                bat 'docker run -d -p 5000:5000 myapp:latest'
            }
        }
    }
    POST{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}