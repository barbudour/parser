# ConsoleScriptHelper - класс
Вспомогательные методы для резолва консольных скриптов.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ConsoleScriptHelper
VB __Копировать
     Public NotInheritable Class ConsoleScriptHelper
C++ __Копировать
     public ref class ConsoleScriptHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ConsoleScriptHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleScriptHelper
##  __Методы
[CreateFinder](M_Tessa_Platform_ConsoleApps_ConsoleScriptHelper_CreateFinder.htm)|
Создаёт объект, позволяющий осуществлять поиск типов
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm) в указанном
каталоге со сборками.  
---|---  
[FindAndGetScripts](M_Tessa_Platform_ConsoleApps_ConsoleScriptHelper_FindAndGetScripts.htm)|
Выполняет поиск и возвращает функции создания объектов скриптов
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm) в папке
приложения. Возвращает для каждого найденного имени скрипта функцию, которая
создаёт объект скрипта. Не возвращает null.  
[GetScripts](M_Tessa_Platform_ConsoleApps_ConsoleScriptHelper_GetScripts.htm)|
Выполняет поиск и возвращает функции создания объектов скриптов
[IConsoleScript](T_Tessa_Platform_ConsoleApps_IConsoleScript.htm) по заданным
параметрам. Возвращает для каждого найденного имени скрипта функцию, которая
создаёт объект скрипта. Не возвращает null.  
## __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
