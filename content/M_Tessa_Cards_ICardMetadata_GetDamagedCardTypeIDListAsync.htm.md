# ICardMetadata.GetDamagedCardTypeIDListAsync - метод
Возвращает список идентификаторов повреждённых типов карточек. Собственно типы
карточек можно получить посредством сервиса типов карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<SealableList<Guid>> GetDamagedCardTypeIDListAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetDamagedCardTypeIDListAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SealableList(Of Guid))
C++ __Копировать
    ValueTask<SealableList<Guid>^> GetDamagedCardTypeIDListAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetDamagedCardTypeIDListAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SealableList<Guid>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SealableList](T_Tessa_Platform_Collections_SealableList_1.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>>  
Возвращаемое значение.
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
