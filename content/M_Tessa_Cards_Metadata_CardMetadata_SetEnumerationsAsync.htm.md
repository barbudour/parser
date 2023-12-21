# CardMetadata.SetEnumerationsAsync - метод
Устанавливает список перечислений.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask SetEnumerationsAsync(
    	CardMetadataEnumerationCollection value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetEnumerationsAsync ( 
    	value As CardMetadataEnumerationCollection,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask SetEnumerationsAsync(
    	CardMetadataEnumerationCollection^ value, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetEnumerationsAsync : 
            value : CardMetadataEnumerationCollection * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override SetEnumerationsAsync : 
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
#### Реализации
[ICardMetadata.SetEnumerationsAsync(CardMetadataEnumerationCollection,
CancellationToken)](M_Tessa_Cards_ICardMetadata_SetEnumerationsAsync.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
