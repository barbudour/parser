# NumberHelper.StoreNumberWithQueueItemAsync - метод
Выполняет сохранение номера в местоположение, заданное в объекте
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm), если тип
местоположения отличен от
[NotAssigned](F_Tessa_Cards_Numbers_NumberLocationTypes_NotAssigned.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> StoreNumberWithQueueItemAsync(
    	INumberObject number,
    	INumberContext context,
    	NumberQueueItem item,
    	NumberStoreMode storeMode = NumberStoreMode.WithNotification,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function StoreNumberWithQueueItemAsync ( 
    	number As INumberObject,
    	context As INumberContext,
    	item As NumberQueueItem,
    	Optional storeMode As NumberStoreMode = NumberStoreMode.WithNotification,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> StoreNumberWithQueueItemAsync(
    	INumberObject^ number, 
    	INumberContext^ context, 
    	NumberQueueItem^ item, 
    	NumberStoreMode storeMode = NumberStoreMode::WithNotification, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member StoreNumberWithQueueItemAsync : 
            number : INumberObject * 
            context : INumberContext * 
            item : NumberQueueItem * 
            ?storeMode : NumberStoreMode * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _storeMode = defaultArg storeMode NumberStoreMode.WithNotification
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
number [INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)
    Номер, который может быть сохранён в заданном местоположении.
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст, в котором выполняется сохранение.
item [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
    Информация по действию с номером, которая содержит местоположение для сохранения.
storeMode [NumberStoreMode](T_Tessa_Cards_Numbers_NumberStoreMode.htm)
(Optional)
    Способ сохранения номера.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если номер был успешно сохранён или сохранение не требуется; false, если
сохранение требуется и номер был сохранён с ошибками.
## __См. также
#### Ссылки
[NumberHelper - ](T_Tessa_Cards_Numbers_NumberHelper.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
