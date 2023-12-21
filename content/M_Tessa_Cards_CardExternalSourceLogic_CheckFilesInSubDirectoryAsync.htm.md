# CardExternalSourceLogic.CheckFilesInSubDirectoryAsync - метод
Логика проверки файлов в поддиректории карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ValidationResult> CheckFilesInSubDirectoryAsync(
    	ISourceDirectoryProvider contentDirectoryProvider,
    	IEnumerable<string>? externalFileNames,
    	bool deleteAllowed,
    	string cardFullPath,
    	Func<string, bool> ignoredFileNamesFunc,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CheckFilesInSubDirectoryAsync ( 
    	contentDirectoryProvider As ISourceDirectoryProvider,
    	externalFileNames As IEnumerable(Of String),
    	deleteAllowed As Boolean,
    	cardFullPath As String,
    	ignoredFileNamesFunc As Func(Of String, Boolean),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     public:
    virtual ValueTask<ValidationResult^> CheckFilesInSubDirectoryAsync(
    	ISourceDirectoryProvider^ contentDirectoryProvider, 
    	IEnumerable<String^>^ externalFileNames, 
    	bool deleteAllowed, 
    	String^ cardFullPath, 
    	Func<String^, bool>^ ignoredFileNamesFunc, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CheckFilesInSubDirectoryAsync : 
            contentDirectoryProvider : ISourceDirectoryProvider * 
            externalFileNames : IEnumerable<string> * 
            deleteAllowed : bool * 
            cardFullPath : string * 
            ignoredFileNamesFunc : Func<string, bool> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
    override CheckFilesInSubDirectoryAsync : 
            contentDirectoryProvider : ISourceDirectoryProvider * 
            externalFileNames : IEnumerable<string> * 
            deleteAllowed : bool * 
            cardFullPath : string * 
            ignoredFileNamesFunc : Func<string, bool> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
contentDirectoryProvider
[ISourceDirectoryProvider](T_Tessa_Platform_SourceProviders_ISourceDirectoryProvider.htm)
    Провайдер поддиректории карточки.
externalFileNames
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
    Имена файлов, которые отонсятся к карточке.
deleteAllowed [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Если true - лишие файлы будут удалены.
cardFullPath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Полный путь к файлу карточки.
ignoredFileNamesFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
    Функция для определеия имен файлов, которые будут игнорироваться при проверке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Результат валидации.
#### Реализации
[ICardExternalSourceLogic.CheckFilesInSubDirectoryAsync(ISourceDirectoryProvider,
IEnumerable<String>, Boolean, String, Func<String, Boolean>,
CancellationToken)](M_Tessa_Cards_ICardExternalSourceLogic_CheckFilesInSubDirectoryAsync.htm)  
##  __См. также
#### Ссылки
[CardExternalSourceLogic - ](T_Tessa_Cards_CardExternalSourceLogic.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
