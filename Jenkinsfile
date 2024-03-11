pipeline {
    agent any

    stages {
        stage('Checkout repository') {
            steps {
                //checkout
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/amnasalahudin/i200488_mlops_task02.git']])
            }
        }

        stage('Install dependencies') {
            steps {
                // Install the required dependencies
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                // Execute the tests
                sh 'pytest test.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    deploy(env.BRANCH_NAME)
                }
            }
        }
    }
}

def deploy(String branchName) {
    if (branchName == 'master') {
        echo "Deploying to production"
       // deploy
    } else if (branchName == 'dev') {
        echo "Deploying to UAT"
      //deploy
    } else {
        echo "Deploying to a non-production/non-UAT branch: ${branchName}"
       //deploy
    }
}
