# NumberBuilder.StoreNumberAsync(INumberContext, INumberObject,
INumberLocation, NumberStoreMode, CancellationToken) - метод
Сохраняет объект с номером в заданном местоположении и контексте.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<bool> StoreNumberAsync(
    	INumberContext context,
    	INumberObject number,
    	INumberLocation location,
    	NumberStoreMode storeMode = NumberStoreMode.WithNotification,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreNumberAsync ( 
    	context As INumberContext,
    	number As INumberObject,
    	location As INumberLocation,
    	Optional storeMode As NumberStoreMode = NumberStoreMode.WithNotification,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    virtual ValueTask<bool> StoreNumberAsync(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	INumberLocation^ location, 
    	NumberStoreMode storeMode = NumberStoreMode::WithNotification, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreNumberAsync : 
            context : INumberContext * 
            number : INumberObject * 
            location : INumberLocation * 
            ?storeMode : NumberStoreMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMode = defaultArg storeMode NumberStoreMode.WithNotification
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
    override StoreNumberAsync : 
            context : INumberContext * 
            number : INumberObject * 
            location : INumberLocation * 
            ?storeMode : NumberStoreMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMode = defaultArg storeMode NumberStoreMode.WithNotification
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Сохраняемый объект с номером.
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
    Местоположение номера для сохранения.
storeMode [NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)
(Optional)
    Способ сохранения номера в карточке.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если текущий номер был успешно сохранён в местоположении location;
false, если возникла ошибка.
#### Реализации
[INumberLocationManager.StoreNumberAsync(INumberContext, INumberObject,
INumberLocation, NumberStoreMode,
CancellationToken)](M_Tessa_Cards_Numbers_INumberLocationManager_StoreNumberAsync.htm)  
##  __См. также
#### Ссылки
[NumberBuilder - ](T_Tessa_Cards_Numbers_NumberBuilder.htm)
[StoreNumberAsync -
перегрузка](Overload_Tessa_Cards_Numbers_NumberBuilder_StoreNumberAsync.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
