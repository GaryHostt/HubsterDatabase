variable "tenancy_ocid" {}
variable "user_ocid" {}
variable "fingerprint" {}
variable "private_key_path" {}
variable "compartment_id" {}
variable "region" {}
variable "autonomous_database_display_name" {}
variable "autonomous_database_db_name" {}
variable "autonomous_database_admin_password" {}
provider "oci" {
  version          = ">= 3.0.0"
  tenancy_ocid     = "${var.tenancy_ocid}"
  user_ocid        = "${var.user_ocid}"
  fingerprint      = "${var.fingerprint}"
  private_key_path = "${var.private_key_path}"
  region           = "${var.region}"
}

resource "oci_database_autonomous_database" "test_autonomous_database" {
    #Required
    admin_password = "${var.autonomous_database_admin_password}"
    compartment_id = "${var.compartment_id}"
    cpu_core_count = "1"
    data_storage_size_in_tbs = "1"
    db_name = "${var.autonomous_database_db_name}"

    #Optional
    db_workload = "OLTP"
    display_name = "${var.autonomous_database_display_name}"
    is_auto_scaling_enabled = "false"
}