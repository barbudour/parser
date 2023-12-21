# SessionService - класс
Сервис, управляющий открытыми сессиями.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionService : ISessionService
VB __Копировать
     Public NotInheritable Class SessionService
    	Implements ISessionService
C++ __Копировать
     public ref class SessionService sealed : ISessionService
F# __Копировать
     [<SealedAttribute>]
    type SessionService = 
        class
            interface ISessionService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionService
Implements
    [ISessionService](T_Tessa_Platform_Runtime_ISessionService.htm)
##  __Конструкторы
[SessionService](M_Tessa_Platform_Runtime_SessionService__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Методы
[CloseSessionAsAdminAsync](M_Tessa_Platform_Runtime_SessionService_CloseSessionAsAdminAsync.htm)|
Закрывает сессию с заданным идентификатором от имени администратора. Закрытие
сессии удаляет её, а также может дополнительно добавить запись в логах аудита
или выполнить другие действия. Возвращает признак того, что сессия ещё была
открыта на момент вызова метода.  
---|---  
[CloseSessionAsync](M_Tessa_Platform_Runtime_SessionService_CloseSessionAsync.htm)|
Закрывает текущую сессию. Закрытие сессии удаляет её, а также может
дополнительно добавить запись в логах аудита или выполнить другие действия.
Возвращает признак того, что сессия ещё была открыта на момент вызова метода.  
[CloseSessionWithTokenAsync](M_Tessa_Platform_Runtime_SessionService_CloseSessionWithTokenAsync.htm)|
Закрывает текущую сессию, причём сессия определяется по токену, передаваемому
в параметре. Закрытие сессии удаляет её, а также может дополнительно добавить
запись в логах аудита или выполнить другие действия. Возвращает признак того,
что сессия ещё была открыта на момент вызова метода.  
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
[IncrementConfigurationVersionAsync](M_Tessa_Platform_Runtime_SessionService_IncrementConfigurationVersionAsync.htm)|
Увеличивает версию конфигурации без внесения в неё фактических изменений, а
также обновляет информацию по текущей версии платформы. Может использоваться,
например, для сброса клиентского кэша. Метод доступен только администраторам.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
