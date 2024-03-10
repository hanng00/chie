variable "container_name" {
  type    = string
  default = "chie-backend"
}

variable "container_port" {
  type    = number
  default = 8000
}

variable "name" {
  type    = string
  default = "chie-backend-api"
}

variable "region" {
  type    = string
  default = "eu-north-1"
}

variable "container_env_vars" {
  type = map(any)
  default = {
  name = "PORT", value = "8000" }

}
