# PdfGeneratorContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PdfGeneratorContext(
    	List<ITempFile> pngPageFiles,
    	List<ITempFile> temporaryFiles = null,
    	List<ITempFolder> temporaryFolders = null,
    	Func<double, CancellationToken, Task> reportProgressActionAsync = null,
    	bool addStamp = false,
    	Object externalContext = null
    )
VB __Копировать
     Public Sub New ( 
    	pngPageFiles As List(Of ITempFile),
    	Optional temporaryFiles As List(Of ITempFile) = Nothing,
    	Optional temporaryFolders As List(Of ITempFolder) = Nothing,
    	Optional reportProgressActionAsync As Func(Of Double, CancellationToken, Task) = Nothing,
    	Optional addStamp As Boolean = false,
    	Optional externalContext As Object = Nothing
    )
C++ __Копировать
     public:
    PdfGeneratorContext(
    	List<ITempFile^>^ pngPageFiles, 
    	List<ITempFile^>^ temporaryFiles = nullptr, 
    	List<ITempFolder^>^ temporaryFolders = nullptr, 
    	Func<double, CancellationToken, Task^>^ reportProgressActionAsync = nullptr, 
    	bool addStamp = false, 
    	Object^ externalContext = nullptr
    )
F# __Копировать
     new : 
            pngPageFiles : List<ITempFile> * 
            ?temporaryFiles : List<ITempFile> * 
            ?temporaryFolders : List<ITempFolder> * 
            ?reportProgressActionAsync : Func<float, CancellationToken, Task> * 
            ?addStamp : bool * 
            ?externalContext : Object 
    (* Defaults:
            let _temporaryFiles = defaultArg temporaryFiles null
            let _temporaryFolders = defaultArg temporaryFolders null
            let _reportProgressActionAsync = defaultArg reportProgressActionAsync null
            let _addStamp = defaultArg addStamp false
            let _externalContext = defaultArg externalContext null
    *)
    -> PdfGeneratorContext
#### Параметры
pngPageFiles
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
     Файлы изображений в формате PNG со страницами в порядке их добавления. В одном файле содержится изображение для одной страницы. 
temporaryFiles
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
(Optional)
     Список временных файлов, которые будут гарантированно удалены после завершения метода. 
temporaryFolders
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFolder](T_Tessa_Platform_IO_ITempFolder.htm)>
(Optional)
     Список временных папок, которые будут гарантированно удалены после завершения метода. 
reportProgressActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
(Optional)
     Метод, принимающий текущий прогресс операции в процентах и отображающий его пользователю. 
addStamp [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
     Признак того, что для документа требуется вывести штамп. При этом формирование штампа обычно выполняется посредством расширений. 
externalContext [Object](https://learn.microsoft.com/dotnet/api/system.object)
(Optional)
     Контекст, в пределах которого выполняется формирование PDF. Например, может быть контекстом [IFileControlExtensionContext](T_Tessa_UI_Files_IFileControlExtensionContext.htm) или null, если контекст неизвестен. 
#### Возвращаемое значение
Объект, содержащий сформированный документ PDF, или null, если формирование
документа не удалось.
## __См. также
#### Ссылки
[PdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
