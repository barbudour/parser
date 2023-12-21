# PluginContractHelper - класс
Вспомогательные методы и константы для работы с плагинами, которые могут
использоваться в самом плагине.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginContractHelper
VB __Копировать
     Public NotInheritable Class PluginContractHelper
C++ __Копировать
     public ref class PluginContractHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PluginContractHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginContractHelper
##  __Свойства
[PluginElementXName](P_Chronos_Contracts_PluginContractHelper_PluginElementXName.htm)|
Имя корневого элемента, описывающего плагин, вместе с пространством имён.  
---|---  
## __Методы
[TryLoadConfig](M_Chronos_Contracts_PluginContractHelper_TryLoadConfig.htm)|
Загружает конфигурационный файл плагина из файла, расположенного по заданному
пути, и возвращает загруженный XML-документ или null, если файл отсутствовал
по заданному пути.  
---|---  
## __Поля
[PluginElementName](F_Chronos_Contracts_PluginContractHelper_PluginElementName.htm)|
Имя корневого элемента, описывающего плагин.  
---|---  
[PluginNamespace](F_Chronos_Contracts_PluginContractHelper_PluginNamespace.htm)|
Пространство имён XML для всех элементов конфигурационного файла.  
## __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
