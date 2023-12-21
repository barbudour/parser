# IIgnoredFilesProvider.GetIgnoredFileNames - метод
Получает список имен игнорируемых файлов
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IEnumerable<string> GetIgnoredFileNames(
    	[NotNullAttribute] string rootFolder,
    	string ignoredFilesPathOverride = null
    )
VB __Копировать
    <NotNullAttribute>
    Function GetIgnoredFileNames ( 
    	<NotNullAttribute> rootFolder As String,
    	Optional ignoredFilesPathOverride As String = Nothing
    ) As IEnumerable(Of String)
C++ __Копировать
    [NotNullAttribute]
    IEnumerable<String^>^ GetIgnoredFileNames(
    	[NotNullAttribute] String^ rootFolder, 
    	String^ ignoredFilesPathOverride = nullptr
    )
F# __Копировать
     [<NotNullAttribute>]
    abstract GetIgnoredFileNames : 
            [<NotNullAttribute>] rootFolder : string * 
            ?ignoredFilesPathOverride : string 
    (* Defaults:
            let _ignoredFilesPathOverride = defaultArg ignoredFilesPathOverride null
    *)
    -> IEnumerable<string> 
#### Параметры
rootFolder [String](https://learn.microsoft.com/dotnet/api/system.string)
    Корневая папка списка игнорируемых файлов.
ignoredFilesPathOverride
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Опционально, путь до файла со списком паттернов для имен игнорируемых файлов.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список имен игнорируемых файлов
##  __См. также
#### Ссылки
[IIgnoredFilesProvider -
](T_Tessa_Applications_Package_IIgnoredFilesProvider.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
