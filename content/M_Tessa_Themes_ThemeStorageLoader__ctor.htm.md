# ThemeStorageLoader - конструктор
Инициализирует новый экземпляр класса
[ThemeStorageLoader](T_Tessa_Themes_ThemeStorageLoader.htm)
##  __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ThemeStorageLoader(
    	Func<CancellationToken, ValueTask<HashSet<string>>> getPathListFuncAsync,
    	Func<CancellationToken, ValueTask<Dictionary<string, Object>>> createThemeStorageFuncAsync,
    	Func<CancellationToken, ValueTask<Dictionary<string, Dictionary<string, Object>>>> createThemeCacheFuncAsync,
    	string folderPathList = null,
    	string fileSearchPattern = "*.json",
    	string propertiesSearchPattern = "props*.json",
    	string defaultThemeName = null
    )
VB __Копировать
     Public Sub New ( 
    	getPathListFuncAsync As Func(Of CancellationToken, ValueTask(Of HashSet(Of String))),
    	createThemeStorageFuncAsync As Func(Of CancellationToken, ValueTask(Of Dictionary(Of String, Object))),
    	createThemeCacheFuncAsync As Func(Of CancellationToken, ValueTask(Of Dictionary(Of String, Dictionary(Of String, Object)))),
    	Optional folderPathList As String = Nothing,
    	Optional fileSearchPattern As String = "*.json",
    	Optional propertiesSearchPattern As String = "props*.json",
    	Optional defaultThemeName As String = Nothing
    )
C++ __Копировать
     public:
    ThemeStorageLoader(
    	Func<CancellationToken, ValueTask<HashSet<String^>^>>^ getPathListFuncAsync, 
    	Func<CancellationToken, ValueTask<Dictionary<String^, Object^>^>>^ createThemeStorageFuncAsync, 
    	Func<CancellationToken, ValueTask<Dictionary<String^, Dictionary<String^, Object^>^>^>>^ createThemeCacheFuncAsync, 
    	String^ folderPathList = nullptr, 
    	String^ fileSearchPattern = L"*.json", 
    	String^ propertiesSearchPattern = L"props*.json", 
    	String^ defaultThemeName = nullptr
    )
F# __Копировать
     new : 
            getPathListFuncAsync : Func<CancellationToken, ValueTask<HashSet<string>>> * 
            createThemeStorageFuncAsync : Func<CancellationToken, ValueTask<Dictionary<string, Object>>> * 
            createThemeCacheFuncAsync : Func<CancellationToken, ValueTask<Dictionary<string, Dictionary<string, Object>>>> * 
            ?folderPathList : string * 
            ?fileSearchPattern : string * 
            ?propertiesSearchPattern : string * 
            ?defaultThemeName : string 
    (* Defaults:
            let _folderPathList = defaultArg folderPathList null
            let _fileSearchPattern = defaultArg fileSearchPattern "*.json"
            let _propertiesSearchPattern = defaultArg propertiesSearchPattern "props*.json"
            let _defaultThemeName = defaultArg defaultThemeName null
    *)
    -> ThemeStorageLoader
#### Параметры
getPathListFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>>>
createThemeStorageFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>>
createThemeCacheFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>>>
folderPathList [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
fileSearchPattern
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
propertiesSearchPattern
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
defaultThemeName
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
## __См. также
#### Ссылки
[ThemeStorageLoader - ](T_Tessa_Themes_ThemeStorageLoader.htm)
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)
