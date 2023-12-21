# PdfPageExtractorContext - конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PdfPageExtractorContext(
    	string pdfFilePath,
    	List<ITempFile> pngPageFiles = null,
    	Func<double, CancellationToken, ValueTask> reportFileProgressActionAsync = null,
    	ScanFileDialogSettings settings = null
    )
VB __Копировать
     Public Sub New ( 
    	pdfFilePath As String,
    	Optional pngPageFiles As List(Of ITempFile) = Nothing,
    	Optional reportFileProgressActionAsync As Func(Of Double, CancellationToken, ValueTask) = Nothing,
    	Optional settings As ScanFileDialogSettings = Nothing
    )
C++ __Копировать
     public:
    PdfPageExtractorContext(
    	String^ pdfFilePath, 
    	List<ITempFile^>^ pngPageFiles = nullptr, 
    	Func<double, CancellationToken, ValueTask>^ reportFileProgressActionAsync = nullptr, 
    	ScanFileDialogSettings^ settings = nullptr
    )
F# __Копировать
     new : 
            pdfFilePath : string * 
            ?pngPageFiles : List<ITempFile> * 
            ?reportFileProgressActionAsync : Func<float, CancellationToken, ValueTask> * 
            ?settings : ScanFileDialogSettings 
    (* Defaults:
            let _pngPageFiles = defaultArg pngPageFiles null
            let _reportFileProgressActionAsync = defaultArg reportFileProgressActionAsync null
            let _settings = defaultArg settings null
    *)
    -> PdfPageExtractorContext
#### Параметры
pdfFilePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файлу PDF.
pngPageFiles
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
(Optional)
    Массив объектов, которые описывают все извлечённые страницы в виде изображений PNG.
reportFileProgressActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[Double](https://learn.microsoft.com/dotnet/api/system.double),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
(Optional)
    Метод, принимающий текущий прогресс операции в процентах и отображающий его пользователю.
settings
[ScanFileDialogSettings](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
(Optional)
     Настройки диалога сканирования, для которых вызывается извлечение страниц. Может быть равны null, если настройки неизвестны. 
## __См. также
#### Ссылки
[PdfPageExtractorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfPageExtractorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
