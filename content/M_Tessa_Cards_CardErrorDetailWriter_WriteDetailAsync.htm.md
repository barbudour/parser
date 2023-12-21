# CardErrorDetailWriter.WriteDetailAsync - метод
Записывает детальную информацию по ошибке.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WriteDetailAsync(
    	Guid id,
    	Guid cardTypeID,
    	string cardTypeCaption,
    	Guid cardID,
    	string cardName,
    	string requestJson,
    	IUser user,
    	DateTime modified,
    	IErrorDescription description,
    	IErrorDetails details,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function WriteDetailAsync ( 
    	id As Guid,
    	cardTypeID As Guid,
    	cardTypeCaption As String,
    	cardID As Guid,
    	cardName As String,
    	requestJson As String,
    	user As IUser,
    	modified As DateTime,
    	description As IErrorDescription,
    	details As IErrorDetails,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ WriteDetailAsync(
    	Guid id, 
    	Guid cardTypeID, 
    	String^ cardTypeCaption, 
    	Guid cardID, 
    	String^ cardName, 
    	String^ requestJson, 
    	IUser^ user, 
    	DateTime modified, 
    	IErrorDescription^ description, 
    	IErrorDetails^ details, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract WriteDetailAsync : 
            id : Guid * 
            cardTypeID : Guid * 
            cardTypeCaption : string * 
            cardID : Guid * 
            cardName : string * 
            requestJson : string * 
            user : IUser * 
            modified : DateTime * 
            description : IErrorDescription * 
            details : IErrorDetails * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override WriteDetailAsync : 
            id : Guid * 
            cardTypeID : Guid * 
            cardTypeCaption : string * 
            cardID : Guid * 
            cardName : string * 
            requestJson : string * 
            user : IUser * 
            modified : DateTime * 
            description : IErrorDescription * 
            details : IErrorDetails * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
id [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор ошибки.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки, с которым связана ошибка.
cardTypeCaption [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя типа карточки, с которым связана ошибка.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор экземпляра карточки, с которым связана ошибка.
cardName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Отображаемое имя (или Digest) экземпляра карточки, с которым связана ошибка.
requestJson [String](https://learn.microsoft.com/dotnet/api/system.string)
    Сериализованная информация по ошибке.
user [IUser](T_Tessa_Platform_Runtime_IUser.htm)
    Сотрудник, который записывает информацию по ошибке. Обычно это текущий сотрудник в сессии.
modified [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Дата и время ошибки в UTC. Обычно это текущие дата и время.
description
[IErrorDescription](T_Tessa_Platform_Runtime_IErrorDescription.htm)
     Описание ошибки. Не должно быть равно null. 
details [IErrorDetails](T_Tessa_Platform_Runtime_IErrorDetails.htm)
     Дополнительное описание ошибки. Не должно быть равно null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IErrorDetailWriter.WriteDetailAsync(Guid, Guid, String, Guid, String, String,
IUser, DateTime, IErrorDescription, IErrorDetails,
CancellationToken)](M_Tessa_Platform_Runtime_IErrorDetailWriter_WriteDetailAsync.htm)  
##  __См. также
#### Ссылки
[CardErrorDetailWriter - ](T_Tessa_Cards_CardErrorDetailWriter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
