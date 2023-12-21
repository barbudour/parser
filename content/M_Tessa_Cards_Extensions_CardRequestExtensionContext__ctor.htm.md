# CardRequestExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на универсальное взаимодействие с
сервисом карточек, информации о типе запроса, о карточке, файле и задании,
метаинформации по типам карточек и сессии пользователя, выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardRequestExtensionContext(
    	CardRequest request,
    	Guid requestType,
    	CardType cardType,
    	string cardTypeName,
    	CardType fileType,
    	string fileTypeName,
    	CardType taskType,
    	string taskTypeName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardRequest,
    	requestType As Guid,
    	cardType As CardType,
    	cardTypeName As String,
    	fileType As CardType,
    	fileTypeName As String,
    	taskType As CardType,
    	taskTypeName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional dbScope As IDbScope = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardRequestExtensionContext(
    	CardRequest^ request, 
    	Guid requestType, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	CardType^ fileType, 
    	String^ fileTypeName, 
    	CardType^ taskType, 
    	String^ taskTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardRequest * 
            requestType : Guid * 
            cardType : CardType * 
            cardTypeName : string * 
            fileType : CardType * 
            fileTypeName : string * 
            taskType : CardType * 
            taskTypeName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardRequestExtensionContext
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос на универсальное взаимодействие с сервисом карточек.
requestType [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
     Идентификатор типа универсального запроса к сервису карточек. Соответствует конкретной операции, которую требуется выполнить. 
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки. Может быть равен null, если неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
fileType [CardType](T_Tessa_Cards_CardType.htm)
    Тип файла. Может быть равен null, если неизвестен.
fileTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа файла. Может быть равно null, если неизвестно. Если задан параметр fileType, то имя получается из него, а этот параметр игнорируется. 
taskType [CardType](T_Tessa_Cards_CardType.htm)
    Тип задания. Может быть равен null, если неизвестен.
taskTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа задания. Может быть равно null, если неизвестно. Если задан параметр taskType, то имя получается из него, а этот параметр игнорируется. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего операцию.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm) (Optional)
     Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и не равно null на сервере. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardRequestExtensionContext -
](T_Tessa_Cards_Extensions_CardRequestExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
