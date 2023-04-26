from typing import Dict, Iterable, Optional, Union

from crowdin_api.api_resources.abstract.resources import BaseResource
from crowdin_api.api_resources.projects.enums import (
    HasManagerAccess,
    ProjectLanguageAccessPolicy,
    ProjectTranslateDuplicates,
    ProjectType,
    ProjectVisibility,
)
from crowdin_api.api_resources.projects.types import (
    NotificationSettings,
    ProjectPatchRequest,
    QACheckCategories,
    PropertyFileFormatSettings,
    XmlFileFormatSettings,
    DocxFileFormatSettings,
    MediaWikiFileFormatSettings,
    TxtFileFormatSettings,
    OtherFileFormatSettings,
    SpecificFileFormatSettings,
    ProjectFilePatchRequest,
)


class ProjectsResource(BaseResource):
    """
    Resource for Storages.

    Using projects, you can keep your source files sorted.
    Use API to manage projects, change their settings, or remove them if required.

    Link to documentation:
    https://developer.crowdin.com/api/v2/#tag/Projects

    """

    def get_projects_path(self, projectId: Optional[int] = None):
        if projectId is not None:
            return f"projects/{projectId}"

        return "projects"

    def list_projects(
        self,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        groupId: Optional[int] = None,
        userId: Optional[Union[int, str]] = None,
        hasManagerAccess: Optional[HasManagerAccess] = None,
    ):
        """
        List Projects.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.getMany
        """

        params = {"userId": userId, "hasManagerAccess": hasManagerAccess, "groupId": groupId}
        params.update(self.get_page_params(page=page, offset=offset, limit=limit))

        return self._get_entire_data(method="get", path=self.get_projects_path(), params=params)

    def add_project(self, request_data: Dict):
        """
        Add Project.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.post
        """

        return self.requester.request(
            method="post", path=self.get_projects_path(), request_data=request_data
        )

    def add_file_based_project(
        self,
        name: str,
        sourceLanguageId: str,
        type: Optional[ProjectType] = None,
        normalizePlaceholder: Optional[bool] = None,
        saveMetaInfoInSource: Optional[bool] = None,
        notificationSettings: Optional[NotificationSettings] = None,
        identifier: Optional[str] = None,
        targetLanguageIds: Optional[Iterable[str]] = None,
        visibility: Optional[ProjectVisibility] = None,
        languageAccessPolicy: Optional[ProjectLanguageAccessPolicy] = None,
        cname: Optional[str] = None,
        description: Optional[str] = None,
        translateDuplicates: Optional[ProjectTranslateDuplicates] = None,
        isMtAllowed: Optional[bool] = None,
        autoSubstitution: Optional[bool] = None,
        autoTranslateDialects: Optional[bool] = None,
        skipUntranslatedStrings: Optional[bool] = None,
        skipUntranslatedFiles: Optional[bool] = None,
        exportApprovedOnly: Optional[bool] = None,
    ):
        """
        Add Project(Files Based Project Form).

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.post
        """

        return self.add_project(
            request_data={
                "name": name,
                "sourceLanguageId": sourceLanguageId,
                "identifier": identifier,
                "type": type,
                "normalizePlaceholder": normalizePlaceholder,
                "saveMetaInfoInSource": saveMetaInfoInSource,
                "notificationSettings": notificationSettings,
                "targetLanguageIds": targetLanguageIds,
                "visibility": visibility,
                "languageAccessPolicy": languageAccessPolicy,
                "cname": cname,
                "description": description,
                "skipUntranslatedStrings": skipUntranslatedStrings,
                "skipUntranslatedFiles": skipUntranslatedFiles,
                "exportApprovedOnly": exportApprovedOnly,
                "translateDuplicates": translateDuplicates,
                "isMtAllowed": isMtAllowed,
                "autoSubstitution": autoSubstitution,
                "autoTranslateDialects": autoTranslateDialects,
            },
        )

    def add_strings_based_project(
        self,
        name: str,
        sourceLanguageId: str,
        identifier: Optional[str] = None,
        type: Optional[ProjectType] = None,
        targetLanguageIds: Optional[Iterable[str]] = None,
        visibility: Optional[ProjectVisibility] = None,
        languageAccessPolicy: Optional[ProjectLanguageAccessPolicy] = None,
        cname: Optional[str] = None,
        description: Optional[str] = None,
        translateDuplicates: Optional[ProjectTranslateDuplicates] = None,
        isMtAllowed: Optional[bool] = None,
        autoSubstitution: Optional[bool] = None,
        autoTranslateDialects: Optional[bool] = None,
        publicDownloads: Optional[bool] = None,
        hiddenStringsProofreadersAccess: Optional[bool] = None,
        useGlobalTm: Optional[bool] = None,
        skipUntranslatedStrings: Optional[bool] = None,
        skipUntranslatedFiles: Optional[bool] = None,
        exportApprovedOnly: Optional[bool] = None,
        inContextProcessHiddenStrings: Optional[bool] = None,
        inContextPseudoLanguageId: Optional[str] = None,
        qaCheckIsActive: Optional[bool] = None,
        qaCheckCategories: Optional[QACheckCategories] = None,
        languageMapping: Optional[Dict] = None,
        glossaryAccess: Optional[bool] = None,
        notificationSettings: Optional[NotificationSettings] = None,
    ):
        """
        Add Project(Strings Based Project Form).

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.post
        """

        return self.add_project(
            request_data={
                "name": name,
                "sourceLanguageId": sourceLanguageId,
                "identifier": identifier,
                "type": type,
                "targetLanguageIds": targetLanguageIds,
                "visibility": visibility,
                "languageAccessPolicy": languageAccessPolicy,
                "cname": cname,
                "description": description,
                "skipUntranslatedStrings": skipUntranslatedStrings,
                "skipUntranslatedFiles": skipUntranslatedFiles,
                "exportApprovedOnly": exportApprovedOnly,
                "translateDuplicates": translateDuplicates,
                "isMtAllowed": isMtAllowed,
                "autoSubstitution": autoSubstitution,
                "autoTranslateDialects": autoTranslateDialects,
                "publicDownloads": publicDownloads,
                "hiddenStringsProofreadersAccess": hiddenStringsProofreadersAccess,
                "useGlobalTm": useGlobalTm,
                "inContextProcessHiddenStrings": inContextProcessHiddenStrings,
                "inContextPseudoLanguageId": inContextPseudoLanguageId,
                "qaCheckIsActive": qaCheckIsActive,
                "qaCheckCategories": qaCheckCategories,
                "languageMapping": languageMapping,
                "glossaryAccess": glossaryAccess,
                "notificationSettings": notificationSettings,
            },
        )

    def get_project(self, projectId: int):
        """
        Get Project.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.get
        """

        return self.requester.request(
            method="get", path=self.get_projects_path(projectId=projectId)
        )

    def delete_project(self, projectId: int):
        """
        Delete Project.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.delete
        """

        return self.requester.request(
            method="delete", path=self.get_projects_path(projectId=projectId)
        )

    def edit_project(self, projectId: int, data: Iterable[ProjectPatchRequest]):
        """
        Edit Project.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.patch
        """
        return self.requester.request(
            method="patch",
            path=self.get_projects_path(projectId=projectId),
            request_data=data,
        )

    def get_project_file_path(
        self,
        projectId: int,
        fileFormatSettingsId: Optional[int] = None
    ):
        if fileFormatSettingsId is not None:
            return f"projects/{projectId}/file-format-settings/{fileFormatSettingsId}"

        return f"projects/{projectId}/file-format-settings"

    def download_project_file_custom_segmentation(self, projectId: int, fileFormatSettingsId: int):
        """
        Download Project File Format Settings Custom Segmentation.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.custom-segmentations.get
        """
        path = self.get_project_file_path(
            projectId=projectId,
            fileFormatSettingsId=fileFormatSettingsId
        )

        return self.requester.request(
            method="get",
            path=f"{path}/custom-segmentations",
        )

    def reset_project_file_custom_segmentation(self, projectId: int, fileFormatSettingsId: int):
        """
        Reset Project File Format Settings Custom Segmentation.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.custom-segmentations.delete
        """
        path = self.get_project_file_path(
            projectId=projectId,
            fileFormatSettingsId=fileFormatSettingsId
        )

        return self.requester.request(
            method="delete",
            path=f"{path}/custom-segmentations",
        )

    def list_project_files(
        self,
        projectId: int,
        page: Optional[int] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        """
        List Project File Format Settings.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.getMany
        """
        params = self.get_page_params(page=page, offset=offset, limit=limit)

        return self._get_entire_data(
            method="get",
            path=self.get_project_file_path(projectId=projectId),
            params=params
        )

    def add_project_file(
        self,
        projectId: int,
        format: str,
        settings: Union[
            PropertyFileFormatSettings, XmlFileFormatSettings, SpecificFileFormatSettings,
            DocxFileFormatSettings, MediaWikiFileFormatSettings, TxtFileFormatSettings,
            OtherFileFormatSettings
        ]
    ):
        """
        Add Project File Format Settings.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.post
        """

        return self.requester.request(
            method="post",
            path=self.get_project_file_path(projectId=projectId),
            request_data={"format": format, "settings": settings}
        )

    def get_project_file(self, projectId: int, fileFormatSettingsId: int):
        """
        Get Project File Format Settings.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.get
        """

        return self.requester.request(
            method="get",
            path=self.get_project_file_path(
                projectId=projectId,
                fileFormatSettingsId=fileFormatSettingsId
            ),
        )

    def delete_project_file(self, projectId: int, fileFormatSettingsId: int):
        """
        Delete Project File Format Settings.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.delete
        """

        return self.requester.request(
            method="delete",
            path=self.get_project_file_path(
                projectId=projectId,
                fileFormatSettingsId=fileFormatSettingsId
            ),
        )

    def edit_project_file(
        self,
        projectId: int,
        fileFormatSettingsId: int,
        data: Iterable[ProjectFilePatchRequest]
    ):
        """
        Edit Project File Format Settings.

        Link to documentation:
        https://developer.crowdin.com/api/v2/#operation/api.projects.file-format-settings.patch
        """

        return self.requester.request(
            method="patch",
            path=self.get_project_file_path(
                projectId=projectId,
                fileFormatSettingsId=fileFormatSettingsId
            ),
            request_data=data,
        )
