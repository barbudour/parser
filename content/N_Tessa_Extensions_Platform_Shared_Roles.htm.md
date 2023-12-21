# Tessa.Extensions.Platform.Shared.Roles - пространство имён
Общие зависимости и константы платформы, связанные с карточками ролей.
##  __Классы
[ClientAndConsoleRegistrator](T_Tessa_Extensions_Platform_Shared_Roles_ClientAndConsoleRegistrator.htm)|  
---|---  
[ClientRoleManagerRequestHelper](T_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerRequestHelper.htm)|
Типы стандартных запросов к сервису карточек через метод
[RequestAsync(CardRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_RequestAsync.htm) для
сервиса
[ClientRoleManagerService](T_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerService.htm)
и другие вспомогательные константы.  
[ClientRoleManagerService](T_Tessa_Extensions_Platform_Shared_Roles_ClientRoleManagerService.htm)|
Объект, выполняющий задания, связанные с пересчётом ролей и замещений.
Использует клиентские расширения карточек для передачи запросов на сервер.  
[InvalidateContextRoleDeleteExtension](T_Tessa_Extensions_Platform_Shared_Roles_InvalidateContextRoleDeleteExtension.htm)|
Удаление контекстной роли из кэша.  
[InvalidateContextRoleStoreExtension](T_Tessa_Extensions_Platform_Shared_Roles_InvalidateContextRoleStoreExtension.htm)|
Создание или изменение контекстной роли в кэше.  
[RoleDeputiesManagementDigestRequestExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementDigestRequestExtension.htm)|  
[RoleDeputiesManagementMetadataExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleDeputiesManagementMetadataExtension.htm)|
Расширение, добавляющее в тип карточки PersonalRole, секции и вкладку из
карточки RoleDeputiesManagement. На клиенте используется для добавления
информации в тип для превью карточки, при этом подразумевается, что доступна
полная метаинформация с сервера. На сервере используется для добавлении
информации в тип при построении.  
[RoleExtensionHelper](T_Tessa_Extensions_Platform_Shared_Roles_RoleExtensionHelper.htm)|
Вспомогательные методы для расширений ролевой модели.  
[RoleTypesMetadataExtension](T_Tessa_Extensions_Platform_Shared_Roles_RoleTypesMetadataExtension.htm)|
Расширение делает статические роли и департаменты админскими, если не
используется кастомная подсистема прав для этих карточек.
