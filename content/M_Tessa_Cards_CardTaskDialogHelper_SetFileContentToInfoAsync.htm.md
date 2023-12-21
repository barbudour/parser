# CardTaskDialogHelper.SetFileContentToInfoAsync - метод
Асинхронно задаёт контент указанных файлов в соответствующие [!:CardFile.Info]
карточки файлов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task SetFileContentToInfoAsync(
    	Card dialogCard,
    	IReadOnlyCollection<IFile?> files,
    	ISession session,
    	IValidationResultBuilder validationResult,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function SetFileContentToInfoAsync ( 
    	dialogCard As Card,
    	files As IReadOnlyCollection(Of IFile),
    	session As ISession,
    	validationResult As IValidationResultBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    static Task^ SetFileContentToInfoAsync(
    	Card^ dialogCard, 
    	IReadOnlyCollection<IFile^>^ files, 
    	ISession^ session, 
    	IValidationResultBuilder^ validationResult, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member SetFileContentToInfoAsync : 
            dialogCard : Card * 
            files : IReadOnlyCollection<IFile> * 
            session : ISession * 
            validationResult : IValidationResultBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
dialogCard [Card](T_Tessa_Cards_Card.htm)
    Карточка диалога.
files
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[IFile](T_Tessa_Files_IFile.htm)>
    Коллекция файлов.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
    Результат валидации.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
