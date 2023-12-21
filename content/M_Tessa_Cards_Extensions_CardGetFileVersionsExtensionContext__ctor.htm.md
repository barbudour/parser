# CardGetFileVersionsExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на получение версий файла, типа и
имени карточки, типа и имени файла, версии которого загружаются,
метаинформации по типам карточек и сессии пользователя, выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardGetFileVersionsExtensionContext(
    	CardGetFileVersionsRequest request,
    	CardGetFileVersionsMethod method,
    	CardType cardType,
    	string cardTypeName,
    	CardType fileType,
    	string fileTypeName,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardGetFileVersionsRequest,
    	method As CardGetFileVersionsMethod,
    	cardType As CardType,
    	cardTypeName As String,
    	fileType As CardType,
    	fileTypeName As String,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional dbScope As IDbScope = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardGetFileVersionsExtensionContext(
    	CardGetFileVersionsRequest^ request, 
    	CardGetFileVersionsMethod method, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	CardType^ fileType, 
    	String^ fileTypeName, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardGetFileVersionsRequest * 
            method : CardGetFileVersionsMethod * 
            cardType : CardType * 
            cardTypeName : string * 
            fileType : CardType * 
            fileTypeName : string * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardGetFileVersionsExtensionContext
#### Параметры
request
[CardGetFileVersionsRequest](T_Tessa_Cards_CardGetFileVersionsRequest.htm)
    Запрос на получение версий файла.
method
[CardGetFileVersionsMethod](T_Tessa_Cards_CardGetFileVersionsMethod.htm)
    Способ загрузки списка версий файла.
cardType [CardType](T_Tessa_Cards_CardType.htm)
     Тип карточки, которая содержит файл с загружаемыми версиями. Может быть равен null, если неизвестен. 
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки, которая содержит файл с загружаемыми версиями. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
fileType [CardType](T_Tessa_Cards_CardType.htm)
    Тип файла или null, если тип файла неизвестен.
fileTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа файла или null, если имя типа неизвестно. Имя может быть задано для несуществующего типа файла. Если задан параметр fileType, то имя получается из него, а этот параметр игнорируется. 
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
[CardGetFileVersionsExtensionContext -
](T_Tessa_Cards_Extensions_CardGetFileVersionsExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
