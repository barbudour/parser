# CardFileVersionStrategy.SetUploadErrorAsync - метод
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором произошла с ошибкой.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetUploadErrorAsync(
    	Guid versionRowID,
    	DateTime errorDate,
    	string errorMessage,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetUploadErrorAsync ( 
    	versionRowID As Guid,
    	errorDate As DateTime,
    	errorMessage As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SetUploadErrorAsync(
    	Guid versionRowID, 
    	DateTime errorDate, 
    	String^ errorMessage, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetUploadErrorAsync : 
            versionRowID : Guid * 
            errorDate : DateTime * 
            errorMessage : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SetUploadErrorAsync : 
            versionRowID : Guid * 
            errorDate : DateTime * 
            errorMessage : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла.
errorDate [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата произошедшей ошибки.
errorMessage [String](https://learn.microsoft.com/dotnet/api/system.string)
    Текст произошедшей ошибки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardFileVersionStrategy.SetUploadErrorAsync(Guid, DateTime, String,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_SetUploadErrorAsync.htm)  
##  __См. также
#### Ссылки
[CardFileVersionStrategy -
](T_Tessa_Cards_ComponentModel_CardFileVersionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
