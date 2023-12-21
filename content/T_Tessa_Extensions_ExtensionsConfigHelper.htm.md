# ExtensionsConfigHelper - класс
Хэлперы для работы с конфигурационным файлом, описывающим сборки с плагинами.
## __Definition
 **Пространство имён:** [Tessa.Extensions](N_Tessa_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ExtensionsConfigHelper
VB __Копировать
     Public NotInheritable Class ExtensionsConfigHelper
C++ __Копировать
     public ref class ExtensionsConfigHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ExtensionsConfigHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ExtensionsConfigHelper
##  __Методы
[LoadAssemblyLocationList](M_Tessa_Extensions_ExtensionsConfigHelper_LoadAssemblyLocationList.htm)|
Возвращает список полных путей до сборок с плагинами, которые были указаны в
конфигурационном файле, располагающемся в указанной папке.
Конфигурационный файл должен иметь имя, заданное в константе
[ConfigFileName](F_Tessa_Extensions_ExtensionsConfigHelper_ConfigFileName.htm).  
---|---  
##  __Поля
[ConfigFileName](F_Tessa_Extensions_ExtensionsConfigHelper_ConfigFileName.htm)|
Имя конфигурационного файла, описывающего сборки с плагинами.  
---|---  
[ConfigNamespace](F_Tessa_Extensions_ExtensionsConfigHelper_ConfigNamespace.htm)|
Пространство имён XML для всех элементов конфигурационного файла.  
## __См. также
#### Ссылки
[Tessa.Extensions - пространство имён](N_Tessa_Extensions.htm)
