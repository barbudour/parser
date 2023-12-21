# ConnectionSettings - класс
Настройки для подключения к сервисам Tessa.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ConnectionSettings : IConnectionSettings, 
    	ISealable
VB __Копировать
     Public NotInheritable Class ConnectionSettings
    	Implements IConnectionSettings, ISealable
C++ __Копировать
     public ref class ConnectionSettings sealed : IConnectionSettings, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type ConnectionSettings = 
        class
            interface IConnectionSettings
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConnectionSettings
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
##  __Конструкторы
[ConnectionSettings](M_Tessa_Platform_Runtime_ConnectionSettings__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[BaseAddress](P_Tessa_Platform_Runtime_ConnectionSettings_BaseAddress.htm)|
Базовый адрес сервисов.  
---|---  
[CloseTimeout](P_Tessa_Platform_Runtime_ConnectionSettings_CloseTimeout.htm)|
Таймаут на закрытие соединения с сервером.  
[Default](P_Tessa_Platform_Runtime_ConnectionSettings_Default.htm)|  Настройки
подключения по умолчанию.  
[DefaultForConfiguration](P_Tessa_Platform_Runtime_ConnectionSettings_DefaultForConfiguration.htm)|
Настройки подключения по умолчанию для использования в приложениях с папкой
конфигурации, которые не используют основную конфигурацию для подключения к
веб-сервису (или вообще не подключаются к веб-сервису).  
[InstanceName](P_Tessa_Platform_Runtime_ConnectionSettings_InstanceName.htm)|
Имя экземпляра.  
[IsSealed](P_Tessa_Platform_Runtime_ConnectionSettings_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[OpenTimeout](P_Tessa_Platform_Runtime_ConnectionSettings_OpenTimeout.htm)|
Таймаут на открытие соединения с сервером.  
[Proxy](P_Tessa_Platform_Runtime_ConnectionSettings_Proxy.htm)| Прокси-объект
для взаимодействия по сети.  
[SendTimeout](P_Tessa_Platform_Runtime_ConnectionSettings_SendTimeout.htm)|
Таймаут на отправку данных на сервер.  
[ServerCode](P_Tessa_Platform_Runtime_ConnectionSettings_ServerCode.htm)|  Код
сервера или null, если код сервера не используется. Необязательный параметр,
может использоваться, например, при отображении кода сервера в процессе логина
в приложении ApplicationManager.  
[SkipWinAuth](P_Tessa_Platform_Runtime_ConnectionSettings_SkipWinAuth.htm)|
Признак того, что при незаданных параметрах логина/пароля пропускается попытка
Windows-аутентификации.  
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
[ParseFromConfigurationSettings](M_Tessa_Platform_Runtime_ConnectionSettings_ParseFromConfigurationSettings.htm)|
Создаёт объект для подключения к сервисам, используя настройки из
конфигурационного файла app.json.  
[Seal](M_Tessa_Platform_Runtime_ConnectionSettings_Seal.htm)| Защищает объект
от изменений.  
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
