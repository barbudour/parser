# CardMetadata.SetValidationResultAsync - метод
Устанавливает результат валидации при построении метаинформации.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask SetValidationResultAsync(
    	ValidationResult value,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetValidationResultAsync ( 
    	value As ValidationResult,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask
C++ __Копировать
     public:
    virtual ValueTask SetValidationResultAsync(
    	ValidationResult^ value, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetValidationResultAsync : 
            value : ValidationResult * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
    override SetValidationResultAsync : 
            value : ValidationResult * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask 
#### Параметры
value [ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
    Устанавливаемое значение.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
#### Реализации
[ICardMetadata.SetValidationResultAsync(ValidationResult,
CancellationToken)](M_Tessa_Cards_ICardMetadata_SetValidationResultAsync.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardMetadata - ](T_Tessa_Cards_Metadata_CardMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
[Tessa.Platform.ObjectSealedException]
