# LocalPackageHelper.GetEnumerateLocalPackageFilePaths - метод
Возвращает перечисление путей к файлам
[LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm)
найденным по пути applicationsPath в том числе дочерних.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IEnumerable<string> GetEnumerateLocalPackageFilePaths(
    	string applicationsPath,
    	string exceptServerCode = null,
    	string exceptApplicationAlias = null,
    	SearchOption searchOption = 0
    )
VB __Копировать
     Public Shared Function GetEnumerateLocalPackageFilePaths ( 
    	applicationsPath As String,
    	Optional exceptServerCode As String = Nothing,
    	Optional exceptApplicationAlias As String = Nothing,
    	Optional searchOption As SearchOption = 0
    ) As IEnumerable(Of String)
C++ __Копировать
     public:
    static IEnumerable<String^>^ GetEnumerateLocalPackageFilePaths(
    	String^ applicationsPath, 
    	String^ exceptServerCode = nullptr, 
    	String^ exceptApplicationAlias = nullptr, 
    	SearchOption^ searchOption = 0
    )
F# __Копировать
     static member GetEnumerateLocalPackageFilePaths : 
            applicationsPath : string * 
            ?exceptServerCode : string * 
            ?exceptApplicationAlias : string * 
            ?searchOption : SearchOption 
    (* Defaults:
            let _exceptServerCode = defaultArg exceptServerCode null
            let _exceptApplicationAlias = defaultArg exceptApplicationAlias null
            let _searchOption = defaultArg searchOption 0
    *)
    -> IEnumerable<string> 
#### Параметры
applicationsPath
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к папке содержащей приложения.
exceptServerCode
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Код сервера. Используется совместно с exceptApplicationAlias для исключения пути к приложению заргуженному с сервера имеющий указанный код.
exceptApplicationAlias
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Алиас приложения. Используется совместно с exceptServerCode для исключения пути к приложению имеющему указанный алиас.
searchOption
[SearchOption](https://learn.microsoft.com/dotnet/api/system.io.searchoption)
(Optional)
    Параметры поиска файлов [LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm) в applicationsPath.
#### Возвращаемое значение
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Перечисление путей к файлам
[LocalPackageFile](F_Tessa_Applications_ApplicationCardConstants_LocalPackageFile.htm).
##  __См. также
#### Ссылки
[LocalPackageHelper -
](T_Tessa_Applications_Synchronization_LocalPackageHelper.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
