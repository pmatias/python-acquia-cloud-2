#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Manipulate environments and perform related actions."""

from requests.sessions import Session

from acapi2.resources.acquiaresource import AcquiaResource


class Environment(AcquiaResource):
    def backups(self, db_name: str) -> Session:
        """
        Return a list of backups.

        :param db_name: Database name, typically lower snake case.
        """
        uri = f"{self.uri}/databases/{db_name}/backups"
        return self.request(uri=uri, method="GET").json()

    def backup_details(self, db_name: str, backup_id: str) -> Session:
        """
        Return details about a specific backup
        :param db_name: Database name, typically lower snake case.
        :param backup_id: Database backup id.
        """
        uri = f"{self.uri}/databases/{db_name}/backups/{backup_id}"
        return self.request(uri=uri, method="GET").json()

    def backup_download(self, db_name: str, backup_id: str) -> Session:
        """
        Get link to be able to download backup.

        :param db_name: Database name, typically lower snake case.
        :param backup_id: Database backup id.
        :return: Acquia response
        """
        uri = (
            f"{self.uri}/databases/{db_name}/backups/{backup_id}/"
            f"actions/download"
        )
        return self.request(uri=uri, method="GET").json()

    def code_switch(self, branch_tag: str) -> Session:
        """
        Switch code on this environment to a different branch or release tag.

        :param branch_tag: The tag to switch to.
        """
        uri = f"{self.uri}/code/actions/switch"
        data = {"branch": branch_tag}

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def configure(self, data: dict) -> Session:
        """
        Modify configuration settings for an environment.

        :param data: Configuration parameters.
        """
        return self.request(uri=self.uri, method="PUT", data=data)

    def create_backup(self, db_name: str) -> Session:
        """
        Create a backup

        :param db_name: Database name, typically lower snake case.
        """
        uri = f"{self.uri}/databases/{db_name}/backups"
        return self.request(uri=uri, method="POST", data={}).json()

    def create_domain(self, domain: str) -> Session:
        """
        Add a domain to the environment.

        :param domain: Domain to add to the environment.
        """
        uri = f"{self.uri}/domains"
        data = {"hostname": domain}
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def create_log_forwarding_destinations(
        self,
        label: str,
        sources: list,
        consumer: str,
        credentials: dict,
        address: str,
    ) -> Session:
        """
        Create a log forwarding destination.
        :param label: Human-friendly identifier of the destination
        :param sources: List of log sources to forward
        :param consumer: Application or provider consuming the logs.
        :param credentials: Dictionary of certificate,key and token.
        :param address: URL or host name and port of the destination.
        :param destination_uuid: Log forwarding destination uuid for given env.
        """
        uri = f"{self.uri}/log-forwarding-destinations"
        data = {
            "label": label,
            "sources": sources,
            "consumer": consumer,
            "credentials": credentials,
            "address": address,
        }
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def databases(self) -> Session:
        """
        Retrieve a list of databases.
        """
        uri = f"{self.uri}/databases"
        return self.request(uri=uri, method="GET").json()

    def delete_backup(self, db_name: str, backup_id: str) -> Session:
        """
        Delete a backup

        :param db_name: Database name, typically lower snake case.
        :param backup_id: Database backup id.
        """
        uri = f"{self.uri}/databases/{db_name}/backups/{backup_id}"
        return self.request(uri=uri, method="DELETE").json()

    def delete_domain(self, domain: str) -> Session:
        """
        Remove the domain from the environment.

        :param domain: Domain name to delete.
        """
        uri = f"{self.uri}/domains/{domain}"
        response = self.request(uri=uri, method="DELETE")

        return response

    def delete_log_forwarding_destinations(
        self,
        destination_uuid: str,
    ) -> Session:
        """
        Delete a log forwarding destination.

        :param destination_uuid: log forwarding destination uuid for given env.
        """
        uri = f"{self.uri}/log-forwarding-destinations/{destination_uuid}"
        response = self.request(uri=uri, method="DELETE")

        return response

    def clear_varnish_domain(self, domain: str) -> Session:
        """
        Clear the Varnish cache for the domain attached to this environment.

        :param domain: Domain name.
        """
        uri = f"{self.uri}/domains/{domain}/actions/clear-varnish"
        data = {"hostname": domain}
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def clear_varnish_domains(self, domains: list) -> Session:
        """
        Clear the Varnish cache for multiple domains
         attached to this environment.

        :param domains: Domain name list.
        """
        uri = f"{self.uri}/domains/actions/clear-varnish"
        data = {"domains": domains}

        response = self.request(uri=uri, method="POST", data=data)

        return response

    def destroy(self):
        """
        Delete a CD environment.
        """
        response = self.request(uri=self.uri, method="DELETE")

        return response

    def deploy_code(self, id_from: str) -> Session:
        """
        Deploy code to this environment.

        :param id_from: uuid for the environment to deploy code from.
        """
        uri = f"{self.uri}/code"
        data = {"source": id_from}

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def deploy_database(self, id_from: str, db_name: str) -> Session:
        """
        Copy a database to this environment.

        :param id_from: uuid for the environment to deploy the db from.
        :param db_name: the database name to use.
        """
        uri = f"{self.uri}/databases"
        data = {"name": db_name, "source": id_from}

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def deploy_files(self, id_from: str) -> Session:
        """
        Copy files to this environment.

        :param id_from: uuid for the environment to deploy the files from.
        """
        uri = f"{self.uri}/files"
        data = {"source": id_from}

        response = self.request(uri=uri, method="POST", data=data)
        return response

    def get_crons(self) -> dict:
        """
        Return a list of the cron jobs on an environment.
        """
        uri = f"{self.uri}/crons"

        response = self.request(uri=uri)
        return response.json()

    def get_log_forwarding_destinations(self) -> dict:
        """
        Return a collection of log forwarding destinations.
        """
        uri = f"{self.uri}/log-forwarding-destinations"

        response = self.request(uri=uri)
        return response.json()

    def get_servers(self) -> dict:
        """
        Return a list of servers.
        """
        uri = f"{self.uri}/servers"

        response = self.request(uri=uri)
        return response.json()

    def get_php_version(self) -> dict:
        """
        Get the PHP version number.
        """
        uri = f"{self.uri}/"

        response = self.request(uri=uri)
        env_config = response.json()
        return {"php_version": env_config["configuration"]["php"]["version"]}

    def set_php_version(self, version: str) -> Session:
        """
        Set the PHP version.

        :param version: PHP version number to use.
        """
        data = {"version": version}

        return self.configure(data)

    def update_log_forwarding_destinations(
        self,
        label: str,
        sources: list,
        consumer: str,
        credentials: dict,
        address: str,
        destination_uuid: str,
    ) -> Session:
        """
        Update a log forwarding destination.
        :param label: Human-friendly identifier of the destination
        :param sources: List of log sources to forward
        :param consumer: Application or provider consuming the logs.
        :param credentials: Dictionary of certificate,key and token.
        :param address: URL or host name and port of the destination.
        :param destination_uuid: Log forwarding destination uuid for given env.
        """
        uri = f"{self.uri}/log-forwarding-destinations/{destination_uuid}"
        data = {
            "label": label,
            "sources": sources,
            "consumer": consumer,
            "credentials": credentials,
            "address": address,
        }
        response = self.request(uri=uri, method="PUT", data=data)

        return response

    def delete_cron(self, cron_id: str) -> Session:
        """
        Deletes a cron job.
        :cron_id: An ID that uniquely identifies a cron job.
        """
        uri = f"{self.uri}/crons/{cron_id}"
        response = self.request(uri=uri, method="DELETE")

        return response

    def disable_cron(self, cron_id: str) -> Session:
        """
        Disables a cron job.
        :cron_id: An ID that uniquely identifies a cron job.
        """
        uri = f"{self.uri}/crons/{cron_id}/actions/disable"
        response = self.request(uri=uri, method="POST", data="")

        return response

    def enable_cron(self, cron_id: str) -> Session:
        """
        Enables a cron job.
        :cron_id: An ID that uniquely identifies a cron job.
        """
        uri = f"{self.uri}/crons/{cron_id}/actions/enable"
        response = self.request(uri=uri, method="POST", data="")

        return response

    def get_ssl_settings(self) -> dict:
        """
        Return the SSL settings for the environment.
        """
        uri = f"{self.uri}/ssl"
        response = self.request(uri=uri)

        return response.json()

    def get_ssl_certs(self) -> dict:
        """
        Return a list of SSL certificates.
        """
        uri = f"{self.uri}/ssl/certificates"
        response = self.request(uri=uri)

        return response.json().get("_embedded", {}).get("items")

    def get_ssl_cert(self, cert_id: str) -> dict:
        """
        Return an SSL cert.
        """
        uri = f"{self.uri}/ssl/certificates/{cert_id}"
        response = self.request(uri=uri)

        return response.json()

    def install_ssl_cert(
        self,
        label: str,
        certificate: str,
        private_key: str,
        ca_certificates: str = None,
        legacy: bool = False,
        csr_id: int = None,
    ) -> Session:
        """
        Add a new SSL cert to the environment.
        :param: label: Human-friendly identifier for the cert.
        :param: certificate: The certificate in PEM format.
        :param: private_key: The private keyfor the cert in PEM format.
        :param: ca_certificates: Any chain certificates, in PEM format.
         Defaults to None.
        :param: legacy: Legacy in the sense of Acquia's legacy architecture,
         not an old version of the SSL or TLS standards. See Acquia's docs
         for more details. Defaults to False.
        :param: csr_id: Associate with an existing installed CSR. Defaults
         to None.
        """
        uri = f"{self.uri}/ssl/certificates"
        data = {
            "legacy": legacy,
            "label": label,
            "certificate": certificate,
            "private_key": private_key,
        }
        if csr_id is not None:
            data["csr_id"] = csr_id
        if ca_certificates is not None:
            data["ca_certificates"] = ca_certificates
        response = self.request(uri=uri, method="POST", data=data)

        return response

    def delete_ssl_cert(self, cert_id: str) -> Session:
        """
        Remove an SSL cert.
        :param: cert_id: The Acquia certificate ID.
        """
        uri = f"{self.uri}/ssl/certificates/{cert_id}"
        response = self.request(uri=uri, method="DELETE")

        return response

    def activate_ssl_cert(self, cert_id: str) -> Session:
        """
        Activate a previously installed SSL cert.
        :param: cert_id: The Acquia certificate ID.
        """
        uri = f"{self.uri}/ssl/certificates/{cert_id}/actions/activate"
        response = self.request(uri=uri, method="POST", data={})

        return response

    def deactivate_ssl_cert(self, cert_id: str) -> Session:
        """
        Deactivate a previously installed SSL cert.
        :param: cert_id: The Acquia certificate ID.
        """
        uri = f"{self.uri}/ssl/certificates/{cert_id}/actions/deactivate"
        response = self.request(uri=uri, method="POST", data={})

        return response
