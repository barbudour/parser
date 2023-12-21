# CardStoreTaskExtensionContext - конструктор
Создаёт экземпляр класса с указанием запроса на сохранение карточки, типа
сохраняемой карточки, сохраняемого задания и его типа, метаинформации по типам
карточек и сессии пользователя, выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreTaskExtensionContext(
    	CardStoreRequest request,
    	CardStoreMethod method,
    	CardType cardType,
    	string cardTypeName,
    	CardTask task,
    	CardType taskType,
    	CardMetadataCompletionOption completionOption,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope,
    	ICardStoreExtensionContext storeContext,
    	Func<DateTime?> getStoreDateTime,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Sub New ( 
    	request As CardStoreRequest,
    	method As CardStoreMethod,
    	cardType As CardType,
    	cardTypeName As String,
    	task As CardTask,
    	taskType As CardType,
    	completionOption As CardMetadataCompletionOption,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	dbScope As IDbScope,
    	storeContext As ICardStoreExtensionContext,
    	getStoreDateTime As Func(Of DateTime?),
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     public:
    CardStoreTaskExtensionContext(
    	CardStoreRequest^ request, 
    	CardStoreMethod method, 
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	CardTask^ task, 
    	CardType^ taskType, 
    	CardMetadataCompletionOption^ completionOption, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope, 
    	ICardStoreExtensionContext^ storeContext, 
    	Func<Nullable<DateTime>>^ getStoreDateTime, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            request : CardStoreRequest * 
            method : CardStoreMethod * 
            cardType : CardType * 
            cardTypeName : string * 
            task : CardTask * 
            taskType : CardType * 
            completionOption : CardMetadataCompletionOption * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            dbScope : IDbScope * 
            storeContext : ICardStoreExtensionContext * 
            getStoreDateTime : Func<Nullable<DateTime>> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardStoreTaskExtensionContext
#### Параметры
request [CardStoreRequest](T_Tessa_Cards_CardStoreRequest.htm)
    Запрос на сохранение карточки.
method [CardStoreMethod](T_Tessa_Cards_CardStoreMethod.htm)
    Способ сохранения карточки.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип сохраняемой карточки. Может быть равен null, если неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Сохраняемое задание.
taskType [CardType](T_Tessa_Cards_CardType.htm)
    Тип сохраняемого задания.
completionOption
[CardMetadataCompletionOption](T_Tessa_Cards_Metadata_CardMetadataCompletionOption.htm)
    Тип сохраняемого задания. Вариант завершения задания или null, если вариант завершения неизвестен или задание не завершается. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, выполняющего операцию.
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
     Объект, обеспечивающий взаимодействие с базой данных. Значение равно null на клиенте и не равно null на сервере. 
storeContext
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
     Контекст сохранения основной карточки, в рамках которого сохраняется/завершается задание. 
getStoreDateTime
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)>>
     Функция, возвращающая текущие дату и время сохранения для использования в транзакции или null, если код не выполняется в транзакции. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
##  __См. также
#### Ссылки
[CardStoreTaskExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
