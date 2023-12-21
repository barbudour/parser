# PluginConfigHelper - класс
Хэлперы для работы с конфигурационным файлом, описывающим плагин.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginConfigHelper
VB __Копировать
     Public NotInheritable Class PluginConfigHelper
C++ __Копировать
     public ref class PluginConfigHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PluginConfigHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginConfigHelper
##  __Методы
[CreateXmlImportingElement](M_Chronos_Platform_PluginConfigHelper_CreateXmlImportingElement.htm)|
Создаёт XML-элемент, содержащий полную информацию об указанном плагине.  
---|---  
[TryLoadXmlImportingItem](M_Chronos_Platform_PluginConfigHelper_TryLoadXmlImportingItem.htm)|
Загружает информацию о плагине из конфигурационного файла.  
## __Поля
[PluginDescriptionAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginDescriptionAttributeName.htm)|
Атрибут корневого элемента, задающий описание плагина.  
---|---  
[PluginDisabledAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginDisabledAttributeName.htm)|
Атрибут корневого элемента, задающий признак того, что плагин не будет
использоваться.  
[PluginDisallowConcurrencyAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginDisallowConcurrencyAttributeName.htm)|
Атрибут корневого элемента, задающий признак запрета на параллельное
выполнение плагина.  
[PluginElementName](F_Chronos_Platform_PluginConfigHelper_PluginElementName.htm)|
Имя корневого элемента, описывающего плагин.  
[PluginLaunchImmediatelyAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginLaunchImmediatelyAttributeName.htm)|
Атрибут корневого элемента, задающий признак гарантированного запуска плагина
сразу после старта хоста.  
[PluginNameAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginNameAttributeName.htm)|
Атрибут корневого элемента, задающий имя плагина.  
[PluginNamespace](F_Chronos_Platform_PluginConfigHelper_PluginNamespace.htm)|
Пространство имён XML для всех элементов конфигурационного файла.  
[PluginVersionAttributeName](F_Chronos_Platform_PluginConfigHelper_PluginVersionAttributeName.htm)|
Атрибут корневого элемента, задающий версию плагина.  
[TriggerCronAttributeName](F_Chronos_Platform_PluginConfigHelper_TriggerCronAttributeName.htm)|
Атрибут, задающий строку в формате Cron для триггера.  
[TriggerElementName](F_Chronos_Platform_PluginConfigHelper_TriggerElementName.htm)|
Имя элемента, описывающего триггер.  
[TriggerRepeatSecondIntervalAttributeName](F_Chronos_Platform_PluginConfigHelper_TriggerRepeatSecondIntervalAttributeName.htm)|
Атрибут, задающий интервал выполнения плагина в секундах для триггера.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
