# DefaultTessaServerDependencies - класс
Зависимости платформы по умолчанию, которые зависят от разновидности сервера
приложений, и определяет возможности такого сервера, требующие дополнительные
зависимости. В этом классе указываются значения, не связанные с конкретным
сервером.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DefaultTessaServerDependencies : ITessaServerDependencies
VB __Копировать
     Public Class DefaultTessaServerDependencies
    	Implements ITessaServerDependencies
C++ __Копировать
     public ref class DefaultTessaServerDependencies : ITessaServerDependencies
F# __Копировать
     type DefaultTessaServerDependencies = 
        class
            interface ITessaServerDependencies
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DefaultTessaServerDependencies
Derived
[Tessa.Server.TessaServerDependencies](T_Tessa_Server_TessaServerDependencies.htm)
Implements
    [ITessaServerDependencies](T_Tessa_Platform_ITessaServerDependencies.htm)
##  __Конструкторы
[DefaultTessaServerDependencies](M_Tessa_Platform_DefaultTessaServerDependencies__ctor.htm)|
Инициализирует новый экземпляр класса DefaultTessaServerDependencies  
---|---  
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
[FinalizeServerRegistration](M_Tessa_Platform_DefaultTessaServerDependencies_FinalizeServerRegistration.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
завершения регистрации, вызываемого на сервере. Метод вызывается после того,
как все другие зависимости были зарегистрированы.  
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
[Initialize](M_Tessa_Platform_DefaultTessaServerDependencies_Initialize.htm)|
Выполняет инициализацию зависимостей платформы. Метод вызывается один раз при
запуске приложения.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterCompilation](M_Tessa_Platform_DefaultTessaServerDependencies_RegisterCompilation.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
регистрации API компиляции, вызываемом на сервере. Метод вызывается после
того, как все другие типовые зависимости были зарегистрированы.  
[RegisterCryptoAPI](M_Tessa_Platform_DefaultTessaServerDependencies_RegisterCryptoAPI.htm)|
Выполняет регистрацию зависимостей, специфичных для типа сервера, в методе
регистрации криптографических API, вызываемых на сервере. Метод вызывается
после того, как все другие типовые зависимости были зарегистрированы.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
