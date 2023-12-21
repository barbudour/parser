# RuntimeHelper.GetDefaultConfigRootPath - метод
Алгоритм поиска по умолчанию для папки, в которой выполняется поиск
конфигурационных файлов, таких как app.json и extensions.xml. Поиск сначала
выполняется в переменной окружения с именем
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetDefaultConfigRootPath()
VB __Копировать
     Public Shared Function GetDefaultConfigRootPath As String
C++ __Копировать
     public:
    static String^ GetDefaultConfigRootPath()
F# __Копировать
     static member GetDefaultConfigRootPath : unit -> string 
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Папка по умолчанию
[ConfigRootPath](P_Chronos_Platform_RuntimeHelper_ConfigRootPath.htm).
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
