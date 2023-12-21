# CommonHelper.ProbingPath - свойство
Список папок, используемых для загрузки сборок в плагинах помимо папки с самим
плагином. Список разделяется точкой с запятой. Для получения списка путей
отдельно используйте метод
[GetProbingPathList()](M_Chronos_Platform_CommonHelper_GetProbingPathList.htm).
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static string ProbingPath { get; }
VB __Копировать
     Public Shared ReadOnly Property ProbingPath As String
    	Get
C++ __Копировать
     public:
    static property String^ ProbingPath {
    	String^ get ();
    }
F# __Копировать
     static member ProbingPath : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
