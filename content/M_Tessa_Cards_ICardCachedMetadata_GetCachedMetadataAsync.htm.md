# ICardCachedMetadata.GetCachedMetadataAsync - метод
Возвращает исходный объект метаинформации, который кэшируется текущим
объектом.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<ICardMetadata> GetCachedMetadataAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetCachedMetadataAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICardMetadata)
C++ __Копировать
     ValueTask<ICardMetadata^> GetCachedMetadataAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetCachedMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICardMetadata> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)>  
Исходный объект метаинформации, который кэшируется текущим объектом.
##  __См. также
#### Ссылки
[ICardCachedMetadata - ](T_Tessa_Cards_ICardCachedMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
