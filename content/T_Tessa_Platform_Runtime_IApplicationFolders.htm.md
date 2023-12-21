# IApplicationFolders - интерфейс
Папки приложений, используемые в системе.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IApplicationFolders
VB __Копировать
     Public Interface IApplicationFolders
C++ __Копировать
     public interface class IApplicationFolders
F# __Копировать
     type IApplicationFolders = interface end
##  __Свойства
[Applications](P_Tessa_Platform_Runtime_IApplicationFolders_Applications.htm)|
Путь к папке с приложениями относительно папки
[LocalData](P_Tessa_Platform_Runtime_IApplicationFolders_LocalData.htm).  
---|---  
[Cache](P_Tessa_Platform_Runtime_IApplicationFolders_Cache.htm)|  Путь к папке
с локальным кэшом для приложений относительно папки
[LocalData](P_Tessa_Platform_Runtime_IApplicationFolders_LocalData.htm).  
[LocalData](P_Tessa_Platform_Runtime_IApplicationFolders_LocalData.htm)|
Полный путь к папке, которая используется как папка %AppData% для приложений
Tessa.  
[RoamingData](P_Tessa_Platform_Runtime_IApplicationFolders_RoamingData.htm)|
Полный путь к папке, которая используется как папка %AppData% для приложений
Tessa.  
[Settings](P_Tessa_Platform_Runtime_IApplicationFolders_Settings.htm)|  Путь к
папке с настройками приложений относительно папки
[RoamingData](P_Tessa_Platform_Runtime_IApplicationFolders_RoamingData.htm).  
## __Методы
[GetApplicationFolder](M_Tessa_Platform_Runtime_IApplicationFolders_GetApplicationFolder.htm)|
Возвращает папку установки приложения для заданных параметров.  
---|---  
[GetBaseAddressFolderName](M_Tessa_Platform_Runtime_IApplicationFolders_GetBaseAddressFolderName.htm)|
Возвращает название папки по базовому адресу.  
[GetInstanceFolderName](M_Tessa_Platform_Runtime_IApplicationFolders_GetInstanceFolderName.htm)|
Возвращает название папки с именем экземпляра сервера, к которому подключается
приложение.  
[GetLocalCacheFolder](M_Tessa_Platform_Runtime_IApplicationFolders_GetLocalCacheFolder.htm)|
Возвращает папку с локальным кэшом приложения для заданных параметров.  
[GetSettingsFolder](M_Tessa_Platform_Runtime_IApplicationFolders_GetSettingsFolder.htm)|
Возвращает папку настроек приложения для заданных параметров.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
