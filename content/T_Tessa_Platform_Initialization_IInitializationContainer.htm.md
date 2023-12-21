# IInitializationContainer - интерфейс
Объект, содержащий информацию, заполняемую при инициализации приложения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IInitializationContainer
VB __Копировать
     Public Interface IInitializationContainer
C++ __Копировать
     public interface class IInitializationContainer
F# __Копировать
     type IInitializationContainer = interface end
##  __Свойства
[CipherInfo](P_Tessa_Platform_Initialization_IInitializationContainer_CipherInfo.htm)|
Объект, содержащий настройки по шифрованию клиентских данных для текущего
пользователя. Может быть равен null, если настройки не получены с сервера.  
---|---  
[ConfigurationCacheIsActual](P_Tessa_Platform_Initialization_IInitializationContainer_ConfigurationCacheIsActual.htm)|
Признак того, что конфигурация в локальном кэше была актуальна на момент
запуска приложения.  
[ConfigurationInfo](P_Tessa_Platform_Initialization_IInitializationContainer_ConfigurationInfo.htm)|
Информация по конфигурации, полученная с сервера в процессе инициализации.  
[Dbms](P_Tessa_Platform_Initialization_IInitializationContainer_Dbms.htm)|
Используемая СУБД.  
[DefaultColors](P_Tessa_Platform_Initialization_IInitializationContainer_DefaultColors.htm)|
Цвета палитры, настроенные по умолчанию для всех пользователей.  
[Info](P_Tessa_Platform_Initialization_IInitializationContainer_Info.htm)|
Дополнительная информация для расширений.  
[IsInitialized](P_Tessa_Platform_Initialization_IInitializationContainer_IsInitialized.htm)|
Признак того, что инициализация была выполнена, и свойства объекта заполнены.  
[PersonalRoleSatellite](P_Tessa_Platform_Initialization_IInitializationContainer_PersonalRoleSatellite.htm)|
Карточка-сателлит для персональной роли пользователя.  
##  __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
