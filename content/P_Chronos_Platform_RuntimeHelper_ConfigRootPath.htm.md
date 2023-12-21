# RuntimeHelper.ConfigRootPath - свойство
Путь к папке, в которой выполняется поиск конфигурационных файлов, таких как
app.json и extensions.xml. Для поиска используется делегат
[ConfigRootPathFunc](P_Chronos_Platform_RuntimeHelper_ConfigRootPathFunc.htm).
Если он не задан или вернул null, то поиск выполняется в переменной окружения
с именем
[ConfigRootPathEnvironmentVariable](F_Chronos_Platform_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string ConfigRootPath { get; }
VB __Копировать
     Public Shared ReadOnly Property ConfigRootPath As String
    	Get
C++ __Копировать
     public:
    static property String^ ConfigRootPath {
    	String^ get ();
    }
F# __Копировать
     static member ConfigRootPath : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[RuntimeHelper - ](T_Chronos_Platform_RuntimeHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
