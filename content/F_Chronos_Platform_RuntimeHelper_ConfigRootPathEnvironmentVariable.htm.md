# RuntimeHelper.ConfigRootPathEnvironmentVariable - поле
Имя переменной окружения, в которой выполняется поиск конфигурационных файлов,
таких как app.json и extensions.xml. Если переменная равна точке ".", то
используется текущая папка приложения Directory.GetCurrentDirectory(). Если
переменная не задана, то выполняется поиск относительно папки Tessa.dll
вызовом
[GetActualLocationFolder(Assembly)](M_Chronos_Platform_PlatformExtensions_GetActualLocationFolder.htm).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public const string ConfigRootPathEnvironmentVariable = "TESSA_CONFIG_ROOT"
VB __Копировать
     Public Const ConfigRootPathEnvironmentVariable As String = "TESSA_CONFIG_ROOT"
C++ __Копировать
     public:
    literal String^ ConfigRootPathEnvironmentVariable = "TESSA_CONFIG_ROOT"
F# __Копировать
     static val mutable ConfigRootPathEnvironmentVariable: string
#### Значение поля
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
