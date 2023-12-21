# IClientInitializationCacheProvider - интерфейс
Объект, предоставляющий средства для сохранения информации по инициализации в
локальном кэше приложения и для загрузки этой информации из кэша.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Initialization](N_Tessa_Platform_Initialization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IClientInitializationCacheProvider
VB __Копировать
     Public Interface IClientInitializationCacheProvider
C++ __Копировать
     public interface class IClientInitializationCacheProvider
F# __Копировать
     type IClientInitializationCacheProvider = interface end
##  __Методы
[SaveResponseAsync](M_Tessa_Platform_Initialization_IClientInitializationCacheProvider_SaveResponseAsync.htm)|
Сохраняет ответ на запрос по инициализации в локальном кэше приложения.  
---|---  
[TryLoadResponseAsync](M_Tessa_Platform_Initialization_IClientInitializationCacheProvider_TryLoadResponseAsync.htm)|
Загружает ответ на запрос по инициализации из локального кэша приложения.
Возвращает null, если ответ на запрос отсутствует в кэше.  
## __См. также
#### Ссылки
[Tessa.Platform.Initialization - пространство
имён](N_Tessa_Platform_Initialization.htm)
