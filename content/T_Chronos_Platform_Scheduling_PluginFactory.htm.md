# PluginFactory - класс
Хэлперы для создания экземпляров плагинов.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginFactory
VB __Копировать
     Public NotInheritable Class PluginFactory
C++ __Копировать
     public ref class PluginFactory abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PluginFactory = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginFactory
##  __Методы
[CreatePlugin](M_Chronos_Platform_Scheduling_PluginFactory_CreatePlugin.htm)|
Создаёт экземпляр плагина, который соответствует указанному типу typeFullName,
загруженному из указанной сборки assembly.  
---|---  
[FromArgs](M_Chronos_Platform_Scheduling_PluginFactory_FromArgs.htm)|
Возвращает информацию для создания плагина из параметров командной строки.  
[FromDictionary](M_Chronos_Platform_Scheduling_PluginFactory_FromDictionary.htm)|
Возвращает информацию для создания плагина из хеш-таблицы.  
[FromImport](M_Chronos_Platform_Scheduling_PluginFactory_FromImport.htm)|
Возвращает информацию для создания плагина из
[PluginImportingItem](T_Chronos_Platform_Scheduling_PluginImportingItem.htm).  
## __См. также
#### Ссылки
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
