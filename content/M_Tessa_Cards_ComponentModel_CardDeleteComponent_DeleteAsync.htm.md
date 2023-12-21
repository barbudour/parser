# CardDeleteComponent.DeleteAsync - метод
Удаляет карточку.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardDeleteResponse> DeleteAsync(
    	CardDeleteRequest request,
    	ICardMetadata cardMetadata,
    	ISession session,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	request As CardDeleteRequest,
    	cardMetadata As ICardMetadata,
    	session As ISession,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardDeleteResponse)
C++ __Копировать
     public:
    virtual Task<CardDeleteResponse^>^ DeleteAsync(
    	CardDeleteRequest^ request, 
    	ICardMetadata^ cardMetadata, 
    	ISession^ session, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            request : CardDeleteRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardDeleteResponse> 
    override DeleteAsync : 
            request : CardDeleteRequest * 
            cardMetadata : ICardMetadata * 
            session : ISession * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardDeleteResponse> 
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос на удаление карточки.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
    Сессия пользователя, удаляющего карточку.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardDeleteResponse](T_Tessa_Cards_CardDeleteResponse.htm)>  
Ответ на запрос по удалению карточки.
#### Реализации
[ICardDeleteComponent.DeleteAsync(CardDeleteRequest, ICardMetadata, ISession,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardDeleteComponent_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardDeleteComponent - ](T_Tessa_Cards_ComponentModel_CardDeleteComponent.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
