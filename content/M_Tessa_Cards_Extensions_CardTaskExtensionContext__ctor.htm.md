# CardTaskExtensionContext - конструктор
Создаёт экземпляр класса с указанием типа сохраняемой карточки, сохраняемого
задания и его типа, метаинформации по типам карточек и сессии пользователя,
выполняющего операцию.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected CardTaskExtensionContext(
    	CardType cardType,
    	string cardTypeName,
    	CardTask task,
    	CardType taskType,
    	ICardMetadata cardMetadata,
    	ISession session,
    	IDbScope dbScope = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Sub New ( 
    	cardType As CardType,
    	cardTypeName As String,
    	task As CardTask,
    	taskType As CardType,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional dbScope As IDbScope = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    )
C++ __Копировать
     protected:
    CardTaskExtensionContext(
    	CardType^ cardType, 
    	String^ cardTypeName, 
    	CardTask^ task, 
    	CardType^ taskType, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	IDbScope^ dbScope = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     new : 
            cardType : CardType * 
            cardTypeName : string * 
            task : CardTask * 
            taskType : CardType * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _dbScope = defaultArg dbScope null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> CardTaskExtensionContext
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип сохраняемой карточки. Может быть равен null, если неизвестен.
cardTypeName [String](https://learn.microsoft.com/dotnet/api/system.string)
     Имя типа карточки. Может быть равно null, если неизвестно. Если задан параметр cardType, то имя получается из него, а этот параметр игнорируется. 
task [CardTask](T_Tessa_Cards_CardTask.htm)
    Сохраняемое задание.
taskType [CardType](T_Tessa_Cards_CardType.htm)
    Тип сохраняемого задания.
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
[CardTaskExtensionContext -
](T_Tessa_Cards_Extensions_CardTaskExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
