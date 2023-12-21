# IKrPermissionsManagerContext - интерфейс
Объект контекста менеджера проверки прав доступа
[IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IKrPermissionsManagerContext : IExtensionContext
VB __Копировать
     Public Interface IKrPermissionsManagerContext
    	Inherits IExtensionContext
C++ __Копировать
     public interface class IKrPermissionsManagerContext : IExtensionContext
F# __Копировать
     type IKrPermissionsManagerContext = 
        interface
            interface IExtensionContext
        end
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Свойства
[CancellationToken](P_Tessa_Extensions_IExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm))  
---|---  
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Card.htm)|
Карточка, по которой идет проверка доступа. Ее наличие и содержимое зависит от
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Mode.htm).  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_CardID.htm)|
Идентификатор карточки или null, если проверка идет вне контекста карточки.  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_CardMetadata.htm)|
Метаданные карточек.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_CardType.htm)|
Тип карточки.  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_DbScope.htm)|
Объект для доступа к базе данных.  
[Descriptor](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Descriptor.htm)|
Дескриптор с результатами проверки правил доступа.  
[DocState](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_DocState.htm)|
Состояние карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_DocTypeID.htm)|
Идентификатор типа документа, если используется тип документа, иначе null.  
[ExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ExtensionContext.htm)|
Контекст расширения, в котором была вызвана проверка прав доступа. Может быть
равен null.  
[FileID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_FileID.htm)|
Идентификатор файла, если идет проверка доступа к файлу.  
[FileVersionID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_FileVersionID.htm)|
Идентификатор версии файла, если идет проверка доступа к конкретной версии
файла.  
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_IgnoreSections.htm)|
Список секций, по которым игнорируется проверка расширенных настроек прав
доступа.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Info.htm)|
Дополнительная информация, используемая при проверке прав доступа.  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_KrTypesCache.htm)|
Кеш типов документов.  
[Method](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Method.htm)|
Имя метода, который был вызван для проверки правил доступа. Может иметь
значение [CheckRequiredPermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_CheckRequiredPermissionsAsync.htm)
или [GetEffectivePermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_GetEffectivePermissionsAsync.htm).  
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Mode.htm)|
Режим проверки доступа к карточке.  
[PermissionsCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_PermissionsCache.htm)|
Версия кеша правил доступа, которая используется для получения данных о
настройках правил доступа. Если не задано, то берется текущая версия правил
доступа из
[IKrPermissionsCacheContainer](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer.htm).  
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_PreviousToken.htm)|
Предыдущий токен прав доступа. Может быть не задан.  
[ServerToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ServerToken.htm)|
Дополнительный токен прав доступа, рассчитанный на сервере. Его настройки
приоритетнее, чем в
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_PreviousToken.htm)
и он всегда считается валидным. Может быть не задан.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Session.htm)|
Сессия текущего сотрудника.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm)|
Билдер результата валидации.  
[WithExtendedPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_WithExtendedPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки прав доступа
карточки.  
[WithRequiredPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_WithRequiredPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки обязательности
полей.  
## __Методы
[AddErrorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_AddErrorAsync.htm)|
Метод для добавления ошибки в
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm),
который пишет дополнительную информацию о контексте в детали.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
