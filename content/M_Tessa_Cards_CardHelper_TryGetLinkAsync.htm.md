# CardHelper.TryGetLinkAsync - метод
Возвращает ссылку на открытие карточки в desktop- или в web-клиенте в
соответствии с объектом сессии.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<string> TryGetLinkAsync(
    	ISession session,
    	ICardCache cardCache,
    	Guid cardID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetLinkAsync ( 
    	session As ISession,
    	cardCache As ICardCache,
    	cardID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    static ValueTask<String^> TryGetLinkAsync(
    	ISession^ session, 
    	ICardCache^ cardCache, 
    	Guid cardID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetLinkAsync : 
            session : ISession * 
            cardCache : ICardCache * 
            cardID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя.
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
    Потокобезопасный кэш с карточками и дополнительными настройками.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор карточки, которая открывается по ссылке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Ссылка на открытие карточки в desktop- или в web-клиенте в соответствии с
объектом сессии илиnull, если сессия была открыта с web-клиента, или это
интеграция через Web API, где не удалось получить базовый адрес web-клиента.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
