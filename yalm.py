import yaml

kubernetes_conponents = {
    "pod": "basic building block of kubernetes",
    "service" : "an abstraction for dealing with pods",
    "volumne" : "a directory accessible to container in a pod",
    "namespace" : "a way to divide cluster resources between users"
}

with open("kubernetes_info.yarml", "w") as yarm_to_write:
    yaml.safe_dump(kubernetes_components, yaml_to_write, default_flow_style = False)