# SessionCredentials - класс
Настройки входа, используемые для открытия сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionCredentials : ISessionCredentials
VB __Копировать
     Public NotInheritable Class SessionCredentials
    	Implements ISessionCredentials
C++ __Копировать
     public ref class SessionCredentials sealed : ISessionCredentials
F# __Копировать
     [<SealedAttribute>]
    type SessionCredentials = 
        class
            interface ISessionCredentials
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionCredentials
Implements
    [ISessionCredentials](T_Tessa_Platform_Runtime_ISessionCredentials.htm)
##  __Конструкторы
[SessionCredentials](M_Tessa_Platform_Runtime_SessionCredentials__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[IsCancelled](P_Tessa_Platform_Runtime_SessionCredentials_IsCancelled.htm)|
Признак того, что авторизация считается отменённой, т.к. логин или пароль не
являются корректными для текущего типа авторизации.  
---|---  
[Login](P_Tessa_Platform_Runtime_SessionCredentials_Login.htm)|  Логин для
входа. Может быть равен null или пустой строке.  
[LoginType](P_Tessa_Platform_Runtime_SessionCredentials_LoginType.htm)| Тип
авторизации в системе.  
[Password](P_Tessa_Platform_Runtime_SessionCredentials_Password.htm)|  Пароль
для входа. Может быть равен null или пустой строке.  
## __Методы
[CreateCopy](M_Tessa_Platform_Runtime_SessionCredentials_CreateCopy.htm)|
Создаёт копию текущего объекта с указанием другого типа авторизации.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
