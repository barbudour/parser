# IPluginMetadataTrigger - интерфейс
Метаданные триггера, на основании которого планировщик будет вызывать плагин.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPluginMetadataTrigger : ISerializableMetadata<IPluginMetadataTrigger>
VB __Копировать
     Public Interface IPluginMetadataTrigger
    	Inherits ISerializableMetadata(Of IPluginMetadataTrigger)
C++ __Копировать
     public interface class IPluginMetadataTrigger : ISerializableMetadata<IPluginMetadataTrigger^>
F# __Копировать
     type IPluginMetadataTrigger = 
        interface
            interface ISerializableMetadata<IPluginMetadataTrigger>
        end
Implements
    [ISerializableMetadata](T_Chronos_Contracts_ISerializableMetadata_1.htm)<IPluginMetadataTrigger>
##  __Заметки
Каждый триггер должен либо описывать только один способ вызова
([Cron](P_Chronos_Contracts_IPluginMetadataTrigger_Cron.htm) или
[RepeatSecondInterval](P_Chronos_Contracts_IPluginMetadataTrigger_RepeatSecondInterval.htm)),
либо ссылаться на конфигурационный файл.
## __Свойства
[ConfigFile](P_Chronos_Contracts_IPluginMetadataTrigger_ConfigFile.htm)|  Имя
или путь к конфигурационному файлу, описывающему плагин, относительно папки со
сборкой плагина.  
---|---  
[Cron](P_Chronos_Contracts_IPluginMetadataTrigger_Cron.htm)|  Описание времени
вызова плагина в строке формата Cron.  
[RepeatSecondInterval](P_Chronos_Contracts_IPluginMetadataTrigger_RepeatSecondInterval.htm)|
Целочисленный интервал в секундах между вызовами плагина.  
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
[ValidateTrigger](M_Chronos_Platform_Scheduling_SchedulingExtensions_ValidateTrigger.htm)|
Выполняет проверку корректности заданных метаданных триггера.  
(Определяется
[SchedulingExtensions](T_Chronos_Platform_Scheduling_SchedulingExtensions.htm))  
##  __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
