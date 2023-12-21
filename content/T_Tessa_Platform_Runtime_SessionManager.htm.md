# SessionManager - класс
Объект для управления клиентскими сессиями.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionManager : ISessionManager, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class SessionManager
    	Implements ISessionManager, IDisposable
C++ __Копировать
     public ref class SessionManager sealed : ISessionManager, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type SessionManager = 
        class
            interface ISessionManager
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionManager
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [ISessionManager](T_Tessa_Platform_Runtime_ISessionManager.htm)
##  __Конструкторы
[SessionManager](M_Tessa_Platform_Runtime_SessionManager__ctor.htm)|  Создаёт
экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_SessionManager_ApplicationID.htm)|
Идентификатор приложения. По умолчанию значение свойства равно
[Tessa.Platform.Runtime.ApplicationIdentifiers.Other]. Стандартные
идентификаторы приложений указаны в полях класса
[Tessa.Platform.Runtime.ApplicationIdentifiers].  
---|---  
[Credentials](P_Tessa_Platform_Runtime_SessionManager_Credentials.htm)|
Параметры входа, используемые при первичном открытии сессии или при повторном
открытии, или null, если при следующем открытии сессии будут использоваться
параметры по умолчанию.  
[IsOpened](P_Tessa_Platform_Runtime_SessionManager_IsOpened.htm)| Признак
того, что сессия открыта.  
[LoginParameters](P_Tessa_Platform_Runtime_SessionManager_LoginParameters.htm)|
Параметры диалога входа (ввода логина и пароля), если используется диалог с
UI. Свойство нельзя установить равным null.  
## __Методы
[CloseAsync](M_Tessa_Platform_Runtime_SessionManager_CloseAsync.htm)|
Закрывает открытую ранее сессию.  
---|---  
[Dispose](M_Tessa_Platform_Runtime_SessionManager_Dispose.htm)| Освобождает
ресурсы, занимаемые объектом.  
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
[OpenAsync](M_Tessa_Platform_Runtime_SessionManager_OpenAsync.htm)|  Открывает
сессию от имени текущего пользователя и гарантирует её периодическое
поддержание. Возвращает признак того, что сессия была успешно открыта.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[SessionClosed](E_Tessa_Platform_Runtime_SessionManager_SessionClosed.htm)|
Событие, происходящее при каждом успешном закрытии сессии (методом Open или
повторное открытие по таймеру при истечении срока сессии).  
---|---  
[SessionOpened](E_Tessa_Platform_Runtime_SessionManager_SessionOpened.htm)|
Событие, происходящее при каждом успешном открытии сессии (методом Open или
повторное открытие по таймеру при истечении срока сессии).  
## __Методы расширения
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
