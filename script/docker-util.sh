function buildImage () {
  IMAGE_NAME=${1}
  DOCKERFILE_DIR=`realpath ${2}`

  echo building ${IMAGE_NAME} using ${DOCKERFILE_DIR}/Dockerfile
  pushd ${DOCKERFILE_DIR}
  docker build . -t ${IMAGE_NAME}
  popd

}
