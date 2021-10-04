echo Installing Sonar Scanner
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.3.0.2102-linux.zip
unzip sonar-scanner-cli-4.3.0.2102-linux.zip
export PATH=$(pwd)/sonar-scanner-4.3.0.2102-linux/bin:$PATH
sonar-scanner -Dsonar.projectKey=$SONAR_PROJECT_KEY -Dsonar.sources=. -Dsonar.host.url=$SONARQUBE_HOST -Dsonar.login=$SONARQUBE_LOGIN
echo Done!