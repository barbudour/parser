# ConfigurationManager - свойства
##  __Свойства
[Configuration](P_Chronos_Platform_Configuration_ConfigurationManager_Configuration.htm)|
Объект, описывающий конфигурацию приложения Tessa.  
---|---  
[Default](P_Chronos_Platform_Configuration_ConfigurationManager_Default.htm)|
Конфигурация приложения, доступная по умолчанию. Рекомендуется использовать
метод
[GetDefaultAsync(CancellationToken)](M_Chronos_Platform_Configuration_ConfigurationManager_GetDefaultAsync.htm)
для асинхронной инициализации конфигурации.  
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm)|
Текущие объявленные символы. По умолчанию соответствуют операционной системе,
разрядности процессора и другим параметрам среды выполнения. В ходе разбора
конфигурационных файлов список символов может изменяться директивой ".define".  
[Errors](P_Chronos_Platform_Configuration_ConfigurationManager_Errors.htm)|
Ошибки, которые возникли при разборе файлов конфигурации сервера.  
[GlobalDefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_GlobalDefinedSymbols.htm)|
Глобально объявленные символы по умолчанию, доступные для всех объектов
конфигурации. По умолчанию соответствуют операционной системе, разрядности
процессора и другим параметрам среды выполнения. Используются для
инициализации начального значения свойства
[DefinedSymbols](P_Chronos_Platform_Configuration_ConfigurationManager_DefinedSymbols.htm)
для каждого объекта конфигурации.  
[Settings](P_Chronos_Platform_Configuration_ConfigurationManager_Settings.htm)|
Настройки для приложения, доступные по умолчанию. В качестве ключа выступает
имя настройки, а в качестве значения - её значение (строка, число и т.п.).
Целые числа обычно представление как тип
[Int64](https://learn.microsoft.com/dotnet/api/system.int64).  
## __См. также
#### Ссылки
[ConfigurationManager -
](T_Chronos_Platform_Configuration_ConfigurationManager.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
