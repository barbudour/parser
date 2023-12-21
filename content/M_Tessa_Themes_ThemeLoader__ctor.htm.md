# ThemeLoader - конструктор
Создаёт объект с указанием списка папок, из которых будет выполняться загрузка
тем, сериализованных в файлы.
## __Definition
 **Пространство имён:** [Tessa.Themes](N_Tessa_Themes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ThemeLoader(
    	string folderPathList = null,
    	string fileSearchPattern = "*.json",
    	string propertiesSearchPattern = "props*.json"
    )
VB __Копировать
     Public Sub New ( 
    	Optional folderPathList As String = Nothing,
    	Optional fileSearchPattern As String = "*.json",
    	Optional propertiesSearchPattern As String = "props*.json"
    )
C++ __Копировать
     public:
    ThemeLoader(
    	String^ folderPathList = nullptr, 
    	String^ fileSearchPattern = L"*.json", 
    	String^ propertiesSearchPattern = L"props*.json"
    )
F# __Копировать
     new : 
            ?folderPathList : string * 
            ?fileSearchPattern : string * 
            ?propertiesSearchPattern : string 
    (* Defaults:
            let _folderPathList = defaultArg folderPathList null
            let _fileSearchPattern = defaultArg fileSearchPattern "*.json"
            let _propertiesSearchPattern = defaultArg propertiesSearchPattern "props*.json"
    *)
    -> ThemeLoader
#### Параметры
folderPathList [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
     Список папок, содержащий загружаемые темы. Может быть равен null или пустой строке, в этом случае сканирование на темы в файлах не выполняется. 
fileSearchPattern
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Шаблон поиска файлов с темами в папках folderPathList. Например, *.json. Не может быть равен null или пустой строке. 
propertiesSearchPattern
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
     Шаблон поиска файлов со свойствами тем в папках folderPathList. Например, *.json. Не может быть равен null или пустой строке. 
## __См. также
#### Ссылки
[ThemeLoader - ](T_Tessa_Themes_ThemeLoader.htm)
[Tessa.Themes - пространство имён](N_Tessa_Themes.htm)
