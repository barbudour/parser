# KrPermissionsManagerContext - класс
Контекст проверки прав доступа с дополнительной информацией для перерасчета
токена
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public class KrPermissionsManagerContext : IKrPermissionsRecalcContext, 
    	IKrPermissionsManagerContext, IExtensionContext
VB __Копировать
     Public Class KrPermissionsManagerContext
    	Implements IKrPermissionsRecalcContext, IKrPermissionsManagerContext, IExtensionContext
C++ __Копировать
     public ref class KrPermissionsManagerContext : IKrPermissionsRecalcContext, 
    	IKrPermissionsManagerContext, IExtensionContext
F# __Копировать
     type KrPermissionsManagerContext = 
        class
            interface IKrPermissionsRecalcContext
            interface IKrPermissionsManagerContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionsManagerContext
Derived
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.KrPermissionsRuleExtensionContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsRuleExtensionContext.htm)
[Tessa.Extensions.Default.Server.Workflow.KrPermissions.TaskPermissionsExtensionContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_TaskPermissionsExtensionContext.htm)
Implements
    [IKrPermissionsManagerContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext.htm), [IKrPermissionsRecalcContext](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsRecalcContext.htm), [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm)
##  __Конструкторы
[KrPermissionsManagerContext(IKrPermissionsManagerContext)](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsManagerContext  
---|---  
[KrPermissionsManagerContext(IDbScope, ISession, IKrPermissionsCache,
ICardMetadata, IKrTypesCache, Card, Nullable<Guid>, CardType, Nullable<Guid>,
Nullable<KrState>, Nullable<Guid>, Nullable<Guid>, Boolean, Boolean,
ICollection<String>, KrPermissionsCheckMode, IValidationResultBuilder,
IDictionary<String, Object>, KrToken, KrToken, ICardExtensionContext,
CancellationToken)](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext__ctor_1.htm)|
Инициализирует новый экземпляр класса KrPermissionsManagerContext  
##  __Свойства
[CancellationToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
---|---  
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Card.htm)|
Карточка, по которой идет проверка доступа. Ее наличие и содержимое зависит от
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_Mode.htm).  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardID.htm)|
Идентификатор карточки или null, если проверка идет вне контекста карточки.  
[CardMetadata](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardMetadata.htm)|
Метаданные карточек.  
[CardType](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_CardType.htm)|
Тип карточки.  
[DbScope](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DbScope.htm)|
Объект для доступа к базе данных.  
[Descriptor](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Descriptor.htm)|
Дескриптор с результатами проверки правил доступа.  
[DocState](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DocState.htm)|
Состояние карточки.  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_DocTypeID.htm)|
Идентификатор типа документа, если используется тип документа, иначе null.  
[ExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ExtensionContext.htm)|
Контекст расширения, в котором была вызвана проверка прав доступа. Может быть
равен null.  
[FileID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_FileID.htm)|
Идентификатор файла, если идет проверка доступа к файлу.  
[FileVersionID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_FileVersionID.htm)|
Идентификатор версии файла, если идет проверка доступа к конкретной версии
файла.  
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_IgnoreSections.htm)|
Список секций, по которым игнорируется проверка расширенных настроек прав
доступа.  
[Info](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Info.htm)|
Дополнительная информация, используемая при проверке прав доступа.  
[IsRecalcRequired](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_IsRecalcRequired.htm)|
Определяет, требуется ли перерасчет токена  
[KrTypesCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_KrTypesCache.htm)|
Кеш типов документов.  
[Method](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Method.htm)|
Имя метода, который был вызван для проверки правил доступа. Может иметь
значение [CheckRequiredPermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_CheckRequiredPermissionsAsync.htm)
или [GetEffectivePermissionsAsync(IKrPermissionsManagerContext,
KrPermissionFlagDescriptor[])](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager_GetEffectivePermissionsAsync.htm).  
[Mode](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Mode.htm)|
Режим проверки доступа к карточке.  
[PermissionsCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_PermissionsCache.htm)|
Версия кеша правил доступа, которая используется для получения данных о
настройках правил доступа. Если не задано, то берется текущая версия правил
доступа из
[IKrPermissionsCacheContainer](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer.htm).  
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_PreviousToken.htm)|
Предыдущий токен прав доступа. Может быть не задан.  
[ServerToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ServerToken.htm)|
Дополнительный токен прав доступа, рассчитанный на сервере. Его настройки
приоритетнее, чем в
[PreviousToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_PreviousToken.htm)
и он всегда считается валидным. Может быть не задан.  
[Session](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_Session.htm)|
Сессия текущего сотрудника.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_ValidationResult.htm)|
Билдер результата валидации.  
[WithExtendedPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_WithExtendedPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки прав доступа
карточки.  
[WithRequiredPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_WithRequiredPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки обязательности
полей.  
## __Методы
[AddErrorAsync](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsManagerContext_AddErrorAsync.htm)|
Метод для добавления ошибки в
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManagerContext_ValidationResult.htm),
который пишет дополнительную информацию о контексте в детали.  
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
