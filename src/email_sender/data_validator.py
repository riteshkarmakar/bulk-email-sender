from schemas import EmailData
import email_sender.utils as utils


class InvalidDataException(Exception):
    pass


class DataValidator:
    def __init__(self, email_data: EmailData):
        self.email_data = email_data
        self.dataframe = email_data["data_frame"]
        self.subject_placeholders = utils.get_placeholders(email_data["subject_template"])
        self.body_placeholders = utils.get_placeholders(email_data["plain_body_template"])

    def validate(self) -> None:
        self.validate_headers()
        self.ensure_no_empty_cells()
        self.validate_emails()
        self.validate_attachments()

    def validate_headers(self) -> None:
        """Ensure that email, attachment (if any) and placeholder columns are present in the dataframe."""
        email_column_name = self.email_data["email_column_name"]
        attachment_column_name = self.email_data.get("attachment_column_name")
        headers = list(self.dataframe)

        for column_name in (self.subject_placeholders + self.body_placeholders):
            if column_name not in headers:
                raise InvalidDataException(
                    f"<b>Invalid Placeholder</b>: No column found named <b>{column_name!r}</b> in the selected data."
                )
        if email_column_name not in headers:
            raise InvalidDataException(
                f"<b>Invalid Email Column Name</b>: No column found named <b>{column_name!r}</b> in the selected data."
            )
        if attachment_column_name and attachment_column_name not in headers:
            raise InvalidDataException(
                f"<b>Invalid Attachment Column Name</b>: No column found named <b>{column_name!r}</b> in the selected data."
            )

    def ensure_no_empty_cells(self) -> None:
        for column_name in self.subject_placeholders + self.body_placeholders + [self.email_data["email_column_name"]]:
            if self.dataframe[column_name].isnull().any():
                raise InvalidDataException(
                    f"<b>Empty Cell(s) Found</b>: There are empty cells in the <b>{column_name!r}</b> column of the the selected data."
                )

    def validate_emails(self) -> None:
        for email_id in self.dataframe[self.email_data["email_column_name"]].tolist():
            if not utils.is_email(str(email_id).strip()):
                raise InvalidDataException(f"<b>Invalid Email ID found in the selected data</b>: {email_id!r}")

        for email_id in self.email_data["cc_emails"]:
            if not utils.is_email(email_id.strip()):
                raise InvalidDataException(f"<b>Invalid Cc Email ID</b>: {email_id!r}")
            
        for email_id in self.email_data["bcc_emails"]:
            if not utils.is_email(email_id.strip()):
                raise InvalidDataException(f"<b>Invalid Bcc Email ID</b>: {email_id!r}")
            
    def validate_attachments(self) -> None:
        attachment_column_name = self.email_data.get("attachment_column_name")
        attachment_folder = self.email_data.get("attachment_folder")
        if not attachment_column_name:
            return
        
        # Iterate over the comma separated paths in the attachment column of the dataframe
        for comma_separated_paths in self.dataframe[attachment_column_name].tolist():
            if not comma_separated_paths: # Ignore the empty cells
                continue

            # Split the comma-separated paths and process each path by cleaning leading/trailing spaces and quotes
            for path in utils.get_paths_from_string(comma_separated_paths):
                if not path.is_absolute():
                    if attachment_folder:
                        # Combine the attachment folder with the relative path to get the full path
                        path = attachment_folder / path
                    else:
                        # Raise an exception if the path is relative and not attachment folder is provided.
                        raise InvalidDataException(
                            "<b>No Attachment Folder is Selected</b>: attachment_folder must be selected if relative paths like "
                            f"<b>{path.as_posix()!r}</b> are provided in the {attachment_column_name} column of the selected data."
                        )

                # Check if the file exists or not
                if not path.is_file():
                    raise InvalidDataException(f"<b>Invalid Attachment File Path</b>: {str(path)!r}.")
                
                # Check the file size and ensure it's not too large (over 20 MB)
                file_size = round(path.stat().st_size / 1024 / 1024, 2)
                SIZE_LIMIT = 20
                if file_size > SIZE_LIMIT:
                    raise InvalidDataException(
                        f"<b> File Size Limit Exceeded</b>: The file <b>{path.as_posix()!r}</b> is of <b>{file_size}MB</b> "
                        f"but the maximum file size allowed is {SIZE_LIMIT}MB."
                    )
