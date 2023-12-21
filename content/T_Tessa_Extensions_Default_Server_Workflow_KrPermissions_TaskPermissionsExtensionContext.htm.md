# TaskPermissionsExtensionContext - класс
Контекст проверки прав доступа с дополнительной информацией для перерасчета
токена
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TaskPermissionsExtensionContext : KrPermissionsManagerContext, 
    	ITaskPermissionsExtensionContext, IKrPermissionsManagerContext, IExtensionContext
VB __Копировать
     Public NotInheritable Class TaskPermissionsExtensionContext
    	Inherits KrPermissionsManagerContext
    	Implements ITaskPermissionsExtensionContext, IKrPermissionsManagerContext, IExtensionContext
C++ __Копировать
     public ref class TaskPermissionsExtensionContext sealed : public KrPermissionsManagerContext, 
    	ITaskPermissionsExtensionContext, IKrPermissionsManagerContext, IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type TaskPermissionsExtensionContext = 
        class
            inherit KrPermissionsManagerContext
            interface ITaskPermissionsExtensionContext
            interface IKrPermissionsManagerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm) __ TaskPermissionsExtensionContext
Implements
    [IKrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext.htm), [ITaskPermissionsExtensionContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_ITaskPermissionsExtensionContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[TaskPermissionsExtensionContext](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_TaskPermissionsExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса TaskPermissionsExtensionContext  
---|---  
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
---|---  
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Card.htm)|
Карточка, по которой идет проверка доступа. Ее наличие и содержимое зависит от
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Mode.htm).  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardID.htm)|
Идентификатор карточки или null, если проверка идет вне контекста карточки.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardMetadata.htm)|
Метаданные карточек.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardType.htm)|
Тип карточки.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DbScope.htm)|
Объект для доступа к базе данных.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Descriptor](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Descriptor.htm)|
Дескриптор с результатами проверки правил доступа.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[DocState](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DocState.htm)|
Состояние карточки.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DocTypeID.htm)|
Идентификатор типа документа, если используется тип документа, иначе null.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[ExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ExtensionContext.htm)|
Контекст расширения, в котором была вызвана проверка прав доступа. Может быть
равен null.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[FileID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_FileID.htm)|
Идентификатор файла, если идет проверка доступа к файлу.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[FileVersionID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_FileVersionID.htm)|
Идентификатор версии файла, если идет проверка доступа к конкретной версии
файла.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_IgnoreSections.htm)|
Список секций, по которым игнорируется проверка расширенных настроек прав
доступа.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Info.htm)|
Дополнительная информация, используемая при проверке прав доступа.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[IsRecalcRequired](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_IsRecalcRequired.htm)|
Определяет, требуется ли перерасчет токена  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_KrTypesCache.htm)|
Кеш типов документов.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Method](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Method.htm)|
Имя метода, который был вызван для проверки правил доступа. Может иметь
значение [CheckRequiredPermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_CheckRequiredPermissionsAsync.htm)
или [GetEffectivePermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_GetEffectivePermissionsAsync.htm).  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Mode.htm)|
Режим проверки доступа к карточке.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[PermissionsCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_PermissionsCache.htm)|
Версия кеша правил доступа, которая используется для получения данных о
настройках правил доступа. Если не задано, то берется текущая версия правил
доступа из
[IKrPermissionsCacheContainer](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer.htm).  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_PreviousToken.htm)|
Предыдущий токен прав доступа. Может быть не задан.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[ServerToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ServerToken.htm)|
Дополнительный токен прав доступа, рассчитанный на сервере. Его настройки
приоритетнее, чем в
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_PreviousToken.htm)
и он всегда считается валидным. Может быть не задан.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Session.htm)|
Сессия текущего сотрудника.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[Task](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_TaskPermissionsExtensionContext_Task.htm)|
Объект задания  
[TaskType](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_TaskPermissionsExtensionContext_TaskType.htm)|
Тип задания  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ValidationResult.htm)|
Билдер результата валидации.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[WithExtendedPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_WithExtendedPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки прав доступа
карточки.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
[WithRequiredPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_WithRequiredPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки обязательности
полей.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
##  __Методы
[AddErrorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_AddErrorAsync.htm)|
Метод для добавления ошибки в
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm),
который пишет дополнительную информацию о контексте в детали.  
(Унаследован от
[KrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext.htm))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Default.Server.Workflow.KrPermissions - пространство
имён](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)
