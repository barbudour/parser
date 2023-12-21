# CommonHelper.GetProbingPathList - метод
Возвращает список папок, используемых для загрузки сборок в плагинах помимо
папки с самим плагином. Метод может вернуть пустой список, но он не возвращает
null.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<string> GetProbingPathList()
VB __Копировать
     Public Shared Function GetProbingPathList As List(Of String)
C++ __Копировать
     public:
    static List<String^>^ GetProbingPathList()
F# __Копировать
     static member GetProbingPathList : unit -> List<string> 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список папок, используемых для загрузки сборок в плагинах помимо папки с самим
плагином. Не равен null.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
