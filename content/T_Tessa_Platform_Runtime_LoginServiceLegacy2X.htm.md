# LoginServiceLegacy2X - класс
Реализация веб-сервиса
[ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm) для маршрута
[Legacy2X](T_Tessa_Platform_Runtime_ServiceRoute.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class LoginServiceLegacy2X : ILoginService
VB __Копировать
     Public NotInheritable Class LoginServiceLegacy2X
    	Implements ILoginService
C++ __Копировать
     public ref class LoginServiceLegacy2X sealed : ILoginService
F# __Копировать
     [<SealedAttribute>]
    type LoginServiceLegacy2X = 
        class
            interface ILoginService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LoginServiceLegacy2X
Implements
    [ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm)
##  __Конструкторы
[LoginServiceLegacy2X](M_Tessa_Platform_Runtime_LoginServiceLegacy2X__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
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
[OpenSessionAsync](M_Tessa_Platform_Runtime_LoginServiceLegacy2X_OpenSessionAsync.htm)|
Выполняет аутентификацию пользователя, используя анонимную аутентификацию по
учётной записи Windows и по заданным параметрам логин/пароль/доменное имя, или
используя аутентификацию для пользователя Tessa. Открывает сессию и возвращает
её токен [Tessa.Platform.Runtime.SessionToken], сериализованный в формате XML.  
[OpenSessionWindowsAuthAsync](M_Tessa_Platform_Runtime_LoginServiceLegacy2X_OpenSessionWindowsAuthAsync.htm)|
Выполняет аутентификацию пользователя по учётной записи Windows. Открывает
сессию и возвращает её токен [Tessa.Platform.Runtime.SessionToken],
сериализованный в формате XML.  
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
