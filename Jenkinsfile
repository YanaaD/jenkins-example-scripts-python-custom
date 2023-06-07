pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('Task1') {
      steps {
        bat 'python Task1.py'
      }
    }
  }
}
