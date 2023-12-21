# NumberHelper.GetNumberAndSetToContextPredicateAsync - метод
Функция предиката, передаваемая в [NotifyOnEventAsync(INumberContext,
NumberEventType, Func<INumberContext, CancellationToken, Task<Boolean>>,
Func<INumberContext, CancellationToken, Task<Boolean>>,
CancellationToken)](M_Tessa_Cards_Numbers_INumberDirectorBase_NotifyOnEventAsync.htm)
и устанавливающая в контексте номер, полученный по заданному типу numberType.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static ValueTask<bool> GetNumberAndSetToContextPredicateAsync(
    	INumberContext context,
    	NumberTypeDescriptor numberType,
    	bool allowEmptyNumber = true,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetNumberAndSetToContextPredicateAsync ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor,
    	Optional allowEmptyNumber As Boolean = true,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Boolean)
C++ __Копировать
     public:
    static ValueTask<bool> GetNumberAndSetToContextPredicateAsync(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType, 
    	bool allowEmptyNumber = true, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetNumberAndSetToContextPredicateAsync : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor * 
            ?allowEmptyNumber : bool * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _allowEmptyNumber = defaultArg allowEmptyNumber true
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<bool> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером, в котором номер будет установлен.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера, который будет получен.
allowEmptyNumber
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
    true, если при невозможности получить номер (т.е. при получении пустого номера) действие будет считаться успешно выполненным; false, если в этом случае действие будет считаться неудачно выполненным. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если действие было успешно выполнено; false в противном случае.
## __См. также
#### Ссылки
[NumberHelper - ](T_Tessa_Cards_Numbers_NumberHelper.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
