First image to build once per sprint for example to speed up build process do:

docker pull your_node_image:version

docker tag your_node_image:version my_own_repo/ubuntu_with_all_i_need_to_build:latest

docker push my_own_repo/ubuntu_with_all_i_need_to_build:latest
