pipeline {
    
    agenty any
    
    environment {
        MAIN_PATH = "/var/lib/jenkins/workspace/vibration-analysis-interface"
    }
    
    stages {

        // Stopping and re-running the UI container
        stage("Setup - UI") {
            when {
                anyOf {
                    changeset "**/ui/**"
                    changeset "**/Jenkinsfile"
                }
            }
            steps {
                sh "sudo docker compose -f $MAIN_PATH/ui/docker-compose.yaml down || true"
                sh "sudo docker rm ui-service || true"
                sh "sudo docker rmi vai/ui:latest || true"
                sh "sudo docker-compose -f $MAIN_PATH/ui/docker-compose.yaml up -d"
            }
        }

        // Stopping and re-running the processing container
        stage("Setup - Processing") {
            when {
                anyOf {
                    changeset "**/processing/**"
                    changeset "**/Jenkinsfile"
                }
            }
            steps {
                sh "sudo docker compose -f $MAIN_PATH/processing/docker-compose.yaml down || true"
                sh "sudo docker rm processing-service || true"
                sh "sudo docker rmi vai/processing:latest || true"
                sh "sudo docker-compose -f $MAIN_PATH/processing/docker-compose.yaml up -d"
            }
        }

    }

}