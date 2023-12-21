# ApplicationFolders - класс
Папки приложений, используемые в системе.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationFolders : IApplicationFolders
VB __Копировать
     Public NotInheritable Class ApplicationFolders
    	Implements IApplicationFolders
C++ __Копировать
     public ref class ApplicationFolders sealed : IApplicationFolders
F# __Копировать
     [<SealedAttribute>]
    type ApplicationFolders = 
        class
            interface IApplicationFolders
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationFolders
Implements
    [IApplicationFolders](T_Tessa_Platform_Runtime_IApplicationFolders.htm)
##  __Конструкторы
[ApplicationFolders](M_Tessa_Platform_Runtime_ApplicationFolders__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationFolders  
---|---  
##  __Свойства
[Applications](P_Tessa_Platform_Runtime_ApplicationFolders_Applications.htm)|
Путь к папке с приложениями относительно папки
[LocalData](P_Tessa_Platform_Runtime_IApplicationFolders_LocalData.htm).  
---|---  
[Cache](P_Tessa_Platform_Runtime_ApplicationFolders_Cache.htm)|  Путь к папке
с локальным кэшом для приложений относительно папки
[LocalData](P_Tessa_Platform_Runtime_IApplicationFolders_LocalData.htm).  
[LocalData](P_Tessa_Platform_Runtime_ApplicationFolders_LocalData.htm)|
Полный путь к папке, которая используется как папка %AppData% для приложений
Tessa.  
[RoamingData](P_Tessa_Platform_Runtime_ApplicationFolders_RoamingData.htm)|
Полный путь к папке, которая используется как папка %AppData% для приложений
Tessa.  
[Settings](P_Tessa_Platform_Runtime_ApplicationFolders_Settings.htm)|  Путь к
папке с настройками приложений относительно папки
[RoamingData](P_Tessa_Platform_Runtime_IApplicationFolders_RoamingData.htm).  
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
[GetApplicationFolder](M_Tessa_Platform_Runtime_ApplicationFolders_GetApplicationFolder.htm)|
Возвращает папку установки приложения для заданных параметров.  
[GetBaseAddressFolderName](M_Tessa_Platform_Runtime_ApplicationFolders_GetBaseAddressFolderName.htm)|
Возвращает название папки по базовому адресу.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInstanceFolderName](M_Tessa_Platform_Runtime_ApplicationFolders_GetInstanceFolderName.htm)|
Возвращает название папки с именем экземпляра сервера, к которому подключается
приложение.  
[GetLocalCacheFolder](M_Tessa_Platform_Runtime_ApplicationFolders_GetLocalCacheFolder.htm)|
Возвращает папку с локальным кэшом приложения для заданных параметров.  
[GetSettingsFolder](M_Tessa_Platform_Runtime_ApplicationFolders_GetSettingsFolder.htm)|
Возвращает папку настроек приложения для заданных параметров.  
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
