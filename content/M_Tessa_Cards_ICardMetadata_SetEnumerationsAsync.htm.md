# ICardMetadata.SetEnumerationsAsync - метод
Устанавливает список перечислений.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask SetEnumerationsAsync(
    	CardMetadataEnumerationCollection value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function SetEnumerationsAsync ( 
    	value As CardMetadataEnumerationCollection,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     ValueTask SetEnumerationsAsync(
    	CardMetadataEnumerationCollection^ value, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract SetEnumerationsAsync : 
            value : CardMetadataEnumerationCollection * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
value
[CardMetadataEnumerationCollection](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)
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
