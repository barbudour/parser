# IPluginMetadata - интерфейс
Метаданные плагина. Содержат метаданные триггера
[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm).
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPluginMetadata : IPluginMetadataTrigger, 
    	ISerializableMetadata<IPluginMetadataTrigger>
VB __Копировать
     Public Interface IPluginMetadata
    	Inherits IPluginMetadataTrigger, ISerializableMetadata(Of IPluginMetadataTrigger)
C++ __Копировать
     public interface class IPluginMetadata : IPluginMetadataTrigger, 
    	ISerializableMetadata<IPluginMetadataTrigger^>
F# __Копировать
     type IPluginMetadata = 
        interface
            interface IPluginMetadataTrigger
            interface ISerializableMetadata<IPluginMetadataTrigger>
        end
Implements
    [IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm), [ISerializableMetadata](T_Chronos_Contracts_ISerializableMetadata_1.htm)<[IPluginMetadataTrigger](T_Chronos_Contracts_IPluginMetadataTrigger.htm)>
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
## __Методы
[GetSerializable](M_Chronos_Contracts_ISerializableMetadata_1_GetSerializable.htm)|
Возвращает метаинформацию, которая может быть сериализована через атрибут
[System.SerializableAttribute]. Если текущий объект уже сериализуется, то он
может вернуть себя же.  
(Унаследован от
[ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm))  
---|---  
##  __Методы расширения
[ConfigFileSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_ConfigFileSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию о конфигурационном
файле.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
---|---  
[CronSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_CronSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию о строке в формате
Cron.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[DescriptionSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_DescriptionSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию об описании
плагина.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[NameSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_NameSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию об имени плагина.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[RepeatSecondIntervalSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_RepeatSecondIntervalSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию об интервале между
вызовами плагина.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[TriggerHasData](M_Chronos_Platform_Scheduling_SchedulingExtensions_TriggerHasData.htm)|
Возвращает признак того, что метаданные содержат какую-либо информацию по
триггеру.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[Validate](M_Chronos_Platform_Scheduling_SchedulingExtensions_Validate.htm)|
Выполняет проверку корректности заданных метаданных, и генерирует исключение в
случае ошибки.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[ValidateTrigger](M_Chronos_Platform_Scheduling_SchedulingExtensions_ValidateTrigger.htm)|
Выполняет проверку корректности заданных метаданных триггера.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
[VersionSpecified](M_Chronos_Platform_Scheduling_SchedulingExtensions_VersionSpecified.htm)|
Возвращает признак того, что метаданные содержат информацию о версии плагина.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
##  __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
