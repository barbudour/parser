# LinuxTessaPlatformDependencies - класс
Зависимости платформы для ОС Linux. Создайте экземпляр класса и установите в
свойстве [Dependencies](P_Tessa_Platform_TessaPlatform_Dependencies.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa.Linux (в Tessa.Linux.dll) Версия: 3.6.0.17
C# __Копировать
    [UsedImplicitlyAttribute]
    public class LinuxTessaPlatformDependencies : DefaultTessaPlatformDependencies
VB __Копировать
    <UsedImplicitlyAttribute>
    Public Class LinuxTessaPlatformDependencies
    	Inherits DefaultTessaPlatformDependencies
C++ __Копировать
    [UsedImplicitlyAttribute]
    public ref class LinuxTessaPlatformDependencies : public DefaultTessaPlatformDependencies
F# __Копировать
     [<UsedImplicitlyAttribute>]
    type LinuxTessaPlatformDependencies = 
        class
            inherit DefaultTessaPlatformDependencies
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm) __ LinuxTessaPlatformDependencies
##  __Конструкторы
[LinuxTessaPlatformDependencies](M_Tessa_Platform_LinuxTessaPlatformDependencies__ctor.htm)|
Инициализирует новый экземпляр класса LinuxTessaPlatformDependencies  
---|---  
##  __Свойства
[EnableServiceRouteFallback](P_Tessa_Platform_DefaultTessaPlatformDependencies_EnableServiceRouteFallback.htm)|
Признак того, что включено автоматическое переключение маршрута, если текущий
маршрут не поддерживается. Например, выполняет переключение маршрута
[Tessa.Platform.Runtime.ServiceRoute.Default] на
[Tessa.Platform.Runtime.ServiceRoute.Legacy2X], если маршрут по умолчанию
вернул ошибку 404. По умолчанию равно false, поэтому явно установите true в
приложении, которое должно поддерживать автоматическую маршрутизацию.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
---|---  
[Features](P_Tessa_Platform_DefaultTessaPlatformDependencies_Features.htm)|
Возможности текущей платформы (операционной системы, исполняющей среды).
Доступны в виде перечисления флагов.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
##  __Методы
[ConfigureClientRouting](M_Tessa_Platform_DefaultTessaPlatformDependencies_ConfigureClientRouting.htm)|
Выполняет конфигурирование настроек для маршрутов сервисов, специфичных для
платформы. На момент выполнения метода все регистрации в контейнере уже
завершены, поэтому может выполняться резолв зависимостей.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
---|---  
[CreateGlobalEvent](M_Tessa_Platform_LinuxTessaPlatformDependencies_CreateGlobalEvent.htm)|
Создаёт событие по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
(Переопределяет
[DefaultTessaPlatformDependencies.CreateGlobalEvent(String)](M_Tessa_Platform_DefaultTessaPlatformDependencies_CreateGlobalEvent.htm))  
[CreateGlobalMutex](M_Tessa_Platform_LinuxTessaPlatformDependencies_CreateGlobalMutex.htm)|
Создаёт мьютекс по глобально уникальному имени, который можно использовать для
синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
(Переопределяет
[DefaultTessaPlatformDependencies.CreateGlobalMutex(String)](M_Tessa_Platform_DefaultTessaPlatformDependencies_CreateGlobalMutex.htm))  
[CreateGlobalStorage](M_Tessa_Platform_LinuxTessaPlatformDependencies_CreateGlobalStorage.htm)|
Создаёт хранилище по глобально уникальному имени, который можно использовать
для синхронизации процессов как минимум в пределах сессии пользователя и всех
процессов в ней.  
(Переопределяет [DefaultTessaPlatformDependencies.CreateGlobalStorage(String,
Int64)](M_Tessa_Platform_DefaultTessaPlatformDependencies_CreateGlobalStorage.htm))  
[CreateHttpClient](M_Tessa_Platform_LinuxTessaPlatformDependencies_CreateHttpClient.htm)|
Создаёт объект HttpClient для взаимодействия с веб-сервисами на основании
объекта с настройками.  
(Переопределяет
[DefaultTessaPlatformDependencies.CreateHttpClient(IConnectionSettings,
Boolean)](M_Tessa_Platform_DefaultTessaPlatformDependencies_CreateHttpClient.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExecuteInImpersonationContext](M_Tessa_Platform_DefaultTessaPlatformDependencies_ExecuteInImpersonationContext.htm)|
Выполняет действие action от имени заданной учётной записи пользователя
accountName. Метод должен вызываться только в том случае, если выполнение от
имени учётной записи поддерживается платформой
[TessaPlatformFeature.Impersonation].  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetNetRuntimeFriendlyName](M_Tessa_Platform_DefaultTessaPlatformDependencies_GetNetRuntimeFriendlyName.htm)|
Возвращает "дружественное" название исполняющей среды .NET с указанием её
версии, которое можно использовать для отображения пользователю. Актуально как
для .NET Framework, так и для .NET Core.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[GetOperatingSystemFriendlyName](M_Tessa_Platform_DefaultTessaPlatformDependencies_GetOperatingSystemFriendlyName.htm)|
Возвращает "дружественное" имя операционной системы, которое можно
использовать для отображения пользователю.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Initialize](M_Tessa_Platform_DefaultTessaPlatformDependencies_Initialize.htm)|
Выполняет инициализацию зависимостей платформы. Метод вызывается один раз при
запуске приложения.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[IsLoginHiddenException](M_Tessa_Platform_DefaultTessaPlatformDependencies_IsLoginHiddenException.htm)|
Возвращает признак того, что заданное исключение, возникшее в процессе входа в
систему, должно быть скрыто от пользователя. Значение true обычно возвращается
в случае, когда исключение соответствует неправильному логину/паролю.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterApplications](M_Tessa_Platform_DefaultTessaPlatformDependencies_RegisterApplications.htm)|
Выполняет регистрацию зависимостей, специфичных для платформы, в методе
регистрации API приложений, вызываемом на клиенте и на сервере. Метод
вызывается после того, как все другие типовые зависимости были
зарегистрированы.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[RegisterClientRouting](M_Tessa_Platform_DefaultTessaPlatformDependencies_RegisterClientRouting.htm)|
Выполняет регистрацию зависимостей, специфичных для платформы, в методе
регистрации клиентских сессий, чтобы предоставить доступ к маршрутам сервисов,
которые используются для обратной совместимости с серверами старых версий.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[RegisterProcessManager](M_Tessa_Platform_DefaultTessaPlatformDependencies_RegisterProcessManager.htm)|
Выполняет регистрацию зависимостей, специфичных для платформы, в методе
регистрации API [Tessa.Platform.Runtime.IProcessManager], вызываемом на
клиенте и на сервере. Метод вызывается после того, как все другие типовые
зависимости были зарегистрированы.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[RegisterServer](M_Tessa_Platform_DefaultTessaPlatformDependencies_RegisterServer.htm)|
Выполняет регистрацию зависимостей, специфичных для платформы, в методе
регистрации сервера unityContainer.RegisterServer(). Метод вызывается после
того, как все другие типовые зависимости были зарегистрированы.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetUserDefaultUILanguage](M_Tessa_Platform_DefaultTessaPlatformDependencies_TryGetUserDefaultUILanguage.htm)|
Возвращает язык UI по умолчанию, установленный для пользователя в операционной
системе, или null, если язык не удалось определить, это аналогично явному
использованию английского языка. Реализация по умолчанию обычно возвращает
язык, предоставленный платформой как язык операционной системы.  
(Унаследован от
[DefaultTessaPlatformDependencies](T_Tessa_Platform_DefaultTessaPlatformDependencies.htm))  
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
