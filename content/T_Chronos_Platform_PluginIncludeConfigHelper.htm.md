# PluginIncludeConfigHelper - класс
Хэлперы для работы с конфигурационным файлом, описывающим сборки с плагинами.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class PluginIncludeConfigHelper
VB __Копировать
     Public NotInheritable Class PluginIncludeConfigHelper
C++ __Копировать
     public ref class PluginIncludeConfigHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type PluginIncludeConfigHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PluginIncludeConfigHelper
##  __Методы
[LoadAssemblyLocationList](M_Chronos_Platform_PluginIncludeConfigHelper_LoadAssemblyLocationList.htm)|
Возвращает список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, располагающемся в указанной папке.
Конфигурационный файл должен иметь имя, заданное в константе
[PluginFileName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginFileName.htm).  
---|---  
##  __Поля
[PluginFileName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginFileName.htm)|
Имя конфигурационного файла, описывающего сборки с плагинами.  
---|---  
[PluginIncludeElementName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginIncludeElementName.htm)|
Имя элемента, описывающего сборку с плагинами.  
[PluginIncludeFileAttributeName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginIncludeFileAttributeName.htm)|
Имя атрибута, указывающего путь к файлу сборки с плагинами относительно папки
с конфигурационным файлом.  
[PluginIncludeNamespace](F_Chronos_Platform_PluginIncludeConfigHelper_PluginIncludeNamespace.htm)|
Пространство имён XML для всех элементов конфигурационного файла.  
[PluginListElementName](F_Chronos_Platform_PluginIncludeConfigHelper_PluginListElementName.htm)|
Имя корневого элемента, описывающего список сборок с плагинами.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
