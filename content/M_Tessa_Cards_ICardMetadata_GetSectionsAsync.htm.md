# ICardMetadata.GetSectionsAsync - метод
Возвращает метаинформацию по секциям карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<CardMetadataSectionCollection> GetSectionsAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetSectionsAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardMetadataSectionCollection)
C++ __Копировать
     ValueTask<CardMetadataSectionCollection^> GetSectionsAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSectionsAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadataSectionCollection> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadataSectionCollection](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)>  
Возвращаемое значение.
##  __См. также
#### Ссылки
[ICardMetadata - ](T_Tessa_Cards_ICardMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
