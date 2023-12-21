# ICardTypeService.GetCachedMetadataAsync - метод
Возвращает метаинформацию, описывающую типы всех карточек, со всей необходимой
информацией. Возвращаемая метаинформация и содержащиеся в ней типы карточек
защищены от изменений.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<CardMetadata> GetCachedMetadataAsync(
    	string builderName = "Default",
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function GetCachedMetadataAsync ( 
    	Optional builderName As String = "Default",
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardMetadata)
C++ __Копировать
     ValueTask<CardMetadata^> GetCachedMetadataAsync(
    	String^ builderName = L"Default", 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetCachedMetadataAsync : 
            ?builderName : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _builderName = defaultArg builderName "Default"
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardMetadata> 
#### Параметры
builderName [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Имя, по которому будет резолвиться объект для построения метаданных.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm)>  
Метаинформация, описывающая типы карточек, защищённые от изменений.
##  __См. также
#### Ссылки
[ICardTypeService - ](T_Tessa_Cards_ICardTypeService.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
