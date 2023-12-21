# ApplicationDependencies - класс
Основные зависимости для объекта
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationDependencies : IApplicationDependencies, 
    	IDisposable
VB __Копировать
     Public NotInheritable Class ApplicationDependencies
    	Implements IApplicationDependencies, IDisposable
C++ __Копировать
     public ref class ApplicationDependencies sealed : IApplicationDependencies, 
    	IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ApplicationDependencies = 
        class
            interface IApplicationDependencies
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationDependencies
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IApplicationDependencies](T_Tessa_Platform_Runtime_IApplicationDependencies.htm)
##  __Конструкторы
[ApplicationDependencies](M_Tessa_Platform_Runtime_ApplicationDependencies__ctor.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
---|---  
## __Свойства
[ApplicationDescriptor](P_Tessa_Platform_Runtime_ApplicationDependencies_ApplicationDescriptor.htm)|
Объект описывающий текущее приложение, которое определяется по клиентской
сессии.  
---|---  
[ApplicationInitializer](P_Tessa_Platform_Runtime_ApplicationDependencies_ApplicationInitializer.htm)|
Объект, выполняющий инициализацию приложения заданного типа.  
[ApplicationPublisher](P_Tessa_Platform_Runtime_ApplicationDependencies_ApplicationPublisher.htm)|
Объект, выполняющий публикацию приложения.  
[CommandExecutor](P_Tessa_Platform_Runtime_ApplicationDependencies_CommandExecutor.htm)|
Объект, выполняющий команды при запуске приложения.  
[CommandParser](P_Tessa_Platform_Runtime_ApplicationDependencies_CommandParser.htm)|
Объект, выполняющая разбор аргументов командной строки.  
[ConnectionSettings](P_Tessa_Platform_Runtime_ApplicationDependencies_ConnectionSettings.htm)|
Настройки для подключения к сервисам Tessa.  
[EnvironmentManager](P_Tessa_Platform_Runtime_ApplicationDependencies_EnvironmentManager.htm)|
Объект, управляющий переменными приложения.  
[ExtensionContainer](P_Tessa_Platform_Runtime_ApplicationDependencies_ExtensionContainer.htm)|
Контейнер расширений.  
[LinkManager](P_Tessa_Platform_Runtime_ApplicationDependencies_LinkManager.htm)|
Объект, используемый для обработки ссылок.  
[MessageProvider](P_Tessa_Platform_Runtime_ApplicationDependencies_MessageProvider.htm)|
Объект, обеспечивающий вывод сообщений.  
[ProcessManager](P_Tessa_Platform_Runtime_ApplicationDependencies_ProcessManager.htm)|
Объект, обеспечивающий запуск дочерних процессов.  
[RouteSettings](P_Tessa_Platform_Runtime_ApplicationDependencies_RouteSettings.htm)|
Настройки маршрута для взаимодействия с веб-сервисами на клиенте.  
[RuntimeSettings](P_Tessa_Platform_Runtime_ApplicationDependencies_RuntimeSettings.htm)|
Настройки, связанные с исполняющей средой системы.  
[Session](P_Tessa_Platform_Runtime_ApplicationDependencies_Session.htm)|
Сессия пользователя. Сессию можно использовать только после того, как она была
открыта в процессе запуска приложения.  
[SessionManager](P_Tessa_Platform_Runtime_ApplicationDependencies_SessionManager.htm)|
Объект для управления клиентскими сессиями.  
[UnityContainer](P_Tessa_Platform_Runtime_ApplicationDependencies_UnityContainer.htm)|
Контейнер Unity, используемый для получения зависимостей для расширений.  
##  __Методы
[CreateContext](M_Tessa_Platform_Runtime_ApplicationDependencies_CreateContext.htm)|
Создаёт контекст, связанный с приложением.  
---|---  
[Dispose](M_Tessa_Platform_Runtime_ApplicationDependencies_Dispose.htm)|
Освобождает ресурсы, занимаемые объектом.  
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
