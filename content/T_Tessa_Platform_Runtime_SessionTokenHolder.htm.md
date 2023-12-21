# SessionTokenHolder - класс
Объект, содержащий токен, связанный с текущей сессией. Используется на клиенте
для передачи данных между запросами.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionTokenHolder : ISessionTokenHolder
VB __Копировать
     Public NotInheritable Class SessionTokenHolder
    	Implements ISessionTokenHolder
C++ __Копировать
     public ref class SessionTokenHolder sealed : ISessionTokenHolder
F# __Копировать
     [<SealedAttribute>]
    type SessionTokenHolder = 
        class
            interface ISessionTokenHolder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionTokenHolder
Implements
    [ISessionTokenHolder](T_Tessa_Platform_Runtime_ISessionTokenHolder.htm)
##  __Конструкторы
[SessionTokenHolder](M_Tessa_Platform_Runtime_SessionTokenHolder__ctor.htm)|
Инициализирует новый экземпляр класса SessionTokenHolder  
---|---  
##  __Свойства
[SessionToken](P_Tessa_Platform_Runtime_SessionTokenHolder_SessionToken.htm)|
Токен для текущей сессии или null, если токен ещё не был задан.  
---|---  
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
[SetSessionTokenAsync](M_Tessa_Platform_Runtime_SessionTokenHolder_SetSessionTokenAsync.htm)|
Устанавливает токен для текущей сессии. Может быть равен null, если считается,
что токен ещё не был задан.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[SessionTokenChanged](E_Tessa_Platform_Runtime_SessionTokenHolder_SessionTokenChanged.htm)|
Событие, происходящее при изменении токена для текущей сессии.  
---|---  
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
