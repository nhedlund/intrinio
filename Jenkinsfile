pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''pip install -r requirements.txt
'''
      }
    }
    stage('Test') {
      steps {
        sh '.bin/runtests'
      }
    }
  }
}