# AdExtensionContext - класс
Контекст операции, связанной с синхронизацией Active Directory.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AdExtensionContext : IAdExtensionContext, 
    	IExtensionContext
VB __Копировать
     Public NotInheritable Class AdExtensionContext
    	Implements IAdExtensionContext, IExtensionContext
C++ __Копировать
     public ref class AdExtensionContext sealed : IAdExtensionContext, 
    	IExtensionContext
F# __Копировать
     [<SealedAttribute>]
    type AdExtensionContext = 
        class
            interface IAdExtensionContext
            interface IExtensionContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AdExtensionContext
Implements
    [IExtensionContext](T_Tessa_Extensions_IExtensionContext.htm), [IAdExtensionContext](T_Tessa_Extensions_Platform_Server_AdSync_IAdExtensionContext.htm)
##  __Конструкторы
[AdExtensionContext](M_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext__ctor.htm)|
Инициализирует новый экземпляр класса AdExtensionContext  
---|---  
##  __Свойства
[Cancel](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Cancel.htm)|
Отмена сохранения карточки.  
---|---  
[CancellationToken](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
[Card](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Card.htm)|
Информация о карточке.  
[Connection](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Connection.htm)|
Соединение с сервером LDAP  
[Entry](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Entry.htm)|
Ldap объект, источник синхронизации  
[Info](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Info.htm)|
Дополнительная информация, связанная с контекстом расширений.  
[SyncContext](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_SyncContext.htm)|
Контекст синхронизации.  
[UpdateUser](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_UpdateUser.htm)|
Обновлять ли пользователей в указанном подразделении/роли  
[Users](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_Users.htm)|
Список пользователей указанного подразделения  
[ValidationResult](P_Tessa_Extensions_Platform_Server_AdSync_AdExtensionContext_ValidationResult.htm)|
Сообщения валидации.  
##  __Методы
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
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
