# CardMetadataBuilderBase.PrepareContainerInternalAsync - метод
Подготавливает контейнер метаинформации
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
перед построением мета информации для карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask PrepareContainerInternalAsync(
    	CardMetadataBuilderBase.MetadataContainer container,
    	ISchemeService schemeService,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function PrepareContainerInternalAsync ( 
    	container As CardMetadataBuilderBase.MetadataContainer,
    	schemeService As ISchemeService,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask PrepareContainerInternalAsync(
    	CardMetadataBuilderBase.MetadataContainer^ container, 
    	ISchemeService^ schemeService, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract PrepareContainerInternalAsync : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            schemeService : ISchemeService * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override PrepareContainerInternalAsync : 
            container : CardMetadataBuilderBase.MetadataContainer * 
            schemeService : ISchemeService * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
container
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
    Контейнер метаинформации, который нужно подготовить.
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
    Объект, предоставляющий информацию об актуальном состоянии схемы.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __Заметки
По умолчанию ничего не делает.
##  __См. также
#### Ссылки
[CardMetadataBuilderBase -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
