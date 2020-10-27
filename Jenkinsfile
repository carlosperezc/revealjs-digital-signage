node('slave') {
  def appName = 'revealjs-digital-signage'
  def imageTag = "alivx/${appName}:${env.BRANCH_NAME}.${env.BUILD_NUMBER}"

  checkout scm

  stage 'Build image'
  sh("docker build -t ${imageTag} .")

  stage "Deploy Application"
  switch (env.BRANCH_NAME) {
    // Roll out to staging
    case "staging":
        sh("docker run -d --name=${appName} -p 5000:5000 ${imageTag}")
        input 'looks good ?'
        sh("docker rm -f ${appName}")
        break

    // Roll out to production
    case "master":
        input 'are you sure ?'
        sh("docker rm -f ${appName}")
        sh("docker run -d --name=${appName} -p 5000:5000 ${imageTag}")
        break

    // Roll out a dev environment
    default:
        // Create namespace if it doesn't exist
        sh("docker ps")
  }
}