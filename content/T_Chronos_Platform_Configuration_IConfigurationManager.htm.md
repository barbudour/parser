# IConfigurationManager - интерфейс
Объект, управляющий конфигурацией приложений Chronos. К объекту возможно
одновременное обращение из нескольких потоков.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IConfigurationManager
VB __Копировать
     Public Interface IConfigurationManager
C++ __Копировать
     public interface class IConfigurationManager
F# __Копировать
     type IConfigurationManager = interface end
##  __Свойства
[Configuration](P_Chronos_Platform_Configuration_IConfigurationManager_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[DefinedSymbols](P_Chronos_Platform_Configuration_IConfigurationManager_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Errors](P_Chronos_Platform_Configuration_IConfigurationManager_Errors.htm)|
Ошибки, которые возникли при разборе файлов конфигурации сервера.  
##  __См. также
#### Ссылки
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
