# KrProcessSharedHelper.TryGetKrTypeAsync - метод
Возвращает эффективные настройки для типа карточки или типа документа
[IKrType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrType.htm) по
карточке card, которая загружена со всеми секциями, или null, если настройки
нельзя получить.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Workflow.KrProcess](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<IKrType> TryGetKrTypeAsync(
    	IKrTypesCache krTypesCache,
    	Card card,
    	Guid cardTypeID,
    	IValidationResultBuilder validationResult = null,
    	Object validationObject = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function TryGetKrTypeAsync ( 
    	krTypesCache As IKrTypesCache,
    	card As Card,
    	cardTypeID As Guid,
    	Optional validationResult As IValidationResultBuilder = Nothing,
    	Optional validationObject As Object = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IKrType)
C++ __Копировать
     public:
    static ValueTask<IKrType^> TryGetKrTypeAsync(
    	IKrTypesCache^ krTypesCache, 
    	Card^ card, 
    	Guid cardTypeID, 
    	IValidationResultBuilder^ validationResult = nullptr, 
    	Object^ validationObject = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member TryGetKrTypeAsync : 
            krTypesCache : IKrTypesCache * 
            card : Card * 
            cardTypeID : Guid * 
            ?validationResult : IValidationResultBuilder * 
            ?validationObject : Object * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _validationResult = defaultArg validationResult null
            let _validationObject = defaultArg validationObject null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IKrType> 
#### Параметры
krTypesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
    Кэш типов карточек.
card [Card](T_Tessa_Cards_Card.htm)
    Карточка, загруженная со всеми секциями.
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
validationResult
[IValidationResultBuilder](T_Tessa_Platform_Validation_IValidationResultBuilder.htm)
(Optional)
     Объект, в который записываются сообщения об ошибках, или null, если сообщения никуда не записываются. 
validationObject
[Object](https://learn.microsoft.com/dotnet/api/system.object) (Optional)
     Объект, информация о котором записывается в сообщениях об ошибках в validationResult, или null, если информация об объекте не будет указана. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IKrType](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrType.htm)>  
Эффективные настройки для типа карточки или типа документа или null, если
настройки нельзя получить.
## __См. также
#### Ссылки
[KrProcessSharedHelper -
](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_KrProcessSharedHelper.htm)
[Tessa.Extensions.Default.Shared.Workflow.KrProcess - пространство
имён](N_Tessa_Extensions_Default_Shared_Workflow_KrProcess.htm)
