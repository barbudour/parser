# DocumentNumberDirector.StoreNumberCoreAsync - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     protected override ValueTask<bool> StoreNumberCoreAsync(
    	INumberContext context,
    	INumberObject number,
    	INumberLocation location,
    	NumberStoreMode storeMode = NumberStoreMode.WithNotification,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overrides Function StoreNumberCoreAsync ( 
    	context As INumberContext,
    	number As INumberObject,
    	location As INumberLocation,
    	Optional storeMode As NumberStoreMode = NumberStoreMode.WithNotification,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     protected:
    virtual ValueTask<bool> StoreNumberCoreAsync(
    	INumberContext^ context, 
    	INumberObject^ number, 
    	INumberLocation^ location, 
    	NumberStoreMode storeMode = NumberStoreMode::WithNotification, 
    	CancellationToken cancellationToken = CancellationToken()
    ) override
F# __Копировать
     abstract StoreNumberCoreAsync : 
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
    override StoreNumberCoreAsync : 
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
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
location [INumberLocation](T_Tessa_Cards_Numbers_INumberLocation.htm)
storeMode [NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)
(Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
