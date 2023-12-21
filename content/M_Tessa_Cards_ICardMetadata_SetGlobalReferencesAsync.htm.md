# ICardMetadata.SetGlobalReferencesAsync - метод
Устанавливает список глобальных объектов ([CardTypeForm], [CardTypeBlock],
[CardTypeControl], [CardTypeValidator], [CardTypeExtension]), совместно
использующиеся в типах карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask SetGlobalReferencesAsync(
    	IReadOnlyCollection<CardSerializableObject> value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetGlobalReferencesAsync ( 
    	value As IReadOnlyCollection(Of CardSerializableObject),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask SetGlobalReferencesAsync(
    	IReadOnlyCollection<CardSerializableObject^>^ value, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetGlobalReferencesAsync : 
            value : IReadOnlyCollection<CardSerializableObject> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
value
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
    Устанавливаемое значение.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
