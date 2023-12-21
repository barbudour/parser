# CardCachedMetadata.GetValidationResultAsync - метод
Возвращает результат валидации при построении метаинформации.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<ValidationResult> GetValidationResultAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetValidationResultAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ValidationResult)
C++ __Копировать
     public:
    virtual ValueTask<ValidationResult^> GetValidationResultAsync(
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetValidationResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
    override GetValidationResultAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValidationResult> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)>  
Возвращаемое значение.
#### Реализации
[ICardMetadata.GetValidationResultAsync(CancellationToken)](M_Tessa_Cards_ICardMetadata_GetValidationResultAsync.htm)  
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
