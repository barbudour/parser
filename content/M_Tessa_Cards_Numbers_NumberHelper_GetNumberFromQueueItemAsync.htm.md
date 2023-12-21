# NumberHelper.GetNumberFromQueueItemAsync - метод
Возвращает номер для выполнения действия по информации, содержащейся в объекте
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm). Возвращённый
номер может быть пустым, но не может быть равен null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<INumberObject> GetNumberFromQueueItemAsync(
    	INumberContext context,
    	NumberQueueItem item,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetNumberFromQueueItemAsync ( 
    	context As INumberContext,
    	item As NumberQueueItem,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of INumberObject)
C++ __Копировать
     public:
    static ValueTask<INumberObject^> GetNumberFromQueueItemAsync(
    	INumberContext^ context, 
    	NumberQueueItem^ item, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetNumberFromQueueItemAsync : 
            context : INumberContext * 
            item : NumberQueueItem * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<INumberObject> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст выполнения действия.
item [NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm)
     Информация по действию с номером в очереди, которая используется для получения номера. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[INumberObject](T_Tessa_Cards_Numbers_INumberObject.htm)>  
Номер для выполнения действия по информации, содержащейся в объекте
[NumberQueueItem](T_Tessa_Cards_Numbers_NumberQueueItem.htm). Возвращённый
номер может быть пустым, но не может быть равен null.
## __См. также
#### Ссылки
[NumberHelper - ](T_Tessa_Cards_Numbers_NumberHelper.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
