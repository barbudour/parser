# IPluginMetadata - свойства
##  __Свойства
[ConfigFile](P_Chronos_Contracts_IPluginMetadataTrigger_ConfigFile.htm)|  Имя
или путь к конфигурационному файлу, описывающему плагин, относительно папки со
сборкой плагина.  
(Унаследован от
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm))  
---|---  
[Cron](P_Chronos_Contracts_IPluginMetadataTrigger_Cron.htm)|  Описание времени
вызова плагина в строке формата Cron.  
(Унаследован от
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm))  
[Description](P_Chronos_Contracts_IPluginMetadata_Description.htm)|  Описание
плагина. Не используется платформой, но может предоставляться в информативных
целях.  
[Disabled](P_Chronos_Contracts_IPluginMetadata_Disabled.htm)|  Признак того,
что плагин не будет использоваться.  
[DisallowConcurrency](P_Chronos_Contracts_IPluginMetadata_DisallowConcurrency.htm)|
Признак запрета параллельного выполнения плагина. Если признак установлен, то,
пока процесс плагина выполняется, другой процесс того же плагина не будет
запущен, а планировщик будет дожидаться следующего срабатывания одного из
триггеров.  
[LaunchImmediately](P_Chronos_Contracts_IPluginMetadata_LaunchImmediately.htm)|
Признак гарантированного запуска плагина сразу после старта хоста, независимо
от расписания.  
[Name](P_Chronos_Contracts_IPluginMetadata_Name.htm)|  Имя плагина.
Используется для логирования и определения уникальности плагина.  
[RepeatSecondInterval](P_Chronos_Contracts_IPluginMetadataTrigger_RepeatSecondInterval.htm)|
Целочисленный интервал в секундах между вызовами плагина.  
(Унаследован от
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm))  
[Version](P_Chronos_Contracts_IPluginMetadata_Version.htm)|  Версия плагина.
Используется для логирования и определения уникальности плагина.  
## __См. также
#### Ссылки
[IPluginMetadata - ](T_Chronos_Contracts_IPluginMetadata.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
