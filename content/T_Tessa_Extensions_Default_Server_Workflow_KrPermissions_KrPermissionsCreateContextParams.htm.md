# KrPermissionsCreateContextParams - класс
Объект с параметрами для создания контекста в
[IKrPermissionsManager](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsManager.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Server.Workflow.KrPermissions](N_Tessa_Extensions_Default_Server_Workflow_KrPermissions.htm)  
 **Сборка:** Tessa.Extensions.Default.Server (в
Tessa.Extensions.Default.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class KrPermissionsCreateContextParams
VB __Копировать
     Public NotInheritable Class KrPermissionsCreateContextParams
C++ __Копировать
     public ref class KrPermissionsCreateContextParams sealed
F# __Копировать
     [<SealedAttribute>]
    type KrPermissionsCreateContextParams = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ KrPermissionsCreateContextParams
##  __Конструкторы
[KrPermissionsCreateContextParams](M_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams__ctor.htm)|
Инициализирует новый экземпляр класса KrPermissionsCreateContextParams  
---|---  
##  __Свойства
[AdditionalInfo](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_AdditionalInfo.htm)|
Дополнительная информация, используемая при проверке прав доступа.  
---|---  
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_Card.htm)|
Карточка. Может быть не передана, если проверка прав доступа выполняется вне
контекста карточки.  
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_CardID.htm)|
Идентификатор карточки. Может быть не передан, если проверка прав доступа
выполняется вне контекста карточки.  
[CardTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_CardTypeID.htm)|
Тип карточки. Должен быть передан, если не передан
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_Card.htm)
или
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_CardID.htm).  
[DocTypeID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_DocTypeID.htm)|
Тип документа. Должен быть передан, если не передан
[Card](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_Card.htm)
или
[CardID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_CardID.htm).  
[ExtensionContext](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_ExtensionContext.htm)|
Контекст расширения, в котором была вызвана данная проверка прав доступа.
Может быть равен null.  
[FileID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_FileID.htm)|
Идентификатор проверяемого файла, если идет проверка доступа к файлу карточки.  
[FileVersionID](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_FileVersionID.htm)|
Идентификатор версии проверяемого файла, если идет проверка доступа к версии
файла.  
[IgnoreSections](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_IgnoreSections.htm)|
Список секций, по которым игнорируется проверка расширенных настроек прав
доступа.  
[IsStore](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_IsStore.htm)|
Определяет, что переданная карточка сохраняется.  
[KrState](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_KrState.htm)|
Состояние документа.  
[PermissionsCache](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_PermissionsCache.htm)|
Версия кеша правил доступа, которая используется для получения данных о
настройках правил доступа. Если не задано, то берется текущая версия правил
доступа из
[IKrPermissionsCacheContainer](T_Tessa_Extensions_Default_Server_Workflow_KrPermissions_IKrPermissionsCacheContainer.htm).  
[PrevToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_PrevToken.htm)|
Предыдущий токен.  
[ServerToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_ServerToken.htm)|
Дополнительный токен прав доступа, рассчитанный на сервере. Его настройки
приоритетнее, чем в
[PrevToken](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_PrevToken.htm)
и он всегда считается валидным.  
[ValidationResult](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_ValidationResult.htm)|
Билдер результата валидации. Может быть не передан, если не требуется
обработка результата валидации.  
[WithExtendedPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_WithExtendedPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки прав доступа
карточки.  
[WithRequiredPermissions](P_Tessa_Extensions_Default_Server_Workflow_KrPermissions_KrPermissionsCreateContextParams_WithRequiredPermissions.htm)|
Флаг определяет, что нужно рассчитать расширенные настройки обязательности
полей.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
