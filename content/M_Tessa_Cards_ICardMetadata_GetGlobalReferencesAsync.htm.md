# ICardMetadata.GetGlobalReferencesAsync - метод
Возвращает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl]), совместно использующиеся в типах карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ValueTask<IReadOnlyCollection<CardSerializableObject>> GetGlobalReferencesAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetGlobalReferencesAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IReadOnlyCollection(Of CardSerializableObject))
C++ __Копировать
    ValueTask<IReadOnlyCollection<CardSerializableObject^>^> GetGlobalReferencesAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetGlobalReferencesAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IReadOnlyCollection<CardSerializableObject>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>>  
Возвращаемое значение.
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
