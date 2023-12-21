# CardRepository.DeleteAsync - метод
Удаляет карточку со всеми файлами и заданиями по информации, переданной в
запросе. Для успешного удаления карточки необходимо предварительно удалить все
карточки, которые на неё ссылаются.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardDeleteResponse> DeleteAsync(
    	CardDeleteRequest request,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteAsync ( 
    	request As CardDeleteRequest,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardDeleteResponse)
C++ __Копировать
     public:
    virtual Task<CardDeleteResponse^>^ DeleteAsync(
    	CardDeleteRequest^ request, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteAsync : 
            request : CardDeleteRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardDeleteResponse> 
    override DeleteAsync : 
            request : CardDeleteRequest * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardDeleteResponse> 
#### Параметры
request [CardDeleteRequest](T_Tessa_Cards_CardDeleteRequest.htm)
    Запрос, содержащий информацию по карточке, которая должна быть удалена.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardDeleteResponse](T_Tessa_Cards_CardDeleteResponse.htm)>  
Ответ на запрос, содержащий информацию о валидации процесса удаления карточки,
включая сообщения об ошибках.
#### Реализации
[ICardRepository.DeleteAsync(CardDeleteRequest,
CancellationToken)](M_Tessa_Cards_ICardRepository_DeleteAsync.htm)  
##  __См. также
#### Ссылки
[CardRepository - ](T_Tessa_Cards_CardRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
