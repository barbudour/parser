# CommonHelper.GetActualProbingPathList - метод
Возвращает список фактически существующих полных путей к папкам, из которых
требуется загружать сборки помимо папки с плагином. Список определяется на
основании метода
[GetProbingPathList()](M_Chronos_Platform_CommonHelper_GetProbingPathList.htm).
Метод может вернуть пустой список, но он не возвращает null.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static List<string> GetActualProbingPathList(
    	Assembly pathRootAssembly = null
    )
VB __Копировать
     Public Shared Function GetActualProbingPathList ( 
    	Optional pathRootAssembly As Assembly = Nothing
    ) As List(Of String)
C++ __Копировать
     public:
    static List<String^>^ GetActualProbingPathList(
    	Assembly^ pathRootAssembly = nullptr
    )
F# __Копировать
     static member GetActualProbingPathList : 
            ?pathRootAssembly : Assembly 
    (* Defaults:
            let _pathRootAssembly = defaultArg pathRootAssembly null
    *)
    -> List<string> 
#### Параметры
pathRootAssembly
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
(Optional)
     Сборка, определяющая папку, относительно которой выполняется поиск для относительных путей, или null, если используется запускающая сборка [GetEntryAssembly()](https://learn.microsoft.com/dotnet/api/system.reflection.assembly.getentryassembly#system-reflection-assembly-getentryassembly). 
#### Возвращаемое значение
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список папок, используемых для загрузки сборок в плагинах помимо папки с самим
плагином. Не равен null.
## __См. также
#### Ссылки
[CommonHelper - ](T_Chronos_Platform_CommonHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
