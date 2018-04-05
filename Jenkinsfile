pipeline {
  agent {
    docker {
      image 'continuumio/anaconda3:5.1.0'
      args '-v $HOME/.cache/intrinio:/root/.cache/intrinio'
    }
  }
  stages {
    stage('Build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh './bin/runtests'
      }
    }
  }
}

