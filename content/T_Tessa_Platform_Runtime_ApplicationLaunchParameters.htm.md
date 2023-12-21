# ApplicationLaunchParameters - класс
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
указаны при запуске.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationLaunchParameters : IApplicationLaunchParameters
VB __Копировать
     Public NotInheritable Class ApplicationLaunchParameters
    	Implements IApplicationLaunchParameters
C++ __Копировать
     public ref class ApplicationLaunchParameters sealed : IApplicationLaunchParameters
F# __Копировать
     [<SealedAttribute>]
    type ApplicationLaunchParameters = 
        class
            interface IApplicationLaunchParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationLaunchParameters
Implements
    [IApplicationLaunchParameters](T_Tessa_Platform_Runtime_IApplicationLaunchParameters.htm)
##  __Конструкторы
[ApplicationLaunchParameters(Guid,
String[])](M_Tessa_Platform_Runtime_ApplicationLaunchParameters__ctor_1.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
[ApplicationLaunchParameters(Guid, Func<CancellationToken, Task>,
String[])](M_Tessa_Platform_Runtime_ApplicationLaunchParameters__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
## __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_ApplicationID.htm)|
Идентификатор приложения для расширений.  
---|---  
[CommandLineArgs](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_CommandLineArgs.htm)|
Параметры командной строки.  
[Info](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_Info.htm)|
Дополнительная информация, связанная с запуском приложения.  
[SkipApplicationExtensions](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_SkipApplicationExtensions.htm)|
Признак того, что при инициализации и при завершении приложения не будут
выполнены соответствующие клиентские расширения. По умолчанию равен false.  
[SkipApplicationInitialization](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_SkipApplicationInitialization.htm)|
Признак того, что при инициализации приложения не будет инициализированы
стандартные данные приложения запросом к серверу. По умолчанию равен false.  
[SkipFilesInitialization](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_SkipFilesInitialization.htm)|
Признак того, что при инициализации приложения не будет инициализирована
подсистема файлов. При этом не будет, например, выполнено удаление временных
файлов, оставшихся с предыдущих запусков. По умолчанию равен false.  
[Splash](P_Tessa_Platform_Runtime_ApplicationLaunchParameters_Splash.htm)|
Сплэш-окно загрузки приложения, отображаемое в процессе его инициализации, или
null, если такое окно не отображается.  
## __Методы
[ActivateShellAsync](M_Tessa_Platform_Runtime_ApplicationLaunchParameters_ActivateShellAsync.htm)|
Активирует главное окно приложения, если такое окно существует.  
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
