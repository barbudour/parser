# CardMetadata.FillAsync - метод
Заполняет в объекте метаинформацию по секциям
[GetSectionsAsync(CancellationToken)](M_Tessa_Cards_Metadata_CardMetadata_GetSectionsAsync.htm),
необходимую для использования типов карточек совместно с пакетом карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task FillAsync(
    	ISchemeService schemeService,
    	ICardMetadataBuilder cardMetadataBuilder,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function FillAsync ( 
    	schemeService As ISchemeService,
    	cardMetadataBuilder As ICardMetadataBuilder,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    Task^ FillAsync(
    	ISchemeService^ schemeService, 
    	ICardMetadataBuilder^ cardMetadataBuilder, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member FillAsync : 
            schemeService : ISchemeService * 
            cardMetadataBuilder : ICardMetadataBuilder * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Объект, используемый для доступа к метаинформации по структуре базы данных. 
cardMetadataBuilder
[ICardMetadataBuilder](T_Tessa_Cards_Metadata_ICardMetadataBuilder.htm)
     Объект, выполняющий построение метаинформации по типам карточек [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm). 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
