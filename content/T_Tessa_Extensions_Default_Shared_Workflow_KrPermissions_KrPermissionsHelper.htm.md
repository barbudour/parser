# KrPermissionsHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static class KrPermissionsHelper
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class KrPermissionsHelper
C++ __Копировать
    [ExtensionAttribute]
    public ref class KrPermissionsHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type KrPermissionsHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionsHelper
##  __Методы
[GetGrantedPermissionsMessage](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_GetGrantedPermissionsMessage.htm)|
Формирует сообщение о выданных правах.  
---|---  
[GetNotEnoughPermissionsErrorMessage](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_GetNotEnoughPermissionsErrorMessage.htm)|
Формирует сообщение об ошибке недостаточности прав.  
[GetPermissionsSplittedByNewLineStartsWithNewLine](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_GetPermissionsSplittedByNewLineStartsWithNewLine.htm)|
Возвращает локализованные разрешения разделенные переводом на новую строку.
Начинает новой строкой.  
[GetUnavailableTypesAsync](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_GetUnavailableTypesAsync.htm)|
Возвращает список недоступных имен для создания эффективных (типы карточек, не
использующие типы документов и типы документов) типов.  
[SetDocTypeID](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_SetDocTypeID.htm)|
Задаёт информацию по идентификатору типа документа в токене безопасности.  
[TryGetDocTypeID](M_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_TryGetDocTypeID.htm)|
Возвращает идентификатор типа документа из токена безопасности.  
## __Поля
[AddRefreshTokenKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_AddRefreshTokenKey.htm)|
Ключ, по которому хранится признак того, что в ответе на сохранение карточки
нужно приложить токен для рефреша карточки.  
---|---  
[AddTopicPermissionsCalculated](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_AddTopicPermissionsCalculated.htm)|  
[CalculateAddTopicPermissions](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_CalculateAddTopicPermissions.htm)|  
[CalculateEditMyMessagesPermissions](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_CalculateEditMyMessagesPermissions.htm)|  
[CalculatePermissionsMark](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_CalculatePermissionsMark.htm)|  
[CalculateResolutionPermissionsMark](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_CalculateResolutionPermissionsMark.htm)|  
[CalculateSuperModeratorPermissions](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_CalculateSuperModeratorPermissions.htm)|  
[DocTypeIDKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_DocTypeIDKey.htm)|
Ключ, по которому в
[Info](P_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrToken_Info.htm)
содержится идентификатор типа документа. Тип значения:
[Nullable<T>](https://learn.microsoft.com/dotnet/api/system.nullable-1), где T
- [Guid](https://learn.microsoft.com/dotnet/api/system.guid).  
[DropPermissionsCacheMark](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_DropPermissionsCacheMark.htm)|  
[EditMyMessagesPermissionsCalculated](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_EditMyMessagesPermissionsCalculated.htm)|  
[FailedMandatoryRulesKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_FailedMandatoryRulesKey.htm)|  
[NewCardSourceKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_NewCardSourceKey.htm)|  
[PermissionsCalculatedMark](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_PermissionsCalculatedMark.htm)|  
[SaveWithPermissionsCalcFlag](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_SaveWithPermissionsCalcFlag.htm)|  
[ServerTokenKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_ServerTokenKey.htm)|  
[SuperModeratorPermissionsCalculated](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_SuperModeratorPermissionsCalculated.htm)|  
[SystemTable](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_SystemTable.htm)|  
[UnavaliableTypesKey](F_Tessa_Extensions_Default_Shared_Workflow_KrPermissions_KrPermissionsHelper_UnavaliableTypesKey.htm)|  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Shared.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrPermissions.htm)
