# ICardNewStrategy.SetSessionInfoAsync - метод
Устанавливает информацию о пользователе, создавшем карточку, по объекту
сессии.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task<bool> SetSessionInfoAsync(
    	CardNewResponse response,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetSessionInfoAsync ( 
    	response As CardNewResponse,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Boolean)
C++ __Копировать
    Task<bool>^ SetSessionInfoAsync(
    	CardNewResponse^ response, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetSessionInfoAsync : 
            response : CardNewResponse * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<bool> 
#### Параметры
response [CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)
    Ответ на запрос по созданию карточки.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Объект сессии, содержащий информацию о пользователе, создавшем карточку.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если информация о пользователе, создавшем карточку, была установлена;
false, если информацию о пользователе не удалось получить из объекта сессии.
## __См. также
#### Ссылки
[ICardNewStrategy - ](T_Tessa_Cards_ComponentModel_ICardNewStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
