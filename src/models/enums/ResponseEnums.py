from enum import Enum

class ResponseSignal(Enum):

    File_VALIDATED_SUCCESS = "file_validated_successfully"
    File_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    FILE_PROCESSING_SUCCESS = "processing_success"
    FILE_PROCESSING_FAILED = "processing_failed"
    NO_FILES_FOUND = "no_files_found"
    FILE_NOT_FOUND = "file_not_found"